import logging
import os

from tgbot.binance.binance_api import Binance

botB = Binance(
    API_KEY='Iw5zIWa7OYqgVicrZaH16Jad2nfZIAfrh0dKScnkTIpOssLdEerT31OvOJwNGeOo',
    API_SECRET='9gezdReZ66fsQQsRxcpDSbkYnZqknxhBJozlRZdRo40qAGNOJrbdGmhQFx0f7Joc'
)

"""
    Пропишите пары, на которые будет идти торговля.
    base - это базовая пара (BTC, ETH,  BNB, USDT) - то, что на бинансе пишется в табличке сверху
    quote - это квотируемая валюта. Например, для торгов по паре NEO/USDT базовая валюта USDT, NEO - квотируемая
"""
pairs = [
   {
        'base': 'ETH',
        'quote': 'ADA',
        'spend_sum': 0.02,  # Сколько тратить base каждый раз при покупке quote
        'profit_markup': 1, # Какой навар нужен с каждой сделки? (1=1%)
        'use_stop_loss': True, # Нужно ли продавать с убытком при падении цены
        'stop_loss': 1,   # 1% - На сколько должна упасть цена, что бы продавать с убытком
        'stop_loss2': 2,  # вторая ступень если цена больше от закупочной на %
        'stop_loss3': 3,  # третья ступень если цена больше от закупочной на %
        'stop_loss4': 4,  # четвертая ступень если цена больше от закупочной на %
        'stop_loss5': 5,  # пятая ступень если цена больше от закупочной на %
        'percent_for_stop2':2,  #процент на какой должна измениться цена для применения второй ступени stop_loss
        'percent_for_stop3':3,  #процент на какой должна измениться цена для применения третьей ступени stop_loss
        'percent_for_stop4':5,  #процент на какой должна измениться цена для применения четвертой ступени stop_loss
        'percent_for_stop5':10,  #процент на какой должна измениться цена для применения пятой ступени stop_loss
        'active': True,
    }, {
        'base': 'USDT',
        'quote': 'NEO',
        'spend_sum': 11,  # Сколько тратить base каждый раз при покупке quote
        'profit_markup': 1, # Какой навар нужен с каждой сделки? (0.001 = 0.1%)
        'use_stop_loss': True, # Нужно ли продавать с убытком при падении цены
        'stop_loss': 1,   # 1% - На сколько должна упасть цена, что бы продавать с убытком
        'stop_loss2': 2,  # вторая ступень если цена больше от закупочной на %
        'stop_loss3': 3,  # третья ступень если цена больше от закупочной на %
        'stop_loss4': 4,  # четвертая ступень если цена больше от закупочной на %
        'stop_loss5': 5,  # пятая ступень если цена больше от закупочной на %
        'percent_for_stop2':2,  #процент на какой должна измениться цена для применения второй ступени stop_loss
        'percent_for_stop3':3,  #процент на какой должна измениться цена для применения третьей ступени stop_loss
        'percent_for_stop4':5,  #процент на какой должна измениться цена для применения четвертой ступени stop_loss
        'percent_for_stop5':10,  #процент на какой должна измениться цена для применения пятой ступени stop_loss
        'active': False,
    }
]

KLINES_LIMITS = 200
POINTS_TO_ENTER = 1


"""
    USE_OPEN_CANDLES = True - использовать последнюю (текущую) свечу для расчетов
    USE_OPEN_CANDLES = False - Использовать только закрытые свечи

    Например, если USE_OPEN_CANDLES = False и таймфрейм часовой, и время 13:21, то будут браться свечи до 13:00.
    После 14:00 свеча с 13:00 по 14:00 тоже попадет в выборку, но не будет браться 14:00 - 15:00 и т.п.
"""
USE_OPEN_CANDLES = True 


TIMEFRAME = "1h"
'''
    Допустимые интервалы:
    •    1m     // 1 минута
    •    3m     // 3 минуты
    •    5m    // 5 минут
    •    15m  // 15 минут
    •    30m    // 30 минут
    •    1h    // 1 час
    •    2h    // 2 часа
    •    4h    // 4 часа
    •    6h    // 6 часов
    •    8h    // 8 часов
    •    12h    // 12 часов
    •    1d    // 1 день
    •    3d    // 3 дня
    •    1w    // 1 неделя
    •    1M    // 1 месяц
'''