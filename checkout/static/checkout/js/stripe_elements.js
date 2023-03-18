/**
 * Stripe 
 * 
 * 
 */

//Creating variable from converted JSON values in checkout > postload.js block 
///removing quotations aroud the text with slice  */
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);

// create instance of Stripe using  stripe javascript included at base.html
//get the stripe card element and then add this into checkout.html by attaching to div - card-element 
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

// adding styling from Code Institute 
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

var card = elements.create('card', {style:style});

//taking stripe card -element and putting into DIV - card-element in checkout.html 
card.mount('#card-element');

// Handle Errors on the card element puts into to the DIV -card-errors in checkout.html  
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

// Handle form submit after payment intent is created
//Used Code Institure code. 
//payment intent is created at checkout page load.
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    //disabling card element to stop double submission
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            //any error gets added into card-errors div
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            //enabling card element
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
            console.log("payment failed")                                  //TEMP for Troubleshooting
        } else {
            // if intent succeeeded then submit and will redirect
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});

