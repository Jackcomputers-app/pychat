#This program is made by Jack McCotter for CYB 220
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__,template_folder='Templates')
socketio = SocketIO(app, cors_allowed_origins="*")


#This is where your code will run on your. If you are planning on running on a server put that locaton. 
host="localhost"
port="5000"

users = {}

BAD_WORDS = {"Badword1", "Badword2", "Badword3"}
GOOD_WORDS = {"Goodword1", "Goodword2", "Goodword3"}

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


