# PYchat
 Chat using python
This will let you chat on a local server using Python. 

Install instructions for Linux

The default directory has the SSL version of pychat running. 

The SSL version is not intended to run locally. If you are looking to run localy run use the http pychat version. 

Ensure you have Python3 installed on your machine

```bash

python3

```

Download the file from this GitHub repo onto your server.

```bash

wget https://github.com/Jackcomputers-app/pychat/archive/refs/heads/main.zip

```

run apt update

```bash

sudo apt update

```

Ensure you have an unzip tool.

```bash

sudo apt install unzip

```

Unzip the folder

```bash

unzip main.zip

```

Move into the directory

```bash

cd pychat-main

```

Install the Python virtual environment toolkit

```bash

sudo apt install python3.12-venv

```

Create a python virtual envioment

```bash

python3 -m venv venv

```

Enter the Python virtual environment

```bash

source venv/bin/activate

```

Your CLI should have a (venv) in it. 

Install Flask

```bash

pip install flask

```

Install socket.io that is used to send and receive messages.

```bash

pip install flask-socketio

```

Install eventlet

```bash

pip install eventlet

```

Install certbot and request an SSL certificate for your domain name. Replace (example.com) with your domain name.

```bash

sudo apt install certbot
sudo certbot certonly --standalone -d example.com

```

Open the python file for the next two parts

```bash

nano chat_server.py

```

Update your domain name in the python script.

```python

host = "example.com"
port = 443

```

Update the ssl locatoin in the python script. Replace example.com with your domain name of your website.  


```python

SSL_CERT = "/etc/letsencrypt/live/example.com/fullchain.pem"
SSL_KEY = "/etc/letsencrypt/live/example.com/privkey.pem

```

Update the JavaScript domain in the index.html file with your domain name.


```bash

cd Templates
nano index.html

```

```javascript

var socket = io.connect("https://example.com");//Replace example.com with the domain name of your website.

```

Run the server and start chatting across the internet.

```bash

python3 chat_server.py

```
