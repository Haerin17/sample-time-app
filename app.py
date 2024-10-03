from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return f"Current time is: {current_time}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

