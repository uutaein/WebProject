(function(t){function e(e){for(var n,o,s=e[0],c=e[1],l=e[2],d=0,u=[];d<s.length;d++)o=s[d],r[o]&&u.push(r[o][0]),r[o]=0;for(n in c)Object.prototype.hasOwnProperty.call(c,n)&&(t[n]=c[n]);h&&h(e);while(u.length)u.shift()();return i.push.apply(i,l||[]),a()}function a(){for(var t,e=0;e<i.length;e++){for(var a=i[e],n=!0,o=1;o<a.length;o++){var s=a[o];0!==r[s]&&(n=!1)}n&&(i.splice(e--,1),t=c(c.s=a[0]))}return t}var n={},o={app:0},r={app:0},i=[];function s(t){return c.p+"js/"+({}[t]||t)+"."+{"chunk-11bb5876":"a521c71b","chunk-2d0d9f82":"56dad4db","chunk-33709a35":"a4b70980","chunk-39289921":"0d20d219","chunk-60dfd1d7":"f6805403","chunk-03096418":"6f60c67c","chunk-d164f47a":"62b22a80","chunk-6e33c70e":"14a95d4f","chunk-7687d1d0":"62fdfc36","chunk-c3214c92":"c4ad07e7","chunk-9223d87e":"9cf2cb18"}[t]+".js"}function c(e){if(n[e])return n[e].exports;var a=n[e]={i:e,l:!1,exports:{}};return t[e].call(a.exports,a,a.exports,c),a.l=!0,a.exports}c.e=function(t){var e=[],a={"chunk-11bb5876":1,"chunk-33709a35":1,"chunk-39289921":1,"chunk-03096418":1,"chunk-7687d1d0":1,"chunk-c3214c92":1,"chunk-9223d87e":1};o[t]?e.push(o[t]):0!==o[t]&&a[t]&&e.push(o[t]=new Promise(function(e,a){for(var n="css/"+({}[t]||t)+"."+{"chunk-11bb5876":"3e720d07","chunk-2d0d9f82":"31d6cfe0","chunk-33709a35":"c661a447","chunk-39289921":"11161fcb","chunk-60dfd1d7":"31d6cfe0","chunk-03096418":"8b8f68bb","chunk-d164f47a":"31d6cfe0","chunk-6e33c70e":"31d6cfe0","chunk-7687d1d0":"2323beb0","chunk-c3214c92":"4d55337a","chunk-9223d87e":"11161fcb"}[t]+".css",r=c.p+n,i=document.getElementsByTagName("link"),s=0;s<i.length;s++){var l=i[s],d=l.getAttribute("data-href")||l.getAttribute("href");if("stylesheet"===l.rel&&(d===n||d===r))return e()}var u=document.getElementsByTagName("style");for(s=0;s<u.length;s++){l=u[s],d=l.getAttribute("data-href");if(d===n||d===r)return e()}var h=document.createElement("link");h.rel="stylesheet",h.type="text/css",h.onload=e,h.onerror=function(e){var n=e&&e.target&&e.target.src||r,i=new Error("Loading CSS chunk "+t+" failed.\n("+n+")");i.code="CSS_CHUNK_LOAD_FAILED",i.request=n,delete o[t],h.parentNode.removeChild(h),a(i)},h.href=r;var p=document.getElementsByTagName("head")[0];p.appendChild(h)}).then(function(){o[t]=0}));var n=r[t];if(0!==n)if(n)e.push(n[2]);else{var i=new Promise(function(e,a){n=r[t]=[e,a]});e.push(n[2]=i);var l,d=document.createElement("script");d.charset="utf-8",d.timeout=120,c.nc&&d.setAttribute("nonce",c.nc),d.src=s(t),l=function(e){d.onerror=d.onload=null,clearTimeout(u);var a=r[t];if(0!==a){if(a){var n=e&&("load"===e.type?"missing":e.type),o=e&&e.target&&e.target.src,i=new Error("Loading chunk "+t+" failed.\n("+n+": "+o+")");i.type=n,i.request=o,a[1](i)}r[t]=void 0}};var u=setTimeout(function(){l({type:"timeout",target:d})},12e4);d.onerror=d.onload=l,document.head.appendChild(d)}return Promise.all(e)},c.m=t,c.c=n,c.d=function(t,e,a){c.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:a})},c.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},c.t=function(t,e){if(1&e&&(t=c(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var a=Object.create(null);if(c.r(a),Object.defineProperty(a,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var n in t)c.d(a,n,function(e){return t[e]}.bind(null,n));return a},c.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return c.d(e,"a",e),e},c.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},c.p="",c.oe=function(t){throw console.error(t),t};var l=window["webpackJsonp"]=window["webpackJsonp"]||[],d=l.push.bind(l);l.push=e,l=l.slice();for(var u=0;u<l.length;u++)e(l[u]);var h=d;i.push([0,"chunk-vendors"]),a()})({0:function(t,e,a){t.exports=a("56d7")},"203d":function(t,e,a){},"3c88":function(t,e){t.exports="data:image/jpeg;base64,/9j/4QAYRXhpZgAASUkqAAgAAAAAAAAAAAAAAP/sABFEdWNreQABAAQAAAA8AAD/4QMfaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLwA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/PiA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJBZG9iZSBYTVAgQ29yZSA1LjYtYzEzOCA3OS4xNTk4MjQsIDIwMTYvMDkvMTQtMDE6MDk6MDEgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOkQ3MDQwMTFBRUNGMDExRThBNjRDQzQyMTE5Mjk5QTQ0IiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOkQ3MDQwMTE5RUNGMDExRThBNjRDQzQyMTE5Mjk5QTQ0IiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE3IE1hY2ludG9zaCI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSI0RjBENjMzNUYyM0RFMUYwNjM4MTY4RTUyODFERkI3QSIgc3RSZWY6ZG9jdW1lbnRJRD0iNEYwRDYzMzVGMjNERTFGMDYzODE2OEU1MjgxREZCN0EiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz7/7gAOQWRvYmUAZMAAAAAB/9sAhAAGBAQEBQQGBQUGCQYFBgkLCAYGCAsMCgoLCgoMEAwM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"},"56d7":function(t,e,a){"use strict";a.r(e);a("14c6"),a("08c1"),a("4842"),a("d9fc");var n=a("a026"),o=a("8c4f"),r=a("8aa5"),i=a.n(r);n["default"].use(o["a"]);var s=new o["a"]({scrollBehavior:function(){return window.scrollTo({top:0,behavior:"smooth"})},mode:"history",routes:[{path:"/Dashboards",name:"analytics",component:function(){return a.e("chunk-33709a35").then(a.bind(null,"9fbd"))},beforeEnter:function(t,e,a){i.a.auth().currentUser?a():(alert("잘못된 접근입니다!"),a("/"))}},{path:"/",name:"login",meta:{layout:"userpages"},component:function(){return a.e("chunk-39289921").then(a.bind(null,"9c4a"))}},{path:"/Register",name:"register-boxed",meta:{layout:"userpages"},component:function(){return a.e("chunk-9223d87e").then(a.bind(null,"bd66"))}},{path:"/pages/Chart",name:"Chart",component:function(){return Promise.all([a.e("chunk-11bb5876"),a.e("chunk-2d0d9f82")]).then(a.bind(null,"6a34"))}},{path:"/pages/Strategy-Simulator",name:"Strategy Simulator",component:function(){return Promise.all([a.e("chunk-60dfd1d7"),a.e("chunk-d164f47a"),a.e("chunk-c3214c92")]).then(a.bind(null,"fb73"))}},{path:"/pages/Stat-Strategy",name:"Stat Strategy",component:function(){return Promise.all([a.e("chunk-60dfd1d7"),a.e("chunk-03096418")]).then(a.bind(null,"a4d5"))}},{path:"/pages/Investment-Game",name:"InvestmentGame",component:function(){return Promise.all([a.e("chunk-60dfd1d7"),a.e("chunk-11bb5876"),a.e("chunk-d164f47a"),a.e("chunk-6e33c70e")]).then(a.bind(null,"7ab1"))}},{path:"/pages/Recommend",name:"Recommend",component:function(){return Promise.all([a.e("chunk-60dfd1d7"),a.e("chunk-7687d1d0")]).then(a.bind(null,"acaa"))}}]}),c=a("9f7b"),l=a.n(c),d=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{attrs:{id:"app"}},[a(t.layout,{tag:"component"},[a("transition",{attrs:{name:"fade",mode:"out-in"}},[a("router-view")],1)],1)],1)},u=[],h="default",p={computed:{layout:function(){return(this.$route.meta.layout||h)+"-layout"}}},f=p,m=(a("5c0b"),a("2877")),_=Object(m["a"])(f,d,u,!1,null,null,null),b=_.exports,v=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"app-container app-theme-white"},[a("transition",{attrs:{name:"fade",mode:"out-in",appear:""}},[a("Header")],1),a("transition",{attrs:{name:"fade",mode:"out-in",appear:""}},[a("Sidebar")],1),a("div",{staticClass:"app-main__outer"},[a("div",{staticClass:"app-main__inner"},[t._t("default")],2),a("transition",{attrs:{name:"fade",mode:"out-in",appear:""}},[a("Footer")],1)],1),a("b-modal",{attrs:{id:"modal1",title:"Bootstrap-Vue"}},[a("p",{staticClass:"my-4"},[t._v("Hello from modal!")])]),a("b-modal",{attrs:{id:"modallg",size:"lg",title:"Large Modal"}},[t._v("\n        Hello Modal!\n    ")]),a("b-modal",{attrs:{id:"modalsm",size:"sm",title:"Small Modal"}},[t._v("\n        Hello Modal!\n    ")])],1)},A=[],g=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"app-header header-shadow"},[a("div",{staticClass:"app-header__content"},[a("div",{staticClass:"app-header-right"},[a("b-button",{attrs:{variant:"primary",size:"sm"},on:{click:t.signOut}},[t._v("Logout")])],1)]),a("div",{staticClass:"app-header__mobile-menu"},[a("div",[a("button",{staticClass:"hamburger close-sidebar-btn hamburger--elastic",class:{"is-active":t.isOpen},attrs:{type:"button"},on:{click:function(e){return t.toggleMobile("closed-sidebar-open")}}},[t._m(0)])])]),a("div",{staticClass:"app-header__menu"},[a("span",[a("b-button",{attrs:{variant:"primary",size:"sm"},on:{click:t.signOut}},[t._v("Logout")])],1)])])},S=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("span",{staticClass:"hamburger-box"},[a("span",{staticClass:"hamburger-inner"})])}],k=(a("a481"),function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("div",{staticClass:"search-wrapper",class:{active:t.searchOpen}},[a("div",{staticClass:"input-holder"},[a("input",{staticClass:"search-input",attrs:{type:"text",placeholder:"Type to search"}}),a("button",{staticClass:"search-icon",on:{click:function(e){t.searchOpen=!t.searchOpen}}},[a("span")])]),a("button",{staticClass:"close",on:{click:function(e){t.searchOpen=!t.searchOpen}}})])])}),I=[],y={data:function(){return{searchOpen:!1}}},G=y,w=Object(m["a"])(G,k,I,!1,null,null,null),C=w.exports,M=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"d-flex"},[n("div",{staticClass:"header-btn-lg pr-0"},[n("div",{staticClass:"widget-content p-0"},[n("div",{staticClass:"widget-content-wrapper"},[n("div",{staticClass:"widget-content-left"},[n("b-dropdown",{attrs:{"toggle-class":"p-0 mr-2","menu-class":"dropdown-menu-lg",variant:"link",right:""}},[n("span",{attrs:{slot:"button-content"},slot:"button-content"},[n("div",{staticClass:"icon-wrapper icon-wrapper-alt rounded-circle"},[n("img",{staticClass:"rounded-circle",attrs:{width:"42",src:a("3c88"),alt:""}})])]),n("button",{staticClass:"dropdown-item",attrs:{type:"button",tabindex:"0"}},[t._v("Menus")]),n("button",{staticClass:"dropdown-item",attrs:{type:"button",tabindex:"0"}},[t._v("Settings")]),n("h6",{staticClass:"dropdown-header",attrs:{tabindex:"-1"}},[t._v("Header")]),n("button",{staticClass:"dropdown-item",attrs:{type:"button",tabindex:"0"}},[t._v("Actions")]),n("div",{staticClass:"dropdown-divider",attrs:{tabindex:"-1"}}),n("button",{staticClass:"dropdown-item",attrs:{type:"button",tabindex:"0"}},[t._v("Dividers")])])],1),t._m(0),n("div",{staticClass:"widget-content-right header-user-info ml-3"},[n("b-btn",{directives:[{name:"b-tooltip",rawName:"v-b-tooltip.hover",modifiers:{hover:!0}}],staticClass:"btn-shadow p-1",attrs:{title:"Tooltip Example",size:"sm",variant:"info"}},[n("font-awesome-icon",{staticClass:"mr-1 ml-1",attrs:{icon:"calendar-alt"}})],1)],1)])])])])},x=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"widget-content-left  ml-3 header-user-info"},[a("div",{staticClass:"widget-heading"},[t._v("Alina Mclourd")]),a("div",{staticClass:"widget-subheading"},[t._v("VP People Manager")])])}],O=a("9d63"),E=a.n(O),H=a("ecee"),Q=a("c074"),j=a("ad3d");H["c"].add(Q["a"],Q["b"],Q["l"],Q["c"],Q["h"],Q["d"],Q["j"],Q["k"],Q["i"],Q["f"]);var B={components:{VuePerfectScrollbar:E.a,"font-awesome-icon":j["a"]},data:function(){return{}},methods:{}},P=B,D=Object(m["a"])(P,M,x,!1,null,null,null),W=D.exports;H["c"].add(Q["g"]);var N={name:"Header",components:{SearchBox:C,UserArea:W,"font-awesome-icon":j["a"]},data:function(){return{isOpen:!1,isOpenMobileMenu:!1}},props:{},methods:{signOut:function(){i.a.auth().signOut().then(function(){alert("Logout"),location.replace("/")}).catch(function(t){alert(t)})},toggleMobile:function(t){var e=document.body;this.isOpen=!this.isOpen,this.isOpen?e.classList.add(t):e.classList.remove(t)},toggleMobile2:function(t){var e=document.body;this.isOpenMobileMenu=!this.isOpenMobileMenu,this.isOpenMobileMenu?e.classList.add(t):e.classList.remove(t)}}},R=N,L=(a("a7ce"),Object(m["a"])(R,g,S,!1,null,null,null)),T=L.exports,Y=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"app-sidebar sidebar-shadow",on:{mouseover:function(e){return t.toggleSidebarHover("add","closed-sidebar-open")},mouseleave:function(e){return t.toggleSidebarHover("remove","closed-sidebar-open")}}},[a("div",{staticClass:"app-header__logo"},[a("div",{staticClass:"header__pane ml-auto"},[a("button",{staticClass:"hamburger close-sidebar-btn hamburger--elastic",class:{"is-active":t.isOpen},attrs:{type:"button"}},[t._m(0)])])]),a("div",{staticClass:"app-sidebar-content"},[t._m(1)],1)])},F=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("span",{staticClass:"hamburger-box"},[a("span",{staticClass:"hamburger-inner"})])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("VuePerfectScrollbar",{staticClass:"app-sidebar-scroll"},[a("sidebar-menu",{attrs:{showOneChild:"",menu:t.menu}})],1)}],z=a("4776"),U={components:{SidebarMenu:z["SidebarMenu"],VuePerfectScrollbar:E.a},data:function(){return{isOpen:!1,sidebarActive:!1,menu:[{header:!0,title:"Main Navigation"},{title:"Dashboards",icon:"pe-7s-rocket",child:[{href:"/Dashboards",title:"Analytics"}]},{title:"Pages",icon:"pe-7s-browser",child:[{href:"/pages/Strategy-Simulator",title:"Strategy Simulator"},{href:"/pages/Chart",title:"Chart"},{href:"/pages/Stat-Strategy",title:"Stat Strategy"},{href:"/pages/Investment-Game",title:"Investment Game"}]}],collapsed:!0,windowWidth:0}},props:{sidebarbg:String},methods:{toggleBodyClass:function(t){var e=document.body;this.isOpen=!this.isOpen,this.isOpen?e.classList.add(t):e.classList.remove(t)},toggleSidebarHover:function(t,e){var a=document.body;this.sidebarActive=!this.sidebarActive,this.windowWidth=document.documentElement.clientWidth,this.windowWidth>"992"&&("add"===t?a.classList.add(e):a.classList.remove(e))},getWindowWidth:function(){var t=document.body;this.windowWidth=document.documentElement.clientWidth,this.windowWidth<"1350"?t.classList.add("closed-sidebar","closed-sidebar-md"):t.classList.remove("closed-sidebar","closed-sidebar-md")}},mounted:function(){this.$nextTick(function(){window.addEventListener("resize",this.getWindowWidth),this.getWindowWidth()})},beforeDestroy:function(){window.removeEventListener("resize",this.getWindowWidth)}},J=U,X=Object(m["a"])(J,Y,F,!1,null,null,null),Z=X.exports,V=function(){var t=this,e=t.$createElement;t._self._c;return t._m(0)},K=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"app-footer"},[a("div",{staticClass:"app-footer__inner text-center"},[t._v("\n        Copyright 2019 DashboardPack.com\n    ")])])}];H["c"].add(Q["g"]);var q={name:"Footer",components:{}},$=q,tt=Object(m["a"])($,V,K,!1,null,null,null),et=tt.exports;H["c"].add(Q["e"]);var at={name:"app",components:{Header:T,Sidebar:Z,Footer:et,VuePerfectScrollbar:E.a,"font-awesome-icon":j["a"]},methods:{}},nt=at,ot=Object(m["a"])(nt,v,A,!1,null,null,null),rt=ot.exports,it=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"app-container app-theme-white"},[t._t("default")],2)},st=[],ct={name:"app",components:{},methods:{}},lt=ct,dt=Object(m["a"])(lt,it,st,!1,null,null,null),ut=dt.exports,ht=a("bc3a"),pt=a.n(ht),ft=pt.a.create({baseURL:"http://localhost:5000/webproject-6135b/us-central1/",timeout:1e5,headers:{"X-Custom-Header":"foobar"}});n["default"].prototype.$axios=ft;var mt=ft,_t=(a("c5f6"),a("2f62"));n["default"].use(_t["a"]);var bt=new _t["a"].Store({state:{chart1_labels:[],chart1_data:[],IG_init_money:0,IG_result_money:0,IG_init_date:"",IG_init_stocks:[],IG_init_index_stock_num:0,IG_init_kospi_stock_num:0,IG_ratio:[],IG_chart_labels:[],IG_chart_data1:[],IG_chart_data2:[],IG_chart_done:!1,IG_profit:0,IG_max_profit:0,IG_chart_total_labels:[],IG_chart_total_data1:[],IG_chart_total_data2:[],IG_chart_total_done:!1,IG_net_money:0,IG_total_net_money:0,IG_total_net_profit:0,SS_init_money:0,SS_init_stocks:[],SS_init_index_stock_num:0,SS_ratio:[],SS_chart_labels:[],SS_chart_data1:[],SS_chart_data2:[],SS_chart_done:!1,SS_whole_profit:0,SS_annual_profit:0},mutations:{addDataToChartSuccess:function(t,e){for(var a=e.data.length-1;a>=0;a--)e.data[a].date,e.data[a].high},addDataToChartFail:function(){console.log("addDataToChart Error!")},calculatePortfolioSuccess:function(t,e){this.state.SS_init_money*=1e4;var a=e.data.length-1,n=e.data[a].length-1,o=n/365;o=o.toFixed(2),t.SS_init_index_stock_num=this.state.SS_init_money/e.data[a][0].close;for(var r=0;r<=n;r++){var i=e.data[a][r].date;t.SS_chart_labels.push(i);var s=t.SS_init_index_stock_num*e.data[a][r].close;t.SS_chart_data1.push(s)}console.log(t.SS_chart_data1);for(r=0;r<=n;r++)t.SS_chart_data2.push(Number(0));for(r=0;r<a;r++){var c=t.SS_init_money*t.SS_ratio[r]/e.data[r][n].close/100;t.SS_init_stocks.push(c)}console.log(t.SS_init_stocks);for(r=0;r<=n;r++)for(var l=0;l<a;l++)t.SS_chart_data2[r]+=Number(t.SS_init_stocks[l]*e.data[l][r].close);t.SS_chart_data2.reverse(),t.SS_whole_profit=(t.SS_chart_data2[n]-t.SS_init_money)/t.SS_init_money*100,t.SS_whole_profit=t.SS_whole_profit.toFixed(3),t.SS_annual_profit=Math.pow(1+t.SS_whole_profit/100,1/o)-1,t.SS_annual_profit=(100*t.SS_annual_profit).toFixed(3),t.SS_chart_done=!0},calculatePortfolioFail:function(t,e){console.log(e)},IGcalculatePortfolioSuccess:function(t,e){var a,n=e.data.length-1,o=e.data[n].length-1;0==t.IG_result_money?(a=t.IG_init_money,t.IG_init_kospi_stock_num=a/e.data[n][0].close):a=t.IG_result_money,t.IG_init_index_stock_num=a/e.data[n][0].close;for(var r=0;r<=o;r++){var i=e.data[n][r].date;t.IG_chart_labels.push(i),t.IG_chart_total_labels.push(i);var s=t.IG_init_index_stock_num*e.data[n][r].close;t.IG_chart_data1.push(s);var c=t.IG_init_kospi_stock_num*e.data[n][r].close;t.IG_chart_total_data1.push(c)}for(r=0;r<=o;r++)t.IG_chart_data2.push(Number(0));for(r=0;r<n;r++){var l=a*t.IG_ratio[r]/e.data[r][o].close/100;t.IG_init_stocks.push(l)}for(r=0;r<=o;r++)for(var d=0;d<n;d++)t.IG_chart_data2[r]+=Number(t.IG_init_stocks[d]*e.data[d][r].close);t.IG_result_money=t.IG_chart_data2[0],t.IG_chart_data2.reverse(),t.IG_chart_total_data2=t.IG_chart_total_data2.concat(t.IG_chart_data2),t.IG_profit=(t.IG_chart_data2[o]-a)/a*100,t.IG_net_money=t.IG_chart_data2[o]-a,t.IG_max_profit<=t.IG_profit&&(t.IG_max_profit=t.IG_profit);var u=t.IG_chart_total_data2.length-1;t.IG_total_net_money=t.IG_chart_total_data2[u]-t.IG_init_money,t.IG_total_net_profit=(t.IG_chart_total_data2[u]-t.IG_init_money)/t.IG_init_money*100,t.IG_chart_done=!0,t.IG_chart_total_done=!0},IGcalculatePortfolioFail:function(t,e){console.log(e)}},actions:{addDataToChart:function(t){var e=t.commit;mt.post("test",{start:this.start}).then(function(t){e("addDataToChartSuccess",t)}).catch(function(t){e("addDataToChartFail",t)})},calculatePortfolio:function(t,e){var a=t.commit;mt.post("test/api",e).then(function(t){a("calculatePortfolioSuccess",t)}).catch(function(t){a("calculatePortfolioFail",t)})},IGcalculatePortfolio:function(t,e){var a=t.commit;mt.post("test/apitest",e).then(function(t){a("IGcalculatePortfolioSuccess",t)}).catch(function(t){a("IGcalculatePortfolioFail",t)})}},modules:{}});n["default"].prototype.$http=mt,n["default"].config.productionTip=!1;var vt={apiKey:"AIzaSyDXnx-Lqn8YH8UoiPv6Awetywx2wK6HGdw",authDomain:"webproject-6135b.firebaseapp.com",databaseURL:"https://webproject-6135b.firebaseio.com",projectId:"webproject-6135b",storageBucket:"webproject-6135b.appspot.com",messagingSenderId:"722237715982",appId:"1:722237715982:web:94a855e17dcd65f9306e5f",measurementId:"G-XHZEQ7ZCV3"};i.a.initializeApp(vt),n["default"].use(l.a),n["default"].component("default-layout",rt),n["default"].component("userpages-layout",ut),new n["default"]({el:"#app",router:s,store:bt,template:"<App/>",components:{App:b}})},"5c0b":function(t,e,a){"use strict";var n=a("5e27"),o=a.n(n);o.a},"5e27":function(t,e,a){},a7ce:function(t,e,a){"use strict";var n=a("203d"),o=a.n(n);o.a}});