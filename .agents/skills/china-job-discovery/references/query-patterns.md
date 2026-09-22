# 中国职位搜索式

Replace placeholders with candidate data. Run focused queries rather than one oversized query.

```text
site:zhipin.com/web/geek/job "ROLE" "CITY"
site:liepin.com/job "ROLE" "CITY"
site:zhaopin.com/jobdetail "ROLE" "CITY"
site:51job.com "ROLE" "CITY"
site:lagou.com/jobs "ROLE" "CITY"
site:maimai.cn "ROLE" 招聘 "CITY"
site:iguopin.com "ROLE" "CITY"
"COMPANY" 招聘 "ROLE" 社会招聘
"COMPANY" 校园招聘 "GRADUATION_YEAR"
"CITY" 事业单位 公开招聘 "YEAR"
```

Useful synonym expansion:

- 人工智能: `AI工程师`, `算法工程师`, `机器学习工程师`, `大模型应用工程师`, `LLM工程师`
- Data: `数据分析师`, `商业分析师`, `BI工程师`, `数据科学家`, `数据工程师`
- Product: `产品经理`, `高级产品经理`, `产品负责人`, `AI产品经理`, `策略产品经理`
- Software: `软件工程师`, `后端开发`, `服务端开发`, `Java开发`, `Go开发`, `Python开发`
- Operations: `用户运营`, `产品运营`, `内容运营`, `增长运营`, `商业化运营`

Add one constraint per pass when needed: `薪资`, `双休`, `远程`, `应届`, `实习`, `社招`, `国企`.
