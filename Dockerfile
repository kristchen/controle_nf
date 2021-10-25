FROM python:3.8.10
RUN mkdir /controle_nf
WORKDIR /controle_nf
ADD . /controle_nf
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "/controle_nf/manage.py", "makemigrations"]
CMD ["python", "/controle_nf/manage.py", "migrate"]
CMD ["cat", "/controle_nf/dump.sql",  "|", "sqlite3 /controle_nf/db.sqlite3"]
CMD ["python", "/controle_nf/manage.py", "runserver", "0.0.0.0:8000" ]
