from telebot import types


def main_markup():
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Что мне приготовить?")
    keyboard.add(button_1)
    return keyboard


def time_markup():
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="На завтрак 🥞")
    keyboard.add(button_1)
    button_2 = types.KeyboardButton(text="На обед 🍜")
    keyboard.add(button_2)
    button_3 = types.KeyboardButton(text="На ужин 🍲")
    keyboard.add(button_3)
    return keyboard


def receipt_markup():
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Другой рецепт 🔄")
    keyboard.add(button_1)
    button_2 = types.KeyboardButton(text="Выбрать другой приём пищи ↩")
    keyboard.add(button_2)
    return keyboard
