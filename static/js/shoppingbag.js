console.log('Testing my shopping bag.js file ')


// Adding Event Handler to listen for click on Product detail page using the update-shoppingbag
//credit to Dennis Ivy @ teachable 
var addEventHandlertoBtns = document.getElementsByClassName('update-shoppingbag')

for (var i= 0; i < addEventHandlertoBtns.length; i++){
    addEventHandlertoBtns[i].addEventListener('click',function(){
       var productId =this.dataset.product
       var action =this.dataset.action
       console.log('productId:', productId, 'action:', action) 
    })
}    