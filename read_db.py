import sqlite3

conn  = sqlite3.connect("escola.db")

cursor = conn.cursor()

cursor.execute(
    """
        SELECT * FROM estudantes
    """
)

conn.commit()

estudantes = cursor.fetchall()

for estudante in estudantes:
    print(estudante)

conn.close()
