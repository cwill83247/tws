console.log('Testing my shopping bag.js file ')


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