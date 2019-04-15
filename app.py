from flask_socketio import SocketIO
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_socket_io_key'
socket_io = SocketIO(app)

rooms = ["nsp1", "nsp2"]


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', nsp=rooms)


@app.route('/sessions', methods=['POST'])
def sessions():
    body = request.form.to_dict()
    username = body["username"]
    nsp = body["nsp"]
    return render_template('sessions.html', username=username, nsp=nsp)


@socket_io.on('msg event', namespace="/nsp1")
def nsp1_msg_event(json):
    socket_io.emit('resp msg event', json, namespace="/nsp1")


@socket_io.on('msg event', namespace="/nsp2")
def nsp2_msg_event(json):
    socket_io.emit('resp msg event', json, namespace="/nsp2")


@socket_io.on('cus event')
def handle_cus_event(json):
    print(json)
    socket_io.emit('resp cus event', json, namespace="/")


if __name__ == '__main__':
    socket_io.run(app, host="0.0.0.0", debug=True, use_reloader=True)
