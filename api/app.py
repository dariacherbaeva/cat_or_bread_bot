import sqlite3

from flask import Flask, request
from telethon import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel

from bot_app import config
from api_helpers import get_chat_last_message_by_bot

app = Flask(__name__)
conn = sqlite3.connect(config.SQLITE_DB_FILE, check_same_thread=False)


@app.route('/api/send-message', methods=['GET'])
def send_message():
    args = request.args
    api_id = args['api_id']
    api_hash = args['api_hash']
    message_text = args['message_text']
    client = TelegramClient('session', int(api_id), api_hash)
    client.connect()
    try:
        receiver = InputPeerUser(config.BOT_ID, 0)

        client.send_message(receiver, message_text, parse_mode='html')
    except Exception:
        return 'status: Error'
    return 'status: OK'


@app.route('/api/get-last-message', methods=['GET'])
def get_last_message():
    cursor = conn.cursor()
    args = request.args
    user_id = args['user_id']
    message = get_chat_last_message_by_bot(user_id, cursor)
    cursor.close()
    return message


if __name__ == '__main__':
    app.run(debug=True)
