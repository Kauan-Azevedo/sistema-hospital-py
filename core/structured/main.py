import mysql.connector
import hospital
import os

db_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sistema_hospital"
)


def main() -> None:
    leave: bool = False
    choice: int = 0

    os.system("clear")
    print("Bem-vindo,\nOque deseja fazer?\n")
    while not leave:
        print("\n0 - Sair\n1 - Registrar Hospital\n2 - Listar Hospitais\n3 - Atualizar Hospital\n4 - Deletar Hospital")
        try:
            choice = int(input("Escolha: "))
        except:
            print("\nSomente numeros sao validos!")

        if choice == 0:
            os.system("clear")
            print("\nAté mais!")
            break

        elif choice == 1:
            os.system("clear")
            name: str = ""
            address: str = ""
            cep: str = ""
            try:
                name = str(input("(Hospital)[CREATE] Digite o nome: "))
                address = str(input("(Hospital)[CREATE] Digite o endereco: "))
                cep = str(input("(Hospital)[CREATE] Digite o CEP: "))
            except:
                print("Valores invalidos!")
            finally:
                hospital.create_hospital(db_conn, name, address, cep)

        elif choice == 2:
            os.system("clear")
            try:
                hospital.read_all_hospital(db_conn)                
            except:
                print("Falha ao completar a requisicao")

        elif choice == 3:
            hospital_name: str = ""
            name: str = ""
            address: str = ""
            cep: str = ""
            try:
                hospital_name = str(input("(Hospital)[UPDATE] Nome do hospital a ser alterado: "))
                name =  str(input("(Hospital)[UPDATE] Digite o nome: "))
                address = str(input("(Hospital)[UPDATE] Digite o endereco: "))
                cep = str(input("(Hospital)[UPDATE] Digite o CEP: "))
            except:
                print("Valores invalidos!")
            finally:
                hospital.update_hospital(db_conn, hospital_name=hospital_name, name=name, cep=cep, address=address)

        elif choice == 4:
            hospital_name: str = ""
            try:
                hospital_name = str(input("(Hospital)[DELETE] Nome do hospital a ser deletado: "))
            except:
                print("Valores invalidos!")
            finally:
                hospital.delete_hospital(db_conn, hospital_name)

        else:
            print("Valor Invalido!\n")
            

if __name__ == "__main__":
    main()