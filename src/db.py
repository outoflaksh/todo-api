import sqlite3


def create_task(todo_detail: str):
    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()

    # Create table for storing data
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS todo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            todo_detail TEXT,
            completed INTEGER DEFAULT '0',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """
    )
    conn.commit()

    insertion_query = "INSERT INTO todo (todo_detail) VALUES (?)"
    r = cur.execute(insertion_query, (todo_detail,))
    conn.commit()


def fetch_all_tasks():
    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()

    res = cur.execute("SELECT * FROM todo;")
    tasks = []

    for r in res:
        tasks.append(
            {
                "id": r[0],
                "todo_detail": r[1],
                "completed": True if r[2] == 1 else False,
                "created_at": r[3],
            }
        )

    return tasks


def complete_task(todo_id):
    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()

    update_query = """UPDATE todo
              SET completed = 1
              WHERE id = ?
              """
    cur.execute(update_query, (todo_id,))
    conn.commit()


def update_task(todo_id, new_todo_detail):
    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()

    update_query = """UPDATE todo
              SET todo_detail = ?
              WHERE id = ?
              """
    cur.execute(update_query, (new_todo_detail, todo_id))
    conn.commit()


def delete_task(todo_id):
    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()

    delete_query = """
        DELETE FROM todo
        WHERE id = ?
    """

    cur.execute(delete_query, (todo_id,))
    conn.commit()
