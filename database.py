import requests
import psycopg2

# Fetch data from API
response = requests.get('https://random-data-api.com/api/v2/users?size=100')
data = response.json()

# Connect to PostgreSQL database
conn = psycopg2.connect(
    host='localhost',
    port=5432,
    user='myuser',
    password='Pranav@321',
    database='mydb'
)
cursor = conn.cursor()

# Create table if it doesn't exist
create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        country TEXT,
        name TEXT,
        surname TEXT,
        gender TEXT
    )
'''
cursor.execute(create_table_query)
conn.commit()

# Insert data into the table
insert_query = '''
    INSERT INTO users (country, name, surname, gender)
    VALUES (%s, %s, %s, %s)
'''

for item in data:
    country = item['country']
    name = item['name']
    surname = item['surname']
    gender = item['gender']
    cursor.execute(insert_query, (country, name, surname, gender))
conn.commit()

# Verify the data
select_query = 'SELECT country, name, surname, gender FROM users'
cursor.execute(select_query)
fetched_data = cursor.fetchall()

for row in fetched_data:
    country, name, surname, gender = row
    print(f'Country: {country}, Name: {name}, Surname: {surname}, Gender: {gender}')

# Close the database connection
cursor.close()
conn.close()
