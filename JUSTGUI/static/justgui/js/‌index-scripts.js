/******************
	@ Prefect JS
********************/


'use strict';

$(window).on('load', function() { 
	/*------------------
		Preloder
	--------------------*/
	$(".loader").fadeOut(); 
	$("#preloder").delay(400).fadeOut("slow");


	/*------------------
		Isotope Filter
	--------------------*/
	var $container = $('.isotope_items');
	$container.isotope();

	$('.portfolio-filter li').on("click", function(){
		$(".portfolio-filter li").removeClass("active");
		$(this).addClass("active");				 
		var selector = $(this).attr('data-filter');
		$(".isotope_items").isotope({
				filter: selector,
				animationOptions: {
				duration: 750,
				easing: 'linear',
				queue: false,
			}
		});
		return false;
	});
});


(function($) {

	/*------------------
		Site Navigation
	--------------------*/
	var navMenu = $('.menu-list')
		navMenu.onePageNav();
	$(window).on('scroll resize',function(e) {
		var introH = $('.intro-section').height() - 90;
		if ($(this).scrollTop() > introH) {
			$('.header-section').addClass('sticky');
		}else{
			$('.header-section').removeClass('sticky');
		}
		e.preventDefault();
	});

	$('.nav-switch').on('click', function(event) {
		$('.mainmenu').toggleClass('active');
		$(this).toggleClass('active');
		event.preventDefault();
	});


	$('.responsive').on('click', function(event) {
		$('.menu-list').toggleClass('nav-show');
		$('.menu-list li a').on('click', function(event) {
			$('.menu-list').removeClass('nav-show');
			event.preventDefault();
		});
		event.preventDefault();
	});


	/*------------------
		Intro Title
	--------------------*/
	$(window).on('scroll', function() {
		if ($(window).scrollTop() >= 200) {
			$(".intro-content").addClass("hideup");
		}
		else {
			return $(".intro-content").removeClass("hideup");
		}
	});


	/*------------------
		Magnific Popup
	--------------------*/
	$('.work-item').magnificPopup({
		type:'image',
		gallery:{enabled:true},
		zoom:{enabled: true, duration: 300}
	});


	/*------------------
		Owl Carousel
	--------------------*/
	$('.review-carousel').owlCarousel({
		dots: true,
		nav: false,
		loop: true,
		smartSpeed: 700,
		items: 1,
		autoplay: true
	});


	/*------------------
		Contact Form
	--------------------*/
	$('#con_form').on('submit', function() {
		var send_btn = $('#send-form'),
			form = $(this),
			formdata = $(this).serialize(),
			chack = $('#form-chack');
			send_btn.text('Wait...');

		function reset_form(){
		 	$("#name").val('');
			$("#email").val('');
			$("#massage").val('');
		}

		$.ajax({
			url:  $(form).attr('action'),
			type: 'POST',
			data: formdata,
			success : function(text){
				if (text == "success"){
					send_btn.addClass('done');
					send_btn.text('Success');
					setTimeout(function() {
						reset_form();
						send_btn.removeClass('done');
						send_btn.text('Send A Massege');
					}, 5000);
				}
				else {
					reset_form();
					send_btn.addClass('error');
					send_btn.text('Error');
					setTimeout(function() {
						send_btn.removeClass('error');
						send_btn.text('Send A Massege');
					}, 4000);
				}
			}
		});
		return false;
	});


})(jQuery);


	/*------------------
		WOW JS
	--------------------*/
	new WOW().init();


	/*------------------
		GOOGLE MAP
	--------------------*/
	function initialize() {
		var myOptions = {
			zoom: 15,
			center: new google.maps.LatLng(40.801485408197856, -73.96745953467104), //change the coordinates
			mapTypeId: google.maps.MapTypeId.ROADMAP,
			scrollwheel: false,
			mapTypeControl: false,
			zoomControl: false,
			streetViewControl: false,
			styles: [{
				"stylers": [{
					"hue": "#000000"
				}, {
					saturation: -110
				}, {
					gamma: 2
				}]
			}]
		};
		var map = new google.maps.Map(document.getElementById("map"), myOptions);
		var marker = new google.maps.Marker({
			map: map,
			animation: google.maps.Animation.DROP,
			position: new google.maps.LatLng(40.801485408197856, -73.96745953467104) //change the coordinates
		});
		google.maps.event.addListener(marker, "click", function() {
			infowindow.open(map, marker);
		});
	}
	google.maps.event.addDomListener(window, 'load', initialize);
