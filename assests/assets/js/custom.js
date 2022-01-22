$('.counting').each(function() {
  var $this = $(this),
      countTo = $this.attr('data-count');

  $({ countNum: $this.text()}).animate({
    countNum: countTo
  },

  {

    duration: 3000,
    easing:'linear',
    step: function() {
      $this.text(Math.floor(this.countNum));
    },
    complete: function() {
      $this.text(this.countNum);
      //alert('finished');
    }

  });


});

$(function(){
  $('#Container').mixItUp();
});

$('#mixitupContent').mixItUp();
         jQuery(".html5lightbox").html5lightbox();

$(document).ready(function(){
    var image = $(".main-banner-section").data('image');
    console.log('image', image);
    $(".main-banner-section").css("background-image", "url(" + image + ")");
});