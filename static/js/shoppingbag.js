console.log('Testing my shopping bag.js file ')

//Credit Code Institute - Boutique ADO project
 // Disable +/- buttons outside 1-99 range
 function handleEnableDisable(itemId) {
    var currentValue = parseInt($(`#id_qty_${itemId}`).val());
    var minusDisabled = currentValue < 2;
    var plusDisabled = currentValue > 98;
    $(`#decrement-qty_${itemId}`).prop('disabled', minusDisabled);
    $(`#increment-qty_${itemId}`).prop('disabled', plusDisabled);
}

// Ensure proper enabling/disabling of all inputs on page load
var allQtyInputs = $('.qty_input');
for(var i = 0; i < allQtyInputs.length; i++){
    var itemId = $(allQtyInputs[i]).data('item_id');
    handleEnableDisable(itemId);
}

// Check enable/disable every time the input is changed
$('.qty_input').change(function() {
    var itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});

// Increment quantity  - looking for value in input-group > .qty_input
$('.increment-qty').click(function(e) {
   e.preventDefault();
   var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
   var currentValue = parseInt($(closestInput).val());
   $(closestInput).val(currentValue + 1);
   var itemId = $(this).data('item_id');
   handleEnableDisable(itemId);
   console.log('in the shoppinbag js increment')
});

// Decrement quantity
$('.decrement-qty').click(function(e) {
   e.preventDefault();
   var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
   var currentValue = parseInt($(closestInput).val());
   $(closestInput).val(currentValue - 1);
   var itemId = $(this).data('item_id');
   handleEnableDisable(itemId);
});




// Adding Event Handler to listen for click on Product detail page using the update-shoppingbag
//credit to Dennis Ivy @ teachable 
var addEventHandlertoBtns = document.getElementsByClassName('update-shoppingbag')

for (var i= 0; i < addEventHandlertoBtns.length; i++){
    addEventHandlertoBtns[i].addEventListener('click',function(){
       var productId =this.dataset.product
       var action =this.dataset.action
       console.log('productId:', productId, 'action:', action) 

//check if user is logged in        
       console.log('User:', user)
       if (user == 'AnonymousUser'){
        console.log('User not logged in')
       }
       else{
         updateUserOrder(productId, action)
       }
    })
}  

function updateUserOrder(productId, action){
    console.log('user logged in')

    var url ='/shoppingbag/update_item/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action})        
    })
    //promise being returned after function has been successful
    //value from urls.py which points to views.py and update_item function, then converting to JSON 1st
    .then((response) =>{
        return response.json()
    })
    //grabbing above now converted to JSON and console.logging value from urls.py which points to views.py and update_item function
   .then((data) =>{
        console.log('data:',data)
    })
}
