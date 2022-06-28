# Documento de Arquitetura de Software

# Introdução
## Proposta

<p align="justify">
Este documento descreve a arquitetura do sistema de maneira geral, utilizando diferentes visões para dar ênfase em determinados aspectos.
</p>

## Escopo

<p align="justify">
O software do robô de irrigação construído para a matéria de Projeto Integrador 2 (2022.1) tem como objetivos principais:

* Fornecer uma interface gráfica ao usuário, permitindo mapear uma área a ser irrigada, exibir dados dos sensores disponíveis, iniciar ou interromper rotinas de irrigação previamente configuradas

* Fornecer uma interface de comunicação entre o robô e a interface gráfica, utilizando uma API REST para envio e recebimento de dados no formato JSON

* Fornecer um backend onde será realizado o processamento da trajetória do robô a partir de uma área estabelecida pelo usuário
</p>

## Definições, Siglas e Acrônimos

* API - Application Programming Interface
* JSON - JavaScript Object Notation
* PaaS - Platform as a Service
* PWA - Progressive Web Application
* REST - Representational State Transfer

# Representação Arquitetural
## Frontend

<p align="justify">
O frontend da aplicação consiste em um PWA, ou seja, um híbrido entre website e app mobile. Através dele, o usuário pode demarcar a área de interesse a ser irrigada, iniciar ou interromper rotinas de irrigação previamente configuradas e acessar dados dos sensores, como temperatura e umidade. Será implementado em JavaScript com a biblioteca React para facilitar a criação de componentes que podem ser reusados.
</p>

## Backend

<p align="justify">
O backend da aplicação serve como uma ponte entre o frontend e o robô, fornecendo uma API para permitir a comunicação entre as partes e a troca de dados. Além disso, existe um módulo que calcula a trajetória a ser seguida pelo robô na área delimitada.
</p>

# Objetivos Arquiteturais e Restrições

São objetivos desta arquitetura:
* Reusabilidade de componentes do frontend
* Simplicidade de endpoints na API
* Permitir flexibilização da troca de informações entre frontend, backend e robô
* Simplicidade de uso para o usuário final

São restrições desta arquitetura:

* A interface de usuário deve estar disponível em navegador web ou mobile
* A rota a ser seguida pelo robô deve ser calculada automaticamente no backend

# Ferramentas Utilizadas

|Nome|Descrição|
|--|--|
|Discod|Ferramenta de comunicação|
|Flask|Framework Python para criação de APIs|
|Git|Controle de versionamento de código-fonte|
|Github|Plataforma de hospedagem de código-fonte|
|Heroku|Plataforma como serviço (PaaS) para deploy do backend|
|React|Biblioteca JavaScript para criação de interface de usuário|
|Telegram|Ferramenta de comunicação|
|Visual Studio Code|Editor de código-fonte|

# Visão Lógica

O frontend da aplicação possui módulos focados em desenvolver as páginas, os componentes compartilhados e trechos de código que podem ser reaproveitados em qualquer ponto. O módulo services é responsável por estabelecer a conexão com o backend da aplicação.

O backend possui a implementação da API, onde são feitas as conexões via REST entre a aplicação e o robô. Além disso, o módulo mappings é responsável por calcular a trajetória que o robô deverá seguir.

## Diagrama de pacotes

![diagrama](./img/diagrama_de_pacotes.png)
