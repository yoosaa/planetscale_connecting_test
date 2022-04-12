import os

from dotenv import load_dotenv
load_dotenv()
import pymysql.cursors
import certifi
from flask import Flask



app = Flask(__name__)

@app.route("/")
def index():
  result = {}

  try:
    connection = connectionSetting()

    try:
      with connection.cursor() as cur:
        sql = "SELECT `id` FROM `users` WHERE `email`=%s"
        cur.execute(sql, ('hp@example.com'))
        result = cur.fetchall()
        return str(result)
    except:
      return 'error!'

  except pymysql.MySQLError as e:
    return e


def connectionSetting ():
  return pymysql.connect(
    host= os.getenv("HOST"),
    user=os.getenv("USERNAME"),
    passwd= os.getenv("PASSWORD"),
    db= os.getenv("DATABASE"),
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor,
    ssl={
      'ca': certifi.where()
    },
  )




if __name__ == "__main__":
  app.run()