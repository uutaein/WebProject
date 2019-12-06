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
});

app.get('/:idx', function (req, res, next) {
    //날짜 req.params.idx로불러 오면됨
    var code_list = connection.query(`select code,name,date_format(start_date,'%Y-%m-%d') as date from code_list where start_date < '${req.params.idx}' order by name asc `,function(err,result){
        res.send(result);
    })
});


app.post('/api', function (req, res, next) {
    var date= req.body.date;//입력받은 날짜
    //console.log(date);
    var stockCode=req.body.stockCode;//선택한 종목코드의 배열
    //console.log(stockCode);
    var querylist = '';
    for(i=0;i<stockCode.length;i++)
    {
        //query = 'SELECT * from c' +stockCode[i] + 'where date between' +date+ 'and "2019-11-20";';
        query = `SELECT close,date from c${stockCode[i]} where date between '${date}' and '2019-11-26';`
        querylist += query;
        
    }
    querylist += `select close,date from ckospi_index where date between '${date}' and '2019-11-26';`
    connection.query(querylist,function(req,result){
        //console.log(result);
        res.send(result);
    })
    //console.log(querylist);
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
        //console.log(result);
        res.send(result);
    })
})
app.post('/stat',function(req,res,next){
    var Min_size = req.body.minstat[0]
    var Min_volume = req.body.minstat[1]
    var Min_momentum= req.body.minstat[2]
    var Min_low_val= req.body.minstat[3]
    var Min_growth= req.body.minstat[4]
    var Min_profit= req.body.minstat[5]
    var Max_size = req.body.maxstat[0]
    var Max_volume = req.body.maxstat[1]
    var Max_momentum= req.body.maxstat[2]
    var Max_low_val= req.body.maxstat[3]
    var Max_growth= req.body.maxstat[4]
    var Max_profit= req.body.maxstat[5]

    
    const Range_size = `size_rank>=${Min_size} and size_rank<=${Max_size}`
    const Range_volume = `volume_rank>=${Min_volume} and volume_rank<=${Max_volume}`
    const Range_momentum = `momentum_3m_profitage_rank>=${Min_momentum} and momentum_3m_profitage_rank<=${Max_momentum}`
    const Range_low_val = `low_val_rank>=${Min_low_val} and low_val_rank<=${Max_low_val}`
    const Range_growth = `growth_rank>=${Min_growth} and growth_rank<=${Max_growth}`
    const Range_profit = `profitage_rank>=${Min_profit} and profitage_rank<=${Max_profit}` 
    console.log(Range_size,Range_volume,Range_momentum,Range_low_val,Range_growth,Range_profit)
    // connection.query(`select * from rank_corp where ${Range_size} and ${Range_volume} and ${Range_momentum} and ${Range_low_val} and ${Range_growth} and ${Range_profit}`,function(err,res){
    //     res.send(result);
    // })
    res.send("돌아가는값")
})
// app.get('/',function(req,res,next){
//     console.log("req.body = " + req.body)
//     connection.query(`SELECT * from c005930 WHERE date=${req.body}`,function(err,result){
//         console.log("result : " + result);
//         res.send(result);
//     })
// })

module.exports = app