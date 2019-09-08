var assert = require("assert");
var in_number_plate = [{NUMBER : 'MH34NK9876' , TIME : '12:30' , DATE : '02:09:2019'},{NUMBER : 'MH78BH6482' , TIME : '21:30' , DATE : '02:09:2019'},{NUMBER : 'MH34SR9456' , TIME : '11:30' , DATE : '03:09:2019'}];
var out_number_plate = [{
    NUMBER: 'MH34MF9540',
    ENTRY_DATE : '01:09:2019',
    EXIT_DATE : '02:09:2019',
    ENTRY_TIME : '17:30',
    EXIT_TIME : '10:30'
}];
var jj = [];
var MongoClient = require('mongodb').MongoClient;
const url = "mongodb+srv://test:test@cluster0-razp3.mongodb.net/test?retryWrites=true&w=majority";
MongoClient.connect(url, { useNewUrlParser: true }, (error, client) => {
    if(error) {
        throw error;
    }
    const db = client.db("Number_plate_detection_in");
    // var cursor = [db.collection('inventory').find({})];
    // console.log(cursor);
    collection = db.collection("in_data");
    collection.count(function (err, res) {
        if (err)
            throw err;
        console.log(res);
        // db.close();
    });
    collection.find({}, {explain:true}).toArray(function(err, docs) {
        assert.equal(null, err);
        jj = docs;
        // console.log(JSON.stringify(docs, null, 4));
        // console.log(docs);
        // var obj2 = JSON.parse(JSON.stringify(docs.ok));
        // console.log(obj2);
        client.close();
    });
    // function iterateFunc(doc) {
    //     console.log(JSON.stringify(doc, null, 4));
    //  }
     
    //  function errorFunc(error) {
    //     console.log(error);
    //  }
     
    //  cursor.forEach(iterateFunc, errorFunc);
    // var js = collection.find({});
    // console.log(js);
    // console.log(js);
    console.log("Connected to `" + "Number_plate_detection_in" + "`!");
    // console.log(db.getCollection());
});
module.exports = function(app){
    
    app.get('/in',function(req,res){
        
        res.render('in',{in_ : in_number_plate, out_ : out_number_plate, j : jj});
    });
    

    // app.delete('/in',function(req,res){
        
    // });

};
// Enter(indate, intime , number) Exit(outdate, out-time, number)