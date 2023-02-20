from flask import Flask
from datetime import datetime
from pytz import timezone
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def time():
    current_time = datetime.now(timezone('Europe/Moscow')).strftime('%H:%M:%S')
    with open('visits', 'a') as file:
        file.write(current_time + '\n')
    return current_time

@app.route('/visits')
def visits():
    with open('visits', 'r') as file:
        return '<div>'.join(file.readlines())

if __name__ == '__main__':
    app.run(host="127.0.0.1")