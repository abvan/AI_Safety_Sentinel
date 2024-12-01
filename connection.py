import psycopg2


#function to connect to the DB
def connect_to_db() :
    dbname = '<Enter DB Name>'
    user = '<Enter UserName>'
    password = '<Enter Password>'
    host = '<Enter Host>'  # e.g., 'localhost' or an IP address
    port = '<Enter port number>'  # Default PostgreSQL port is 5432

    connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
    print("Connection to the database was successful!")
    return connection
    

