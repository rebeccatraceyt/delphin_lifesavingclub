
$(function() {
    
    // Get Current Year for Footer
    document.getElementById("footer-date").innerHTML = new Date().getFullYear();

    // Previous page button
    // ref: https://stackoverflow.com/questions/2968425/get-back-to-previous-page
    $("#back_btn").click(function (){
        window.history.back();
      });
});

