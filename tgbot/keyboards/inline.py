from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardButton, InlineKeyboardBuilder
from aiogram import Bot, types
from aiogram.filters.callback_data import CallbackData
from typing import Optional


def main_menu_button():
    example = InlineKeyboardBuilder()
    example.add(types.InlineKeyboardButton(
        text='Профіль',
        callback_data='profile'
    ))
    example.add(types.InlineKeyboardButton(
        text='Інструкції',
        callback_data='instructions'
    ))
    example.add(types.InlineKeyboardButton(
        text='Список монет',
        callback_data='monets_list'
    ))
    example.add(types.InlineKeyboardButton(
        text='Отримати прогноз',
        callback_data='get_prediction'
    ))
    example.add(types.InlineKeyboardButton(
        text='Подивитись статистику',
        callback_data='view_stats'
    ))
    example.adjust(2)
    return example