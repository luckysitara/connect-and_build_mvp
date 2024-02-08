import mysql.connector

# Connect to the MySQL server
connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Create a cursor object
cursor = connection.cursor()

# Example query
query = "SELECT * FROM your_table"

# Execute the query
cursor.execute(query)

# Fetch the results
results = cursor.fetchall()

# Process the results
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()

