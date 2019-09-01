from pymongo import MongoClient
client = MongoClient("mongodb://test:test@cluster0-shard-00-00-razp3.mongodb.net:27017,cluster0-shard-00-01-razp3.mongodb.net:27017,cluster0-shard-00-02-razp3.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.get_database('number_plate_det_iot');
records = db.number_plate
new_number_plate = {
    'MODE' : 'OUT',
    'NUMBER': 'MH13UE9098',
    'DATE' : '01:09:2019',
    'TIME' : '16:30'
}
records.insert_one(new_number_plate)
ans = records.count_documents({})

print(ans)
#  <!-- <% for(var i=0;i<inData.length;i++){%>
#                 <tr>
#                     <td><%= inData[i].DATE%></td>
#                     <td><%= inData[i].NUMBER%></td> 
#                     <td><%= inData[i].TIME%></td>
#                 </tr>
#                 <%}%> -->