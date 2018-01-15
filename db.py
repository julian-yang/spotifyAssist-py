import os
from urllib.parse import urlparse
import psycopg2

url = urlparse(os.environ["DATABASE_URL"])

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

cur = conn.cursor()

def hello():
    return 'hello world!'

def fetchUser():
    try:
        cur.execute("SELECT * from users")
        user = cur.fetchone()
        print("""user: {user}""".format(user=user), flush=True)
        return user
    except Exception as e:
        print("""err: {err}""".format(err=e), flush=True)
        return None 