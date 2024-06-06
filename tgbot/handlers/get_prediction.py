from aiogram import Router, Bot, types,F
from aiogram.types import Message, FSInputFile
# from aiogram.filters.content_types import ContentTypesFilter
from tgbot.config import load_config

from tgbot.binance.config import (botB, pairs, TIMEFRAME, KLINES_LIMITS, POINTS_TO_ENTER, USE_OPEN_CANDLES)
from tgbot.binance import indicators as ind

from aiogram.filters import Command
from tgbot.misc.texts import messages
from tgbot.misc.data import timeframe as tf
from tgbot.misc.get_all_crypto import get_all_crypto
from tgbot.misc.calc_indicators import calculate
from tgbot.misc.build_chart import build_chart,build_stat_chart
from tgbot.misc.states import getPre,getPre2

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from tgbot.db.users_update import reg_user, add_set,update_counter

config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

get_router = Router()

@get_router.callback_query(lambda c: c.data=="get_prediction")
async def user_start(callback_query: types.callback_query, state: FSMContext): 
    userid = callback_query.from_user.id
    
    await bot.send_message(userid, messages["send_currecy"])
    await state.set_state(getPre.pair)
    
@get_router.message(F.text, getPre.pair)
async def user_start(message: Message, state: FSMContext):
    userid = message.from_user.id
    crypto = await get_all_crypto()
    user_pair = message.text.upper()
    if user_pair in crypto:
        
        await state.update_data(pair = user_pair)
        
        await bot.send_message(userid, messages["send_timeframe"])
        await state.set_state(getPre.timeframe)
    else:
        await bot.send_message(userid, "Нет такой пары, введите еще раз\nПолучить список всех пар можно командой /getcur")
        await state.set_state(getPre.pair)
    
    
@get_router.message(F.text, getPre.timeframe)
async def user_start(message: Message, state: FSMContext):
    userid = message.from_user.id
    
    await state.update_data(timeframe=message.text)
    
    if message.text not in tf:
        await bot.send_message(userid, "Неверный timeframe\n" + messages["send_timeframe"])
        await state.set_state(getPre.timeframe)
    else:
        await bot.send_message(userid, "Проверяем наши индикаторы...")
        await state.update_data(timeframe=message.text)
        user_data = await state.get_data()
        await add_set(user_data['timeframe'],user_data['pair'],userid)    
        await state.clear()
        
        await build_chart(userid)
        
        photo = FSInputFile('tgbot/img/' + str(userid) + '.png')
        await bot.send_photo(userid, photo , caption="Индикаторы")
        
        prediction = calculate(userid)
        if prediction >= 18:
            await bot.send_message(userid, messages["short"])
        elif prediction <= 4:
            await bot.send_message(userid, messages["long"])
        else:
            await bot.send_message(userid, messages["netrual"])
        
        await update_counter(userid)
        await bot.send_message(userid, messages["warning"])
        
        
@get_router.callback_query(lambda c: c.data=="view_stats")
async def user_start(callback_query: types.callback_query, state: FSMContext): 
    userid = callback_query.from_user.id
    
    await bot.send_message(userid, messages["send_currecy"])
    await state.set_state(getPre2.pair)
    
@get_router.message(F.text, getPre2.pair)
async def user_start(message: Message, state: FSMContext):
    userid = message.from_user.id
    crypto = await get_all_crypto()
    user_pair = message.text.upper()
    if user_pair in crypto:
        
        await state.update_data(pair = user_pair)
        
        await bot.send_message(userid, messages["send_timeframe"])
        await state.set_state(getPre2.timeframe)
    else:
        await bot.send_message(userid, "Нет такой пары, введите еще раз\nПолучить список всех пар можно командой /getcur")
        await state.set_state(getPre2.pair)
    
    
@get_router.message(F.text, getPre2.timeframe)
async def user_start(message: Message, state: FSMContext):
    userid = message.from_user.id
    
    await state.update_data(timeframe=message.text)
    
    if message.text not in tf:
        await bot.send_message(userid, "Неверный timeframe\n" + messages["send_timeframe"])
        await state.set_state(getPre2.timeframe)
    else:
        await bot.send_message(userid, "Отримуємо новітні дані...")
        await state.update_data(timeframe=message.text)
        user_data = await state.get_data()
        await add_set(user_data['timeframe'],user_data['pair'],userid)    
        
        await build_stat_chart(userid)
        pair = user_data['pair']
        response = botB.ticker24hr(
            symbol=pair,
        )
        
        mess = f'''Графік пари {response["symbol"]}
Ціна наразі: {response["prevClosePrice"]}
Зміна ціни за остані 24год: {response["priceChangePercent"]}
Максимум ціни за 24год: {response["highPrice"]}
Мінімум ціни за 24год: {response["lowPrice"]}
Об'єм торгім: {response["volume"]}
'''
        
        
        
        photo = FSInputFile('tgbot/img/' + str(userid) + 'stat.png')
        await bot.send_photo(userid, photo , caption=mess)
        await state.clear()
        
        
        
    