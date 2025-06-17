"""Библиотека для работы с бд"""
import sqlite3

def sql_execute(query:str, table_name:str,):
    con = sqlite3.Connection('db_main.db')
    cursor = con.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    con.execute(query)
    con.close()
    return 1

def chats_create():
    """Создает базу данных из времени сосания и id чата"""
    
    query = '''CREATE TABLE IF NOT EXISTS chats (
        "id_chat" INTEGER,
        "time" TEXT),
        UNIQUE(id_chat, id_user);;'''

    sql_execute(query, "chats")
    return 1

def db_user_create():
    """Создает таблицу с личными данными пользователей"""
    
    query = '''CREATE TABLE IF NOT EXISTS users (
        "id_user" INTEGER,
        "image_id" INTEGER),
        UNIQUE(id_chat, id_user);;'''

    sql_execute(query, "users")
    return 1

def db_user_chat_connect_create():
    """Создает таблицу связи чатов и пользователей"""
    
    query = '''CREATE TABLE IF NOT EXISTS chat_users (
        "id_chat" INTEGER,
        "id_user" INTEGER),
        UNIQUE(id_chat, id_user);'''

    sql_execute(query, "chat_users")
    return 1

def write_chat(new_time, chat_id):
    """Записывает значение времени сосания для нового id чата"""
    con = sqlite3.Connection('db_main.db')
    cursor = con.cursor()
    cursor.execute("""INSERT OR REPLACE INTO chats (id_chat, time) VALUES (?, ?)""", (chat_id, new_time))
    con.commit()
    con.close()
    return 1

def write_time(new_time, chat_id):
    """Записывает новое значение времени сосания по id чата"""
    con = sqlite3.Connection('db_main.db')
    con.execute("UPDATE chats SET time = ? WHERE id_chat = ?", (new_time, chat_id))
    con.commit()
    con.close()
    return 1

def write_user(id_chat, id_user):
    """Записывает нового пользователя в чат"""
    con = sqlite3.Connection('db_main.db')
    cursor = con.cursor()
    cursor.execute("""INSERT OR REPLACE INTO chat_users (id_chat, id_user) VALUES (?, ?)""", (id_chat, id_user))
    con.commit()
    con.close()
    return 1

def get_time(chat_id):
    """Возвращает значение времени сосания по id чата"""
    con = sqlite3.Connection('db_main.db')
    cursor = con.cursor()
    cursor.execute("SELECT time FROM chats WHERE id_chat = ?", (chat_id,))
    result = cursor.fetchone()
    con.close()
    return result[0]

def save_image(user_id, image_id):
    """Добавляет новое фото или обновляет существующее фото пользователя в базе данных."""
    con = sqlite3.connect('db_main.db')
    cursor = con.cursor()

    cursor.execute("SELECT image_id FROM users WHERE id_user = ?", (user_id,))
    existing = cursor.fetchone()

    if existing:
        cursor.execute("UPDATE users SET image_id = ? WHERE id_user = ?", (image_id, user_id))
    else:
        cursor.execute("INSERT INTO users (id_user, image_id) VALUES (?, ?)", (user_id, image_id))

    con.commit()
    con.close()
    return 1

def get_image(user_id:str):
    """Возвращает id картинки сосания по id чата"""
    con = sqlite3.Connection('db_main.db')
    cursor = con.cursor()
    cursor.execute("SELECT image_id FROM users WHERE id_user = ?", (user_id,))
    result = cursor.fetchone()
    con.close()
    return result

def get_users(chat_id) -> list:
    """Возвращает список всех пользователей в чате"""
    con = sqlite3.Connection('db_main.db')
    cursor = con.cursor()
    cursor.execute("SELECT id_user FROM chat_users WHERE id_chat = ?", (chat_id,))
    #result = list(cursor.fetchone())
    result = [row[0] for row in cursor.fetchall()]
    con.close()
    return result