from app.database import get_db_connection


class Usuario:

  def __init__(self, username, password, id=None):
    self.id = id
    self.username = username
    self.password = password

  @staticmethod
  def get_by_username(username):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, username, password FROM usuarios WHERE username = ?",
        (username,),
    )
    row = cursor.fetchone() #recolhe o resultado de um registro
    cursor.close()
    conn.close()

    if row:
      return Usuario(
          username=row["username"], password=row["password"], id=row["id"]
      )
    return None

  @staticmethod
  def get_all():
    """Busca todos os utilizadores para a tela de listagem (SELECT)"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username FROM usuarios")
    rows = cursor.fetchall() #recolhe todos os registros do banco
    cursor.close()
    conn.close()

    # Retorna uma lista de instâncias da classe Usuario ou dicionários
    return [
        {"id": row["id"], "username": row["username"]} for row in rows
    ]

  def save(self):
    """Salva o utilizador atual no banco de dados"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO usuarios (username, password) VALUES (?, ?)",
        (self.username, self.password),
    )
    conn.commit()
    cursor.close()
    conn.close()