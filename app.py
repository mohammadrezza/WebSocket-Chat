from flask_socketio import SocketIO
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)


@app.route('/',methods=['GET'])
def sessions():
    return render_template('session.html')


def message_received():
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=message_received)


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", debug=True)
