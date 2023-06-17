import psycopg2
from table import create_table

try:
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host="postgres",
        port="5432",
        dbname="mydb",
        user="myuser",
        password="Pranav@321"
    )

    # Get a cursor object to interact with the database
    cursor = conn.cursor()

    # Call the create_table function to create the table
    create_table(cursor)

    # Commit the changes to the database
    conn.commit()

    # Close the cursor and database connection
    cursor.close()
    conn.close()

except psycopg2.OperationalError as e:
    print("Authentication Error: Failed to connect to the PostgreSQL server.")
    print(e)
