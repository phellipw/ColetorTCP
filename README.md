# Projeto Coletor TCP IP

## Objetivo

Criação de Script em Python que possa ser utilizado para recebimento de pacotes TCP/IP e conversão
dos mesmo em texto.

## Por que Python ?

Esse pequeno projeto, faz parte de um projeto de exercício, que é o 100 days of code.


## Status atual do coletor

O coletor atualmente recebe pacotes e os converte para texto, porém ainda apresenta algumas  
incosistências quando uma conexão é perdida entrando em looping de conexão no log, 
aguardando essa conexão.

Issue referente ao looping corrigida.

Próximas melhorias, serão atreladas a múltiplas conexões em uma nova versão desse mesmo coletor.
Usando o conceito de threads.
