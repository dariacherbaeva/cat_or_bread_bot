def db_add_user(user_id: int, username: str, chat_id: str, conn, cursor):
    cursor.execute('INSERT INTO user_info (user_id, username, chat_id) VALUES (?, ?, ?)',
                   (user_id, username, chat_id))
    conn.commit()


def db_add_message(message_text: str, user_id: str, previous_message_text: str,
                   next_message_text: str, timestamp, conn, cursor):
    cursor.execute(
        'INSERT INTO message (user_info_id, message_text, timestamp, previous_bot_message_text,'
        ' next_bot_message_text) VALUES (?, ?, ?, ?, ?)',
        (user_id, message_text, timestamp, previous_message_text, next_message_text))
    conn.commit()


def db_check_user_exists(user_id: str, cursor):
    cursor.execute('SELECT * FROM user_info WHERE user_id=?', (user_id,))
    result = cursor.fetchall()
    return True if result else False
