from flask import Flask, jsonify
from MongoDB import Database
app = Flask(__name__)

@app.route('/')
def test():
    collection = Database.test

    rs = collection.find()
    op = {}
    for x in rs:
        _id = str(x['_id'])
        x.pop('_id')
        op[_id] = x

    return jsonify(op)

if __name__ == "__main__":
    app.run(debug=True, port=8000)