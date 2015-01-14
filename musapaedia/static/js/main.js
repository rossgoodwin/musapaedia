 $.getJSON( "stanzas.json", function( data ) {
  var items = [];
  $.each( data, function( key, val ) {
    items.push( "<li id='" + key + "'>" + val + "</li>" );
  });
 
  $( "<ul/>", {
    "class": "my-new-list",
    html: items.join( "" )
  }).appendTo( "body" );
});

  // var global_place=0;
  // var pics=[{"id": "outline_dog", "image": "img/so.jpg"},
  //       	  {"id": "picture_dog", "image": "img/sn.jpg"},
  //       	  {"id": "picture_dog", "image": "img/2o.jpg"},
  //       	  {"id": "picture_dog", "image": "img/2n.jpg"},
  //       	  {"id": "picture_dog", "image": "img/3o.jpg"},
  //       	  {"id": "picture_dog", "image": "img/3n.jpg"},
  //       	  {"id": "picture_dog", "image": "img/4o.jpg"},
  //       	  {"id": "picture_dog", "image": "img/4n.jpg"},
  //       	  {"id": "picture_dog", "image": "img/5o.jpg"},
  //       	  {"id": "picture_dog", "image": "img/5n.jpg"},
  //           {"id": "picture_dog", "image": "img/6o.jpg"},
  //           {"id": "picture_dog", "image": "img/6n.jpg"},];

  // function loadReveal(callback){
  //   callback();
  // }

  // loadReveal(function() {
  //    // alert('Reveal');
  // });

  // addEventListener('click',function(evt) {
  //    document.getElementById('before').src = pics[global_place].image;
  //    global_place = (global_place + 1) % pics.length;
  //    console.log(global_place);
  // },false);


  //images from http://www.telegraph.co.uk/travel/picturegalleries/9252196/Queens-Diamond-Jubilee-London-then-and-now.html
