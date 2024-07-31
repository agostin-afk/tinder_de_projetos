# Tinder de Projetos

![GitHub repo size](https://img.shields.io/github/repo-size/agostin-afk/tinder_de_projetos?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/agostin-afk/tinder_de_projetos?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/agostin-afk/tinder_de_projetos?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/agostin-afk/tinder_de_projetos?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/agostin-afk/tinder_de_projetos?style=for-the-badge)



>A criação de uma plataforma para divulgação de projetos. Suprimindo a necessidade de monitorar as redes sociais, correndo o risco de deixar uma oportunidade passar.

### Ajustes e melhorias

O projeto ainda está em desenvolvimento e as próximas atualizações serão voltadas nas seguintes tarefas:

- [ ] Cadastrar projetos
- [ ] Feed com os projetos cadastrados
- [ ] Envio de Emails
- [ ] Alert para usuarios

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- `<Python3>`
- `<Windows / Linux / Mac>`


## 🚀 Instalando Tinder de Projetos

Para instalar o Tinder de Projetos, siga estas etapas:


Windows, Linux e macOS:

```
<pip install -r requirements.txt>
```

## ☕ Usando Tinder de Projetos

Para usar Tinder de Projetos, siga estas etapas:
- Crie um super-usuario
```
<python manage.py createsuperuser>
```
- Faça as migrações
``` 
<python manage.py makemigrations && python manage.py migrate>
```
- Inicie o servidor
``` 
<python manage.py runserver>
```