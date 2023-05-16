import mysql.connector

db_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sistema_hospital"
)

def create_hospital(name: str, address: str, cep: str):
    cursor = db_conn.cursor()
    
    try:
        query: str = "INSERT INTO Hospital(nome, endereco, cep) VALUES(%(name)s, %(address)s, %(cep)s)"
        query_params: dict = {"name": name, "address": address, "cep": cep}
        cursor.execute(query, query_params)
        db_conn.commit()
    except:
        print("Falha ao inserir os dados")
    finally:
        print("Dados salvos com sucesso!")

    cursor.close()
    
def read_all_hospital():
    cursor = db_conn.cursor()
    
    try:
        query: str = "SELECT * FROM Hospital"
        cursor.execute(query)
        result = cursor.fetchall()
        
        print("\n+---------- Hospitais ----------+\n")
        for row in result:
            print(f"Id: {row[0]}\nNome: {row[1]}\nEndereco: {row[2]}\nCep: {row[3]}")

            print("+--------------------+")
        print("\n+---------- Fim ----------+")
        
    except:
        print("Falha ao completar a tarefa")


    cursor.close()

def update_hospital(hospital_name: str, name: str, address: str, cep: str):
    cursor = db_conn.cursor()

    try:
        query: str = "UPDATE Hospital SET nome = %(name)s, endereco = %(address)s, cep = %(cep)s WHERE nome = %(hospital_name)s"
        query_params: dict = {"name": name, "address": address, "cep": cep, "hospital_name": hospital_name}
        cursor.execute(query, query_params)
        db_conn.commit()
    except:
        print("Ocorreu um erro ao executar a acao")
    finally:
        print("Dados alter com sucesso!")
        
    cursor.close()
    
def delete_hospital(name: str):
    cursor = db_conn.cursor()

    try:
        query = "DELETE FROM Hospital WHERE nome = %(name)s"
        query_params = {'name': name}
        cursor.execute(query, query_params) # type: ignore
        db_conn.commit()
    except:
        print("Falha ao deletar os dados")
    finally:
        affected_rows = cursor.rowcount
        print(f"{affected_rows} registros atualizados.")

def main() -> None:
    leave: bool = False
    choice: int = 0

    print("Bem-vindo,\nOque deseja fazer?\n")
    while not leave:
        print("\n0 - Sair\n1 - Registrar Hospital\n2 - Listar Hospitais\n3 - Atualizar Hospital\n4 - Deletar Hospital")
        try:
            choice = int(input("Escolha: "))
        except:
            print("\nSomente numeros sao validos!")

        if choice == 0:
            print("\nAté mais!")
            break

        elif choice == 1:
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
                create_hospital(name, address, cep)

        elif choice == 2:
            try:
                read_all_hospital()                
            except:
                print("Falha ao completar a requisicao")

        elif choice == 3:
            hospital_name: str = ""
            name: str = ""
            address: str = ""
            cep: str = ""
            try:
                hospital_name = str(input("(Hospital)[UPDATE] Nome do hospital a ser alterado: "))
                name = str(input("(Hospital)[UPDATE] Digite o nome: "))
                address = str(input("(Hospital)[UPDATE] Digite o endereco: "))
                cep = str(input("(Hospital)[UPDATE] Digite o CEP: "))
            except:
                print("Valores invalidos!")
            finally:
                update_hospital(hospital_name=hospital_name, name=name, cep=cep, address=address)

        elif choice == 4:
            hospital_name: str = ""
            try:
                hospital_name = str(input("(Hospital)[DELETE] Nome do hospital a ser deletado: "))
            except:
                print("Valores invalidos!")
            finally:
                delete_hospital(hospital_name)

        else:
            print("Valor Invalido!\n")
            

if __name__ == "__main__":
    main()