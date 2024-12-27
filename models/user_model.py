from dbconfig import get_db_connection

def create_user_table():
    connection = get_db_connection()
    cursor = connection.cursor()

    # Create the users table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL
        )
    """)
    connection.commit()
    cursor.close()
    connection.close()

def insert_user(username, email):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO users (username, email)
        VALUES (%s, %s)
    """, (username, email))

    connection.commit()
    cursor.close()
    connection.close()

def get_users():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT id, username, email FROM users")
    users = cursor.fetchall()

    cursor.close()
    connection.close()

    return users
