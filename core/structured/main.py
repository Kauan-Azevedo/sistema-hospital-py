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
        print("\n0 - Sair\n1 - Registrar Hospital\n2 - Listar Hospitais\n3 - Atualizar Hospital")
        try:
            escolha = int(input("Escolha: "))
        except:
            print("\nSomente numeros sao validos!")

        if escolha == 0:
            print("\nAté mais!\n\n")
            break
        elif escolha == 1:
            try:
                nome = str(input("(Hospital)Digite o nome: "))
                endereco = str(input("(Hospital)Digite o endereco: "))
                cep = str(input("(Hospital)Digite o CEP: "))
            except:
                print("Valores invalidos!")
                pass
            finally:
                if not nome == "" or not endereco == "" or not cep == "":
                    print("Dados salvos!")
                else:
                    print("Nome, Endereco e/ou Cep invalido(s)")

        else:
            print("Valor Invalido!\n")


if __name__ == "__main__":
    main()