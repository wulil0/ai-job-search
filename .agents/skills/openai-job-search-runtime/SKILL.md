---
name: openai-job-search-runtime
description: >
  Run this job-search repository with Codex, ChatGPT, or the OpenAI Responses API instead
  of Claude Code. Use when configuring OpenAI model access, mapping repository commands to
  an OpenAI-powered agent, choosing a model, or sending a repository workflow prompt through API.
allowed-tools: Bash(python3 tools/openai_responses.py *)
---

# OpenAI / ChatGPT Runtime

This repository's canonical workflow remains in `.claude/`; use it as methodology, not as a
runtime requirement. `AGENTS.md` is the portable entry point.

## Choose an access mode

### Codex

Open the repository in Codex. Read `AGENTS.md`, then load only the relevant canonical file:

| User intent | Canonical workflow |
|---|---|
| set up profile | `.claude/commands/setup.md` |
| find jobs | `.claude/skills/job-scraper/SKILL.md` |
| rank jobs | `.claude/commands/rank.md` |
| apply to a role | `.claude/commands/apply.md` |
| prepare interview | `.claude/commands/interview.md` |
| identify skill gaps | `.claude/skills/upskill/SKILL.md` |

For mainland China, also load `china-job-discovery` or `china-job-application`.

### ChatGPT interactive use

Attach or connect the repository, start with `AGENTS.md`, and state the task in natural language.
Examples: “根据 `.claude/commands/apply.md` 评估并申请这个岗位” or “使用
`china-job-discovery` 搜索上海的 AI 产品经理岗位”. Keep generated personal files inside the
ignored workspace paths documented in `.gitignore`.

### OpenAI API

Set credentials in the process environment:

```bash
export OPENAI_API_KEY="YOUR_KEY"
export OPENAI_MODEL="gpt-5.6-terra"       # optional
export OPENAI_BASE_URL="https://api.openai.com/v1"  # optional
```

Send a prompt through the Responses API helper:

```bash
python3 tools/openai_responses.py \
  --system-file AGENTS.md \
  --context-file .agents/skills/china-job-application/SKILL.md \
  --context-file .claude/commands/apply.md \
  --prompt-file documents/postings/TARGET.txt \
  --output output.md
```

Use `--model` to override `OPENAI_MODEL`, `--reasoning` for supported reasoning levels,
and `--dry-run` to inspect the request without sending it. The helper uses only Python's
standard library, sends `store: false`, and writes only the returned text to `--output`.

## Model choice

- Use a high-capability reasoning model for fit evaluation, truthful tailoring, final review,
  and complex interview preparation.
- Use a balanced model for routine rewriting, summaries, recruiter messages, and form answers.
- Pin `OPENAI_MODEL` in your own environment when reproducibility matters; keep model IDs out
  of personal profile files so the workflow stays portable.

## Runtime translation

- “Claude” in a role sentence means the active assistant.
- Claude-specific `Agent` steps become a fresh reviewer context or a second API request.
- `WebFetch`/`WebSearch` steps use the active runtime's web tools.
- Claude permission files under `.claude/settings.json` apply only to Claude Code; use the
  active runtime's approval and sandbox controls.
- Slash commands may be invoked as natural-language requests pointing to their Markdown file.

## Data handling

Keep API keys in environment variables. Do not include unrelated personal documents in a
request. Use `--context-file` only for files required by the current step and review generated
materials before submitting them to an employer.
