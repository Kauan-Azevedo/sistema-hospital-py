import mysql.connector
from hospital import create_hospital, read_all_hospital, update_hospital, delete_hospital
from clinica import create_clinica, read_all_clinicas
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
    print("Bem-vindo ao gerenciador de prontuarios,\nO que deseja fazer?\n")
    while leave is not True:
        print("0 - Sair\n\n1 - Registrar Hospital\n2 - Listar Hospitais\n3 - Atualizar Hospital\n4 - Deletar Hospital\n\n5 - Registrar Clinica\n6 - Listar Clinicas\n7 - Atualizar Clinica\n")
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
                
                if name == '' or address == '' or cep == '':
                    raise ValueError('Nome, Endereco e/ou Cep nao podem ser vazios')
            except ValueError as error:
                print(f"\nOcorreu um erro: {repr(error)}\n" )
                break
            else:
                create_hospital(db_conn, name, address, cep)

        elif choice == 2:
            os.system("clear")
            try:
                read_all_hospital(db_conn)                
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
            else:
                update_hospital(db_conn, hospital_name, name, cep, address)

        elif choice == 4:
            hospital_name: str = ""
            try:
                hospital_name = str(input("(Hospital)[DELETE] Nome do hospital a ser deletado: "))
            except:
                print("Valores invalidos!")
            else:
                delete_hospital(db_conn, hospital_name)

        elif choice == 5:
            os.system("clear")
            name: str = ""
            address: str = ""
            cep: str = ""
            hospital: str = ""
            try:
                name =  str(input("(Clinica)[CREATE] Digite o nome: "))
                address = str(input("(Clinica)[CREATE] Digite o endereco: "))
                cep = str(input("(Clinica)[CREATE] Digite o cep: "))
                hospital = str(input("(Clinica)[CREATE] Digite o nome do Hospital: "))

                if name == "" or address == "" or cep == "" or hospital == "":
                    raise ValueError("Nome, Endereco, Cep e/ou Hospital")
            except ValueError as error:
                print(f"\nOcorreu um erro: {repr(error)}")
                break
            else:
                create_clinica(db_conn, name, address, cep, hospital)

        elif choice == 6:
            os.system("clear")
            try:
                read_all_clinicas(db_conn)
            except:
                print("Falha ao completar a requisicao")


        else:
            print("Valor Invalido!\n")
            

if __name__ == "__main__":
    main()