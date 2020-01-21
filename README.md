# desafio-certi

## Pré requisitos:
Para executar esta aplicação você deve ter o Docker instalado.
* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

## Uso:
Clone este repositório
```shell
$ git clone https://github.com/KaelKill/desafio-certi.git
```
Navegue para o diretório clonado
```shell
$ cd desafio_certi
```

Monte o container
```shell
$ docker build desafio_certi .
```
Execute o container em segundo plano
```shell
$ docker run -d -p 5000:5000 desafio_certi
```

Acesse o endereço 127.0.0.1:5000/*numeros* passando numeros entre -99999 e 99999
```shell
$ curl 127.0.0.1:5000/5000
{"extenso": "cinco mil"}

$curl 127.0.0.1:5000/-14753
{"extenso": "menos quatorze mil e setecentos e cinquenta e tres"}
```
É possivel obter a resposta em ingles acrescentando */en* à URL:
```shell
$ curl 127.0.0.1:5000/5000
{"written form": "five thousand"}
```