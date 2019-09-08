from pymongo import MongoClient
from flask import Flask, render_template
import json
app = Flask(__name__)
client = MongoClient("mongodb://test:test@cluster0-shard-00-00-razp3.mongodb.net:27017,cluster0-shard-00-01-razp3.mongodb.net:27017,cluster0-shard-00-02-razp3.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.get_database('number_plate_detection')

in_record = db.in_
out_record = db.out
final_record = db.final

# in_number_plate = [{
#     'NUMBER': 'UP23NJ4567',
#     'DATE' : '01:09:2019',
#     'TIME' : '17:30'
# },{
#     'NUMBER': 'HT83DJH7486',
#     'DATE' : '02:09:2019',
#     'TIME' : '17:30'
# },{
#     'NUMBER': 'NR85ND9495',
#     'DATE' : '03:09:2019',
#     'TIME' : '17:30'
# },{
#     'NUMBER': 'LA75DJ4950',
#     'DATE' : '04:09:2019',
#     'TIME' : '17:30'
# },{
#     'NUMBER': 'NF76MF4070',
#     'DATE' : '05:09:2019',
#     'TIME' : '17:30'
# },{
#     'NUMBER': 'DG56DH5758',
#     'DATE' : '06:09:2019',
#     'TIME' : '17:30'
# },{
#     'NUMBER': 'AP75JD7592',
#     'DATE' : '07:09:2019',
#     'TIME' : '17:30'
# }]

# out_number_plate = [{
#     'NUMBER': 'UP23NJ4567',
#     'DATE' : '01:09:2019',
#     'TIME' : '18:30'
# },{
#     'NUMBER': 'HT83DJH7486',
#     'DATE' : '02:09:2019',
#     'TIME' : '18:30'
# },{
#     'NUMBER': 'NR85ND9495',
#     'DATE' : '03:09:2019',
#     'TIME' : '18:30'
# },{
#     'NUMBER': 'LA75DJ4950',
#     'DATE' : '04:09:2019',
#     'TIME' : '18:30'
# },{
#     'NUMBER': 'NF76MF4070',
#     'DATE' : '05:09:2019',
#     'TIME' : '18:30'
# },{
#     'NUMBER': 'DG56DH5758',
#     'DATE' : '06:09:2019',
#     'TIME' : '18:30'
# },{
#     'NUMBER': 'AP75JD7592',
#     'DATE' : '07:09:2019',
#     'TIME' : '18:30'
# }]
# in_record.insert_many(in_number_plate)
# out_record.insert_many(out_number_plate)


@app.route('/')
def real():
    return render_template('real.html', in_ = _in_, out_ = _final_)

if __name__ == "__main__":
    k = 'c'
    while  k != 'g':
        _in_ = list(in_record.find())
        _out_ = list(out_record.find())
        _final_ = list(final_record.find())

        for item in _out_:
            NUMBER = item['NUMBER'] 
            EXIT_DATE = item['DATE']
            EXIT_TIME = item['TIME']
            ENTRY_TIME = item['TIME']
            ENTRY_DATE = item['DATE']
            for i in _in_:
                if i['NUMBER'] == item['NUMBER']:
                    ENTRY_DATE = i['DATE']
                    ENTRY_TIME = i['TIME']
                    break
            js = {
                'NUMBER' : NUMBER,
                'ENTRY DATE' : ENTRY_DATE,
                'ENTRY TIME' : ENTRY_TIME,
                'EXIT DATE' : EXIT_DATE,
                'EXIT TIME' : ENTRY_TIME
            }
            in_record.delete_one({
                'NUMBER' : NUMBER,
                'DATE' : ENTRY_DATE,
                'TIME' : ENTRY_TIME
            })
            _final_.append(js)
            final_record.insert_one(js)
        # print("final")
        # print(_final_)
        out_record.delete_many({})

        # print("new count")
        in_ = in_record.count_documents({})
        out_ = out_record.count_documents({})
        final_ = final_record.count_documents({})
        # print(in_)
        # print(out_)
        # print(final_)
        app.run()
        k = input("input : ")