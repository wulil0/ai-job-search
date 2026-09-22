---
framework_version: 1.1.0
---

# Agent Guidelines: AI Job Search

This workspace is structured to manage job search activities, scraper tools, CVs, cover letters, and interview preparation.

## Thin-Pointer Design (Single Source of Truth)

To prevent duplication and configuration drift across different AI agent frameworks (Claude Code, Google Antigravity, Codex, Cursor, Gemini CLI, etc.), this workspace uses a unified thin-pointer design. All agent runtimes should load the canonical specifications and candidate profiles from the files and directories below:

1. **Personal Candidate Profile:**
   - The candidate profile, contact details, education, and target preferences are defined in [CLAUDE.md](CLAUDE.md) and the individual profile methodology files under [.claude/skills/job-application-assistant/](.claude/skills/job-application-assistant/) (specifically `01-*.md` etc.).
2. **Canonical Workflow Specifications:**
   - The step-by-step instructions and triggers for tasks (setup, scrape, rank, apply, upskill, interview) are defined in the [.claude/](.claude/) directory (specifically under `.claude/skills/` and `.claude/commands/`).
   - Do not duplicate these rules or specifications. Treat `.claude/` files as the single source of truth.
3. **Portal Search Skills:**
   - Job-portal search CLIs live under [.agents/skills/](.agents/skills/) in the portable Agent Skills format (with a `SKILL.md` per portal). Codex and Antigravity discover these automatically; the `/scrape` workflow in [.claude/skills/job-scraper/](.claude/skills/job-scraper/) orchestrates them.

## OpenAI / ChatGPT Runtime

When the active runtime is Codex, ChatGPT, or a tool backed by the OpenAI API:

1. Read the portable workflow in [`.agents/skills/openai-job-search-runtime/SKILL.md`](.agents/skills/openai-job-search-runtime/SKILL.md).
2. Treat references to “Claude” in canonical files as the active assistant unless a step is specifically about Claude Code UI or permissions.
3. Use the repository files directly instead of translating the whole `.claude/` tree. Load only the command or skill needed for the current task.
4. For direct API access, use `tools/openai_responses.py`. Keep credentials in environment variables; never write API keys into repository files.
5. For mainland-China job searches and applications, also load the `china-job-discovery` and `china-job-application` skills.
