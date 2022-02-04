import os

import psycopg2
from dotenv import load_dotenv

load_dotenv


def init_db():
    # DBの情報誌を取得
    dsn = os.environ.get('DATABASE_URL')
    # print(dsn)
    # DBに接続(コネクションを貼る)
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    # SQLを用意
    with open('schema.sql', encoding="utf-8") as f:
        sql = f.read()
    # SQLを実行
    cur.execute(sql)
    sql = """CREATE TABLE users (
                                          name TEXT,
                                          age INTEGER
                                      );"""
    # SQLを実行
    cur.execute(sql)
    # 実行状態を保存
    conn.commit()
    # コネクションを閉じる
    conn.close()

    def register_user(name, age):
        dsn = os.environ.get('DATABASE_URL')
        conn = psycopg2.connect(dsn)
        cur = conn.cursor()
        # SQLを用意
        sql = "INSERT INTO users (name, age) VALUES (%(name)s, %(age)s)"
        # SQLを実行
        cur.execute(sql, {'name': name, 'age': age})
        conn.commit()
        conn.close()

    def all_users():
        dsn = os.environ.get('DATABASE_URL')
        conn = psycopg2.connect(dsn)
        cur = conn.cursor()
        sql = "SELECT * FROM users;"
        cur.execute(sql)
        users = cur.fetchall()
        conn.commit()
        conn.close()
        return users

    def main():
        init_db()

        msg = """===== Welcome to CRM Application =====
                    [S]how: Show all users info
                    [A]dd: Add new user
                    [Q]uit: Quit The Application
                ======================================
        """
        print(msg)

        register_user(name, age)

        users = all_users()
        print(users)

        command = input('Your command > ')
        if command == 'A':
            name = input('New user name > ')
            age = input('New user age > ?')
            register_user(name, age)

    if __name__ == '__main__':
        main()
