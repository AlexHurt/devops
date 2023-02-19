FROM python:3.10

COPY . /app_python
WORKDIR /app_python

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python" ]

CMD ["server.py" ]

EXPOSE 5000