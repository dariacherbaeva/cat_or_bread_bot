import telebot
import config
import dbworker

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.send_message(message.chat.id, config.FIRST_QUESTION)
    dbworker.set_state(message.chat.id, config.States.S_FIRST_QUESTION.value)


@bot.message_handler(commands=["reset"])
def cmd_reset(message):
    bot.send_message(message.chat.id, config.FIRST_QUESTION)
    dbworker.set_state(message.chat.id, config.States.S_FIRST_QUESTION.value)


@bot.message_handler(
    func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_FIRST_QUESTION.value)
def answer_first_question(message):
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


@bot.message_handler(
    func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_SECOND_QUESTION.value)
def answer_second_message(message):
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


if __name__ == "__main__":
    bot.infinity_polling()
