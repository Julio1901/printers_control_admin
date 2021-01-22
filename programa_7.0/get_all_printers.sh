cat mostra_desenvolvedor.txt


sleep 2

echo "Coletando informações de impressoras, aguarde"


while read IP
do
  echo IP=$IP
   IP_ID=`echo $IP | tr -d "."`
   copias='copias_'$IP_ID'.py'
   echo $copias
   #Retorna Número do contador
   echo "Número de cópias impressas"
   x=`snmpwalk -c public -v1 $IP 1.3.6.1.2.1.43.10.2.1.4.1.1 -Ov  | cut -d\: -f2 | tr -d " " | head -1`
   c=`cat ./printers_log/$copias | grep "ultimo" | cut -d\( -f2 | cut -d\) -f1`
  
   echo ultimo_contador = '('$c')' > ultimo_printers_log/ultimo_$copias

   echo number_copies = '('$x')' > printers_log/$copias
   #Retorna número do serial 
   echo "Serial Number"
   y=`snmpwalk -c public -v1 $IP 1.3.6.1.2.1.1.6.0 -Ov | cut -d: -f2 | tr -d " "` 
   echo serial_number = '("'$y'")' >> printers_log/$copias
   #Retorna Nome da impressora
   echo "Printer name"
   z=`snmpwalk -c public -v1 $IP 1.3.6.1.2.1.1.5.0 -Ov | cut -d: -f2 | tr -d " "` 
   echo printer_name = '("'$z'")' >> printers_log/$copias
   #Atribui ultimo contador fictício
   #echo`cat ./printers_log_ultimo_contador/$copias` >> printers_log/$copias 
   #tinha funcionado a linha abaixo:
   #echo ultimo_contador = $c  >> printers_log/$copias
   echo ultimo_contador = '('`cat ./ultimo_printers_log/ultimo_$copias | grep "ultimo" | cut -d\( -f2 | cut -d\) -f1`')' >> printers_log/$copias
   #echo ultimo_contador =`cat ./printers_log/ultimo_$copias | grep "ultimo" | cut -d\( -f2 | cut -d\) -f1` >> printers_log/$copias
   echo arquivo_name = '"'copias_$IP'"' | tr -d "." >> printers_log/$copias

   #cat ./printers_log_pedidos/$copias >> printers_log/$copias


     echo "-------------------------------------"
done << EOF
192.168.1.152
192.168.1.153
192.168.1.155
192.168.1.157
192.168.1.158
192.168.2.155
192.168.2.156
192.168.2.157
192.168.3.151
192.168.3.153
192.168.3.154
192.168.3.155
192.168.3.156
192.168.3.157
192.168.3.158
192.168.3.159
192.168.4.154
192.168.4.155
192.168.4.156
192.168.4.157
192.168.4.158
192.168.4.159
192.168.8.54
192.168.8.55
192.168.8.57
192.168.8.58
192.168.8.59
EOF

echo "Coleta de dados completa"

sleep 2

echo "Iniciando análise de dados e automação de e-mail"

sleep 2

echo "Carregando script python"

sleep 2

python programa_6.0.py

sleep 3

sh /home/Julio/Desktop/python_barkev/printerControl/log/log_programa.sh


echo 'O programa será encerrado em 30 segundos']

sleep 30
