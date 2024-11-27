import sys
import os

# Adiciona o diretório pai ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.connection import DatabaseConnection
from controllers.controller import SistemaController

if __name__ == "__main__":
    with DatabaseConnection() as db_connection:
        print('Iniciando o sistema de controle de ponto,conectando ao banco de dados')
        print("Sistema de Controle de Ponto")
        print("Desenvolvido por: Julia Negri, Maria Isabel, Rafael Caires")
        print("Professor: Howard Roatti")
        sistema = SistemaController(db_connection)
        sistema.exibir_menu_principal()
