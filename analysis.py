#!/usr/bin/env python3

import psycopg2
from datetime import datetime


def get_results(query):
    # To Connect database
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    db.close()
    return rows

# function for query 1


def most_popular_articles():

    query1 = """
        select articles.title, count(*)
        as views
        from articles,log
        where log.path ='/article/' || articles.slug and status='200 OK'
        group by articles.title
        order by views
        desc limit 3;
    """

    # prints the results for query1
    results = get_results(query1)

    count = 1
    print("The most popular articles are:")
    for i in results:
        print("Article" + "-" + str(
            count) + " " + i[0] + ' --- ' + str(i[1]) + "views")
        count += 1

# function for query 2


def most_popular_authors():

    # Build Query Strin
    query2 = """ select authors.name, count(log.path)
    as views from articles , authors , log
    where log.path=('/article/' || articles.slug)
    and author=authors.id and log.status like '200%'
    group by name
    order by views
    desc limit 10;
"""

# prints the results for query2
    results = get_results(query2)

    count = 1
    print("The most popular authors are:")
    for i in results:
        print("Author" + "-" + str(
            count) + " " + i[0] + ' --- ' + str(i[1]) + "views")
        count += 1

# function for query 3


def request_error_days():
    query3 = """
        select count(status),
        round((count(status) filter(where status = '404 NOT FOUND') *
        100.0 / count(status) ),2),
        date(time) from log group by date(time)
        having round((count(status) filter(where status = '404 NOT FOUND') *
        100.0 / count(status) ),2) > 1.0;

    """

    # prints the result for query3
    results = get_results(query3)
    print("Days with more than 1% request errors")
    for i in results:
        print (" " + str((i[2])) + " error " + str(i[1]) + "%")

# print all three query results with the help of their respective functions.


most_popular_articles()
print("\n")
most_popular_authors()
print("\n")
request_error_days()
