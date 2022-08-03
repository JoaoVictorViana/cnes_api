# Projeto de Obtenção dos dados do CNES

## Requerimentos:

- Python 3.8 ou mais
- Python Pip
- Python Flask

## Instalar

pip install -r ./requirements.txt

## Como utilizar

Antes de rodar a aplicação é necessário setar o valor da constante FLASK_APP:

export set FLASK_APP=app

Para rodar a aplicação basta rodar o comando:

flask run

Ao rodar a aplicação, será liberado uma url para fazer o download dos arquivos da CNES em csv, para isso, entre no seu navegador e acesse:

http://localhost:5000/download/PF/CE/2021/07

O padrão dos paramêtros são

http://localhost:5000/download/tipo/uf/ano/mes
