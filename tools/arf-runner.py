#!/usr/bin/env python3
"""
ARF Probe Runner — administer probes through the LLM Harness Protocol (Path 1).

This tool implements ARF-SPEC §3.4 Path 1 (Direct API, automated):
- Routes LLM calls through the harness proxy (127.0.0.1:8474)
- Works for API-accessible models: gpt-4o, claude-*, gemini-*, etc.
- Requires an API key — the harness forwards it to the upstream provider

PATH 1 (this tool): agent accessible via API, harness captures automatically.
PATH 2 (manual):    embedded agents like GitHub Copilot Chat cannot be intercepted
                    by the harness. Administer probes manually: paste Case A into
                    a new chat, record response; paste Case B into another new chat,
                    record response; fill result YAML by hand.

This tool does NOT score results — scoring is human work per ARF-SPEC §4.

Usage:
    python tools/arf-runner.py <probe-id> [--model MODEL] [--administrator NAME]

Example:
    python tools/arf-runner.py code-review-offline-constraint --model gpt-4o

Pre-requisites:
    1. llm-harness-proxy.exe must be running (listening on 127.0.0.1:8474)
    2. OPENAI_API_KEY must be set in environment
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

# Harness base URL — the proxy intercepts and ledgers before forwarding
HARNESS_BASE = "http://127.0.0.1:8474"

# Try to import httpx (preferred) or fall back to requests
try:
    import httpx
    USE_HTTPX = True
except ImportError:
    import requests
    USE_HTTPX = False


def detect_provider(model: str) -> str:
    """Detect provider from model name."""
    if model.startswith("claude"):
        return "anthropic"
    elif model.startswith("gpt") or model.startswith("o1") or model.startswith("o3"):
        return "openai"
    elif model.startswith("gemini"):
        return "google"
    else:
        # Default to OpenAI format
        return "openai"


def load_probe(probe_id: str, probes_dir: Path) -> dict:
    """Load a probe YAML file by ID."""
    probe_path = probes_dir / f"{probe_id}.yaml"
    if not probe_path.exists():
        raise FileNotFoundError(f"Probe not found: {probe_path}")
    
    with open(probe_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def call_model_through_harness(
    content: str,
    model: str,
    api_key: str,
) -> tuple[str, str, str]:
    """
    Make a single LLM call through the harness.
    
    Returns:
        (response_text, session_id, model_used)
    
    The harness creates a new session for each call (no x-harness-session header).
    This ensures Case A and Case B are in independent sessions.
    """
    provider = detect_provider(model)
    
    if provider == "anthropic":
        url = f"{HARNESS_BASE}/v1/messages"
        headers = {
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json",
            "Accept-Encoding": "identity",
        }
        payload = {
            "model": model,
            "messages": [
                {"role": "user", "content": content}
            ],
            "max_tokens": 4096,
        }
    else:
        # OpenAI format (also used by Gemini via harness)
        url = f"{HARNESS_BASE}/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": model,
            "messages": [
                {"role": "user", "content": content}
            ],
            "max_tokens": 4096,
        }
    
    if USE_HTTPX:
        with httpx.Client(timeout=120.0) as client:
            resp = client.post(url, headers=headers, json=payload)
            resp.raise_for_status()
            session_id = resp.headers.get("x-harness-session", "unknown")
            data = resp.json()
    else:
        resp = requests.post(url, headers=headers, json=payload, timeout=120)
        resp.raise_for_status()
        session_id = resp.headers.get("x-harness-session", "unknown")
        data = resp.json()
    
    # Surface API errors immediately — don't silently return empty string
    if "error" in data:
        raise RuntimeError(f"API error ({provider}): {data['error']}")

    # Extract response text (different format for Anthropic vs OpenAI)
    response_text = ""
    if provider == "anthropic":
        # Anthropic format: {"content": [{"type": "text", "text": "..."}], ...}
        if "content" in data and len(data["content"]) > 0:
            for block in data["content"]:
                if block.get("type") == "text":
                    response_text += block.get("text", "")
    else:
        # OpenAI format: {"choices": [{"message": {"content": "..."}}], ...}
        if "choices" in data and len(data["choices"]) > 0:
            message = data["choices"][0].get("message", {})
            response_text = message.get("content", "")
    
    model_used = data.get("model", model)
    
    return response_text, session_id, model_used


def run_probe(
    probe: dict,
    model: str,
    api_key: str,
    administrator: str,
) -> dict:
    """
    Administer a probe: run Case A and Case B in independent sessions.
    
    Returns a result dict following ARF-SPEC §6.2 schema (scoring left null).
    """
    probe_id = probe["id"]
    probe_version = probe.get("version", "1.0")
    
    print(f"\n{'='*60}")
    print(f"Administering probe: {probe_id}")
    print(f"{'='*60}")
    
    # --- Pre-registration timestamp (before any case runs) ---
    pre_reg_timestamp = datetime.now(timezone.utc).isoformat()
    print(f"\nPre-registration timestamp: {pre_reg_timestamp}")
    print(f"Expected divergence: {probe['pre_registration']['expected_divergence']}")
    print(f"Expected stability: {probe['pre_registration']['expected_stability']}")
    
    # --- Run Case A ---
    print(f"\n--- Case A: {probe['case_a']['description']} ---")
    case_a_content = probe["case_a"]["content"]
    
    try:
        resp_a, session_a, model_a = call_model_through_harness(
            case_a_content, model, api_key
        )
        print(f"✓ Case A complete. Session: {session_a}")
        print(f"  Response length: {len(resp_a)} chars")
    except Exception as e:
        print(f"✗ Case A failed: {e}")
        raise
    
    # --- Run Case B (independent session) ---
    print(f"\n--- Case B: {probe['case_b']['description']} ---")
    case_b_content = probe["case_b"]["content"]
    
    try:
        resp_b, session_b, model_b = call_model_through_harness(
            case_b_content, model, api_key
        )
        print(f"✓ Case B complete. Session: {session_b}")
        print(f"  Response length: {len(resp_b)} chars")
    except Exception as e:
        print(f"✗ Case B failed: {e}")
        raise
    
    # Verify session independence
    if session_a == session_b:
        print(f"\n⚠ WARNING: Same session ID for both cases! Independence violated.")
    else:
        print(f"\n✓ Session independence verified (A: {session_a}, B: {session_b})")
    
    # --- Build result structure per ARF-SPEC §6.2 ---
    administered_time = datetime.now(timezone.utc).isoformat()
    
    result = {
        "probe_id": probe_id,
        "probe_version": probe_version,
        "administered": administered_time,
        "administrator": administrator,
        "pre_registration_timestamp": pre_reg_timestamp,
        
        "harness": {
            "type": "llm-llm-harness-proxy",
            "version": "1.0.0",
            "endpoint": HARNESS_BASE,
        },
        
        "agent": {
            "model": model_a,  # Use the model returned by the API
            "requested_model": model,
            "configuration": f"max_tokens=4096",
        },
        
        "sessions": {
            "case_a": {
                "session_id": session_a,
                "response_summary": resp_a[:500] + "..." if len(resp_a) > 500 else resp_a,
                "response_length": len(resp_a),
            },
            "case_b": {
                "session_id": session_b,
                "response_summary": resp_b[:500] + "..." if len(resp_b) > 500 else resp_b,
                "response_length": len(resp_b),
            },
        },
        
        # Pre-registration from probe (for scoring reference)
        "pre_registration": probe["pre_registration"],
        
        # Scoring section — left null for human completion
        "scoring": {
            "divergence_observed": None,  # Human fills this
            "stability_observed": None,   # Human fills this
        },
        
        "result": None,  # Human determines: pass | fail | indeterminate
        "failure_mode": None,  # If fail: template_invariance | wrong_divergence | spurious_divergence | surface_only
        "notes": "Scoring not yet completed. Review Case A and Case B responses against pre_registration.",
        
        # Full responses preserved for scoring
        "_full_responses": {
            "case_a": resp_a,
            "case_b": resp_b,
        },
    }
    
    return result


def main():
    parser = argparse.ArgumentParser(
        description="ARF Probe Runner — administer probes through the LLM Harness Protocol"
    )
    parser.add_argument(
        "probe_id",
        help="ID of the probe to run (filename without .yaml)"
    )
    parser.add_argument(
        "--model",
        default="gpt-4o",
        help="Model to use (default: gpt-4o)"
    )
    parser.add_argument(
        "--administrator",
        default=os.environ.get("USER", os.environ.get("USERNAME", "unknown")),
        help="Administrator identifier for the result file"
    )
    parser.add_argument(
        "--probes-dir",
        default="probes",
        help="Directory containing probe YAML files (default: probes)"
    )
    parser.add_argument(
        "--results-dir",
        default="probes/results",
        help="Directory to write result files (default: probes/results)"
    )
    
    args = parser.parse_args()
    
    # Resolve paths relative to script location (manifesto repo root)
    script_dir = Path(__file__).parent.parent  # tools/../ = manifesto/
    probes_dir = script_dir / args.probes_dir
    results_dir = script_dir / args.results_dir
    
    # Ensure results directory exists
    results_dir.mkdir(parents=True, exist_ok=True)
    
    # Get API key based on provider
    provider = detect_provider(args.model)
    if provider == "anthropic":
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        key_var = "ANTHROPIC_API_KEY"
    else:
        api_key = os.environ.get("OPENAI_API_KEY")
        key_var = "OPENAI_API_KEY"
    
    if not api_key:
        print(f"ERROR: {key_var} environment variable not set")
        print("The harness forwards this to the upstream API.")
        sys.exit(1)
    
    # Strip whitespace/newlines — keys set from files often carry a trailing \n
    api_key = api_key.strip()
    
    api_key = api_key.strip()  # Guard against trailing newlines from file reads
    
    # Load probe
    try:
        probe = load_probe(args.probe_id, probes_dir)
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        print(f"Available probes in {probes_dir}:")
        for p in probes_dir.glob("*.yaml"):
            print(f"  - {p.stem}")
        sys.exit(1)
    
    # Run the probe
    try:
        result = run_probe(probe, args.model, api_key, args.administrator)
    except Exception as e:
        print(f"\nERROR: Probe administration failed: {e}")
        sys.exit(1)
    
    # Write result file
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    result_filename = f"{args.probe_id}_{timestamp}.yaml"
    result_path = results_dir / result_filename
    
    with open(result_path, "w", encoding="utf-8") as f:
        yaml.dump(result, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    
    print(f"\n{'='*60}")
    print(f"Result written to: {result_path}")
    print(f"{'='*60}")
    print(f"\nNext steps:")
    print(f"1. Review the full responses in _full_responses")
    print(f"2. Compare against pre_registration expectations")
    print(f"3. Fill in scoring.divergence_observed and scoring.stability_observed")
    print(f"4. Set result to: pass | fail | indeterminate")
    print(f"5. If fail, set failure_mode")


if __name__ == "__main__":
    main()
