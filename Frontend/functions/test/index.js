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
        //select * from `c005930` join `c066570` on c005930.date = c066570.date and c005930.date between '2019-11-20' and '2019-11-26'
        //connection.query(`SELECT * from c005930 join c000020 WHERE date= ${req.body.start}`,function(err,result)
        
        //made by 201521005 박병건
        connection.query(`select * from c005930 join c066570 where c005930.date = c066570.date and c005930.date between '2019-11-20' and '2019-11-26'`,function(err,result){
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