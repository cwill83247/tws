/**
 * Stripe 
 * 
 * 
 */

/**Creating variable from converted JSON values in checkout > postload.js block   **/
/**removing quotations aroud the text with slice  */
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);

/** create instance of Stripe using  stripe javascript included at base.html**/
/**get the stripe card element and then add this into checkout.html by attaching to div - card-element */
var stripe = Stripe(stripe_public_key);


/** adding styling from Code Institute */
const appearance = {
    theme: 'stripe',
  
    variables: {
      colorPrimary: '#0570de',
      colorBackground: '#0000ff',
      colorText: '#30313d',
      colorDanger: '#df1b41',
      fontFamily: 'Ideal Sans, system-ui, sans-serif',
      spacingUnit: '2px',
      borderRadius: '4px',
      
    }
  };

var elements =stripe.elements({appearance});
var card = elements.create('card');
/**taking stripe card -element and putting into DIV - card-element in checkout.html **/
card.mount('#card-element');

