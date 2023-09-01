# ProjectDataBitCoin
Projeto final da matéria Data Engineer Data Science do MBA Full Stack Impacta. Trabalhando com dados do BitCoin

#Visão Geral do Projeto :

Projeto trata-se do consumo da API CoinApi afim de recuperar dados sobre as precificações do Bitcoin nos últimos 30 dias e últimos 5 anos. O código fonte foi construído em Python armazenando as informações em banco de dados SQL Server.

Linguagem de Progamação: Python 3.7.4
Banco de Dados: SQL Server

#Metodologia :
Para essa aplicação utilizei uma abordagem de código estrutural organizando as funcionalidades do mesmo em funções. A chamada da API foi feita com a lib requests, onde posteriormente com o JSON retornado é feito a conversão em DataFrame com a biblioteca Pandas. 

Utilizo a lib sqlalchemy para uso do recurso engine, que permite a inserção dos dados coletados através do próprio DataFrame. Essa se torna uma abordagem mais abrangente, permitindo um maior conforto na adaptação da automação, pois caso seja necessário mudar a tecnologia de banco de dados basta apenas trocar a string de conexão, dado o mesmo não estar limitado em inserção por Query. 

Após a persistência dos dados utilizo duas libs diferentes para elaboração dos gráficos. A visão do gráfico de 5 anos é feita com a biblioteca matplotlib enquanto que a visão do gráfico de 30 dias é feito com a biblioteca bokeh. A biblioteca bokeh se mostrou mais flexível para implementação com visão candlestick
