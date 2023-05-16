def create_hospital(db_conn, name: str, address: str, cep: str):
    cursor = db_conn.cursor()
    
    try:
        query: str = "INSERT INTO Hospital(nome, endereco, cep) VALUES(%(name)s, %(address)s, %(cep)s)"
        query_params: dict = {"name": name, "address": address, "cep": cep}
        cursor.execute(query, query_params)
        db_conn.commit()
    except:
        print("Falha ao inserir os dados")
    else:
        print("Dados salvos com sucesso!")

    cursor.close()
    
def read_all_hospital(db_conn):
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

def update_hospital(db_conn, hospital_name: str, name: str, address: str, cep: str):
    cursor = db_conn.cursor()

    try:
        query: str = "UPDATE Hospital SET nome = %(name)s, endereco = %(address)s, cep = %(cep)s WHERE nome = %(hospital_name)s"
        query_params: dict = {"name": name, "address": address, "cep": cep, "hospital_name": hospital_name}
        cursor.execute(query, query_params)
        db_conn.commit()
    except:
        print("Ocorreu um erro ao executar a acao")
    else:
        print("Dados alterados com sucesso!")
        
    cursor.close()
    
def delete_hospital(db_conn, name: str):
    cursor = db_conn.cursor()

    try:
        query = "DELETE FROM Hospital WHERE nome = %(name)s"
        query_params = {'name': name}
        cursor.execute(query, query_params) # type: ignore
        db_conn.commit()
    except:
        print("Falha ao deletar os dados")
    else:
        affected_rows = cursor.rowcount
        print(f"{affected_rows} registros atualizados.")

