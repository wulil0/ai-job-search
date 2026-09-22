---
name: china-job-application
description: >
  Create and review mainland-China job application materials in Chinese, including
  one-page Chinese resumes, recruiter opening messages, self-introductions, project
  descriptions, application-form answers, interview preparation, and salary negotiation.
  Use for 中国求职、中文简历、BOSS招呼语、猎聘沟通、校招网申、社招面试和谈薪.
---

# 中国求职申请

Use the canonical factual profile and fit-evaluation rules. Write in natural Simplified
Chinese by default. Preserve the user's requested language for foreign companies or
English-language postings.

## Deliverable selection

- **Resume:** one page by default for students and early-career candidates; expand only
  when substantial relevant experience justifies it. Prioritize recent, relevant evidence.
- **Recruiter opening message:** 60–120 Chinese characters, specific to the role, with one
  strong match and a clear invitation to review the resume.
- **Self-introduction:** prepare 30-second, 1-minute, and 3-minute variants when interview
  preparation is requested.
- **Application answers:** answer each field directly; respect visible character limits.
- **Cover letter:** create when requested by the employer or useful for a foreign company;
  do not assume it is mandatory for every China-market application.
- **Interview preparation:** include role knowledge, project deep-dives, behavioral stories,
  likely Chinese interview questions, questions to ask, and salary-positioning notes.

## Resume rules

1. Keep identity/contact information minimal and relevant. Add photo, age, gender, marital
   status, ID number, political status, or health data only when the user explicitly chooses
   to include it or an application form requires the field.
2. Lead each bullet with action and business context, then method and measurable result.
   Preserve the source fact; do not manufacture metrics.
3. Translate terminology for the target audience while retaining recognized technical names.
4. Put target role, core strengths, skills, experience/projects, and education in the order
   that best proves fit. Students may place education first; experienced candidates usually
   place experience first.
5. Keep every claim traceable to `CLAUDE.md` or user-provided evidence. Mark a true gap as a
   gap and suggest a positioning strategy rather than inserting the missing skill.
6. Check Chinese PDF fonts and text extraction. The final PDF should copy/paste cleanly and
   keep dates, company names, phone, and email visible as literal text.

## Recruiter opening-message template

```text
您好，我关注到贵司的「ROLE」岗位。我有 EXPERIENCE，曾通过 METHOD 达成 RESULT，
与岗位要求中的 REQUIREMENT 较匹配。简历已附上，期待进一步沟通，谢谢。
```

Vary the wording; never send a mass-message tone when the role offers concrete details.

## Evaluation additions

Alongside canonical fit scoring, check:

- city, commute, relocation, travel, remote policy;
- monthly base, salary months, bonus certainty, commission, probation discount;
- `双休/大小周/单休`, overtime expectations and compensatory time;
- direct employment, outsourcing, dispatch, contractor, or internship status;
- social insurance/housing fund base, annual leave, non-compete, background check;
- degree type, graduation year, professional qualification, language, age or other stated gates.

## Final verification

Return a Chinese checklist covering factual accuracy, JD keyword coverage, unsupported claims,
language quality, salary units, date consistency, contact details, PDF page count, font embedding,
and text-layer extraction.
