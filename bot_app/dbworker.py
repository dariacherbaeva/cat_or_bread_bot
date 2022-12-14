from vedis import Vedis
import config


def get_current_state(user_id):
    with Vedis(config.VEDIS_DB_FILE) as db:
        try:
            return db[user_id].decode()
        except KeyError:
            return config.States.S_START.value


def set_state(user_id, value):
    with Vedis(config.VEDIS_DB_FILE) as db:
        try:
            db[user_id] = value
            return True
        except Exception:
            raise False
