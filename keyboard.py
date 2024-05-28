from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard_1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = KeyboardButton('Отправь фотку машины')
    button_2 = KeyboardButton('Перейти на следующую клавиатуру')
    keyboard.add(button_1, button_2)



def get_keyboard_2():
    keyboard_2 = ReplyKeyboardMarkup(resize_keyboard=True)
    button_3 = KeyboardButton('Отправь фотку мотоцикла')
    button_4 = KeyboardButton('Вернуться на 1 клавиутуру')
    keyboard_2.add(button_3, button_4)
