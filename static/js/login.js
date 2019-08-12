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