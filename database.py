import mysql.connector
from dotenv import load_dotenv
from crypt import crypt_context
import os

# Load environment variables
load_dotenv()

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB")

# Connect to MySQL
def connect_to_mysql():
    try:
        db_connection = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB
        )
        print("Connected to MySQL successfully!")
        return db_connection
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None


# Inside database.py
def create_user(name, password, email):
    conn = connect_to_mysql()
    cursor = conn.cursor()
    query = "INSERT INTO users (name, password, email) VALUES (%s, %s, %s)"
    values = (name, password, email)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return cursor.lastrowid

#verification
def verify_user(email):
    conn = connect_to_mysql()
    if not conn:
        return None
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE email = %s"
    values = (email,)
    cursor.execute(query, values)
    result = cursor.fetchone()
    conn.close()

verify_user('philip.lominoque.a5d@ap.denso.com')

# Example usage
db_connection = connect_to_mysql()
if db_connection:
    # Do something with the connection
    db_connection.close()