var express = require('express');
var BodyParser = require("body-parser");
var inMode = require('./controllers/inMode');
var app = express();

//set up engine
app.set('view engine', 'ejs');

//use static files
app.use(express.static(__dirname+'/public/assets'));
app.use(BodyParser.json());
app.use(BodyParser.urlencoded({ extended: true }));
//fire InMode controller
inMode(app);

app.listen(3402);