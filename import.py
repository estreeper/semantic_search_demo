import csv
import psycopg2
import sys

import db
import instructor

if len(sys.argv) != 2:
    print("Error: you should provide the file path as an argument to this script")
    sys.exit(1)

data_file = sys.argv[1]
conn = db.create_conn()
cur = conn.cursor()

with open(data_file, 'r') as f:
    reader = csv.reader(f)
    next(reader)  # skip the header
    count = 0
    for row in reader:
        published_date = row[0]
        title = row[1]
        embedding = instructor.calculate_embedding('Represent the news article title for retrieval:', title)
        query = 'INSERT INTO articles (published_date, title, embedding) VALUES (%s, %s, %s)'
        data = (published_date, title, embedding)
        cur.execute(query, data)
        count += 1
        if count % 500 == 0:
            print("On record {0}".format(count))

conn.commit()
cur.close()
conn.close()
