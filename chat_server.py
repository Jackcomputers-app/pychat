from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

host="localhost"
port="5000"

users = {}

BAD_WORDS = {"Fuck", "Dam", "Shit"}
GOOD_WORDS = {"Human", "AU Cyber", "Brandon"}

print("The server is running on",host,"port",port)

#Function to Load the web page
@app.route('/')
def home():
    return render_template("index.html")


@socketio.on('message')
def handle_message(data):
    username = data.get("username", "Anonymous")
    message = data.get("message", "")

    if username not in users:
        users[username] = 0

    words = set(message.lower().split())
    score_change = sum(1 for word in words if word in GOOD_WORDS) - sum(1 for word in words if word in BAD_WORDS)

    users[username] += score_change
    response = f"{username}: {message} (Score: {users[username]})"

    send(response, broadcast=True)


@socketio.on('get_scores')
def send_scores():
    leaderboard = "\n".join(
        f"{name}: {score}" for name, score in sorted(users.items(),))
    send(f"Leaderboard:\n{leaderboard}", broadcast=True)


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)


