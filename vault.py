# Created by Sumit Gupta

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/getkey')
def getKey():
	f = open("key.txt", rw)
	line1 = f.readline()
	if(isExpired(line1)):
		pass
	else:
		pass

@app.route('/setkey')
def setKey():
	pass
