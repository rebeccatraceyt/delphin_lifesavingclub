/* 

Setup Stripe Elements
Step 1 - When user hits checkout page: Checkout view creates Stripe paymentintent
Step 2 - When Stripe creates paymentintent: Stripe returns client_secret, which is returned to template
Step 3 - Call the confirm card payemnt: Use client_secret in the template to call confirmCardPayment() and verify card

(Core payment logic adapted from Boutique Ado Mini project)

*/

// Get public key and client secret
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);

// Set up Stripe
var stripe = Stripe(stripe_public_key);

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