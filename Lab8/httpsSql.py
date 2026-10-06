'''Using HTTPS, retrieve users (id, name, username, email) 
from a URL, store the data in an SQLite database, and 
display all the stored users.'''

import requests
import sqlite3

url = "https://jsonplaceholder.typicode.com/users"

# HTTPS GET request
users = requests.get(url).json()

# SQLite database
con = sqlite3.connect("users.db")
cur = con.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    username TEXT,
    email TEXT
)
""")

# Store data
for user in users:
    cur.execute(
        "INSERT OR REPLACE INTO users VALUES (?, ?, ?, ?)",
        (user["id"], user["name"], user["username"], user["email"])
    )

con.commit()

# Display data
cur.execute("SELECT * FROM users")

print("ID | Name | Username | Email")
print("-" * 60)

for row in cur.fetchall():
    print(row)

con.close()