
var serviceAccount = require('./webproject.json');
var admin = require('firebase-admin');
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});
var db = admin.firestore();

{

  //test콜렉션에서 title값이 'second'인 값만 가져오기
  // ref = db.collection('stock')
  // .where('DATE','==','2019-11-27')
  // .get()
  // .then(snapshot =>{
  //    snapshot.forEach(doc =>{
  //       console.log(doc.data());
  //    })
  // }).catch(err =>{
  //       console.log('Error getting documents', err);
  // });


  //date 넣는 example
  // var examref = db.collection("prac");

  // examref.doc("prac2").set({
  //   time : new Date('2015-11-27')
  // });

  //date 넣은것을 query
  let start = new Date('2013-01-01');
  let end = new Date('2019-11-28');
  pracref = db.collection('prac').where('time','>',start).where('time','<',end).get()
            .then(snapshot => {
              snapshot.forEach(doc => {
                console.log(doc.data());
              })
            }).catch(err => {
              console.log('Error',err);
            });
}

