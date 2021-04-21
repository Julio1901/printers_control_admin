<h1>Printers control admin</h1>
<p>Programa simples feito para ser implementado em rede afim de administrar a vida útil de toners de impressoras. O mesmo tem uma proposta simples mas funcional:</p>
* Colhe os dados das impressoras na rede através do protocolo SNMP implementado em um Shell Script
* Trata os dados colhidos, confrontando os mesmos com históricos previamente salvos das impressoras
* Analisa com base no modelo da impressora e número de cópias emitidas pela mesma desde a última substituição de toner se será necessário uma nova substituição em breve
* Envia um e-mail de alerta para o administrador responsável pela rede informando que em breve será necessário substituir o toner de uma determinada impressora

> Status do Projeto: Em desenvolvimento :warning:

<p>:exclamation: ATUALMENTE O PROJETO ESTÁ SENDO REFATORADO. O MESMO SE MOSTROU EXTREMAMENTE EFICAZ, PORÉM, UM NOVO CÓDIGO ESTÁ SENDO CONSTRUÍDO COM O PARADIGMA ORIENTADO À OBJETOS E INTEGRAÇÃO DA APLICAÇÃO À UM BANCO DE DADOS. O MESMO SERÁ CONSTRUÍDO COMO UM APLICATIVO WEB CONTANDO COM UMA INTERFACE GRÁFICA PARA O ADMINISTRADOR</p>

# Requeriments:

* Python 3.8
* SNMP instalado em sua máquina


## Motivação:
<p>Ao tomar posse do emprego no qual me encontro no momento, verifiquei que a rotina repetitiva de administração de toners de imperssoras era feita manualmente todos os dias. Sendo assim, iniciei a tarefa da criação desse pequeno programa que, uma vez implementado, possibilitou que os integrantes do setor de T.I se concentrem em outras tarefas no dia-a-dia uma vez que essa administração que tomava um tempo considerável, agora, é feita de forma automatizada. <p/>
