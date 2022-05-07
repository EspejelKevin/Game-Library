import psycopg2
from decouple import config


def connect():
    """Connect to the PostgreSQL database. Returns a database connection."""
    return psycopg2.connect(
        database="game-library",
        user=config("DB_USERNAME"),
        password=config("DB_PASSWORD"),
        host=config("DB_HOST"),
    )


def get_user_by_username(username):
    """Get the user by username from the database."""
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT * FROM users
            WHERE username = %s
        """, (username,))
        user = cursor.fetchone()
        connection.close()
        return user
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None


def insert_user(data):
    """Insert a new user into the database."""
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO users(username, email, password, name, lastname, age)
            VALUES(%s, %s, %s, %s, %s, %s)
        """, data)
        connection.commit()
        connection.close()
        return True
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return False

