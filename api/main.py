from fastapi import FastAPI
import sqlite3
con = sqlite3.connect("todo_app.db")
cursor = con.cursor()

try:
    cursor.execute("""CREATE TABLE users 
        (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT
        )""")
except:
    pass

try:
    cursor.execute("CREATE TABLE tasks (task_id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, task TEXT)")
except:
    pass

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return {"users": users}

@app.get("/user/{user_name}")
async def user(user_name: str):
    cursor.execute("SELECT * FROM users WHERE user_name=?", (user_name,))
    user = cursor.fetchone()
    if user:
        return {"user_id": user[0], "user_name": user[1]}
    else:
        return {"message": "User not found"}
    
@app.post("/user/{user_name}")
async def create_user(user_name: str):
    cursor.execute("INSERT INTO users (user_name) VALUES (?)", (user_name,))
    con.commit()
    return {"message": f"User {user_name} created", "user_id": cursor.lastrowid}

@app.get("/tasks")
async def tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return {"tasks": tasks}

@app.get("/task/{user_id}")
async def task(user_id: int):
    cursor.execute("SELECT * FROM tasks WHERE user_id=?", (user_id,))
    tasks = cursor.fetchall()
    return {"tasks": tasks}

@app.post("/task/{user_id}")
async def create_task(user_id: int, task: str):
    cursor.execute("INSERT INTO tasks (user_id, task) VALUES (?, ?)", (user_id, task))
    con.commit()
    return {"message": f"Task {task} created"}

