def get_chat_last_message_by_bot(user_id: str, cursor):
    cursor.execute('SELECT next_bot_message_text FROM message WHERE user_info_id=? ORDER BY id DESC LIMIT 1',
                   (user_id,))
    result = cursor.fetchall()
    return result[0][0]
