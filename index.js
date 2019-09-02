var express = require('express');
var inMode = require('./controllers/inMode');
var app = express();

//set up engine
app.set('view engine', 'ejs');

//use static files
app.use(express.static('.public'));

//fire InMode controller
inMode(app);

app.listen(3402);