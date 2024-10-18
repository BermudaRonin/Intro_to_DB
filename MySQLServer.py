import mysql.connector
from mysql.connector import errorcode


cursor = mydb.cursor()


def main():
    try:
        # Connect to client
        client = mysql.connector.connect(
            host="localhost", user="root", passwd="root", database="mydatabase"
        )

        cursor = client.cursor()

        # Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    
        # Terminate connection
        cursor.close()
        client.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)


if __name__ == "__main__":
    main()
