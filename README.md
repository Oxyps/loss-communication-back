# [Comunicação de Perdas API](https://github.com/oxyps/loss-communication-back)

## Primeiros passos para rodar o projeto
1. Clonar ou baixar o repositório do [projeto](https://github.com/oxyps/loss-communication-back);

1. Certificar-se de que já possui a linguagem [Python](https://www.python.org/downloads/) e o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/installing/) instalado, utlizando o comando no terminal:
	``` shell
		> pip --version
	```

1. Instalar a ferramenta de gerenciamento de ambiente e pacotes [Pipenv](https://pypi.org/project/pipenv/):
	``` shell
		> pip install pipenv
	```

1. Ativar o ambiente:
	``` shell
		> pipenv shell
	```

1. Checar se atende aos requisitos mínimos do projeto:
	``` shell
		> pipenv check
	```

1. Instalar todas as dependências do projeto:
	``` shell
		> pipenv install
		> pipenv install --dev
	```

1. Esta API utiliza uma biblioteca de geo-referenciamento para auxiliar na parte de localização das lavouras, sendo assim pode ser que seja necessário instalar algumas bibliotecas extras para ser possível rodar o projeto em desenvolvimento.
Caso o erro `Could not find gdal-config. Make sure you have installed the GDAL native library and development headers.` seja apresentado, é possível baixar essas dependências faltantes, utilizando o comando (Linux):
	``` shell
		> sudo apt install -y gdal-bin libgdal-dev libgeos-dev libproj-dev
	```

1. Caso utilize outro SO, na [documentação do Django](https://docs.djangoproject.com/en/3.1/ref/contrib/gis/install/) tem algumas instruções para baixar esses pacotes.

1. Essa API utiliza o Banco de Dados MySQL, sendo assim deve ser criada uma tabela com o nome `loss_communication_db` ou os dados referentes ao usuário, senha ou nome do BD devem ser alteradas no arquivo `/core/settings.py` na propriedade `DATABASES`; Para criar o banco utiliza-se:
	``` sql
		> CREATE DATABASE loss_communication_db;
	```

1. Dentro do diretório raíz `./loss-communication-back`, rodar as `migrations` para gerar as tabelas do banco de dados:
	``` shell
		> python manage.py migrate
	```

1. Começar a servir a API:
	``` shell
		> python manage.py runserver
	```

1. Realizar os passos do [frontend](https://github.com/Oxyps/loss-communication-front):
	``` shell
		> python manage.py runserver
	```


## Rotas

**Lavouras**
* Listagem e cadastro de lavouras (GET e POST): `localhost:8000/api/loss/tillages/`;
* Detalhe, edição e exclusão de produto (GET, PUT, PATCH, DELETE): `localhost:8000/api/loss/tillages/:id/`.
* A filtragem do modelo lavoura pode ser realizada adicionando os query params `?id=1&type=Milho&harvest_date=2021-04-04` na rota de listagem.
* As buscas podem ser feitas adicionando os query params `?search=Milho` na rota de listagem.

**Agricultores**
* Listagem e cadastro de agricultores (GET e POST): `localhost:8000/api/loss/farmers/`;
* Detalhe, edição e exclusão de agricultor (GET, PUT, DELETE): `localhost:8000/api/loss/farmers/:id/`.
* A filtragem do modelo agricultor pode ser realizada adicionando os query params `?id=1&name=Abel&cpf=085&email=abel_castro_junior@hotmail.com` na rota de listagem.

**Comunicações de perda**
* Listagem e cadastro de comunicações (GET e POST): `localhost:8000/api/loss/communications/`;
* Detalhe, edição e exclusão de comunicação (GET, PUT, DELETE): `localhost:8000/api/loss/communications/:id/`.
* A filtragem do modelo comunicação de perda pode ser realizada adicionando os query params `?id=1&loss_cause=DRY` na rota de listagem.

**Buscas**
* As buscas podem ser feitas adicionando o query param `?search=Qualquer+valor+a+ser+procurado` na rota de listagem do modelo.

**Todas as rotas da API possuem uma interface gráfica fornecida pelo framework Django**
* Para acessar o painel de administrador também fornecido pelo framework Django, é utilizada a rota `localhost:8000/admin/`. Para tanto, é necessário que seja cadastrado um usuário administrador no BD, por meio do comando abaixo (estando na pasta raíz) e sejam seguidos os passos exibidos.
	``` shell
		> python manage.py createsuperuser
	```

## Tecnologias utilizadas
- [x] [Python](https://docs.python.org/3/)
- [x] [Django Framework](https://docs.djangoproject.com/en/3.1/)
- [x] [Django Rest Framework](https://www.django-rest-framework.org)
