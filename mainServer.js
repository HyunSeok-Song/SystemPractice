var fs = require('fs');
var express = require('express');
var app = express();

mysql = require('mysql');
var connection = mysql.createConnection({
    host: 'localhost',
    user: 'sensor',
    password: 'kmucs',
    database: 'data'
})
connection.connect();

app.get("/insert", function(req, res) {
	req.query.value = Number(req.query.value)
	fs.appendFile('data.txt', JSON.stringify(req.query),function(err){});
	var query = connection.query('insert into sensors set ?', req.query, function(err, rows, cols) {
		if (err) throw err;
    	});
	console.log("data received >> " + JSON.stringify(req.query));
	console.log("send Data to DB");
	res.send("data received >> " + JSON.stringify(req.query));
});


app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
})
