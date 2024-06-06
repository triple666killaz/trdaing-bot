import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs
from tgbot.config import  DB_URI

from tgbot.config import load_config
config = load_config(".env")

# start bd/ connect and create if does'nt exists
async def postgre_start():
    base = psycopg2.connect(dbname=config.db.database,
    user=config.db.user,
    password=config.db.password,
    host=config.db.host,)
    cur = base.cursor()
    if base:
        print('data base connect Ok!')
    cur.execute('''CREATE TABLE IF NOT EXISTS users(
        id text primary key,
        name text,
        timeframe text,
        pair text,
        gets_advice int default 0
        )''')
    
    base.commit()
    cur.close()
    base.close()