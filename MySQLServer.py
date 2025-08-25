# MySQLServer.py
import mysql.connector
from mysql.connector import Error

try:
    # 1. Connect to MySQL server
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Mageza@20252'  # keep the quotes
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # 2. Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    # 3. Close cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
