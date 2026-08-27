import sqlite3

conn = sqlite3.connect("escola.db")
cursor = conn.cursor()


cursor.execute(
    """
        SELECT estudantes.nome, disciplinas.nome_disciplina 
        FROM disciplinas
        INNER JOIN estudantes 
        ON estudantes.id = disciplinas.estudante_id
    """
)


resultados = cursor.fetchall()

for linha in resultados:
    print(f"estudante: {linha[0]} - Disciplina: {linha[1]}")

conn.close()