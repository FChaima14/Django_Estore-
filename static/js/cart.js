console.log('heeelooo');
/* navbar menu icon a when the screen is phone*/
let menu=document.querySelector('#menu');
let navbar=document.querySelector('.nav-menu')
if(menu){
    menu.onclick=()=>{
        menu.classList.toggle('fa-times');
        navbar.classList.toggle('active');
    }
    window.onscroll=()=>{
        menu.classList.remove('fa-times');
        navbar.classList.remove('active');
    }
}

/*the slider fonctionality*/
let slider=document.querySelectorAll('.slide-container');
let index=0;

function next(){
    slider[index].classList.remove('active');
    index=(index+1) % slider.length;
    slider[index].classList.add('active')
}
function prev(){
    slider[index].classList.remove('active');
    index=(index-1+ slider.length) % slider.length;
    slider[index].classList.add('active')
}
/*add to cart fonctionality */
var btnAddtoCart=document.getElementsByClassName('update_Cart');
for(var i=0 ; i<btnAddtoCart.length ; i++){
    btnAddtoCart[i].addEventListener('click', function(){
        var productId=this.dataset.product;
        var action=this.dataset.action;
        console.log('productId', productId, 'action:', action)

        console.log("user:" ,user)
        if(user==='AnonymousUser'){
            console.log('User is not authenticated')
            alert('User is not authenticated')
        }
        else{
            updateDataOrder(productId, action)
        }
    } )

}
/* update the cart order by calling the backend server*/
function updateDataOrder(productId, action){
    console.log('user is authenticated, sending data..')

    url='/product/updateItem';
     fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken':  csrftoken,
        },
        body: JSON.stringify({
            'productId': productId,
            'action': action,
        })
    }).then((response)=>{
        return response.json();
    }).then((data)=>{
        console.log('Data', data)
        location.reload()
    })
}

/*popover function*/
var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
  return new bootstrap.Popover(popoverTriggerEl)
})

$('[data-bs-toggle="popover"]').popover({html: true});