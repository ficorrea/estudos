import sqlite3
import hashlib
import os

def create_database():
    # Conecta ao banco de dados (cria se não existir)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Cria tabela de usuários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT UNIQUE,
            user_type TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            is_active BOOLEAN DEFAULT 1
        )
    ''')
    
    # Cria um usuário admin padrão (senha: admin123)
    admin_password = hash_password('admin123')
    try:
        cursor.execute('''
            INSERT OR IGNORE INTO users (username, password, email, user_type)
            VALUES (?, ?, ?, ?)
        ''', ('admin', admin_password, 'admin@example.com', 'admin'))
    except:
        pass
    
    conn.commit()
    conn.close()

def hash_password(password):
    """Gera hash da senha usando SHA-256"""
    salt = "streamlit_auth_salt"  # Em produção, use um salt aleatório por usuário
    return hashlib.sha256((password + salt).encode()).hexdigest()

def verify_password(password, hashed):
    """Verifica se a senha corresponde ao hash"""
    return hash_password(password) == hashed

if __name__ == '__main__':
    create_database()
    print("Banco de dados criado com sucesso!")