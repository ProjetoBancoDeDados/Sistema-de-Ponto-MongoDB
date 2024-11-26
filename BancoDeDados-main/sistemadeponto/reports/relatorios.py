from pymongo import MongoClient

class Relatorios:
    def __init__(self, db_connection):
        self.db = db_connection

    def horas_trabalhadas(self):
        try:
            pipeline = [
                {
                    "$lookup": {
                        "from": "funcionarios",
                        "localField": "funcionario_id",
                        "foreignField": "_id",
                        "as": "funcionario"
                    }
                },
                {
                    "$unwind": "$funcionario"
                },
                {
                    "$group": {
                        "_id": "$funcionario._id",
                        "nome": {"$first": "$funcionario.nome"},
                        "total_registros": {"$sum": 1},
                        "horas_trabalhadas": {
                            "$sum": {
                                "$divide": [
                                    {"$subtract": ["$hora_saida", "$hora_entrada"]}, 3600000
                                ]
                            }
                        }
                    }
                }
            ]
            return list(self.db.registros_de_ponto.aggregate(pipeline))
        except Exception as error:
            raise Exception(f"Erro ao gerar relatório de horas trabalhadas: {error}")

    def registros_ponto(self):
        try:
            return list(self.db.registros_de_ponto.find())
        except Exception as error:
            raise Exception(f"Erro ao gerar relatório de registros de ponto: {error}")