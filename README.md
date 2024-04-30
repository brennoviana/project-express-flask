# project-express-flask

Este é um projeto utilizando a ferramenta Docker Compose para orquestrar serviços, Express.js e Flask.

## Pré-requisitos
- Docker e Docker Compose instalados
- Node.js e npm instalados
- Python e pip instalados

## Instruções de Configuração

1. Na raiz do projeto, execute o Docker Compose:
```bash
    docker-compose up
```
2. Configure o projeto Express:
```bash
    cd express-project
    npm install
    npm run start
    cd ..
```
3. Configure o projeto Flask:
```bash
    cd flask-project
    python3 -m venv venv
    source venv/bin/activate  # No Windows use 'venv\Scripts\activate'
    pip install -r requirements.txt
    python run.py dev
    cd ..
```
## Instruções das Rotas

- Login: Acesse localhost:3000 para fazer login.
- Página Flask: Acesse localhost:5000/movie/ para ver a página dos filmes.
- Cadastro de Usuários: Para cadastrar usuários, utilize a rota http://localhost:3000/users/.

## Certifique-se de que:
- Todos os serviços necessários estão definidos no `docker-compose.yml`.
- Os scripts de inicialização do `npm` e do Python estão corretos.
- O arquivo `requirements.txt` do Flask está presente e correto, se você estiver usando um para gerenciar as dependências do Python.

## Explicação:
- Essas instruções ajudam a garantir que qualquer pessoa que utilize seu projeto possa fazê-lo sem problemas, seguindo um  passo a passo claro e estruturado. Se precisar de ajuda para configurar qualquer parte específica do Docker Compose ou dos projetos Node.js/Python, estou aqui para ajudar!
