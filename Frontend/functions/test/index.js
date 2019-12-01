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
app.post('/',function(req,res,next){
        console.log("body:  "+ req.body.start);
    connection.query(`SELECT * from c005930 WHERE date= ${req.body.start}`,function(err,result){
        console.log(result);

        res.send(result);
    })
})
// app.get('/',function(req,res,next){
//     console.log("req.body = " + req.body)
//     connection.query(`SELECT * from c005930 WHERE date=${req.body}`,function(err,result){
//         console.log("result : " + result);
//         res.send(result);
//     })
// })

module.exports = app