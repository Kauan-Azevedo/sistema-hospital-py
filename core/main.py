import mysql.connector

db_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sistema-hospital"
)

cursor = db_conn.cursor()
cursor.close()

def main() -> None:
    sair = False

    print("Bem-vindo")
    while not sair:
        ...


if __name__ == "__main__":
    main()