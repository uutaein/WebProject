const app = require('express')()

app.get('/',(req,res) => {
    res.send('read ok')
});



module.exports = app