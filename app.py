from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/item", defaults={'item_id':0},methods=["GET", "POST", "PUT", "COPY"])
@app.route("/item/<item_id>", methods=["GET", "POST", "PUT", "COPY"])
def items(item_id):
	if request.method=="POST":
		return "POST"
	elif request.method=="PUT":
		return "PUT"
	elif request.method=="GET":
		if item_id==0:
			return "GET_LIST"
		return "GET %s" %(item_id)
	else:
		return "DEUZIKA!!!"

if __name__ == "__main__":
    app.run()