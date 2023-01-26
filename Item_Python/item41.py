#Item 4
 
from flask import Flask 
import socket 
app = Flask(__name__) 
@app.route('/') 
def ip_address(): 
hostname = socket.gethostname() 
ip = socket.gethostbyname(hostname) 
return f'La ip de conexion es {ip}:8000' 
if __name__ == '__main__': 
app.run(port=8000)
