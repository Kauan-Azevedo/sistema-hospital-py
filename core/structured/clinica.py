def create_clinica(db_conn, name: str, address: str, cep:str, hospital: str):
    cursor = db_conn.cursor()

    try:
        query: str = "INSERT INTO Clinica(nome, endereco, cep, Hospital_idHospital) VALUES (%(name)s, %(address)s, %(cep)s, (SELECT nome FROM Hospital WHERE nome = %(hospital)s)"
        query_params: dict = {"name": name, "address": address, "cep": cep, "hospital": hospital}
        cursor.execute(query, query_params)
        db_conn.commit() 
    except:
        print("Falha ao inserir os dados")
    else:
        print("Dados salvos com sucesso!")
    cursor.close()

def read_all_clinicas(db_conn):
    cursor = db_conn.cursor()

    try:
        hospital_query: str = ""
        query: str = "SELECT * FROM Clinica"
        cursor.execute(query)
        result = cursor.fetchall()
                
        print("\n+---------- Clinica ----------+\n")
        for row in result:
            hospital_query: str = f"SELECT nome FROM hospital WHERE nome = {row}"
            print(f"Id: {row[0]}\nNome: {row[1]}\nEndereco: {row[2]}\nCep: {row[3]}\nNome do Hospital: {hospital_query}")

            print("+--------------------+")
        print("\n+---------- Fim ----------+")
        pass
    except:
        print("Falha ao completar a tarefa")
        
    cursor.close()

