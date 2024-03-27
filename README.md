# Open-Source Semantic Search Demo

This is a repo with the code to run a full semantic search demo using the Instructor embedding model, pgvector, and Flask.

## Requirements

You need PostgreSQL installed, and you need to have the `pgvector` extension compiled as well. You can also use the docker image.

```
docker pull pgvector/pgvector:pg16
```

### Install the necessary packages:

```pip install flask InstructorEmbedding torch numpy tqdm sentence_transformers==2.2.2 psycopg2```

### Log in to the database and set up the extension and table:

```
psql -U postgres
postgres=# CREATE DATABASE news_search;
postgres=# \c news_search
postgres=# CREATE EXTENSION vector;
postgres=# CREATE TABLE articles (id BIGSERIAL PRIMARY KEY, published_date VARCHAR(40), title TEXT, embedding vector(768));
```
### Slim down the data file

This gets the first 5000 rows:

```head -n 5001 abcnews-date-text.csv > first_5k_headlines.csv```

### Run the import script

```python import.py first_5k_headlines.csv```

## Run the App

The app is a single endpoint that accepts GET requests, in which case it returns an HTML file, or POST requests, in which case it returns JSON of the results.

It calculates the embedding for the search term on the fly, just like it did for the data embeddings, and uses consine similarity (by default) to retrieve results.

```flask run```

Now visit http://localhost:5000/search
