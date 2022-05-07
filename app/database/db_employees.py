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


def get_employee_by_num_employee(num_employee):
    """Get the employee by num_employee from the database."""
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT * FROM employees
            WHERE num_employee = %s
        """, (num_employee,))
        employee = cursor.fetchone()
        connection.close()
        return employee
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None


def insert_employee(data):
    """Insert a new employee into the database."""
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO users(num_employee, name, lastname, email, password, id_rol)
            VALUES(%s, %s, %s, %s, %s, %s)
        """, data)
        connection.commit()
        connection.close()
        return True
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return False