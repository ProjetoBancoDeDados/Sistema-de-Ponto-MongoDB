from pymongo import MongoClient

class DatabaseConnection:
    def __init__(self):
        # Configurações de conexão
        self.uri = "mongodb://localhost:27017/"  
        self.nome_banco = "labdatabase"
        self.client = None
        self.db = None

    def conectar(self):
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.nome_banco]
            print("Conexão estabelecida com sucesso!")
        except Exception as error:
            print(f"Erro ao conectar ao banco de dados: {error}")
            raise

    def __enter__(self):
        self.conectar()
        return self.db  

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.client:
            self.client.close() 
            print("Conexão fechada.")