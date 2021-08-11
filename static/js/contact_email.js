/* 
    EmailJs used to send email from contact form
*/

/* Checking if form is valid 
Sourced from https://codepen.io/tetnuc/pen/gRqOEO */
$('#contactForm').validate({
    rules: {
        uname: {
            required: true
        },
        uemail: {
            required: true
        },
        umessage: {
            required: true
        }
    },
    messages: {
        uname: {
            required: "Please complete all fields"
        },
        uemail: {
            required: "Please complete all fields"
        },
        umessage: {
            required: "Please complete all fields"
        }
    },

});

// EmailJs Function
$('#contactFormSubmit').click(function (event) {
    event.preventDefault();
    if($('#contactForm').valid()) {
        Swal.fire({
            icon: 'success',
            title: 'Thank You!',
            text: 'Your message has been received',
            showConfirmButton: false,
            timer: 1500
        });
        sendMail();
    }
});
function sendMail(){
    // reference: CI tutorial and https://www.youtube.com/watch?v=x7Ewtay0Q78
    let tempParams = {
        user_name: document.getElementById("uname").value,
        user_email: document.getElementById("uemail").value,
        user_msg: document.getElementById("umessage").value,
    };
    emailjs.send('service_k339kpr', 'template_lrrt8os', tempParams);
}