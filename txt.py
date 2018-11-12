#!/usr/bin/python

import psycopg2


# psql query processing function
def read_psql_data(query):
    # we first establish connection with the news database
    db = psycopg2.connect(database="news")
    # initialize the cursor which will fetch our data
    c = db.cursor()
    # execute our query
    c.execute(query)
    # temporary store fetched data from the cursor
    tempVal = c.fetchall()
    # initiliaze a counter for loop below
    i = 0
    while(i < len(tempVal)):
        # check if query is from question (1) or (2) and if so, proceed
        if "articles.title" in query or "authors.name" in query:
            # fetch the first cell of the returned array from
            temp = tempVal[i]
            # print in
            print("\"" + str(temp[0]) + "\" - " + str(temp[1]) + " views")
            # increment counter for next array cell
            i = i + 1
            # if query is from question (3), proceed here
        else:
            # same process as loop
            temp = tempVal[i]
            print(str(temp[0]) + " - " + str(temp[1]) + "% errors")
            i = i + 1
    # finished printing formatted text - close database connection
    db.close()


if __name__ == '__main__':
    # print first question
    print("\n1. What are the most popular three articles of all time?")
    # create query (selecting title from articles,
    # and count where slug of articles is equivalent to a substring of log.path
    # - ordering by count and setting the fetched data limit to 3)
    query = "select articles.title, count(*) as num from log, "\
        "articles where articles.slug = substr(log.path, 10) "\
        "group by articles.title order by num desc limit 3"
    # process query
    read_psql_data(query)

    # print second question
    print("\n2. Who are the most popular article authors of all time?")
    # create query (selecting names from author table and count when log
    # status is OK and the id of author is equivalent to the author from
    # articles, slug from articles is equivalent to the substring of log.path
    # - ordering by num (count) and descending order)
    query = "select authors.name, count(*) as num from articles, authors, "\
        "log where log.status = '200 OK' and authors.id = articles.author "\
        "and articles.slug = substr(log.path, 10) group by authors.name "\
        "order by num desc"
    # process query
    read_psql_data(query)

    # REQUESTS PER DAY (for validation purposes of outputted values)
    # query = "select date, count(*) as totalrequests from
    # (select date(log.time), count(substring(log.status, 0, 4)) as
    # counterperday from log group by log.time)as foo group by date
    # order by totalrequests desc"

    # ERRORS PER DAY (for validation purposes of outputted values)
    # query = "select date, count(*) as errorrequests from
    # (select date(log.time), count(substring(log.status, 0, 4)) as
    # counterperday from log where substring(log.status, 0, 4)::INTEGER >= 400
    #  group by log.time)as foo group by date order by errorrequests desc"

    # (ERRORS PER DAY / TOTAL REQUESTS PER DAY) * 100 = ERROR PERCENTAGE
    # print third question
    print("\n3. On which days did more than 1% of requests lead to errors?")
    # create query (calculating errors per day in subquery, then
    # calculating percentage by dividing the calculated daily errors by
    # another subquery which calculates the total errors per day and multiply
    # it by 100 - after finishing the process,
    # we order by the error percentage in descending and set limit to 1)
    query = "select date, totalFailure from (select date(log.time), "\
        "round((sum(case when substring(log.status, 0, 4):: INTEGER >= 400 "\
        "then 1 else 0 end) * 100.0)::DECIMAL / (count(log.status)), 1) "\
        "as totalFailure from log group by date(log.time) "\
        "order by totalFailure desc) as foo where totalFailure >= 1"
    # process query
    read_psql_data(query)
