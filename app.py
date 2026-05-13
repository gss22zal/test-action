from flask import Flask, jsonify
import os
import socket
from datetime import datetime
# деплой 3
app = Flask(__name__)

@app.route('/')
def home():
    """Главная страница"""
    return jsonify({
        'message': 'Добро пожаловать в Flask тестовое приложение!',
        'status': 'running',
        'container_id': os.environ.get('HOSTNAME', 'unknown')
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
        'PORT': os.environ.get('PORT', '8000')
    }
    return jsonify({'environment': safe_vars})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)
