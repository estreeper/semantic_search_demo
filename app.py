from flask import Flask, request, jsonify, send_file
import psycopg2

import db
import instructor

app = Flask(__name__)

@app.route("/search", methods=['POST', 'GET'])
def search():
    if request.method == 'GET':
        return send_file('search.html')

    data = request.get_json()
    search_string = data.get('query')

    instruction = "Represent the news article question for retrieving relevant article titles:"
    embedding = "{0}".format(instructor.calculate_embedding(instruction, search_string))
    query = "SELECT title, published_date FROM articles ORDER BY embedding <=> %s LIMIT 10;"
    conn = db.create_conn()
    cur = conn.cursor()
    cur.execute(query, (embedding,))
    results = cur.fetchall()
    conn.close()

    return jsonify({'results': results}), 200
