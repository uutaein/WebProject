(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-9223d87e"],{"0136":function(e,t,a){"use strict";var s=a("ee64"),r=a.n(s);r.a},bd66:function(e,t,a){"use strict";a.r(t);var s=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("div",{staticClass:"h-100 bg-premium-dark"},[a("div",{staticClass:"d-flex h-100 justify-content-center align-items-center"},[a("b-col",{staticClass:"mx-auto app-login-box",attrs:{md:"8"}},[a("div",{attrs:{id:"title"}},[e._v("\n                    My Asset\n                ")]),a("div",{staticClass:"modal-dialog w-100"},[a("div",{staticClass:"modal-content"},[a("div",{staticClass:"modal-body"},[a("h5",{staticClass:"modal-title"},[a("h4",{staticClass:"mt-2"},[a("div",[e._v("Welcome,")]),a("span",[e._v("It only takes a "),a("span",{staticClass:"text-success"},[e._v("few seconds")]),e._v(" to create your account")])])]),a("div",{staticClass:"divider"}),a("b-form-group",{attrs:{id:"exampleInputGroup1","label-for":"exampleInput1",description:"We'll never share your email with anyone else."}},[a("b-form-input",{attrs:{id:"exampleInput1",type:"email",required:"",placeholder:"Enter email..."},model:{value:e.email,callback:function(t){e.email=t},expression:"email"}})],1),a("b-form-group",{attrs:{id:"exampleInputGroup12","label-for":"exampleInput12"}},[a("b-form-input",{attrs:{id:"exampleInput12",type:"text",required:"",placeholder:"Enter username..."},model:{value:e.username,callback:function(t){e.username=t},expression:"username"}})],1),a("div",{staticClass:"row"},[a("div",{staticClass:"col-md-6"},[a("b-form-group",{attrs:{id:"exampleInputGroup2","label-for":"exampleInput2"}},[a("b-form-input",{attrs:{id:"exampleInput2",type:"password",required:"",placeholder:"Enter password..."},model:{value:e.password,callback:function(t){e.password=t},expression:"password"}})],1)],1),a("div",{staticClass:"col-md-6"},[a("b-form-group",{attrs:{id:"exampleInputGroup2","label-for":"exampleInput2"}},[a("b-form-input",{attrs:{id:"exampleInput2",type:"password",required:"",placeholder:"Repeat password..."},model:{value:e.passwordconfirm,callback:function(t){e.passwordconfirm=t},expression:"passwordconfirm"}})],1)],1)]),a("div",{staticClass:"divider"})],1),a("div",{staticClass:"modal-footer d-block text-center"},[a("b-button",{staticClass:"btn-wide btn-pill btn-shadow btn-hover-shine",attrs:{color:"primary",size:"lg"},on:{click:e.signUp}},[e._v("Create Account\n                            ")])],1)])]),a("div",{staticClass:"text-center text-white opacity-8 mt-3"},[e._v("\n                    Copyright © ArchitectUI 2019\n                ")])])],1)])])},r=[],i=(a("a481"),a("8aa5")),o=a.n(i),n={name:"registerBox",data:function(){return{email:"",password:"",username:"",passwordconfirm:""}},methods:{signUp:function(){var e=this;this.passwordconfirm==this.password?o.a.auth().createUserWithEmailAndPassword(this.email,this.password).then(function(t){t.username=e.username,alert("Sign Up success! Welcome  "+t.username),e.email="",e.password="",e.passwordconfirm="",e.username="",location.replace("/")}).catch(function(e){alert(e)}):alert("Check you password again!")}}},l=n,c=(a("0136"),a("2877")),p=Object(c["a"])(l,s,r,!1,null,null,null);t["default"]=p.exports},ee64:function(e,t,a){}}]);