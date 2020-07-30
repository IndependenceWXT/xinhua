"""
统计配置进度， 生成表格
"""
import os

from spider.db import DB

usr = os.getenv("mysql_usr")
pwd = os.getenv("mysql_pwd")
mysql_uri = f"mysql://{usr}:{pwd}@rm-2ze3450z16n1c2msxco.mysql.rds.aliyuncs.com:3306/xinhuaspider"
db = DB().create(mysql_uri)

sql_detail = """/* 统计配置人员配置数量 */
SELECT
    `user` AS "用户",
    sum(if_configured) AS "已配置",
    sum(if_submit) AS "已提交",
    sum(if_configured) - sum(if_submit) as "未提交",
    sum(if_approved) AS "已通过",
    sum(if_online) AS "已上线", 
    CEILING(sum(if_approved)/sum(if_configured) *100) as "通过率%"
FROM
    progress
WHERE
     conf_date BETWEEN "2020-07-27"
 AND "2020-07-31"
GROUP BY `user`"""

sql_total = """/*统计总进度*/
SELECT
    sum( `if_configured` ) AS "已配置",
    sum( `if_submit` ) AS "已提交",
    sum( `if_approved` ) AS "已通过",
    sum( `if_online` ) AS "已上线"
FROM
    progress
WHERE
    conf_date BETWEEN "2020-07-1" AND "2020-07-31"
"""


reports = []
reports.append("| 用户 | 已配置 | 已提交 |未提交 | 已通过 | 已上线 | 通过率% |")
reports.append("|----|----|----|----|----|----|----|")
res = db.query_all(sql_detail)
for each in res:
    user, configured, submit, to_sub, approved, online, score = each
    reports.append(
        f"| {user} | {configured} | {submit} | {to_sub} | {int(approved)} | {online} | {score} |"
    )
else:
    with open("../reports/progress.md", mode="w", encoding="utf-8") as r:
        r.write("\n".join(reports) + "\n" * 5)

reports = []
reports.append("| 已配置 | 已提交 | 已通过 | 已上线 |")
reports.append("|----|----|----|----|")
res = db.query_all(sql_total)
for each in res:
    configured, submit, approved, online = each
    reports.append(f"| {configured} | {submit} | {int(approved)} | {online} |")
else:
    with open("../reports/progress.md", mode="a", encoding="utf-8") as r:
        r.write("\n".join(reports))
