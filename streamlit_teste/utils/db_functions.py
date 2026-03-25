import sqlite3
import hashlib
import pandas as pd
import streamlit as st

# Funções de banco de dados
def get_db_connection():
    """Retorna uma conexão com o banco de dados"""
    return sqlite3.connect('users.db')

def hash_password(password):
    """Gera hash da senha"""
    salt = "streamlit_auth_salt"  # Mesmo salt usado na criação
    return hashlib.sha256((password + salt).encode()).hexdigest()

def authenticate_user(username, password):
    """Autentica o usuário no banco de dados"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    hashed_password = hash_password(password)
    
    cursor.execute('''
        SELECT id, username, email, user_type, is_active  
        FROM users 
        WHERE username = ? AND password = ? AND is_active = 1
    ''', (username, hashed_password))
    
    user = cursor.fetchone()
    conn.close()
    
    return user

def get_all_users():
    """Retorna todos os usuários (apenas para admin)"""
    conn = get_db_connection()
    query = "SELECT id, username, email, user_type, created_at, is_active FROM users"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def update_user_type(username, user_type):
    """Atualiza tipo do usuário"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE users 
        SET user_type = ?
        WHERE username = ?
    ''', (user_type, username))
    conn.commit()
    conn.close()

def get_user(username):
    """Retorna usuário"""
    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"SELECT username, email, user_type FROM users WHERE username = '{username}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    return user

def act_deact_user(username, status):
    """Atualiza tipo do usuário"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE users 
        SET is_active = ?
        WHERE username = ?
    ''', (status, username))
    conn.commit()
    conn.close()