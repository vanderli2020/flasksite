FROM python:latest
COPY . /a/app
WORKDIR /a/app
RUN pip install -r requirements.txt
EXPOSE 7001
ENTRYPOINT [ "python" ]
CMD [ "meu_site.py" ]