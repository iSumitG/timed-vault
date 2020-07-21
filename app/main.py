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
		raise Exception("A lock is in progress")

@app.route('/setkey')
def setKey():
	f = open("key.txt", rw)
	line1 = f.readline()
	if(isExpired(line1)):
		# proceed with setting the key
		pass
	else:
		raise Exception("A lock is in progress")
