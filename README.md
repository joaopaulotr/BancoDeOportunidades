# Banco de Oportunidades

Plataforma completa para conectar prestadores de serviços e clientes, com backend em FastAPI + SQLAlchemy + MySQL e frontend em Vue.js + Vite.

## Visão Geral
Este projeto tem como objetivo facilitar a busca, contratação e gestão de serviços locais, promovendo oportunidades para prestadores e praticidade para clientes.

- **Backend:** FastAPI, SQLAlchemy, MySQL
- **Frontend:** Vue.js, Vite
- **Arquitetura:** RESTful, POO, separação clara entre camadas

## Funcionalidades
- Cadastro e autenticação de usuários (cliente, prestador, admin)
- Gerenciamento de serviços por categorias
- Contratação, acompanhamento e avaliação de serviços
- CRUD completo para Usuários, Serviços, Categorias e Transações
- Relacionamentos e integridade garantidos via banco relacional

## Estrutura do Projeto
```
banco_oportunidades/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   ├── database.py
│   │   └── __init__.py
│   └── requirements.txt
├── database_model/
│   └── modelo.sql
├── frontend/
│   ├── src/
│   │   ├── App.vue
│   │   ├── main.js
│   │   └── ...
│   ├── public/
│   └── package.json
└── README.md
```

## Como Executar
### Backend
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure o arquivo `.env` com as credenciais do MySQL.
3. Execute o servidor:
   ```bash
   uvicorn app.main:app --reload
   ```

### Frontend
1. Instale as dependências:
   ```bash
   npm install
   ```
2. Execute o servidor de desenvolvimento:
   ```bash
   npm run dev
   ```

## Banco de Dados
O modelo relacional está em `database_model/modelo.sql` e segue o padrão:
- Tabelas: `Usuarios`, `Categorias`, `Servicos`, `Transacoes`
- Relacionamentos via FKs
- Tipos e nomes de campos idênticos ao schema SQL

## Tecnologias Utilizadas
- **FastAPI**: API rápida e moderna
- **SQLAlchemy**: ORM para Python
- **MySQL**: Banco de dados relacional
- **Vue.js**: Framework progressivo para frontend
- **Vite**: Build rápido para Vue

## Contribuição
Pull requests são bem-vindos! Siga o padrão de código e mantenha a integridade do banco.

## Licença
MIT

---
Projeto para AEP de Engenharia de Software 4 Semestre.
Desenvolvido por João Paulo | Heitor Ferrari | Maria Eduarda.
