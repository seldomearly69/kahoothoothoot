from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://ryanlee99324:BrImAqgUaXaNuEz6@esdproj.r2bp9gh.mongodb.net/'
mongo = PyMongo(app)


#Find Bookings by email
@app.route("/routes/get/<string:email>")
def find_booking(email):
    r = mongo.db.routes.find_one({"email": email})
    if r:
        return jsonify(
            {
                "code": 200, 
                "data": r
            }
        )
    return jsonify(
        {
            "code": 404, 
            "message": "Record not found."
        }
    ), 404



#Save Routes
@app.route("/routes/save/<string:email>", methods=['PUT'])
def update_record(email):

    data = request.get_json()
    result = mongo.db.routes.update_one({"email": email}, {"$set": {"routes": data}}, upsert = True)
    if result.modified_count > 0:
        return jsonify(data), 200
    else:
        return jsonify("No records updated"),500



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=True)
