# Processamento-Linguagem-Natual-Estudo

app.py - Arquivo contendo o código da aplicação com rotas criadas através do Flask <br>
utils.py - Arquivo contendo o código de algumas funções utilizadas no app para importar o modelo criado (mymodel) e pré-processar os dados de entrada

## Objetivo
Este projeto tem por objetivo a criação de uma aplicação de Análise de Sentimentos.

## Passo a Passo
## 1)
Inicialmente foi feito todo o pipeline de processamento de linguagem natural com processo com:
### 
 - Aquisição
 - Importação
 - pré-processamento
 - Remoção de Stopwords
 - Etapa de Lemming/Stemming
 - Tokenização
 - Divisão dos dados em treino/teste
 - Criação de uma Rede Neural
 - Treinamento da Rede Neural
 - Exportação

## 2)
Após isso, foi feito a criação do app utilizando Flask, importando o modelo, criando as rotas e renderizando um template HTML (também criado por mim) que receberá as informações do formulário e estas a partir de uma função de pré-processamento transformadas em dados no mesmo formato de entrada que a Rede Neural foi treinada.

<p align="center"> 
<img src="./prints/telainicial.png" >
</p>
