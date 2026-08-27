import sqlite3

conn  = sqlite3.connect("escola.db")

cursor = conn.cursor()


# cursor.execute(
#     """
#         INSERT INTO estudantes(nome, idade) \
#         VALUES (?, ?)
#     """,
#     ("Joana", 30)
# )

cursor.execute(
    """
        INSERT INTO disciplinas(estudante_id, nome_disciplina) \
        VALUES (?, ?)
    """,
    (1, "matematica")
)

conn.commit()
conn.close()