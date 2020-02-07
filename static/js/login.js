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

$(document).ready(function() {
    //Hide Incorrect password message
    $(".GeoSpyLogin-IncorrectKey").hide();
    delete localStorage.GeoSpy;

    $(".GeoSpyLogin-Wrapper--Form---Body").on("submit", function(event) {
        //Stop form reload
        event.preventDefault();
        //Set variable to sent
        var id = { 
            id : $("#dataKey").val()
        };

        //Send data to the py server
        $.ajax({
            url: "/login",
            data: id,
            dataType: "json",
            type: "POST",
            success: function(response) {
                if (response.status == "OK") {
                    // Set the temporal id on localStorage variable
                    localStorage.setItem("GeoSpy", id.id);
                    // Redirect to the panel
                    window.location.replace(response.path);
                } else {
                    //Show Incorrect password message
                    $(".GeoSpyLogin-IncorrectKey").fadeIn(300).delay(2600).fadeOut(600);
                }
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
