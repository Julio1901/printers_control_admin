
import smtplib
from email.mime.text import MIMEText






#Importa o arquivo para poder usar tudo o que está dentro 

from printers_log import copias_1921681152

printers_list =["192.168.1.153","192.168.1.155","192.168.1.157","192.168.1.158","192.168.2.155","192.168.2.156","192.168.2.157","192.168.3.151","192.168.3.153","192.168.3.154","192.168.3.155","192.168.3.156","192.168.3.157","192.168.3.158","192.168.3.159","192.168.4.154","192.168.4.155","192.168.4.156","192.168.4.157","192.168.4.158","192.168.4.159","192.168.8.54","192.168.8.55","192.168.8.57","192.168.8.58","192.168.8.59"]

#Verifica quantas impressoras tem na lista
total_impressoras = (len(printers_list))
index = 0


while index < total_impressoras:
    #pega todos os ips de printers_list e joga para arquivo_log_formatado sem ponto entre os números
    arquivo_log = printers_list[index]
    arquivo_log_formatado = (arquivo_log.replace(".", ""))
    #cria variável que irá guardar todos os nomes dos arquivos gerados no diretório de logs das impressoras "copias_IPDAIMPRESSORASEMPONTOS"
    arquivo_printers = ("copias_" + arquivo_log_formatado)
    #print (arquivo_printers)

    index += 1


#importa todos os arquivos de log manualmente (verificar um módulo de importar eles como biblicoteca, se possível)


#########################################################################
#Loja 04
from printers_log import copias_1921681152
from printers_log import copias_1921681153
from printers_log import copias_1921681155
from printers_log import copias_1921681157
from printers_log import copias_1921681158

#Loja02
from printers_log import copias_1921682155
from printers_log import copias_1921682156
from printers_log import copias_1921682157

#LOJA 05 E CD

from printers_log import copias_1921683151
from printers_log import copias_1921683153
from printers_log import copias_1921683154
from printers_log import copias_1921683155
from printers_log import copias_1921683156
from printers_log import copias_1921683157
from printers_log import copias_1921683158
from printers_log import copias_1921683159

#LOJA 01

from printers_log import copias_1921684154
from printers_log import copias_1921684155
from printers_log import copias_1921684156
from printers_log import copias_1921684157
from printers_log import copias_1921684158
from printers_log import copias_1921684159

#LOJA 08

from printers_log import copias_192168854
from printers_log import copias_192168857
from printers_log import copias_192168858
from printers_log import copias_192168859
########################################################################






arquivos_contadores = [copias_1921683151, copias_1921683153,copias_1921683154, copias_1921683155, copias_1921683156, copias_1921683157, copias_1921683158, copias_1921683159, copias_1921681152, copias_1921681153, copias_1921681155, copias_1921681157, copias_1921681158, copias_1921682155, copias_1921682157, copias_1921684154, copias_1921684155, copias_1921684156, copias_1921684157, copias_1921684158, copias_1921684159, copias_192168854, copias_192168858, copias_192168859]

#Importa biblioteca para deixar saída colorida no terminal
from termcolor import colored 

#Importa mensagem de erro
import mensagem_erro

#importa nome do desenvolvedor
import mostra_desenvolvedor

def separa():
    print(30 *"*")

#mostra_desenvolvedor.mostra_desenvolvedor()

number = 0 

stop = len(arquivos_contadores)

#Numero de cópias alcancado para solicitar toner



#IMPORTANDO BIBLIOTECA PARA TRABALHAR COM COMANDOS DO SISTEMA
import sys
#import gera_log



##############################
#INSERINDO CLASS IMPRESSORA
############################




toners_solicitados = 0
while number < stop:
    tipo_retorno = (type(arquivos_contadores[number].number_copies))
    
    if tipo_retorno == int:
        separa()
        #VERIFICA LOJA DA IMPRESSORA
        impressora_individual = printers_list[number]
        if impressora_individual[8] == "3":
            print ("Impressora do ariston")
        elif impressora_individual[8] == "1":
            print("Impressora da loja 4")
        elif impressora_individual[8] == "4":
            print("Impressora da Matriz")
        elif impressora_individual[8] == "2":
            print("Impressora da loja 2")
        elif impressora_individual[8] == "8":
            print("Impressora de Cajamar")
        else:
            print("Impressora não identificada")
        print (colored ("Impressora: {}".format(arquivos_contadores[number].printer_name), 'green'))
        print (colored ("Contador: ", "red") , arquivos_contadores[number].number_copies)
        print ("Ultimo contador", arquivos_contadores[number].ultimo_contador) 
        print ("Arquivo de referência: ", arquivos_contadores[number].arquivo_name)
                
        #Verifica o modelo da impressora e estabelece quantas cópias a mesma pode imprimir entre um pedido e outro
        maximo_copias = 0

        verifica_modelo = arquivos_contadores[number].serial_number[0:2]

        if verifica_modelo == ("AK"):
            maximo_copias = 8500
        elif verifica_modelo != ("AK"):
            maximo_copias = 14000
        else:
            print("MODELO DE IMPRESSORA NÃO IDENTIFICADO, IMPOSSÍVEL ESTABELECER O NÚMERO LIMITE DE IMPRESSÕES PARA SOLICITAR TONER")

        

        nome = arquivos_contadores[number].arquivo_name
        contador = arquivos_contadores[number].number_copies
        ultimo_contador = arquivos_contadores[number].ultimo_contador 
        

        


        #Verifica se solicitação de toner é necessária
        if contador > ultimo_contador + maximo_copias:
            print('\33[5m' + colored("SOLICITE TONER.", "yellow") + '\33[6m' + '\033[m')
            toners_solicitados += 1
            with open('./printers_log/' + str(nome) + ".py" , 'w') as arquivo:
                print('ultimo_contador = ({})\nnumber_copies= ({})\nserial_number= ("{}")\nprinter_name= ("{}")\narquivo_name= ("{}")'.format(arquivos_contadores[number].number_copies, arquivos_contadores[number].number_copies, arquivos_contadores[number].serial_number, arquivos_contadores[number].printer_name, arquivos_contadores[number].arquivo_name) , file=arquivo)


                #print('ultimo_contador = ({})\nnumber_copies= ({})\nserial_number= ("{}")\nprinter_name= ("{}")\narquivo_name= ("{}")'.format(nome.ultimo_contador, nome.number_copies, nome.serial_number, nome.printer_name, nome.arquivo_name) , file=arquivo)




            #ENVIA E-MAIL CASO SEJA NECESSÁRIO SOLICITAR O TONER

            # conexão com os servidores do google
            smtp_ssl_host = 'smtp.gmail.com'
            smtp_ssl_port = 465
            # username ou email para logar no servidor
            username = 'fictitiousmail@gmail.com'
            password = 'fictitiouspasswd'

            from_addr = 'fictitiousmail@gmail.com'
            to_addrs = ['recipientsmail@casasaopedro.com.br']

            # a biblioteca email possuí vários templates
            # para diferentes formatos de mensagem
            # neste caso usaremos MIMEText para enviar
            # somente texto
            message = MIMEText('Solicitar toner para impressora {}'.format(arquivos_contadores[number].printer_name))
            message['subject'] = 'Solicitar toner para impressora'
            message['from'] = from_addr
            message['to'] = ', '.join(to_addrs)

            # conectaremos de forma segura usando SSL
            server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
            # para interagir com um servidor externo precisaremos
            # fazer login nele
            server.login(username, password)
            server.sendmail(from_addr, to_addrs, message.as_string())
            server.quit()

        else:
            print("Não solicite ainda")
            print ("Aguardar impressora imprimir mais : ", ( maximo_copias - (contador - ultimo_contador) ), (" copias para solicitar toner"))

           # with open('./printers_log_ultimo_contador/' + str(nmeome) + ".py" , 'w') as arquivo:
             #   print ('contador_pedido =({})'.format("CONSEGUIR COLOCAR O CALOR DA VARIÁVEL DE DENTRO DE printers_log_backup_Com_contadores_Certos AQUI"), file=arquivo)


            
                
 
        
        

    else:
        separa()
        #'\33[5m faz piscar no terminal
        print ('\33[5m' + colored("Impossível estabelecer comunicação com a impressora.", "red") + '\33[6m' + '\033[m')
        mensagem_erro.mensagem_erro()
    number +=1 

number = 0


print (arquivo_log_formatado)
print("Total de toners: ", toners_solicitados)
print ("FIM")
#sintaxe do gerador de arquivos de log arquivo = open("log_" + str(msg) + ".txt",'a+')



#TESTE DE EXECUÇÃO AUTONOMO DELETAR:


with open('/home/Julio/Desktop/python_barkev/printerControl/log/log_programa.txt', 'a') as arquivo:
    print ('Python executado com sucesso', file = arquivo)
    
