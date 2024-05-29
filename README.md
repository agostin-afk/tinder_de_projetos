# Tinder de Projetos

_Em desenvolvimento_


Um projeto idealizado no primeiro semestre no curso de Engenharia de Computação.


A criação de uma plataforma para divulgação de projetos dentro da UFC(universidade federal do ceará), suprimindo a necessidade do docente de monitorar as redes sociais de diversos laboratórios e projetos correndo o risco de deixar uma oportunidade passar. 



_atualmente estou usando apenas Django, mas futuramente implementarei outras ferramentas como o React_



## Funcionalidades

- Cadastrar projetos

- feed com os projetos cadastrados, com as respectivas informações

- Envio de Emails dos interessados para os criadores dos projetos

- aviso do início de PS(processos seletivos) de projetos do interesse do usuário

## Instalação

Rode esses comandos no terminal da raiz do projeto:

```bash
python -m venv nome_ambienteVirtual
nome_ambienteVirtual/Scripts/Activate.ps1
pip install -r requirements.txt
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
python manage.py ceatesuperuser
python manage.py runserver
```
    
## Bibliotecas

Com o ambiente virtual ativado, instale as seguintes dependências antes de rodar os comandos migrate:<br></br>
_caso o comando ```bash pip install -r requirements.txt``` não funcione_
```bash
asgiref==3.8.1
Django>=5.0.6
sqlparse>=0.5.0
tzdata>=2024.1
psycopg2-binary>=2.9.6
psycopg2>=2.9.9
Pillow>=9.5.0
django-summernote>=0.8.20.0
python-dotenv>=1.0.1
django-axes>=6.4.0
bleach==6.1.0
six==1.16.0
webencodings==0.5.1
```


