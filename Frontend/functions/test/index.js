const app = require('express')()
const cors = require('cors')


app.use(cors({ origin : true}))

//Made by 201521005 , 박병건 
var mysql      = require('mysql');
var connection = mysql.createConnection({
    multipleStatements: true,
    host     : 'db-mysql.cj5nhbnzm5ke.ap-northeast-2.rds.amazonaws.com',
    user     : 'admin',
    password : 'adminroot',
    port     :3306,
    database : 'stockdb'
})
connection.connect();

app.get('/:idx', function (req, res, next) {
    //날짜 req.params.idx로불러 오면됨
    var code_list = connection.query(`select code,name,start_date from code_list where start_date < '${req.params.idx}' order by code `,function(err,result){
        res.send(result);
    })
});

app.post('/api', function (req, res, next) {
    var date= req.body.date;//입력받은 날짜
    console.log(date);
    var stockCode=req.body.stockCode;//선택한 종목코드의 배열
    console.log(stockCode);
    var querylist = '';
    for(i=0;i<stockCode.length;i++)
    {
        //query = 'SELECT * from c' +stockCode[i] + 'where date between' +date+ 'and "2019-11-20";';
        query = `SELECT * from c${stockCode[i]} where date between '${date}' and '2019-11-20';`
        querylist += query;
        
    }
    querylist += `select close,date from ckospi_index where date between '${date}' and '2019-11-20';`
    connection.query(querylist,function(req,result){
        console.log(result);
        res.send(result);
    })
    console.log(querylist);
});

app.post('/apitest', function (req, res, next) {
    var start_date= req.body.start_date;//입력받은 날짜
    var end_date = req.body.end_date;
    var stockCode=req.body.stockCode;//선택한 종목코드의 배열
    var querylist = '';
    for(i=0;i<stockCode.length;i++)
    {
        //query = 'SELECT * from c' +stockCode[i] + 'where date between' +date+ 'and "2019-11-20";';
        query = `SELECT * from c${stockCode[i]} where date between '${start_date}' and '${end_date}';`
        querylist += query;
        
    }
    querylist += `select close,date from ckospi_index where date between '${start_date}' and '${end_date}';`
    connection.query(querylist,function(req,result){
        console.log(result);
        res.send(result);
    })
    console.log(querylist);
});

//Made by 201521005 , 박병건 
app.post('/',function(req,res,next){
        //select * from `c005930` join `c066570` on c005930.date = c066570.date and c005930.date between '2019-11-20' and '2019-11-26'
        //connection.query(`SELECT * from c005930 join c000020 WHERE date= ${req.body.start}`,function(err,result)
        
        //made by 201521005 박병건
        connection.query(`SELECT * from c005930 WHERE date between '2019-10-26' and '2019-11-26'`,function(err,result){
        //connection.query(`select * from c005930 join c066570 where c005930.date = c066570.date and c066570.date between '2019-11-20' and '2019-11-26'`,function(err,result){
        console.log(result);
        res.send(result);
    })
})
app.post('/strategy',function(req,res,next){
    
})
// app.get('/',function(req,res,next){
//     console.log("req.body = " + req.body)
//     connection.query(`SELECT * from c005930 WHERE date=${req.body}`,function(err,result){
//         console.log("result : " + result);
//         res.send(result);
//     })
// })

module.exports = app