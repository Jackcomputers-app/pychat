# PYchat
 Chat using python
This will let you chat on a local server using Python. 

Install instructions for Liunx

The default directory has the SSL version of pychat running. 

This will not run localy if you would like to run localy use the http pychat version.

Ensure you have Python3 installed on your machine

```bash

python3

```

Download the file from this github repo onto your computer.

```bash

wget https://github.com/Jackcomputers-app/pychat/archive/refs/heads/main.zip

```

Unzip the folder

```bash

unzip main.zip

```

Install the Python virtual envorment toolkit 

```bash

sudo apt install python3.12-venv

```

Create a python virtual envioment

```bash

python3 -m venv venv

```

Enter the Python virtual envoment

```bash

source venv/bin/activate

```

Your CLI should have a (venv) in it. 

Install Flask

```bash

pip install flask

```

Install socket.io that is used to send and recieve messages. 

```bash

pip install flask-socketio

```

Install eventlet

```bash

pip install eventlet

```

Install certbot and request an ssl certifate for your domain name. Replace (example.com) with your domain name. 

```bash

sudo apt install certbot
sudo certbot certonly --standalone -d example.com

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

Update the javascript domain in the index.html file with your domain name. 


```bash

cd Templates
nano index.html

```

```javascript

var socket = io.connect("https://example.com");//Replace example.com with the domain name of your website.

```

Run the server and start chating accross the internet. 

```bash

python3 chat_server.py

```
