import mysql.connector

db_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sistema_hospital"
)

def create_hospital(nome: str, endereco: str, cep: str):
    cursor = db_conn.cursor()
    
    try:
        query = '''
        INSERT INTO Hospital(nome, endereco, cep) VALUES(%s, %s, %s)
        '''
        hospital = (nome, endereco, cep)
        cursor.execute(query, hospital)
        db_conn.commit()
    except:
        print("Falha ao inserir os dados")
    finally:
        print("Dados salvos com sucesso!")

    cursor.close()
    
def read_all_hospital():
    cursor = db_conn.cursor()
    
    try:
        query = '''
        SELECT * FROM Hospital
        '''
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

def update_hospital(hospital_name: str, name: str, endereco: str, cep: str):
    cursor = db_conn.cursor()

    try:
        query = '''
        UPDATE Hospital SET nome = %s, endereco = %s, cep = %s WHERE nome = %s
        '''
        hospital = (name, endereco, cep, hospital_name)
        cursor.execute(query, hospital)
        db_conn.commit()
    except:
        print("Ocorreu um erro ao executar a acao")
    finally:
        print("Dados alter com sucesso!")
        
    cursor.close()
    
def delete_hospital(nome: str):
    cursor = db_conn.cursor()

    try:
        query = '''
        DELETE FROM Hospital WHERE nome = %s
        '''
        hospital = (nome)
        cursor.execute(query, hospital)
        db_conn.commit()
    except:
        print("Falha ao deletar os dados")
    finally:
        print("Dados deletados com sucesso!")

def main() -> None:
    sair = False
    escolha: int = 0

    print("Bem-vindo,\nOque deseja fazer?\n")
    while not sair:
        print("\n0 - Sair\n1 - Registrar Hospital\n2 - Listar Hospitais\n3 - Atualizar Hospital")
        try:
            escolha = int(input("Escolha: "))
        except:
            print("\nSomente numeros sao validos!")

        if escolha == 0:
            print("\nAté mais!")
            break

        elif escolha == 1:
            nome: str = ""
            endereco: str = ""
            cep: str = ""

            try:
                nome = str(input("(Hospital)Digite o nome: "))
                endereco = str(input("(Hospital)Digite o endereco: "))
                cep = str(input("(Hospital)Digite o CEP: "))
            except:
                print("Valores invalidos!")
            finally:
                create_hospital(nome, endereco, cep)

        elif escolha == 2:
            try:
                read_all_hospital()                
            except:
                print("Falha ao completar a requisicao")

        elif escolha == 3:
            nome_hospital: str = ""
            nome: str = ""
            endereco: str = ""
            cep: str = ""

            try:
                nome_hospital = str(input("(Hospital)[UPDATE] Nome do hospital a ser alterado: "))
                nome = str(input("(Hospital)[UPDATE] Digite o nome: "))
                endereco = str(input("(Hospital)[UPDATE] Digite o endereco: "))
                cep = str(input("(Hospital)[UPDATE] Digite o CEP: "))
            except:
                print("Valores invalidos!")
            finally:
                update_hospital(hospital_name=nome_hospital, name=nome, cep=cep, endereco=endereco)

        elif escolha == 4:
            nome_hospital: str = ""

            try:
                nome_hospital = str(input("(Hospital)[DELETE] Nome do hospital a ser deletado: "))

            except:
                print("Valores invalidos!")
                pass
            finally:
                delete_hospital(nome_hospital)
                
        else:
            print("Valor Invalido!\n")
            

if __name__ == "__main__":
    main()