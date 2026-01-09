from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Docker Lab - Python</title>
        <style>
            body {{ font-family: Arial; max-width: 800px; margin: 50px auto; }}
            .info {{ background: #e8f5e9; padding: 20px; border-radius: 8px; }}
        </style>
    </head>
    <body>
        <h1>Docker Python Rakendus</h1>
        <div class="info">
            <p><strong>Server Time:</strong> {datetime.datetime.now()}</p>
            <p><strong>Hostname:</strong> {socket.gethostname()}</p>
            <p>See Python Flask rakendus töötab Docker container'is</p>
        </div>
    </body>
    </html>
    '''

@app.route('/api/info')
def info():
    return jsonify({
        'hostname': socket.gethostname(),
        'timestamp': datetime.datetime.now().isoformat(),
        'status': 'running'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

=> CACHED [2/4] COPY requirements.txt .
=> CACHED [3/4] RUN pip install --no-cache-dir -r requirements.txt

