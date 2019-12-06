const functions = require('firebase-functions');
const app = require('express')()
const cors = require('cors')
require('express-async-errors')

app.use(cors())

// // Create and Deploy Your First Cloud Functions
// // https://firebase.google.com/docs/functions/write-firebase-functions
//

// exports.helloWorld = functions.https.onRequest((request, response) => {
//  response.send("Hello from Firebase!");
// });

exports.test = functions.https.onRequest(require('./test'))