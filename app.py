from flask import Flask, jsonify, request
import os
import socket
from datetime import datetime
# деплой 3
app = Flask(__name__)

@app.route('/')
def home():
    """Главная страница"""
    base_url = request.url_root.rstrip('/')
    return jsonify({
        'message': 'Добро пожаловать в Flask тестовое приложение!',
        'status': 'running',
        'container_id': os.environ.get('HOSTNAME', 'unknown'),
        'endpoints': {
            'home': f'{base_url}/',
            'health': f'{base_url}/health',
            'info': f'{base_url}/info',
            'env': f'{base_url}/env',
            'server_time': f'{base_url}/time',
            'server_date': f'{base_url}/date',
            'server_datetime': f'{base_url}/datetime'
        }
    })


@app.route('/health')
def health():
    """Эндпоинт для проверки работоспособности"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'hostname': socket.gethostname()
    })


@app.route('/info')
def info():
    """Информация о контейнере"""
    return jsonify({
        'app': 'Flask Action Test',
        'version': '1.0.5',
        'python_version': os.popen('python --version').read().strip(),
        'container_id': os.environ.get('HOSTNAME', 'unknown'),
        'environment': os.environ.get('FLASK_ENV', 'development')
    })


@app.route('/env')
def get_env():
    """Показывает переменные окружения (безопасные)"""
    safe_vars = {
        'FLASK_ENV': os.environ.get('FLASK_ENV'),
        'APP_NAME': os.environ.get('APP_NAME', 'Flask Test'),
        'PORT': os.environ.get('PORT', '8080')
    }
    return jsonify({'environment': safe_vars})


@app.route('/time')
def server_time():
    """Возвращает текущее время сервера"""
    now = datetime.utcnow()
    return jsonify({
        'server_time': now.isoformat() + 'Z',
        'timestamp': int(now.timestamp()),
        'timezone': 'UTC'
    })


@app.route('/date')
def server_date():
    """Возвращает текущую дату сервера"""
    now = datetime.utcnow()
    return jsonify({
        'server_date': now.strftime('%Y-%m-%d'),
        'day_of_week': now.strftime('%A'),
        'day_of_year': now.timetuple().tm_yday
    })


@app.route('/datetime')
def server_datetime():
    """Возвращает полную дату и время сервера"""
    now = datetime.utcnow()
    return jsonify({
        'datetime': now.isoformat() + 'Z',
        'date': now.strftime('%Y-%m-%d'),
        'time': now.strftime('%H:%M:%S'),
        'timestamp': int(now.timestamp()),
        'timezone': 'UTC',
        'formatted': now.strftime('%Y-%m-%d %H:%M:%S UTC')
    })


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)
