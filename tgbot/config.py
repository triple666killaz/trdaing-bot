from dataclasses import dataclass


@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    database: str


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]
    use_redis: bool


@dataclass
class Miscellaneous:
    other_params: str = None


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig
    misc: Miscellaneous


def load_config(path: str = None):

    return Config(
        tg_bot=TgBot(
            token="5257942822:AAFqBBqGZs6UJZsF3fJ6fY-f8pCFQelxXRw",
            admin_ids=[],
            use_redis=False,
        ),
        db=DbConfig(
            host='localhost',
            password='2545',
            user='postgres',
            database='testuni'
        ),
        misc=Miscellaneous()
    )
    
DB_URI = "jdbc:postgresql://localhost:5432/testuni"
    

