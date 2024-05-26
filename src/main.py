'''
    Estando dentro do diretório criado pelo virtualenv (projeto)
    Instalar o scrapy:
    $ pip install scrapy
    Criar o projeto scrapy:
    $ scrapy createproject <Nome do projeto scrapy>
    Entrar no diretório do projeto
    $ cd <Nome do projeto>
    Gerar o projeto Spider:
    $ scrapy genspider <projeto_spider> <url do domínio de busca>
    Abrir o shell para testes e seleção/verificação dos itens:
    $ scrapy shell
        fatch('https://www.imdb.com/chart/top') -> se resultado 200 deu certo a conexão
        Usar o plugin cssSelector do Chrome ou o F12 para identificar as partes de informação que precisamos pegar
    O desenvolvimento é feito no arquivo <projeto_spider>.py que fica dentro da pasta
        <Nome do projeto>/<Nome do projeto scrapy>/<Nome do projeto scrapy>/spiders
    Executar o projeto:
    $ scrapy crawl <projeto_spider>
    $ scrapy crawl <projeto_spider> -O <arquivo>.json # a opção -o faz append
    $ scrapy crawl <projeto_spider> -O <arquivo>.csv  # a opção -o faz append
'''

