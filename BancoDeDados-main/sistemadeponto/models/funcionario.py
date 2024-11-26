from pymongo import MongoClient

class Funcionario:
    def __init__(self, db_connection):
        self.db = db_connection

    def inserir(self, nome, cargo, data_contratacao):
        if not nome or not cargo or not data_contratacao:
            raise ValueError("Nome, cargo e data de contratação são obrigatórios")
        
        funcionario = {
            "nome": nome,
            "cargo": cargo,
            "data_contratacao": data_contratacao
        }
        
        try:
            result = self.db.funcionarios.insert_one(funcionario)
            return result.inserted_id
        except Exception as error:
            raise Exception(f"Erro ao inserir funcionário: {error}")

    def atualizar(self, funcionario_id, nome=None, cargo=None):
        update_fields = {}
        if nome is not None:
            update_fields["nome"] = nome
        if cargo is not None:
            update_fields["cargo"] = cargo
        
        if not update_fields:
            raise ValueError("Nenhum dado para atualizar.")

        try:
            result = self.db.funcionarios.update_one(
                {"_id": funcionario_id},
                {"$set": update_fields}
            )
            if result.modified_count == 0:
                raise ValueError(f"Funcionário com ID {funcionario_id} não encontrado.")
        except Exception as error:
            raise Exception(f"Erro ao atualizar funcionário: {error}")

    def remover(self, funcionario_id):
        try:
            result = self.db.funcionarios.delete_one({"_id": funcionario_id})
            if result.deleted_count == 0:
                raise ValueError(f"Funcionário com ID {funcionario_id} não encontrado.")
        except Exception as error:
            raise Exception(f"Erro ao remover funcionário: {error}")

    def listar_todos(self):
        try:
            return list(self.db.funcionarios.find())
        except Exception as error:
            raise Exception(f"Erro ao listar funcionários: {error}")