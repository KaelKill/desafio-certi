FROM python:3.7-alpine

RUN adduser -D desafio_certi

WORKDIR /home/desafio_certi

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY app app
RUN chown -R desafio_certi:desafio_certi ./
USER desafio_certi

EXPOSE 5000
ENTRYPOINT ["venv/bin/python"]
CMD ["app/server.py"]