import sqlite3

conn  = sqlite3.connect("escola.db")

cursor = conn.cursor()


cursor.execute(
    """
        INSERT INTO estudantes(nome, idade) \
        VALUES (?, ?)
    """,
    ("Joana", 30)
)

conn.commit()
conn.close()