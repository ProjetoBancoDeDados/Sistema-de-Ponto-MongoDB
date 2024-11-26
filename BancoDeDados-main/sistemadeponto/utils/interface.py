# utils/interface.py
import os
from datetime import datetime

import pg8000

class Interface:
    @staticmethod
    def limpar_tela():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def exibir_splash_screen(db):
        Interface.limpar_tela()
        print("=" * 40)
        print("Sistema de Controle de Ponto")
        print("Desenvolvido por: Julia Negri, Maria Isabel, Rafael Caires")
        print("Professor: Howard Roatti")
        print("=" * 40)

        try:
            db.cursor.execute("SELECT COUNT(*) FROM Funcionarios")
            count_funcionarios = db.cursor.fetchone()[0]
            db.cursor.execute("SELECT COUNT(*) FROM Registros_de_Ponto")
            count_registros = db.cursor.fetchone()[0]
            print(f"\nTotal de Funcionários: {count_funcionarios}")
            print(f"Total de Registros de Ponto: {count_registros}")
        except pg8000.DatabaseError as error:
            print(f"Erro ao consultar contagem de registros: {error}")
        
        input("\nPressione Enter para continuar...")
