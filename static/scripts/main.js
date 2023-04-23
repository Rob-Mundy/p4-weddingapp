// Submit guest on submit
$('#add-guest-form').on('submit', function(event){
    event.preventDefault();
    console.log("guest submitted!")  // sanity check
    add_guest();
});

// AJAX for posting
function add_guest() {
    console.log("add guest is working!") // sanity check
    $.ajax({
        url : "guestlist/", // the endpoint
        type : "POST", // http method
        data : { the_guest : $('#guest-name').val() }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#guest-name').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            $("#talk").prepend("<li><strong>"+json.guest+"</strong> - <em> "+json.user+"</em> - <span> </span></li>");
            console.log("success"); // another sanity check
        },        

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

