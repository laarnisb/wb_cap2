from security import hash_password, verify_password
from sqlalchemy import text
from database import engine

def register_user(username, password, income):
    hashed_pw = hash_password(password)
    with engine.connect() as conn:
        conn.execute(text("""
            INSERT INTO users (username, password_hash, income)
            VALUES (:username, :password_hash, :income)
        """), {"username": username, "password_hash": hashed_pw, "income": income})
        conn.commit()

def authenticate_user(username, password):
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT password_hash FROM users WHERE username = :username
        """), {"username": username}).fetchone()
        if result:
            return verify_password(password, result[0])
    return False