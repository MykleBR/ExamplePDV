import pymysql
# aqui teriam constantes com credenciais do banco mais foram removidas!
class MySQLDatabase:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = database


    def connect(self):
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db_name,
            )
            self.cursor = self.connection.cursor()
            print('Conexão bem sucedida!')
        except Exception as e:
            print(f'Erro na conexão com o banco de dados: {e}')

    def disconnect(self):
        try:
            self.connection.close()
            print('Desconexão bem sucedida!')
        except Exception as e:
            print(f'Erro na desconexão com o banco de dados: {e}')
            
    
    def register_produto(self, codigo, unidades, produto, val_unitario, val_total):
        
        query = "INSERT INTO tabela (codigo, unidades, produto, val_unitario, val_total) VALUES (%s, %s, %s, %s, %s)"
        values = (codigo, unidades, produto, val_unitario, val_total)
        self.cursor.execute(query, values)
        self.connection.commit()
        
