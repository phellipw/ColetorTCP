#########################################################
# Coletor TCP/IP - Python                               #
# Phellipe Aparecido Gomes Fogaça Ferraz                #
# phellipefferraz@hotmail.com                           #
#########################################################

import subprocess
import socket
import select
from datetime import datetime

HOST = 'localhost' 
PORTA = 5050 
orig = (HOST, PORTA)
conexao = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print(f'Aguardando conexão na porta: {PORTA}') 
conexao.bind((HOST, PORTA)) 
conexao.listen() 
open('bilhete.txt', 'w', encoding = 'utf-8') 
log = open('log.txt', 'w', encoding = 'utf-8') 


while True:
    conn, addr = conexao.accept()
    print(f"Conexão recebida de {addr} na porta:{PORTA}")

    while True:
        data = conn.recv(1024000)
        datatraduzida = str(data,'utf-8')
        if not data:
            print('Conexão foi perdida!')
            log = open('log.txt', 'a', encoding = 'utf-8')
            datahora = datetime.now()
            datahoratxt = datahora.strftime('%d/%m/%Y %H:%M')
            log.write(f'{datahoratxt} - Sem conexão\n')
            break 
        else:
         while True: 
            datahora = datetime.now()
            datahoratxt = datahora.strftime('%d/%m/%Y %H:%M')
            print(f'{datahoratxt} - Dados enviados de {addr} e depositados em bilhete.txt')
            log = open('log.txt', 'a', encoding = 'utf-8')
            log.write(f'{datahoratxt} - Dados enviados de {addr} e depositados em bilhete.txt\n')
            textfile2 = open('bilhete.txt', 'a', encoding = 'utf-8')
            textfile2.write(datatraduzida)
            break
