
# Tutorial: criando uma aplicação web com Flask e React
Este tutorial tem o propósito de ajudar na criação de novos projetos com Flask e React.

# BackEnd
- Criando diretório raiz para o projeto  
	`$ mkdir flask-react-todo-list`
- Entrando no diretório raiz do projeto  
	`$ cd flask-react-todo-list/`
- Criando diretório para o backend com Flask
    `$ mkdir backend`
- Criando ambiente virtual com Python3  
	`$ virtualenv -p python3.6 venv`
- Ativando o ambiente virtual  
	`$ source venv/bin/activate`
- Salvando lista de pacotes pip para posterior instalação rápida  
	`$ pip freeze > requirements-dev.txt`
- Salvando estrutura de diretórios e arquivos do projeto em forma de árvore  
	`$ tree > project.tree`
- Inicializando um diretório para monitoramento de versões com git  
	`$ git init`
- Adicionando a identificação do usuário  
  `$ git config --global user.email "clebiano@alumni.usp.br"`  
  `$ git config --global user.name "Clebiano da Costa Sá"`  
- Ver status do monitoramento  
  `$ git status`  
- Criando arquivo .gitignore, necessário para ignorar arquivos e/ou diretórios durante o commit do projeto  
	`$ touch .gitignore`  
- Adicionando arquivos e diretórios ao arquivo .gitignore  
	`$ echo 'venv' >> .gitignore`  
    `$ echo '*.sqlite3' >> .gitignore`  
    `$ echo '.idea' >> .gitignore`  
- Ver status do monitoramento  
  `$ git status`  
- Adicionando todas as alterações na lista de espera  
  `$ git add .`  
- Ver status do monitoramento  
  `$ git status`  
- Confirmando mudanças no projeto  
  `$ git commit -m "First project commit."`
- Verificando o log dos commits  
  `$ git log`  
  `$ git log -p` #mostra o diff de cada commit  
  `$ git log --pretty=oneline`  
- Instalando o Flask mais recente no ambiente virtual venv  
	`$ source venv/bin/activate`  
	`$ pip install Flask`  
- Instalando flask-sqlalchemy para que o SQL seja gerado a partir das configurações em Python  
    - `$ pip install flask-sqlalchemy` 
    - `$ pip install Flask-Migrate`
    - `$ pip install Flask-Script`
- Referência: https://www.youtube.com/watch?v=tJZjniFdaIw&list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX&index=5
- Testando a aplicação
    - `$ python run.py runserver`
- Inicializando as migrações
    - `$ python run.py db init`
- Migrando alterações para o banco de dados
    - `$ python run.py db migrate`
    - `$ python run.py db upgrade`
- Instalação do sqlite3 e sqlitebrowser
    - https://linuxhint.com/install_sqlite_browser_ubuntu_1804/
    - `$ sudo apt install sqlite3`
    - `$ sudo apt-get install sqlitebrowser`

# FrontEnd
- Instalação do Node.js v12.x no Ubuntu
    - `$ curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -`
    - `$ sudo apt-get install -y nodejs`
    - `$ node --version`
    - `$ npm --version`

- Instalação do yarn e react
    - `$ sudo npm install -g yarn`
    - `$ yarn global add create-react-app react-scripts`
- Configurando o frontend com react
    - `$ npx create-react-app frontend`
- Remova do frontend os arquivos .git, README.md e .gitignore. Antes disso, use o conteúdo desse .gitignore para o .gitignore do diretório raiz




- Criando o projeto inicial django no ambiente virtual venv  
	`$ django-admin.py startproject proj .` # o "." permite que o arquivo "manage.py" seja criado na raiz do projeto  
- Verificando se existem alterações para o banco de dados  
	`$ python manage.py makemigrations`
- Migrando alterações do django para o banco de dados  
	`$ python manage.py migrate`  
- Testando o projeto  
	`$ python manage.py runserver`  
	Entre na página inicial da plataforma colocando o link http://127.0.0.1:8000/ no Browser (ex.: Chrome, Firefox ...)  
- Criando uma conta administrativa  
	`$ python manage.py createsuperuser`  
	Username (leave blank to use 'clebiano'): 03939033383  
	Email address: clebiano@alumni.usp.br  
	Password: \*\*\*\*\*\*\*  
- Instalação do django-rest-framework  
	- `$ pip install djangorestframework`  
	- `$ pip install markdown       # Markdown support for the browsable API.`  
	- `$ pip install django-filter  # Filtering support`  
- Adicionar `'rest_framework',` ao apps instalados em settings.py  
- Adicionar os pacotes pip, instalados na venv, no arquivo requirements-dev.txt   
    - `$ pip freeze > requirements-dev.txt`
- Entrar no ambiente Admin do Django  
	http://127.0.0.1:8000/admin/  
- Instalação do postman para gerenciamento de api  
	- `$sudo snap install postman`
- No grupo do LEB, crie um diretório privado com o mesmo nome do diretório raiz  
- Adicionando todas as alterações na lista de espera  
  `$ git add .`  
- Ver status do monitoramento  
  `$ git status`  
- Confirmando mudanças no projeto  
  `$ git commit -m "First project commit."`  
- push do diretório para o github  
`$ git remote add origin https://github.com/leb-fmvz-usp/django-vpsdb.git`  
`$ git push -u origin master`  

- Estrutura inicial pronta!

## Criando uma nova APP  
- Criando a APP home  
	`$ python manage.py startapp home`  
- Registrar a APP home em INSTALLED_APPS do settings.py  
    `'home',`
- Criar demais arquivos e diretórios da APP  
- Após as alterações, executar:
    - `$ ./manage.py makemigrations`
    - `$ ./manage.py migrate`
    

## API  
- Criar endpoints simples  
- Os nomes dos recursos são, por padrão, no plural  
- Documentar a API  
- Versionar a API para poder migrar usuários entre versões: /v1/recursos  

# Arquivos estáticos no Heroku  
https://github.com/clebiano/django-heroku  
http://whitenoise.evans.io/en/stable/  
https://stackoverflow.com/questions/15856358/heroku-collectstatic-not-run-during-deployment  
`$ heroku run python manage.py collectstatic --dry-run --noinput`  

# Instalação do projeto em uma nova máquina  
- Deletar o diretório venv quando houver  
- Criar uma nova venv  
    - `$ sudo apt install virtualenv`  
    - `$ virtualenv -p python3.6 venv`  
    - `$ source venv/bin/activate`  
    - `$ pip install -r requirements-dev.txt`  
    - `$ ./manage.py makemigrations`
    - `$ ./manage.py migrate`
- Criando uma conta administrativa  
	`$ python manage.py createsuperuser`  
	Username (leave blank to use 'clebiano'): 03939033383  
	Email address: clebiano@alumni.usp.br  
	Password: \*\*\*\*\*\*\*
