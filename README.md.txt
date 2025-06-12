# 🧾 Sistema de Cadastro de Clientes

Sistema simples de cadastro de clientes feito com **Python**, rodando no terminal. Os dados são armazenados localmente em um arquivo `.json`.

---
## Funcionalidades

- ✅ Cadastrar clientes  
- ✅ Listar todos os clientes  
- ✅ Atualizar dados de clientes existentes  
- ✅ Deletar clientes  
- 💾 Salvamento dos dados em JSON  
- 📁 Estrutura modular com arquivos separados  
- 🧪 Testes automatizados com `unittest`

---
## 💻 Como executar

```bash
# Clone o repositório
git clone https://github.com/julianordn/cadastro-clientes.git

# Acesse a pasta do projeto
cd cadastro-clientes

# Execute o sistema
python cadastro_clientes.py

---
## 🖼️ Exemplo de uso no terminal
![Print do terminal](screenshot-terminal.png)

---
## 📁 Estrutura do projeto

cadastro-clientes/
├── cadastro_clientes.py       # Execução principal
├── cliente.py                 # CRUD dos clientes
├── utils.py                   # Validações e manipulação JSON
├── clientes.json              # Banco de dados local
├── screenshot-terminal.png    # Print do terminal
├── tests/
│   └── test_utils.py          # Testes com unittest
└── README.md                  # Documentação do projeto

---
## 🛠️ Tecnologias utilizadas

- Python 3.x  
- Módulo `json` — para salvar e carregar dados  
- Módulo `os` — para limpar o terminal (opcional)  
- Módulo `unittest` — para testes automatizados  

---
## 📚 Próximos passos (ideias de evolução)

- 🧼 Adicionar validações robustas com regex (e-mail, telefone)  
- 🖼️ Criar interface gráfica com Tkinter  
- 🌐 Criar versão web com Flask ou FastAPI  
- ✅ Ampliar cobertura de testes com unittest ou pytest  

---
## 📌 Autor

Juliano Nascimento  
🔗 GitHub: [@julianordn](https://github.com/julianordn)

---

## 🧠 Nota final

Este projeto faz parte do meu aprendizado como desenvolvedor júnior.  
Estou sempre aberto a feedbacks, sugestões e colaborações!



