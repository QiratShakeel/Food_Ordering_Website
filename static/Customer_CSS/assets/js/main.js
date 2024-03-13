


// /* -------------------------------------------------------------------------- */
// /*                            Cart Button Work                            */
// /* -------------------------------------------------------------------------- */
//if cart btn is clicked
// $('#cart_btn_').click(function(){
//   console.log("btn is clicked")
//   cart= JSON.parse(localStorage.getItem('cart'));
//   if(cart.length === 0){
//     console.log("Empty");
//   }
//   else{
//     cart_ids=[];
//     for (var i = 0; i < cart.length; i++) {
//       id=parseInt(cart[i].id)
//       cart_ids.push(id);      
//     }
//     console.log(cart_ids)
//     $.ajax({
//       url: 'cart/',
//       type: 'GET',
//       data: { cart_ids: cart_ids },
//       success: function(response) {
//         console.log(response); // Log the entire response object
//         if (response && response.items_in_cart) {
//             console.log(response.items_in_cart); // Log the items_in_cart property
//             // Your code to iterate over cart items and update HTML
//         } else {
//             console.error("Response or items_in_cart is undefined:", response);
//         }
    
//         cartItems=response.items_in_cart;
//           // Clear previous cart items from HTML
//         //$('#cart_items').empty();
        
//         // Iterate over cartItems and update HTML
//         for (var i = 0; i < cartItems.length; i++) {
//             var item = cartItems[i];
//             var html = '<div class="row" style="border-bottom: 1px solid lightgrey;">' +
//                 '<div class="col-3" style="padding: 0;">' +
//                 '<img src="' + item.food_img + '" style="width:100px">' +
//                 '<p></p>' +
//                 '</div>' +
//                 '<div class="col-4" style="padding:0;line-height: 5;padding-left: 9px;font-weight: 600;font-size: large;">' +
//                 '<p>' + item.food_item_name + '</p>' +
//                 '<p></p>' +
//                 '</div>' +
//                 '<div class="col-5 d-flex" style="justify-content:flex-end;align-items:flex-end;flex-direction: column;">' +
//                 '<p style="margin-top: revert-layer;margin-bottom: unset;">Rs. ' + item.food_item_price + '</p>' +
//                 '</div>' +
//                 '</div>';
//             $('#cart_items').html(html);
//         };
//       },
//       error: function(xhr, status, error) {
//           console.error("ajax error is:",xhr.responseText);
//       }
//   });
//   }
// })


$(document).ready(function(){

// /* -------------------------------------------------------------------------- */
// /*                            Modal Work                            */
// /* -------------------------------------------------------------------------- */
    $('#item_modal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget); // Button that triggered the modal
        var objectId = button.data('item-id'); // Extract object ID from data attribute
        var food_item_detail_Url = document.getElementById("food_item_detail_url").textContent;
        // Perform AJAX request to fetch object details using the object ID
        // For demonstration, let's assume the details are retrieved and then displayed in the modal body
        $.ajax({
            url: food_item_detail_Url,
            type: 'GET',
            data: { object_id: objectId },
            success: function(response) {
                //console.log(response);
                try {
                  // Update modal content with data from response
                  $('#modal_name').text(response.name);
                  $('#modal_desc').text(response.description);
                  $('#modal_price').text("Rs."+response.price);
                  $('#modal_image').attr('src', response.image);
                  $('.cart').attr('id', "pr"+ objectId);
                  $('.minus').attr('id', "minuspr"+ objectId);
                  $('.plus').attr('id', "pluspr"+ objectId);
                  $('.divpr').attr('id', "divpr"+ objectId);
                  $('.valpr').attr('id', "valpr"+ objectId);
                  $('.inst').attr('id', "inst"+ objectId);
                } catch (error) {
                  console.error('Error updating modal content:', error);
                }
            },
            error: function(xhr, status, error) {
                console.error("ajax error is:",xhr.responseText);
            }
        });
    });





// /* -------------------------------------------------------------------------- */
// /*                            Local Storage Work                            */
// /* -------------------------------------------------------------------------- */
    //if item is present in local storage
    if(localStorage.getItem('cart')==null){
    var cart=[]
    }
    else{
    cart= JSON.parse(localStorage.getItem('cart'));
    updateCart(cart)
    }




// /* -------------------------------------------------------------------------- */
// /*                            Add to Cart button Work                            */
// /* -------------------------------------------------------------------------- */
    //if add to cart button is clicked
    $('.cart').click(function(){
    var idstr= this.id.toString();
    id=idstr.slice(2,)
    console.log("this is add to cart id:",id);
    var element = document.querySelector("#valpr"+id);
    var textareaValue = document.getElementById("inst"+id).value;  
    if (textareaValue!=""){
      instructions=textareaValue;
    } else {
      instructions=""};
      console.log(instructions)
      qty=element.innerText;
      item={
        "id": id,
        "qty": qty,
        "instructions": instructions
      }
      var idExists = false;
    for (var i = 0; i < cart.length; i++) {
    if (cart[i].id === id) {
      // Update the quantity if the id exists
      cart[i].qty = qty;
      cart[i].instructions = instructions;
      idExists = true;
      break;
    }
    }
    if (!idExists) {
    cart.push(item);
    }
    //console.log(Object.values(cart));
    updateCart(cart)   
    });









// /* -------------------------------------------------------------------------- */
// /*                            Update Cart In Local Storage & Cart Icon Increament Work                            */
// /* -------------------------------------------------------------------------- */
    //update the cart button with plus or minus 
    function updateCart(cart){
    sum=0;
    for (var i = 0; i < cart.length; i++) {
      qty=parseInt(cart[i].qty)
      sum += qty;      
    }
    localStorage.setItem('cart',JSON.stringify(cart));
    document.getElementById('cartno').innerHTML = sum;      
    }







// /* -------------------------------------------------------------------------- */
// /*                            Modal Qty Minus Button Work                            */
// /* -------------------------------------------------------------------------- */   
    //if minus is clicked 
  $('.divpr').on("click","button.minus",function(){
    console.log("minus clicked");
    id=this.id.slice(5,);
    console.log(id)
    //var element = document.querySelector("#valpr"+id);
    var element = $("#val" + id);
    var qty = parseInt(element.text());
    qty = Math.max(0, qty -1);
    element.text(qty);
    if(qty==0){
      element.text("1");
    }else{
      element.text(qty);
    }
  })





// /* -------------------------------------------------------------------------- */
// /*                            Modal Qty Plus Button Work                            */
// /* -------------------------------------------------------------------------- */
  //is plus is clicked
  $('.divpr').on("click","button.plus",function(){
    console.log("plus clicked");
    id=this.id.slice(4,);
    console.log(id)
    var element = $("#val" + id);
    qty=parseInt(element.text());
    qty+=1;
    element.text(qty);
  })

  var sum_of_prices = 0;

// /* -------------------------------------------------------------------------- */
// /*                           Clear Cart Button Work                            */
// /* -------------------------------------------------------------------------- */
  //if cart is clear 
  $('.clear_cart').on("click",
  function() {
    localStorage.clear();
    cart=[];
    updateCart(cart);
    document.getElementById("cart_items_offcanvas").innerHTML = "";
    document.getElementById("cart_items_offcanvas").insertAdjacentHTML("beforeend", `Empty`);
    sum_of_prices = 0;
  })
  

// /* -------------------------------------------------------------------------- */
// /*                            Modal CLose with Close Button Work                            */
// /* -------------------------------------------------------------------------- */
  //modal close
  $('.btn-close').on("click",function(){
    document.querySelector(".valpr").innerHTML = 1;
    document.getElementById("instruction").value = "";
  })

// /* -------------------------------------------------------------------------- */
// /*                            Cart Button Work                            */
// /* -------------------------------------------------------------------------- */
  //if cart btn is clicked
  $('#cart_btn_').click(function(){
    cart= JSON.parse(localStorage.getItem('cart'));
    console.log("cart",cart)
  if(cart.length === 0){
    document.getElementById("cart_items_offcanvas").innerHTML += `Empty Cart`;
  }
  else{
    cart_ids=[];
    for (var i = 0; i < cart.length; i++) {
      id=parseInt(cart[i].id)
      cart_ids.push(id);      
    }
    console.log(cart_ids)
    var cartUrl = document.getElementById("cart_url").textContent;
    $.ajax({
      url: cartUrl,
      type: 'GET',
      data: { cart_ids: cart_ids },
      success: function(response) {
        console.log(response); // Log the entire response object
        if (response && response.items_in_cart) {
            console.log(response.items_in_cart); // Log the items_in_cart property
            // Your code to iterate over cart items and update HTML
            cartItems = response.items_in_cart;
            var cartItemsContainer = document.getElementById("cart_items_offcanvas");
            cartItemsContainer.innerHTML = "";
        
        if (cartItems.length === 0) {
          cartItemsContainer.innerHTML += `Empty`;
        } else {
            
        for (var i = 0; i < cartItems.length; i++) {
            var item = cartItems[i];
            console.log(item.food_item_name);
            totalprice= item.food_item_price* parseInt(cart[i].qty)
            sum_of_prices+=totalprice;
            console.log("Total price is:",totalprice)
            document.getElementById("cart_items_offcanvas")
                .insertAdjacentHTML("beforeend",  `<div class="row" style="border-bottom: 1px solid lightgrey;">
                  <ul style="display: flex;
                      list-style: none;
                      align-items: center;
                      justify-content: space-around;
                      ">
                      <li><img src="`+item.food_img+`" style="width:100px"></li>
                      <li><p>`+item.food_item_name+`</p></li>
                        <div class="counter" style="display: flex;
                        flex-wrap: wrap;
                        flex-direction: row-reverse;
                        justify-content: center;">
                          <button class="button is-ghost btn_cart_minus" id="btn_cart_minus`+cart[i].id+`"><i class="counter-icons fa-solid fa-minus"></i></button>
                          <p id="btn_qty_val`+cart[i].id+`" style="padding:5px;font-weight:600;margin-top:0;">`+cart[i].qty+`</p>  
                          <button class="button is-ghost btn_cart_plus" id="btn_cart_plus`+cart[i].id+`"><i class="counter-icons fa-solid fa-plus"></i></button>
                          </div>
                      <p>Rs.
                      <span id="total_price`+cart[i].id+`">`+totalprice+`</span>
                      <span style="display:none;" id="Original_price`+cart[i].id+`">`+item.food_item_price+`</span>
                      </p>
                  </ul>
                  </div>`);
                //$('#cart_items').append(html);
        };
        document.getElementById("cart_items_offcanvas").innerHTML += `<div class="row" style="margin-top:20px">
        <div class="col-6" style="text-align:center;">Total Price :</div>
        <div class="col-6">Rs. <span id="sum_of_prices">`+sum_of_prices+`</span></div>
        </div>
        <div class="row" style="justify-content:center;"><a id="cart_checkout_btn_" class="btn-gradee btn-danger" style="margin-top:20px;width:300px">Checkout</a>
        </div>`;
        // Checkout Btn Click 
        $(document).on('click','#cart_checkout_btn_',function(){
          var checkoutUrl = document.getElementById("checkout_url").textContent;
          document.location.href = checkoutUrl;
        });
      }
      } else {
      console.error("Response or items_in_cart is undefined:", response);
      }
      },
      error: function(xhr, status, error) {
          console.error("ajax error is:",xhr.responseText);
      }
    });
    }
  });

  


// /* -------------------------------------------------------------------------- */
// /*                            Cart Section Minus Button Qty Work               */
// /* -------------------------------------------------------------------------- */
  //minus cart button
  $(document).on('click', 'button.btn_cart_minus', function() {
    // Get the ID of the minus button
    var id = $(this).attr('id').replace('btn_cart_minus', '');
    console.log("Minus button with ID " + id + " is clicked");
    
    // Update the quantity for this specific item
    var element = $("#btn_qty_val" + id);
    var original_priceId = $("#Original_price" + id);
    var total_priceId = $("#total_price" + id);
    var sumId = $("#sum_of_prices");
    var qty = parseInt(element.text());
    var price = parseInt(original_priceId.text());
    qty = Math.max(0, qty -1);
    new_totalprice=price*qty;
    sum_of_prices -= price; 
    element.text(qty);
    total_priceId.text(new_totalprice)
    sumId.text(sum_of_prices)

    cart=JSON.parse(localStorage.getItem('cart'));
    for (var i = 0; i < cart.length; i++) {
    if (cart[i].id === id) {
      // Update the quantity if the id exists
      cart[i].qty = qty;
      break;
    }
    }
    updateCart(cart)
  });


// /* -------------------------------------------------------------------------- */
// /*                            Cart Section Plus Button Qty Work                */
// /* -------------------------------------------------------------------------- */
  //plus cart button
  $(document).on('click', 'button.btn_cart_plus', function() {
        // Get the ID of the minus button
    var id = $(this).attr('id').replace('btn_cart_plus', '');
    console.log("PLus button with ID " + id + " is clicked");
    
    // Update the quantity for this specific item
    var element = $("#btn_qty_val" + id);
    var original_priceId = $("#Original_price" + id);
    var total_priceId = $("#total_price" + id);
    var sumId = $("#sum_of_prices");
    var qty = parseInt(element.text());
    var price = parseInt(original_priceId.text());
    qty =qty+ 1;
    element.text(qty);
    new_totalprice=price*qty;
    sum_of_prices += price; 
    total_priceId.text(new_totalprice)
    sumId.text(sum_of_prices)

    cart=JSON.parse(localStorage.getItem('cart'));
    for (var i = 0; i < cart.length; i++) {
    if (cart[i].id === id) {
      // Update the quantity if the id exists
      cart[i].qty = qty;
      break;
      }
    } 
    updateCart(cart)
  });



  // //////////////////////////Food Type Select Page Work/////////////////////
  // var selectElement = document.getElementById("food_type");

    // Add event listener for change event
    $('#food_type').change(function() {
        // Get the selected option value
        var food_type_id = $(this).val();
        console.log("Selected value:", food_type_id);
        food_type_fk=$(".category_food_type_fk").text()
        console.log("Food Type Fk:", food_type_fk);
        // food_type_fk.text(food_type_id)
        if(food_type_fk== food_type_id){
          $('.carouselSearchByFood_carousel-item').hide();
          $('.carouselSearchByFood_carousel-item[data-food-type="' + food_type_id + '"]').show();
          $('#carouselSearchByFood').carousel('dispose').carousel();
        }else{
          $('.carouselSearchByFood_carousel-item').show();
        }
      // Show only the carousel items that match the selected food type

      // Trigger the carousel to update its state
    });














});