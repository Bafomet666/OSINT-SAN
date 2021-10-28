//===================
//  Odometer
//  Here set the numebers
//===================

setTimeout(function(){
  $('.odometer.01').html(23578);
}, 1000);
setTimeout(function(){
  $('.odometer.02').html(12702);
}, 1000);


//===================
//  Magnific Popup
//===================

jQuery(document).ready(function() {
  jQuery('.image-gallery').magnificPopup({
    delegate: '.item a', // child items selector, by clicking on it popup will open
    type:'image'
  });

  //===================
  //  WOW
  //  do not touch
  //===================

  new WOW().init();

});



//===================
// Scroller
//  do not touch
//===================

$(function(){

  $('nav.pushy a[href*=#]').click(function() {

  if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'')
      && location.hostname == this.hostname) {

          var $target = $(this.hash);

          $target = $target.length && $target || $('[name=' + this.hash.slice(1) +']');

          if ($target.length) {

              var targetOffset = $target.offset().top -0;

              $('html,body').animate({scrollTop: targetOffset}, 800);

              return false;

          }

      }

  });

});
