from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

messages = []


@app.route('/', methods=['GET', 'POST'])
def chat():
    global messages
    if request.method == 'POST':
        # Simulate CPU load for HPA testing
        for _ in range(1000000):
            pass  # Busy loop

        username = request.form['username']
        message = request.form['message']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        messages.append({'username': username, 'message': message, 'timestamp': timestamp})
    return render_template('chat.html', messages=messages)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
