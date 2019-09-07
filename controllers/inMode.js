var data = [{NUMBER : 'MH34NK9876' , TIME : '12:30' , DATE : '02:09:2019'},{NUMBER : 'MH78BH6482' , TIME : '21:30' , DATE : '02:09:2019'},{NUMBER : 'MH34SR9456' , TIME : '11:30' , DATE : '03:09:2019'}];
// var mongoose = require('mongoose').MongoClient
// mongoose.connect('mongodb://localhost:2701mongodb+srv://test:test@cluster0-razp3.mongodb.net/test?retryWrites=true&w=majority');

// var inSchema = new mongoose.Schema({
//     MODE : String,
//     NUMBER : String,
//     DATE : String,
//     TIME : String
// });

// var inn = mongoose.model('inn',inSchema);

// var itemOne = Todo({NUMBER : 'MH34NK9876' , TIME : '12:30' , DATE : '02:09:2019'}).save(function(err){
//     if (err) throw err;
//     console.log('plate pushed')
// });

// var mongo = require('mongodb').MongoClient;
// var url = 'mongodb://localhost:27017';

// mongo.connect(url, {
//     useNewUrlParser: true,
//     useUnifiedTopology: true
//   }, (err, client) => {
//   if (err) {
//     console.error(err)
//     return
//   }
//   //...
// });
// var db = client.db('kennel');
// var collection = db.collection('dogs');
// collection.insertOne({name: 'Roger'}, (err, result) => {

// });
// collection.insertMany([{name: 'Togo'}, {name: 'Syd'}], (err, result) => {

// });
module.exports = function(app){
    
    app.get('/in',function(req,res){
        
        res.render('in',{name : data});
    });
    

    app.delete('/in',function(req,res){
        
    });

};
