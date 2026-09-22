---
name: china-job-discovery
description: >
  Search, normalize, deduplicate, and rank jobs for candidates in mainland China.
  Use for BOSS直聘、猎聘、智联招聘、前程无忧、拉勾、脉脉、国聘、事业单位招聘、
  校园招聘、社招、远程职位，以及按城市、薪资、学历、经验、行业筛选中国岗位。
---

# 中国职位搜索

Use this skill with the repository's canonical scraper and ranking workflow. It adds
China-specific discovery, normalization, and filtering without replacing the user's
profile or inventing experience.

## Search order

Choose sources by the user's goal instead of querying every portal:

1. **General social recruitment:** BOSS直聘、猎聘、智联招聘、前程无忧.
2. **Internet and technology:** BOSS直聘、拉勾、脉脉招聘、company career pages.
3. **Campus recruitment:** 国聘、应届生求职网、牛客校招、高校就业网、company campus pages.
4. **State-owned enterprises and public institutions:** 国聘、国资委/央企招聘 pages、地方人社部门、事业单位公开招聘 pages.
5. **Remote or international teams:** LinkedIn and the installed `freehire-search` skill.

Read [references/portals.md](references/portals.md) when selecting sources or handling
login, app-only pages, verification, or incomplete public pages. Read
[references/query-patterns.md](references/query-patterns.md) when constructing searches.

## Workflow

1. Load the candidate's target roles, cities, salary floor, experience, education,
   employment type, industry preferences, and hard constraints from `CLAUDE.md`.
2. Normalize Chinese synonyms before searching. Examples: `产品经理/产品负责人`,
   `算法工程师/机器学习工程师/AI工程师`, `开发/研发/软件工程师`.
3. Search only relevant sources. Prefer public result pages, employer career pages,
   and search-engine `site:` queries when a portal requires an interactive session.
4. Save enough evidence for each result: title, company, city/district, salary text,
   experience, education, employment type, publish/update date, source, URL, and a
   short requirement summary. Preserve “面议” and missing fields as unknown.
5. Normalize salary to a comparable monthly range while preserving the original text:
   - `20-30K·13薪` → monthly `20-30K`, annual estimate `260-390K`.
   - `30-50万/年` → annual `300-500K`, monthly equivalent `25.0-41.7K`.
   - Do not include uncertain bonus, stock, allowance, or commission in guaranteed pay.
6. Deduplicate by employer + normalized title + city. Keep the employer's own page as
   canonical when the same role appears on several portals; retain other URLs as sources.
7. Apply hard filters first, then rank with the canonical fit framework. Mark ambiguous
   phrases such as “有竞争力的薪酬” as unknown rather than favorable.
8. Present a concise Chinese shortlist. Include why it matches, concrete gaps, salary,
   freshness, source, and the next action.

## China-specific filters

- Distinguish `统招本科` from a generic bachelor's requirement; preserve the exact wording.
- Treat `985/211/双一流优先`, age, gender, marital status, and similar conditions as explicit
  posting constraints in the summary, not inferred candidate qualities.
- Separate base city, workplace district, travel frequency, relocation, and remote policy.
- Recognize `双休/大小周/单休`, overtime language, probation salary, social insurance and
  housing fund, dispatch/outsourcing status, and non-compete clauses as decision factors.
- Label recruiter-posted and employer-posted listings separately when the source reveals it.

## Output schema

Return JSON to downstream steps when practical:

```json
{
  "title": "岗位名称",
  "company": "公司名称",
  "location": {"city": "城市", "district": "区域", "remote": "unknown"},
  "salary": {"raw": "20-30K·13薪", "monthly_min_cny": 20000, "monthly_max_cny": 30000, "months": 13},
  "requirements": {"experience": "3-5年", "education": "本科", "keywords": []},
  "work_schedule": "unknown",
  "employment_type": "全职",
  "date": "YYYY-MM-DD",
  "source": "SOURCE",
  "url": "URL",
  "fit_notes": [],
  "gaps": []
}
```
