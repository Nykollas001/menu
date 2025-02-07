# Sistema de Gestão de Despesas e Tarefas

Este é um sistema Django para gerenciamento de despesas domésticas e tarefas, desenvolvido com Django 5.1.6.

## Funcionalidades

- Gerenciamento de despesas
- Sistema de tarefas
- Autenticação de usuários
- Dashboard com visualização de dados
- Interface responsiva

## Requisitos

- Python 3.8+
- Django 5.1.6
- Outras dependências listadas em `requirements.txt`

## Configuração do Ambiente

1. Clone o repositório:
```bash
git clone [url-do-repositorio]
cd menu
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

5. Execute as migrações:
```bash
python manage.py migrate
```

6. Crie um superusuário:
```bash
python manage.py createsuperuser
```

7. Inicie o servidor:
```bash
python manage.py runserver
```

## Estrutura do Projeto

- `home_expenses/`: Configurações principais do projeto
- `expenses/`: Aplicação de gerenciamento de despesas
- `tarefas/`: Aplicação de gerenciamento de tarefas
- `templates/`: Templates globais
- `static/`: Arquivos estáticos
- `media/`: Arquivos de mídia enviados pelos usuários
- `logs/`: Arquivos de log

## Desenvolvimento

- Use `black` para formatação de código
- Use `flake8` para linting
- Execute os testes com `pytest`
- Use `coverage` para relatórios de cobertura de testes

## Contribuindo

1. Crie uma branch para sua feature
2. Escreva testes para suas alterações
3. Execute os testes
4. Envie um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT.