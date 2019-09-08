from pymongo import MongoClient
from flask import Flask, render_template
client = MongoClient("mongodb://test:test@cluster0-shard-00-00-razp3.mongodb.net:27017,cluster0-shard-00-01-razp3.mongodb.net:27017,cluster0-shard-00-02-razp3.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.get_database('Number_plate_detection_in');
db2 = client.get_database('Number_plate_detection_out');

records = db.in_data
records2 = db2.Out_time

in_number_plate = {
    'NUMBER': 'MH34MF9540',
    'DATE' : '01:09:2019',
    'TIME' : '17:30'
}

out_number_plate = {
    'NUMBER': 'MH34MF9540',
    'ENTRY DATE' : '01:09:2019',
    'EXIT DATE' : '02:09:2019',
    'ENTRY TIME' : '17:30',
    'EXIT TIME' : '10:30'
}


# records.insert_one(in_number_plate)
# records2.insert_one(out_number_plate)
in_ = records.count_documents({})
out_ = records.count_documents({})

print(in_)
print(out_)
_in_ = list(records.find())
_out_ = list(records2.find())
print(_in_)
print(_out_)


app = Flask(__name__)

@app.route('/')
def real():
    return render_template('real.html', in_ = _in_, out_ = _out_)

if __name__ == "__main__":
    app.run()
