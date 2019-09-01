// var mongoose = require('mongoose');

// mongoose.connect("mongodb+srv://test:test@cluster0-razp3.mongodb.net/test?retryWrites=true&w=majority");

// var inSchema = new mongoose.Schema({
//     MODE : String,
//     NUMBER : String,
//     DATE : String,
//     TIME : String
// });

// var inMode = mongoose.model('inMode',inSchema);

module.exports = function(app){
    
    app.get('/in',function(req,res){
        res.render('in');
    });


    app.delete('/in/:NUMBER',function(req,res){
        
    });

};
