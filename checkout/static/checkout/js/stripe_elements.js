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
    // handles the overlay and applies the customCSS
    // whilst payment is being processed
    $('#payment-form').fadeToggle(100);
    $('#payment-processing-overlay').fadeToggle(100);
    
    // SAVE ADDRESS Variable HERE  once added to form  

    // From using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        // SAVE ADDRESS 'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

    //posting data to the view 
    $.post(url, postData).done(function() {
        //passing information to Stripe from checkout form 
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.first_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address:{
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        //state: $.trim(form.county.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.first_name.value),
                phone: $.trim(form.phone_number.value),
                //email: $.trim(form.email.value),
                address:{
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    country: $.trim(form.country.value),
                    postal_code: $.trim(form.postcode.value),
                    //state: $.trim(form.county.value),
                }
            },
            
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
                // handles the overlay and applies the customCSS
                $('#payment-form').fadeToggle(100);
                $('#payment-processing-overlay').fadeToggle(100);

                //enabling card element
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
                console.log("payment failed")                                 
            } else {
                // if intent succeeeded then submit and will redirect
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });     
    }).fail(function () {
        location.reload();
    })   
   
});

