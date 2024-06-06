import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs
from tgbot.config import  DB_URI

from tgbot.config import load_config
config = load_config(".env")

async def get_profile(userid):
    base = psycopg2.connect(dbname=config.db.database,
    user=config.db.user,
    password=config.db.password,
    host=config.db.host,)
    cur = base.cursor()
    data = (str(userid),)
    cur.execute('SELECT * FROM users WHERE id = %s',data)
    user = cur.fetchone()
    name = user[1]
    gets_advice = user[4]
    base.commit()
    cur.close()
    base.close()
    
    return name, gets_advice