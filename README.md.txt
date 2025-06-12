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

# Acesse a pasta
cd cadastro-clientes

# Execute o sistema
python cadastro_clientes.py
🖼️ Exemplo de uso no terminal
Adicione o print do seu terminal com o nome screenshot-terminal.png na pasta principal do projeto.

markdown
Copiar
Editar
![Print do terminal](screenshot-terminal.png)
📁 Estrutura do projeto
bash
Copiar
Editar
cadastro-clientes/
├── cadastro_clientes.py       # Execução principal
├── cliente.py                 # CRUD dos clientes
├── utils.py                   # Validações e manipulação JSON
├── clientes.json              # Banco de dados local
├── screenshot-terminal.png    # Print do terminal
├── tests/
│   └── test_utils.py          # Testes com unittest
└── README.md                  # Documentação do projeto
🛠️ Tecnologias utilizadas
Python 3.x

Módulo json – salvar e carregar dados

Módulo os – limpar terminal (opcional)

Módulo unittest – testes automatizados

📚 Próximos passos (ideias de evolução)
🧼 Adicionar validações robustas com regex (e-mail, telefone)

🖼️ Criar interface gráfica com Tkinter

🌐 Criar versão web com Flask ou FastAPI

✅ Ampliar cobertura de testes com unittest ou pytest

📌 Autor
Juliano Nascimento
🔗 GitHub: @julianordn

🧠 Nota final
Este projeto faz parte do meu aprendizado como desenvolvedor júnior.
Estou sempre aberto a feedbacks, sugestões e colaborações!




