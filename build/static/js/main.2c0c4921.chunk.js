(this["webpackJsonpsecret-chat-ui"]=this["webpackJsonpsecret-chat-ui"]||[]).push([[0],{140:function(e,t,n){},141:function(e,t,n){"use strict";n.r(t);var r=n(0),a=n(55),c=n.n(a),o=n(26),s=n(70),i=n(177),l=n(175),u=n(43),d=n(34),b=n(2),j=function(){return Object(b.jsx)(d.a,{styles:"\n      /* Copied from https://fonts.googleapis.com/css2?family=Open+Sans:wght@700&family=Roboto+Mono&display=swap */\n      /* latin-ext */\n      @font-face {\n        font-family: 'Open Sans';\n        font-style: normal;\n        font-weight: 700;\n        font-display: swap;\n        src: url(https://fonts.gstatic.com/s/opensans/v18/mem5YaGs126MiZpBA-UN7rgOXOhpOqc.woff2) format('woff2');\n        unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;\n      }\n      /* latin */\n      @font-face {\n        font-family: 'Open Sans';\n        font-style: normal;\n        font-weight: 700;\n        font-display: swap;\n        src: url(https://fonts.gstatic.com/s/opensans/v18/mem5YaGs126MiZpBA-UN7rgOUuhp.woff2) format('woff2');\n        unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;\n      }\n      /* latin-ext */\n      @font-face {\n        font-family: 'Roboto Mono';\n        font-style: normal;\n        font-weight: 400;\n        font-display: swap;\n        src: url(https://fonts.gstatic.com/s/robotomono/v13/L0xuDF4xlVMF-BfR8bXMIhJHg45mwgGEFl0_3vq_SuW4Ep0.woff2) format('woff2');\n        unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;\n      }\n      /* latin */\n      @font-face {\n        font-family: 'Roboto Mono';\n        font-style: normal;\n        font-weight: 400;\n        font-display: swap;\n        src: url(https://fonts.gstatic.com/s/robotomono/v13/L0xuDF4xlVMF-BfR8bXMIhJHg45mwgGEFl0_3vq_ROW4.woff2) format('woff2');\n        unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;\n      }\n      "})},h=n(17),x=n(60),f=Object(s.b)({name:"user",initialState:{logged:!1,token:null,user_id:null},reducers:{loginAction:function(e,t){var n=t.payload,r=n.token,a=n.user_id;e.logged=!0,e.token=r,e.user_id=a},logoutAction:function(e,t){e.logged=!1,e.token=null,e.user_id=null}}}),p=f.actions,g=p.loginAction,O=p.logoutAction,m=f.reducer,v=n(12),w=n.n(v),k=n(21),y=n(4),U=n(143),C=n(155),S=n(157),F=n(158),_=n(45),A=n(159),R=n(178),D=n(107),M=n(36),W=n.n(M),I="https://jakki-secret-chat.herokuapp.com/api",B=function(){var e=Object(k.a)(w.a.mark((function e(t,n){var r,a,c;return w.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.prev=0,e.next=3,W.a.post("".concat(I,"/login"),{username:t,password:n});case 3:return r=e.sent,a=r.data,c=Object(x.a)(a.access_token),e.abrupt("return",{access_token:a.access_token,user_id:c.identity});case 9:e.prev=9,e.t0=e.catch(0),console.log(e.t0);case 12:case"end":return e.stop()}}),e,null,[[0,9]])})));return function(t,n){return e.apply(this,arguments)}}(),z=function(){var e=Object(k.a)(w.a.mark((function e(){var t,n;return w.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=localStorage.getItem("token"),e.prev=1,e.next=4,W.a.get("".concat(I,"/user"),{headers:{Authorization:"JWT ".concat(t)}});case 4:return n=e.sent,e.abrupt("return",n.data);case 8:e.prev=8,e.t0=e.catch(1),console.log(e.t0);case 11:case"end":return e.stop()}}),e,null,[[1,8]])})));return function(){return e.apply(this,arguments)}}();var E={login:B},T=Object(o.b)((function(e){return{user:e.user}}),E)((function(e){var t=Object(h.g)(),n=Object(r.useState)(""),a=Object(y.a)(n,2),c=a[0],s=a[1],i=Object(r.useState)(""),l=Object(y.a)(i,2),u=l[0],d=l[1],j=Object(o.c)(),x=function(){var e=Object(k.a)(w.a.mark((function e(n){var r;return w.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return n.preventDefault(),console.log("Email: ".concat(c," & Password: ").concat(u)),e.next=4,B(c,u);case 4:r=e.sent,localStorage.setItem("token",r.access_token),j(g({token:r.access_token,user_id:r.user_id})),t.push("/");case 8:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),f=Object(U.c)("white","gray.800");return Object(b.jsx)(C.a,{align:"center",justifyContent:"center",maxW:"100%",maxH:"100%",p:10,rounded:"md",bgColor:f,m:5,boxShadow:"md",children:Object(b.jsxs)(S.a,{p:8,maxWidth:"500px",borderWidth:1,borderRadius:8,boxShadow:"lg",children:[Object(b.jsx)(S.a,{textAlign:"center",children:Object(b.jsx)(F.a,{children:"Login"})}),Object(b.jsx)(S.a,{my:4,textAlign:"left",children:Object(b.jsxs)("form",{onSubmit:x,children:[Object(b.jsxs)(_.a,{isRequired:!0,children:[Object(b.jsx)(A.a,{children:"Username"}),Object(b.jsx)(R.a,{type:"text",placeholder:"mystery-user-1",onChange:function(e){return s(e.currentTarget.value)}})]}),Object(b.jsxs)(_.a,{mt:6,isRequired:!0,children:[Object(b.jsx)(A.a,{children:"Password"}),Object(b.jsx)(R.a,{type:"password",placeholder:"*******",onChange:function(e){return d(e.currentTarget.value)}})]}),Object(b.jsx)(D.a,{width:"full",color:"teal",mt:4,type:"submit",children:"Sign In"})]})})]})})})),H=n(16),Y=n(164),J=n(165),L=n(179),G=n(166),P=n(167),q=n(162),N=n(168),V=n(169),X=n(160),Z=n(161),K=n(176),Q=n(163);var $=function(e){var t=new Date(e.time),n="".concat(t.getHours(),".").concat(t.getMinutes());return Object(b.jsxs)(C.a,{justifyContent:e.justifyContent,width:"100%",children:[Object(b.jsxs)(S.a,{display:"flex",boxShadow:"md",bgColor:"white",m:"3",p:"3",borderRadius:"20px",children:[Object(b.jsx)(X.a,{mr:3,p:1,children:e.content}),Object(b.jsx)(Z.a,{}),Object(b.jsx)(X.a,{fontSize:"xs",alignSelf:"flex-end",children:n})]}),Object(b.jsxs)(K.a,{children:[Object(b.jsx)(K.b,{as:q.a,alignSelf:"center",color:"gray.200",bgColor:"transparent","aria-label":"Options",icon:Object(b.jsx)(Q.a,{}),_hover:{background:"transparent",color:"teal.500"},_focus:{outline:"0"},children:" "}),Object(b.jsx)(K.d,{minW:"4rem",children:Object(b.jsx)(K.c,{children:"Delete"})})]})]})},ee=function(e,t){return e.getFullYear()===t.getFullYear()&&e.getMonth()===t.getMonth()&&e.getDate()===t.getDate()};var te=function(e){var t=new Date;console.log("TODAY",t);var n,r,a,c=new Date(e.date);if(console.log("DATE PROPS",c),ee(t,c))n="Today";else if(a=c,(r=t).getFullYear()===a.getFullYear()&&r.getMonth()===a.getMonth()&&r.getDate()===a.getDate()+1)n="Yesterday";else{var o=c.toLocaleString("default",{month:"long"});n="".concat(c.getDate(),". ").concat(o," ").concat(c.getFullYear())}return console.log(n),Object(b.jsx)(C.a,{justifyContent:"center",width:"100%",children:Object(b.jsx)(S.a,{boxShadow:"md",bgColor:"yellow.200",m:"1",p:"1",borderRadius:"20px",children:Object(b.jsx)(X.a,{fontSize:"xs",p:1,children:n})})})},ne="https://jakki-secret-chat.herokuapp.com/api",re=function(){var e=Object(k.a)(w.a.mark((function e(t){var n,r;return w.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return n=localStorage.getItem("token"),e.prev=1,e.next=4,W.a.get("".concat(ne,"/message/chatroom/").concat(t),{headers:{Authorization:"JWT ".concat(n)}});case 4:return r=e.sent,e.abrupt("return",r.data);case 8:e.prev=8,e.t0=e.catch(1),console.log(e.t0);case 11:case"end":return e.stop()}}),e,null,[[1,8]])})));return function(t){return e.apply(this,arguments)}}(),ae=function(){var e=Object(k.a)(w.a.mark((function e(t){var n,r;return w.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return n=localStorage.getItem("token"),e.prev=1,e.next=4,W.a.get("".concat(ne,"/message/user/").concat(t),{headers:{Authorization:"JWT ".concat(n)}});case 4:return r=e.sent,e.abrupt("return",r.data);case 8:e.prev=8,e.t0=e.catch(1),console.log(e.t0);case 11:case"end":return e.stop()}}),e,null,[[1,8]])})));return function(t){return e.apply(this,arguments)}}(),ce=function(){var e=Object(k.a)(w.a.mark((function e(t){var n,r;return w.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return n=localStorage.getItem("token"),e.prev=1,e.next=4,W.a.post("".concat(ne,"/message"),t,{headers:{Authorization:"JWT ".concat(n)}});case 4:return r=e.sent,e.abrupt("return",r.data);case 8:e.prev=8,e.t0=e.catch(1),console.log(e.t0);case 11:case"end":return e.stop()}}),e,null,[[1,8]])})));return function(t){return e.apply(this,arguments)}}();var oe=Object(o.b)((function(e){return{user:e.user}}),null)((function(e){var t=Object(r.useState)([]),n=Object(y.a)(t,2),a=n[0],c=n[1],o=Object(r.useState)(""),s=Object(y.a)(o,2),i=s[0],l=s[1],u=Object(r.useState)(null),d=Object(y.a)(u,2),j=(d[0],d[1],Object(r.useRef)(null)),h=Object(r.useRef)();Object(r.useEffect)(Object(k.a)(w.a.mark((function t(){var n,r,a,o;return w.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if(!e.private){t.next=9;break}return t.next=3,ae(e.id);case 3:n=t.sent,r=n.data,r=x(r),c(r),t.next=15;break;case 9:return t.next=11,re(e.id);case 11:a=t.sent,o=a.data,o=x(o),c(o);case 15:setTimeout((function(){h.current.scrollIntoView()}),1);case 16:case"end":return t.stop()}}),t)}))),[]);var x=function(e){return e.sort((function(e,t){return new Date(e.updated_at)>new Date(t.updated_at)?1:-1}))},f=function(){var t=Object(k.a)(w.a.mark((function t(){var n,r,o;return w.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if(""==i){t.next=8;break}return n=e.private?{content:i,user_id:e.user.user_id,recipient_id:e.id}:{content:i,user_id:e.user.user_id,room_id:e.id},t.next=4,ce(n);case 4:r=t.sent,o=x([].concat(Object(H.a)(a),[r.data])),c(o),l("");case 8:case"end":return t.stop()}}),t)})));return function(){return t.apply(this,arguments)}}(),p=Object(U.c)("white","gray.800");return a.length,Object(b.jsxs)(C.a,{maxW:"100%",maxH:"100%",boxShadow:"sm",rounded:"md",bgColor:p,m:2,flexDirection:"column",children:[Object(b.jsxs)(S.a,{display:"flex",borderTopRadius:"md",alignItems:"center",justifyContent:"center",m:0,p:0,bgColor:"teal",maxW:"100%",height:"70px",textAlign:"center",children:[Object(b.jsx)(Y.a,{size:"md",name:"Dan Abrahmov",src:"https://bit.ly/dan-abramov",mr:"3"}),Object(b.jsx)(F.a,{as:"h4",size:"md",color:"white",children:"User"})]}),Object(b.jsxs)(J.a,{maxW:"100%",height:"75vh",overflowY:"scroll",bgColor:"gray.50",css:{"::-webkit-scrollbar":{width:"5px",borderRadius:"10px"},"::-webkit-scrollbar-track":{background:"#f1f1f1",borderRadius:"10px"},"::-webkit-scrollbar-thumb":{background:"#888",borderRadius:"10px"},"::-webkit-scrollbar-thumb:hover":{background:"#555"}},children:[Object(b.jsx)(J.b,{children:Object(b.jsx)("div",{ref:j})},"top"),a.map((function(t,n,r){return 0==n?Object(b.jsxs)(b.Fragment,{children:[Object(b.jsx)(J.b,{width:"100%",children:Object(b.jsx)(te,{date:t.updated_at})},n+1e3),Object(b.jsx)(J.b,{width:"100%",justifyContent:1===t.user_id?"flex-end":"flex-start",children:Object(b.jsx)($,{content:t.content,time:t.updated_at,justifyContent:t.user_id===e.user.user_id?"flex-end":"flex-start"})},t.id)]}):function(e,t){var n=new Date(e.updated_at),r=new Date(t.updated_at);return ee(n,r)}(t,r[n-1])?Object(b.jsx)(J.b,{width:"100%",justifyContent:1===t.user_id?"flex-end":"flex-start",children:Object(b.jsx)($,{content:t.content,time:t.updated_at,justifyContent:t.user_id===e.user.user_id?"flex-end":"flex-start"})},t.id):Object(b.jsxs)(b.Fragment,{children:[Object(b.jsx)(J.b,{width:"100%",children:Object(b.jsx)(te,{date:r[n-1].updated_at})},n+1e3),Object(b.jsx)(J.b,{width:"100%",justifyContent:1===t.user_id?"flex-end":"flex-start",children:Object(b.jsx)($,{content:t.content,time:t.updated_at,justifyContent:t.user_id===e.user.user_id?"flex-end":"flex-start"})},t.id)]})})),Object(b.jsx)(J.b,{children:Object(b.jsx)("div",{ref:h})},"bottom")]}),Object(b.jsx)(S.a,{maxW:"100%",height:"40px",children:Object(b.jsx)(L.a,{spacing:4,children:Object(b.jsxs)(G.a,{children:[Object(b.jsx)(P.a,{pointerEvents:"none",children:Object(b.jsx)(N.a,{color:"gray.300"})}),Object(b.jsx)(R.a,{size:"md",placeholder:"Message",focusBorderColor:"teal.500",value:i,onChange:function(e){l(e.target.value)},onKeyPress:function(e){return"Enter"===e.key&&f()}}),Object(b.jsx)(P.b,{children:Object(b.jsx)(q.a,{borderTopRadius:"0px",borderBottomLeftRadius:"0px",borderBottomRightRadius:"md",colorScheme:"teal","aria-label":"Send",icon:Object(b.jsx)(V.a,{}),onClick:function(){return f()}})})]})})})]})})),se=function(e){return Object(b.jsx)("span",{className:"emoji",role:"img","aria-label":e.label?e.label:"","aria-hidden":e.label?"false":"true",children:e.symbol})},ie=function(){var e=Object(k.a)(w.a.mark((function e(){var t,n;return w.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=localStorage.getItem("token"),e.prev=1,e.next=4,W.a.get("".concat("https://jakki-secret-chat.herokuapp.com/api","/chatroom"),{headers:{Authorization:"JWT ".concat(t)}});case 4:return n=e.sent,console.log(n),console.log(n.data),e.abrupt("return",n.data);case 10:e.prev=10,e.t0=e.catch(1),console.log(e.t0);case 13:case"end":return e.stop()}}),e,null,[[1,10]])})));return function(){return e.apply(this,arguments)}}();var le=function(e){var t=Object(r.useState)([]),n=Object(y.a)(t,2),a=n[0],c=n[1],o=Object(r.useState)([]),s=Object(y.a)(o,2),i=s[0],l=s[1];Object(r.useEffect)(Object(k.a)(w.a.mark((function e(){var t,n,r,a;return w.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,z();case 2:return t=e.sent,n=t.data,e.next=6,ie();case 6:return r=e.sent,a=r.data,e.next=10,c(n);case 10:return e.next=12,l(a);case 12:case"end":return e.stop()}}),e)}))),[]);var u=Object(U.c)("white","gray.800");return Object(U.c)("#123123","#643345"),Object(b.jsxs)(C.a,{maxW:"100%",maxH:"100%",p:2,boxShadow:"sm",rounded:"md",bgColor:u,m:2,children:[Object(b.jsxs)(S.a,{flexGrow:"1",textAlign:"center",children:[Object(b.jsxs)(F.a,{as:"h3",size:"lg",children:[Object(b.jsx)(se,{symbol:"\ud83d\udc65"})," Join a room!"]}),Object(b.jsx)(J.a,{maxHeight:"80vh",overflowY:"scroll",spacing:3,m:1,p:3,css:{"::-webkit-scrollbar":{width:"5px",borderRadius:"10px"},"::-webkit-scrollbar-track":{background:"#f1f1f1",borderRadius:"10px"},"::-webkit-scrollbar-thumb":{background:"#888",borderRadius:"10px"},"::-webkit-scrollbar-thumb:hover":{background:"#555"}},children:i.map((function(e){return Object(b.jsx)(J.b,{children:Object(b.jsx)(D.a,{size:"md",height:"48px",width:"100%",border:"2px",borderColor:"teal",as:"a",href:"/chatroom/"+e.id,children:e.name})},e.id)}))})]}),Object(b.jsxs)(S.a,{flexGrow:"1",textAlign:"center",children:[Object(b.jsxs)(F.a,{as:"h3",size:"lg",children:[Object(b.jsx)(se,{symbol:"\ud83e\udd2b"})," Private chat!"]}),Object(b.jsx)(J.a,{maxHeight:"80vh",overflowY:"scroll",spacing:3,m:1,p:3,css:{"::-webkit-scrollbar":{width:"5px",borderRadius:"10px"},"::-webkit-scrollbar-track":{background:"#f1f1f1",borderRadius:"10px"},"::-webkit-scrollbar-thumb":{background:"#888",borderRadius:"10px"},"::-webkit-scrollbar-thumb:hover":{background:"#555"}},children:a.map((function(e){return Object(b.jsx)(J.b,{children:Object(b.jsx)(D.a,{size:"md",height:"48px",width:"100%",border:"2px",borderColor:"teal",as:"a",href:"/chatroom/private/"+e.id,children:e.username})},e.id)}))})]})]})},ue=n(83),de=n(172),be=n(170),je=n(171);var he=function(){var e=Object(U.b)(),t=e.colorMode,n=e.toggleColorMode;return Object(b.jsx)("div",{style:{display:"show"},children:Object(b.jsx)(S.a,{textAlign:"right",py:4,mr:12,children:Object(b.jsx)(q.a,{icon:"light"===t?Object(b.jsx)(be.a,{}):Object(b.jsx)(je.a,{}),onClick:n})})})};var xe={logoutAction:O},fe=Object(o.b)((function(e){return{user:e.user}}),xe)((function(e){var t=Object(o.c)(),n=Object(h.g)(),r=Object(U.c)("white","gray.800");return Object(b.jsxs)(C.a,{align:"center",p:2,boxShadow:"md",borderBottomRadius:"md",bgColor:r,children:[Object(b.jsx)(S.a,{as:"button",p:"2",onClick:function(){n.push("/")},outline:"0",children:Object(b.jsx)(de.a,{src:"/logo_200.png",alt:"Secret Chat",htmlHeight:"100px",htmlWidth:"150px"})}),Object(b.jsx)(Z.a,{}),e.user.logged?Object(b.jsx)(D.a,{mr:4,colorScheme:"teal",onClick:function(){return t(O()),localStorage.removeItem("token"),void n.push("/login")},children:"Log out"}):Object(b.jsx)(D.a,{mr:4,colorScheme:"teal",onClick:function(){n.push("/login")},children:"Log in"}),Object(b.jsx)(he,{})]})})),pe=n(173);var ge=function(e){var t=Object(U.c)("teal","gray.800");return Object(b.jsx)(b.Fragment,{children:Object(b.jsx)(pe.a,{bgColor:t,h:"60px",color:"white",mt:"auto",borderTopRadius:"md",boxShadow:"md",children:Object(b.jsx)(X.a,{fontSize:"lg",children:"Made with \ud83d\udc96 from Helsinki"})})})};var Oe=function(e){var t=Object(U.c)("gray.200","gray.900");return Object(b.jsx)(b.Fragment,{children:Object(b.jsx)(S.a,{width:"100vw",height:"100vh",maxWidth:"100vw",maxHeight:"100vh",mx:"auto",bgColor:t,backgroundImage:"url('/bg.svg')",children:Object(b.jsxs)(C.a,Object(ue.a)(Object(ue.a)({direction:"column",maxW:{xl:"1200px"},height:"100%",m:"0 auto"},e),{},{children:[Object(b.jsx)(fe,{}),Object(b.jsx)(S.a,{flex:"1 0 auto",children:e.children}),Object(b.jsx)(ge,{flexShrink:"0"})]}))})})};var me=function(e){var t=Object(U.c)("white","gray.800");return Object(b.jsx)(C.a,{align:"center",justifyContent:"center",maxW:"100%",maxH:"100%",p:2,boxShadow:"sm",rounded:"md",bgColor:t,m:2,children:Object(b.jsxs)("div",{children:[Object(b.jsx)(de.a,{}),Object(b.jsx)(X.a,{fontSize:"3xl",children:"404 Not found"})]})})};var ve=Object(o.b)((function(e){return{user:e.user}}),null)((function(e){var t=Object(o.c)(),n=function(){if(e.user.token||localStorage.getItem("token")){if(e.user.token)localStorage.getItem("token")||localStorage.setItem("token",e.user.token);else{var n=localStorage.getItem("token"),r=Object(x.a)(n).identity;t(g({token:n,user_id:r}))}return!0}return!1},r=Object(h.h)("/chatroom/:id"),a=Object(h.h)("/chatroom/private/:id"),c=!!a;return Object(b.jsx)(b.Fragment,{children:Object(b.jsxs)(h.d,{children:[Object(b.jsx)(h.b,{path:["/chatroom/:id","/chatroom/private/:id"],children:function(){return n()?Object(b.jsx)(Oe,{children:Object(b.jsx)(oe,{private:c,id:Number(c?a.params.id:r.params.id)})}):Object(b.jsx)(h.a,{to:"/login"})}}),Object(b.jsx)(h.b,{path:"/login",children:function(){return n()?Object(b.jsx)(h.a,{to:"/"}):Object(b.jsx)(Oe,{children:Object(b.jsx)(T,{})})}}),Object(b.jsx)(h.b,{exact:!0,path:"/",children:function(){return n()?Object(b.jsx)(Oe,{children:Object(b.jsx)(le,{})}):Object(b.jsx)(h.a,{to:"/login"})}}),Object(b.jsx)(h.b,{children:Object(b.jsx)(Oe,{children:Object(b.jsx)(me,{})})})]})})})),we=n(25),ke=Object(we.c)({user:m}),ye=(n(140),n(174)),Ue=Object(ye.a)({fonts:{heading:"Open Sans",body:"Roboto Mono"},config:{initialColorMode:"light",useSystemColorMode:!1}}),Ce=Object(s.a)({reducer:ke}),Se=document.getElementById("root");c.a.render(Object(b.jsxs)(i.a,{theme:Ue,children:[Object(b.jsx)(l.a,{initialColorMode:Ue.config.initialColorMode}),Object(b.jsx)(j,{}),Object(b.jsx)(o.a,{store:Ce,children:Object(b.jsx)(u.a,{children:Object(b.jsx)(ve,{})})})]}),Se)}},[[141,1,2]]]);
//# sourceMappingURL=main.2c0c4921.chunk.js.map