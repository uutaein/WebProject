const app = require('express')()
const cors = require('cors')


app.use(cors({ origin : true}))

//Made by 201521005 , 박병건 
var mysql      = require('mysql');
var connection = mysql.createConnection({
    host     : 'db-mysql.cj5nhbnzm5ke.ap-northeast-2.rds.amazonaws.com',
    user     : 'admin',
    password : 'adminroot',
    port     :3306,
    database : 'stockdb'
})
connection.connect();

//Made by 201521005 , 박병건 
app.get('/',function(req,res,next){
    connection.query(`SELECT * from c000020 WHERE date>20191120`,function(err,result){
        console.log(result);

        res.send(result);
    })
})


module.exports = app