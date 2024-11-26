-- Criação da tabela Funcionarios
CREATE TABLE IF NOT EXISTS Funcionarios (
    funcionario_id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    cargo VARCHAR(255) NOT NULL,
    data_contratacao DATE NOT NULL
);

-- Criação da tabela Registros_de_Ponto
CREATE TABLE IF NOT EXISTS Registros_de_Ponto (
    registro_id SERIAL PRIMARY KEY,
    funcionario_id INTEGER NOT NULL,
    data DATE NOT NULL,
    hora_entrada TIME,
    hora_saida TIME,
    FOREIGN KEY (funcionario_id) REFERENCES Funcionarios(funcionario_id) ON DELETE CASCADE
);