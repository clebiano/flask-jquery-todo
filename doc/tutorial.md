
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
- Remova do frontend os arquivos .git, README.md e .gitignore. Antes disso, use o conteúdo desse .gitignore para o .gitignore do diretório raiz. Na verdade, quando já existe um diretório .git/ na raiz do projeto não é criado outro .git/.
- Adicionando todas as alterações na lista de espera  
  `$ git add .`  
- Ver status do monitoramento  
  `$ git status`  
- Confirmando mudanças no projeto  
  `$ git commit -m "First project commit."`
- Após o commit execute o comando (Dá erro se não tiver realizado o commit das últimas alterações)
    - `$ cd frontend/`
    - `$ npm run eject`
- Após a configurações descritas em https://www.youtube.com/watch?v=_RSVoqXWzSw&t=105s execute
    - `frontend$ npm run build`

# Instalação do projeto em uma nova máquina  
- Deletar o diretório venv quando houver `$ rm -rf venv/`
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

- Instalação do Node.js v12.x no Ubuntu
    - `$ curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -`
    - `$ sudo apt-get install -y nodejs`
    - `$ node --version`
    - `$ npm --version`
- Instalação do yarn e react
    - `$ sudo npm install -g yarn`
    - `$ yarn global add create-react-app react-scripts`
- Instalação do servidor web nginx e gunicorn
    - `$ sudo apt-get install nginx`
    - `$ pip install gunicorn`

# Deploy AWS
- Referências:
    - AWS https://console.aws.amazon.com/
    - Criar conta AWS: https://www.youtube.com/playlist?list=PLWMAkZq0y_ZMQyoztoxwwD3QBsyNbZKL9 
    - Deploy https://www.youtube.com/playlist?list=PL5KTLzN85O4KTCYzsWZPTP0BfRj6I_yUP
    - Deploy https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04
- Acesso via SSH:
    - `$ cd /media/clebiano/clebiano_data/programas`
    - `$ ssh -i flask-react-ccs.pem ubuntu@3.86.142.40`
    - `$ chmod 400 flask-react-ccs.pem`
    - `$ ssh -i flask-react-ccs.pem ubuntu@3.86.142.40`
    - `$ python3 -V`
    - `$ sudo apt-get update`
    - `$ sudo apt-get install python3-pip`
    - `$ htop`
- Atualizei o requirements-dev.txt do projeto na minha máquina
- Fiz um commit das últimas alterações
- Compactando diretório
    - `$ tar -zcf flask-react-todo-list.tar.gz flask-react-todo-list/`
- Copiando o pacote do meu notebook para a instância na AWS
    - Entrar no diretório onde está a chave de segurança `$ cd /media/clebiano/clebiano_data/programas`
    - `$ scp -i flask-react-ccs.pem flask-react-todo-list.tar.gz ubuntu@3.86.142.40:`
- Descompactando / descomprimindo / descompactar / Extraindo o pacote
    - `$ tar -xzf flask-react-todo-list.tar.gz`
- Removendo o flask-react-todo-list.tar.gz
    - `rm flask-react-todo-list.tar.gz`
- Principais arquivos de configuração:
   - `$ sudo nano /etc/systemd/system/flask-react-todo-list.service`

	[Unit]
	Description=Gunicorn instance to serve flask-react-todo-list
	After=network.target

	[Service]
	User=ubuntu
	Group=www-data
	WorkingDirectory=/home/ubuntu/flask-react-todo-list/backend
	Environment="PATH=/home/ubuntu/flask-react-todo-list/venv/bin"
	ExecStart=/home/ubuntu/flask-react-todo-list/venv/bin/gunicorn --workers 3 --bind unix:flask-react-todo-list.sock -m 007 manager:app

	\#[Install]
	\#WantedBy=multi-user.target

    - `$ sudo nano /etc/nginx/sites-available/flask-react-todo-list`

	server{
	   \#listen 80;
	   listen 8080;
	   server_name 3.86.142.40;

	\#   location / {
	\#        proxy_pass http://127.0.0.1:8000;
	\#   }
	\#}


	\#server {
	\#    listen 80;
	\#    server_name ec2-3-86-142-40.compute-1.amazonaws.com www.ec2-3-86-142-40.compute-1.amazonaws.com;
	\#    server_name 3.86.142.40 www.3.86.142.40;

	    location / {
		\#include proxy_params;
		proxy_pass http://unix:/home/ubuntu/flask-react-todo-list/backend/flask-react-todo-list.sock;
	    }
	}

- Dicas para evitar problemas:
    - Estar atento aos caminhos informados: colocar o usuário e nome do diretório corretamente
    - Em ExecStart fica o caminho do Gunicorn instalado na máquina virtual venv
    - Não deixar variações/cópias dos arquivos descritos acima. Exclua arquivos como "flask-react-todo-list.save"
    - Fique atento ao local onde está o arquivo principal do projeto Flask, o manager.py. Sempre informe corretamente o local do diretório. Nesse projeto é o backend/.
- Testar o deploy com o IP público na AWS e a porta utilizada na configuração
    - http://3.86.142.40:8080/
- Uma vez feitas as configurações de deploy um teste rápido da app poderá ser via:
    - `frontend$ npm run build`
    - `backend(venv)$ gunicorn manager:app` ou `$ python manager.py runserver`
    -  http://127.0.0.1:8000


 New minor version of npm available! 6.12.0 → 6.13.0       │
   │   Changelog: https://github.com/npm/cli/releases/tag/v6.13.0   │
   │               Run npm install -g npm to update!  

Erro: eu estava chamando as funcionalidades do gunicorn e do manager no mesmo arquivo.
Resolvi criando um arquivo wsgi.

# Referências

https://www.youtube.com/watch?v=_RSVoqXWzSw&t=105s

https://github.com/Eyongkevin/hello_template

https://github.com/spacedevs-team/react_flask_statusok/blob/master/package.json

https://codeburst.io/creating-a-full-stack-web-application-with-python-npm-webpack-and-react-8925800503d9

https://github.com/angineering/FullStackTemplate/blob/master/fullstack_template/static/webpack.config.js

https://github.com/viniciuschiele/flask-apscheduler/issues/50#issuecomment-315114627












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

# App.js

//      <header className="App-header">
//        <img src={logo} className="App-logo" alt="logo" />
//        <p>
//          Edit <code>src/App.js</code> and save to reload.
//        </p>
//        <p>My Token = {window.token}</p>
//        <h1>Clebiano da Costa Sá</h1>
//        <h1>TESTE 55555</h1>
//        <a
//          className="App-link"
//          href="https://reactjs.org"
//          target="_blank"
//          rel="noopener noreferrer"
//        >
//          Learn React
//        </a>
//      </header>


# Index.css

body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", "Oxygen",
    "Ubuntu", "Cantarell", "Fira Sans", "Droid Sans", "Helvetica Neue",
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, "Courier New",
    monospace;
}


#APP.css

.App {
  text-align: center;
}

.App-logo {
  height: 40vmin;
}

.App-header {
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
  color: white;
}

.App-link {
  color: #09d3ac;
}





Instalei essa dependecncias por causa de um tutorial, mas no final nem utilizei (ignorar)
    - # instalar dependencies do frontend
    - `$ npm i`
    - `$ npm i @blueprintjs/core`
