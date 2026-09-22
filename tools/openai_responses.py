#!/usr/bin/env python3
"""Minimal OpenAI Responses API client for repository workflows.

Uses only the Python standard library. Credentials come from environment variables.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path


DEFAULT_MODEL = "gpt-5.6-terra"


def read_text(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def build_input(prompt: str, context_files: list[str]) -> str:
    sections: list[str] = []
    for filename in context_files:
        sections.append(f"<context_file path={json.dumps(filename, ensure_ascii=False)}>\n")
        sections.append(read_text(filename))
        sections.append("\n</context_file>\n")
    sections.append("<user_request>\n")
    sections.append(prompt)
    sections.append("\n</user_request>")
    return "".join(sections)


def extract_output_text(response: dict) -> str:
    direct = response.get("output_text")
    if isinstance(direct, str) and direct:
        return direct
    chunks: list[str] = []
    for item in response.get("output", []):
        if not isinstance(item, dict):
            continue
        for content in item.get("content", []):
            if isinstance(content, dict) and content.get("type") == "output_text":
                text = content.get("text")
                if isinstance(text, str):
                    chunks.append(text)
    return "".join(chunks)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    prompt = parser.add_mutually_exclusive_group(required=True)
    prompt.add_argument("--prompt", help="Prompt text")
    prompt.add_argument("--prompt-file", help="UTF-8 prompt file")
    prompt.add_argument("--stdin", action="store_true", help="Read prompt from stdin")
    parser.add_argument("--system", help="Developer/system instruction text")
    parser.add_argument("--system-file", help="UTF-8 developer/system instruction file")
    parser.add_argument("--context-file", action="append", default=[], help="Context file; repeatable")
    parser.add_argument("--model", default=os.getenv("OPENAI_MODEL", DEFAULT_MODEL))
    parser.add_argument("--reasoning", choices=("none", "low", "medium", "high", "xhigh"))
    parser.add_argument("--output", help="Write response text to this UTF-8 file")
    parser.add_argument("--dry-run", action="store_true", help="Print request JSON and exit")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.prompt_file:
        prompt = read_text(args.prompt_file)
    elif args.stdin:
        prompt = sys.stdin.read()
    else:
        prompt = args.prompt

    instructions = args.system or (read_text(args.system_file) if args.system_file else None)
    payload: dict = {
        "model": args.model,
        "input": build_input(prompt, args.context_file),
        "store": False,
    }
    if instructions:
        payload["instructions"] = instructions
    if args.reasoning and args.reasoning != "none":
        payload["reasoning"] = {"effort": args.reasoning}

    if args.dry_run:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("OPENAI_API_KEY is not set", file=sys.stderr)
        return 2
    base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    request = urllib.request.Request(
        f"{base_url}/responses",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=300) as result:
            response = json.loads(result.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        print(f"OpenAI API HTTP {exc.code}: {body}", file=sys.stderr)
        return 1
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        print(f"OpenAI API request failed: {exc}", file=sys.stderr)
        return 1

    output = extract_output_text(response)
    if not output:
        print(json.dumps(response, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1
    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
    else:
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
