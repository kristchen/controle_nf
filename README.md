# Controle de Notas Fiscais

Back-End de uma aplicação utilizada para controle de notas fiscais com o objetivo de ajudar micro-emprendedores a se organizarem fiscalmente de forma mais efetiva.

## Escopo

O escopo desse projeto contempla as seguintes funcionalidades
- Cadastro de Empresas Parceiras (Clientes)
- Cadastro de Categorias de Despesas
- Cadastro de Despesas e Receitas
- Cadastro de Usuários
- Relatorios de receitas

## Tecnologia

Esse projeto foi construidos usando como base as bibliotecas Django e DjangoRestFramework, ambas desenvolvidas na linguagem Python (ver 3.8.10).
Essa bibliotecas foram escolhidas para dar mais agilidade ao processo de desenvolvimento e manutenção do código.

As APIs principais foram implemetadas utilizando [ViewSets ](https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset) que são poderosas classes que implementam os principais metodos HTTP visando uma maior reutilização do código e pouca escrita.

## Instalação

Essa aplicação está instalada dentro de um container Docker e para inicializa-la basta excutar os seguintes comandos dentro da pasta principal do projeto:

```sh
docker build -t controle_nf .
docker run -dp 8000:8000 controle_nf
```
O ambiente de teste conta com um usuário cadastrado para executar os testes das APIs implementadas:

- usuario: master
- senha: master123

As APIs implementadas podem ser vizualizadas na seguinte collection do Postman:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/4057040-05dcdd6a-da2b-4ecc-a2a6-3d471a672070?action=collection%2Ffork&collection-url=entityId%3D4057040-05dcdd6a-da2b-4ecc-a2a6-3d471a672070%26entityType%3Dcollection%26workspaceId%3Deb251739-ef92-4852-85a4-903aecec4319)

## Produção

Para a aplicação ser instalada no ambiente de produção devera ser desevolvido um arquivo seettings.py com todas as informações e variaveis de ambientes do servidor de produção.

O arquivo settings.py é responsavel por todas as configurações do projeto e o modo como ele irá se comportar em determinados ambientes.

## Issues

Os endpoints archives para categories e customers não foram implementados. Ao invés disso o campo status foi criado para as duas entidades (Category e Customer) e são atualizadas pelo respectivo metodo PUT.




