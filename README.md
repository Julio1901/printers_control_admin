<h1>Printers control admin</h1>

<p><b>Programa simples feito para ser implementado em rede afim de administrar a vida útil de toners de impressoras. O mesmo tem uma proposta simples mas funcional:</b></p>

* Colhe os dados das impressoras na rede através do protocolo SNMP implementado em um Shell Script
* Trata os dados colhidos, confrontando os mesmos com históricos previamente salvos das impressoras
* Analisa com base no modelo da impressora e número de cópias emitidas pela mesma desde a última substituição de toner se será necessário uma nova substituição em breve
* Envia um e-mail de alerta para o administrador responsável pela rede informando que em breve será necessário substituir o toner de uma determinada impressora

> Status do Projeto: Em desenvolvimento :warning:

<p>:exclamation: <b><i>atualmente o projeto está sendo refatorado. o mesmo se mostrou extremamente eficaz, porém, um novo código está sendo construído com o paradigma orientado à objetos e integração da aplicação à um banco de dados. o mesmo será construído como um aplicativo web contando com uma interface gráfica para o administrador</i></b></p>

# Requeriments:

* Python 3.8
* SNMP instalado em sua máquina


## Motivação:
<p>Ao tomar posse do emprego no qual me encontro no momento, verifiquei que a rotina repetitiva de administração de toners de imperssoras era feita manualmente todos os dias. Sendo assim, iniciei a tarefa da criação desse pequeno programa que, uma vez implementado, possibilitou que os integrantes do setor de T.I se concentrem em outras tarefas no dia-a-dia pois, agora, essa administração que tomava um tempo considerável, é feita de forma automatizada. <p/>
