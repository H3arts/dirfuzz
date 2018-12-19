# coding:utf8

from database import db

results = db.results.distinct("url_path")

for r in results:
    print(r)