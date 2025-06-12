# utils.py
import json
import os

ARQUIVO_CLIENTES = "clientes.json"

def validar_nome(nome):
    return len(nome.strip()) > 0

def validar_email(email):
    return "@" in email and "." in email

def validar_telefone(telefone):
    return telefone.isdigit() and (8 <= len(telefone) <= 15)

def carregar_clientes():
    if not os.path.exists(ARQUIVO_CLIENTES):
        return []
    with open(ARQUIVO_CLIENTES, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_clientes(clientes):
    with open(ARQUIVO_CLIENTES, "w", encoding="utf-8") as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)
