from flask_socketio import SocketIO
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/chatroom', methods=['POST'])
def sessions():
    data = request.form.to_dict()
    username = data["username"]
    print(username)
    return render_template('session.html', username=username)


@socketio.on('msg event')
def handle_msg_event(json):
    # socketio.send(json, broadcast=True)
    print(json)
    socketio.emit('msg event', json)


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", debug=True, use_reloader=True)
