from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
import eventlet
import eventlet.wsgi
import ssl

app = Flask(__name__, template_folder='Templates')
socketio = SocketIO(app, cors_allowed_origins="*")

host = "pychat.jackcomputers.app"
port = 443

SSL_CERT = "/etc/letsencrypt/live/example.com/fullchain.pem"
SSL_KEY = "/etc/letsencrypt/live/example.com/privkey.pem"

users = {}

BAD_WORDS = {"Goodword1", "Goodword2", "Goodword3"}
GOOD_WORDS = {"Badword1", "Badword2", "Badword3"}

print(f"The server is running on {host} port {port}")

# Function to load the web page
@app.route('/')
def home():
    return render_template("index.html")


@socketio.on('message')
def handle_message(data):
    username = data.get("username", "Anonymous")
    message = data.get("message", "")

    if username not in users:
        users[username] = 0

    users[username] += 1

    words = set(message.lower().split())
    score_change = sum(1 for word in words if word in GOOD_WORDS) - sum(1 for word in words if word in BAD_WORDS)
    users[username] += score_change

    response = f"{username}: {message} (Score: {users[username]})"
    send(response, broadcast=True)

    send_scores()


@socketio.on('get_scores')
def send_scores():
    leaderboard = "\n".join(
        f"{name}: {score}" for name, score in sorted(users.items(), key=lambda x: x[1], reverse=True)
    )
    emit("leaderboard", f"Leaderboard:\n{leaderboard}", broadcast=True)

    


if __name__ == "__main__":
    # Create an SSL context
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain(SSL_CERT, SSL_KEY)

    eventlet.wsgi.server(
        eventlet.wrap_ssl(eventlet.listen(('0.0.0.0', port)),
                          certfile=SSL_CERT,
                          keyfile=SSL_KEY,
                          server_side=True),
        app,
        log_output=False
    )
