import telebot
import sqlite3

import config
import dbworker
from db.db_helpers import db_check_user_exists, db_add_user, db_add_message

bot = telebot.TeleBot(config.token)

conn = sqlite3.connect(config.sqlite_db_file, check_same_thread=False)


@bot.message_handler(commands=["start"])
def cmd_start(message):
    cursor = conn.cursor()
    bot.send_message(message.chat.id, config.FIRST_QUESTION)
    dbworker.set_state(message.chat.id, config.States.S_FIRST_QUESTION.value)
    if not db_check_user_exists(message.from_user.id, cursor):
        db_add_user(message.from_user.id, message.from_user.username, message.chat.id, conn, cursor)
    cursor.close()


@bot.message_handler(commands=["reset"])
def cmd_reset(message):
    cursor = conn.cursor()
    bot.send_message(message.chat.id, config.FIRST_QUESTION)
    dbworker.set_state(message.chat.id, config.States.S_FIRST_QUESTION.value)
    if not db_check_user_exists(message.from_user.id, cursor):
        db_add_user(message.from_user.id, message.from_user.username, message.chat.id, conn, cursor)
    cursor.close()


@bot.message_handler(
    func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_FIRST_QUESTION.value)
def answer_first_question(message):
    cursor = conn.cursor()
    db_add_message(message.text, message.from_user.id,
                   config.FIRST_QUESTION, message.date, conn, cursor)
    text = message.text.lower()
    if text in config.YES_LIST:
        bot.send_message(message.chat.id, config.SECOND_QUESTION)
        dbworker.set_state(message.chat.id, config.States.S_SECOND_QUESTION.value)
    elif text in config.NO_LIST:
        bot.send_message(message.chat.id, config.CAT_RESULT)
        dbworker.set_state(message.chat.id, config.States.S_CAT_RESULT.value)
        bot.send_message(message.chat.id, config.RESTART)
    else:
        bot.send_message(message.chat.id, config.ERROR)
    cursor.close()


@bot.message_handler(
    func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_SECOND_QUESTION.value)
def answer_second_message(message):
    cursor = conn.cursor()
    db_add_message(message.text, message.from_user.id,
                   config.SECOND_QUESTION, message.date, conn, cursor)
    text = message.text.lower()
    if text in config.YES_LIST:
        bot.send_message(message.chat.id, config.CAT_RESULT)
        dbworker.set_state(message.chat.id, config.States.S_CAT_RESULT.value)
        bot.send_message(message.chat.id, config.RESTART)
    elif text in config.NO_LIST:
        bot.send_message(message.chat.id, config.BREAD_RESULT)
        dbworker.set_state(message.chat.id, config.States.S_BREAD_RESULT.value)
        bot.send_message(message.chat.id, config.RESTART)
    else:
        bot.send_message(message.chat.id, config.ERROR)
    cursor.close()


if __name__ == "__main__":
    bot.infinity_polling()
