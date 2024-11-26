from pymongo import MongoClient

class RegistroPonto:
    def __init__(self, db_connection):
        self.db = db_connection

    def inserir(self, funcionario_id, data, hora_entrada, hora_saida):
        if not all([funcionario_id, data, hora_entrada, hora_saida]):
            raise ValueError("Todos os campos são obrigatórios")
        
        registro = {
            "funcionario_id": funcionario_id,
            "data": data,
            "hora_entrada": hora_entrada,
            "hora_saida": hora_saida
        }
        
        try:
            result = self.db.registros_de_ponto.insert_one(registro)
            return result.inserted_id
        except Exception as error:
            raise Exception(f"Erro ao inserir registro de ponto: {error}")

    def atualizar(self, registro_id, data=None, hora_entrada=None, hora_saida=None):
        update_fields = {}
        if data is not None:
            update_fields["data"] = data
        if hora_entrada is not None:
            update_fields["hora_entrada"] = hora_entrada
        if hora_saida is not None:
            update_fields["hora_saida"] = hora_saida
        
        if not update_fields:
            raise ValueError("Nenhum dado para atualizar.")

        try:
            result = self.db.registros_de_ponto.update_one(
                {"_id": registro_id},
                {"$set": update_fields}
            )
            if result.modified_count == 0:
                raise ValueError(f"Registro com ID {registro_id} não encontrado.")
        except Exception as error:
            raise Exception(f"Erro ao atualizar registro de ponto: {error}")

    def remover(self, registro_id):
        try:
            result = self.db.registros_de_ponto.delete_one({"_id": registro_id})
            if result.deleted_count == 0:
                raise ValueError(f"Registro com ID {registro_id} não encontrado.")
        except Exception as error:
            raise Exception(f"Erro ao remover registro de ponto: {error}")

    def listar_todos(self):
        try:
            return list(self.db.registros_de_ponto.find())
        except Exception as error:
            raise Exception(f"Erro ao listar registros de ponto: {error}")