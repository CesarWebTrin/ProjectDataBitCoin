# ProjectDataBitCoin
Projeto final da matéria Data Engineer Data Science do MBA Full Stack Impacta. Trabalhando com dados do BitCoin

# Visão Geral do Projeto :

Projeto trata-se do consumo da API CoinApi afim de recuperar dados sobre as precificações do Bitcoin nos últimos 30 dias e últimos 5 anos. O código fonte foi construído em Python armazenando as informações em banco de dados SQL Server.

Linguagem de Programação: Python 3.7.4

Banco de Dados: SQL Server

# Metodologia :
Para essa aplicação utilizei uma abordagem de código estrutural organizando as funcionalidades do mesmo em funções. A chamada da API foi feita com a lib requests, onde posteriormente com o JSON retornado é feito a conversão em DataFrame com a biblioteca Pandas. 

Utilizo a lib sqlalchemy para uso do recurso engine, que permite a inserção dos dados coletados através do próprio DataFrame. Essa se torna uma abordagem mais abrangente, permitindo um maior conforto na adaptação da automação, pois caso seja necessário mudar a tecnologia de banco de dados basta apenas trocar a string de conexão, dado o mesmo não estar limitado em inserção por Query. 

Após a persistência dos dados utilizo duas libs diferentes para elaboração dos gráficos. A visão do gráfico de 5 anos é feita com a biblioteca matplotlib enquanto que a visão do gráfico de 30 dias é feito com a biblioteca bokeh.plotting. 

# Limitações:
Para elaboração dos gráficos candlestick a biblioteca matplotlib se mostrou muito complexa, se tornando o principal motivador para o uso da biblioteca bokeh, onde a mesma se mostrou mais flexível para implementação com visão candlestick.

Reforço o uso do engine para persistência das informações em banco de dados, se tornando algo mais genérico não tendo depêndencia do uso da linguagem do banco de dados, contudo enfrentei alguns erros para uso da mesma pois algumas versões da biblioteca sqlalchemy não estão funcionando para essa funcionalidade

# Descobertas:

Nesse projeto a grande descoberta foi o uso da biblioteca bokeh.plotting ! Digo isso pois a mesma contém diversas possibilidades para a elaboração dos gráficos, podendo até mesmo ser utilizada outras visões como linhas e pontos. 

# Como usar ?

Para uso da aplicação é recomendado que crie uma máquina virtual para mesma e em seguida faça a atualização do Pip para garantir que o mesmo está atualizado.
Criação da VM: python -m venv venv 
Atualização PIP: python -m pip install --upgrade pip

Feito esses passos a única coisa a ser feita é instalar os requirements com o seguinte comando:
pip install -r requirements.txt

Para execução da aplicação basta startar o arquivo main.ipynb 
