from aiogram import Router, Bot, types
from aiogram.types import Message, FSInputFile
from tgbot.config import load_config
from datetime import datetime
from aiogram.fsm.context import FSMContext

from tgbot.binance.config import (botB, pairs, TIMEFRAME, KLINES_LIMITS, POINTS_TO_ENTER, USE_OPEN_CANDLES)
from tgbot.binance import indicators as ind

from aiogram.filters import Command
from tgbot.misc.texts import messages
from tgbot.misc.af_status import af_status
from tgbot.misc.get_info import get_profile
from tgbot.misc.get_time import get_time
from tgbot.misc.get_all_crypto import get_all_crypto

from tgbot.keyboards.inline import main_menu_button

from tgbot.db.users_update import reg_user, add_set
user_router = Router()

config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')


@user_router.message(Command("start"))
async def user_start(message: Message):
    userid = message.from_user.id
    name = message.from_user.first_name
    
    status = await af_status(userid)
    if status == False:
        await reg_user(userid,name)
        
    btn = main_menu_button()
    await bot.send_message(userid, messages["gretting"],reply_markup = btn.as_markup())
    
    
@user_router.callback_query(lambda c: c.data=="instructions")
async def user_start(callback_query: types.callback_query, state: FSMContext): 
    userid = callback_query.from_user.id
    
    await bot.send_message(userid, messages["instructions"])

@user_router.callback_query(lambda c: c.data=="profile")
async def user_start(callback_query: types.callback_query, state: FSMContext): 
    userid = callback_query.from_user.id
    name, advices = await get_profile(userid)
    time = get_time()
    print(type(time))
    
    await bot.send_message(userid,f"Ваш id: {userid}\nИмя: {name}\nКоличество полученых сигналов: {advices}" )
    
@user_router.callback_query(lambda c: c.data=="monets_list")
async def user_start(callback_query: types.callback_query, state: FSMContext): 
    userid = callback_query.from_user.id
    await get_all_crypto()
    
    file = FSInputFile('tgbot/misc/crypto.txt')
    await bot.send_document(userid, file)
