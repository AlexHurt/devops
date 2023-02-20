from flask import Flask
from datetime import datetime
from pytz import timezone
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def time():
    current_time = datetime.now(timezone('Europe/Moscow')).strftime('%H:%M:%S')
    return current_time


if __name__ == '__main__':
    app.run(host="127.0.0.1")