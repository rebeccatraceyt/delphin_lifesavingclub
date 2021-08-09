/* 

Setup Stripe Elements
Step 1 - When user hits checkout page: Checkout view creates Stripe paymentintent
Step 2 - When Stripe creates paymentintent: Stripe returns client_secret, which is returned to template
Step 3 - Call the confirm card payemnt: Use client_secret in the template to call confirmCardPayment() and verify card

(Core payment logic adapted from Boutique Ado Mini project)

*/

// Get public key and client secret
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);

// Set up Stripe
var stripe = Stripe(stripePublicKey);

// Create an instance of stripe elements
var elements = stripe.elements();

// Styling of card element
var style = {
    base: {
        color: '#0A0A0A',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialised',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4' 
        }
    },
    invalid: {
        color: '#B8060B',
        iconColor: '#B8060B'
    }
};

// Create card element
var card = elements.create('card', {style: style});

// mount card to card div
card.mount('#card-element');

// Handle realtime validation erros on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    // Prevents default POST action when submit is clicked
    ev.preventDefault();

    // disable card element and submit to prevent multilple submissions
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#loading-overlay').fadeToggle(100);

    // Get boolean value of save info box (checked or not)
    var saveInfo = Boolean($('#id-save-info').attr('checked'));

    // From using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

    // pass information to new view 
    // and clients secret for payment intent
    var postData = {
        'csrfmiddlewaretoken' : csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };

    // url variable
    var url = '/checkout/cache_checkout_data/';

    // post data to the view (the url) which updates payment intent
    // .done waits for response that payment intent was updated,
    // before calling the confirmed payment method
    $.post(url, postData).done(function() {
        // Call Confirm Card method
        stripe.confirmCardPayment(clientSecret, {
            // provide card to stripe
            payment_method: {
                card: card,
                // apply form data into payment intent object
                // allows it to be retrieved once a webhook is received
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address: {
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        state: $.trim(form.county.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    // billing postal code comes from card element
                    // Stripe would over ride it
                    postal_code: $.trim(form.postcode.value),
                    state: $.trim(form.county.value),
                }
            }
        }).then(function(result) {
            // Then execute this function
            if (result.error) {
                // put error message in card-error div
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>
                `;
    
                // if there is an error, re-enable card element and submit button
                $(errorDiv).html(html);
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                // if status of payment intent is succeeded, submit form
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function() {
        // reloads page, the error will be in django messages
        location.reload();
    })

});