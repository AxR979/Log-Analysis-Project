#!/usr/bin/env python3

import psycopg2

db = psycopg2.connect("dbname=news")
c = db.cursor()

# query = """SELECT articles.title, COUNT(*) as num
# FROM articles, log 
# WHERE log.path ILIKE '%' || articles.slug 
# GROUP BY articles.title
# ORDER BY num desc
# LIMIT 3"""

# query = """SELECT authors.name, COUNT(*) as num
# FROM authors, articles, log 
# WHERE log.path ILIKE '%' || articles.slug AND authors.id = articles.author
# GROUP BY authors.name
# ORDER BY num desc"""


query = """select to_char(time, 'fmmonth fmdd yyyy'), count(*) as num 
           from log where status like '404%' 
           group by to_char(time, 'fmmonth fmdd yyyy')
           order by num desc; """


c.execute(query)
rows = c.fetchall()
for row in rows:
    print(row)
db.close()
