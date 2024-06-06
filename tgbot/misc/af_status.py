import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs
from tgbot.config import  DB_URI

from tgbot.config import load_config
config = load_config(".env")

async def af_status(userid):
    base = psycopg2.connect(dbname=config.db.database,
    user=config.db.user,
    password=config.db.password,
    host=config.db.host,)
    cur = base.cursor()
    userid = str(userid)
    cur.execute('SELECT * FROM users ')
    users = cur.fetchall()
    answer = False
    for user in users:
        if user[0] == userid:
            answer = True
    base.commit()
    cur.close()
    base.close()
    return answer