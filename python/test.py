import sqlite3

def get_user_data(username):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    # Vulnerable SQL query - no input sanitization
    query = "SELECT * FROM users WHERE username='" + username + "'"

    cursor.execute(query)
    user_data = cursor.fetchone()

    connection.close()

    return user_data

username = input("Enter username: ")
user_data = get_user_data(username)
print("User data:", user_data)
