# Open-Source Semantic Search Demo

This is a repo with the code to run a full semantic search demo using the Instructor embedding model, pgvector, and Flask.

## Requirements

You need Python3 installed. On Linux or Mac computers, this is already included, but you can verify the version by running `python --version`. For Windows you may need to install it.

We also need PostgreSQL, a popular relational database (RDBMS). You can install it on your computer, but you need to have the `pgvector` extension compiled as well. On Macs, this is bundled with newer versions of Postgres.app. On any platform, you can also install Docker and use the docker image:

```
docker pull pgvector/pgvector:pg16
```

Then you could run it with:

```
docker run --name pgvector -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d pgvector/pgvector:pg16
```

### Set up a Virtual Environment

This isn't required, but will generally make life a lot easier. We can set up a "virtual environment" in Python, which lets us install packages to that environment, rather than globally on our computer, which can cause conflicts and issues. It's also best to work in a virtual environment when working with Python!

```python -m venv venv```

This will create our virtual directory within a directory named `venv`, our last argument. You could call it anything you want though.

Now we activate the virtual environment, and any packages we install will only be installed there:

```source venv/bin/activate```

You should also see `(venv)` prepended to your prompt to let you know you're using the virtual environment.

### Install the necessary packages:

This should get all the packages you need to get it up and running:

```pip install flask InstructorEmbedding torch numpy tqdm sentence_transformers==2.2.2 psycopg2```

### Log in to the database and set up the extension and table:

You'll need the `psql` client installed, which is used for connecting to Postgres databases. You can then connect using:

```psql -U postgres -h localhost```

You'll be prompted to enter the password, which we set when we ran the container as `postgres`. Then, you should be in the `psql` shell. Run these commands:

```
postgres=# CREATE DATABASE news_search;
postgres=# \c news_search
postgres=# CREATE EXTENSION vector;
postgres=# CREATE TABLE articles (id BIGSERIAL PRIMARY KEY, published_date VARCHAR(40), title TEXT, embedding vector(768));
```
### Slim down the data file

Our data file is 1.2M rows! You're certainly welcome to try loading them all, but it might be best to try it with a smaller subset of article titles first. This gets the first 5000 rows (including an extra for the header row 😉):

```head -n 5001 abcnews-date-text.csv > first_5k_headlines.csv```

### Run the import script

Take a look at the import.py file. You'll see that it reads the data file, and for each row, generates a vector embedding using Instructor, which it inserts into the database. This may take a few minutes to run.

```python import.py first_5k_headlines.csv```

## Run the App

The app is built using Flask, a Python-based web framework. It has a single endpoint that accepts GET requests, in which case it returns an HTML file (`search.html`), or POST requests, in which case it returns JSON of the results.

It calculates the embedding for the search term on the fly, just like we did for the data embeddings, and uses cosine similarity (by default) to retrieve results.

To run the app:

```flask run```

Now visit http://localhost:5000/search
