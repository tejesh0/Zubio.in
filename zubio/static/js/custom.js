$(function() {
	$('.search-field input').focus(function(){
		$('.search-field').addClass('red-border');
	});

	$('.search-field input').focusout(function(){
		$('.search-field').removeClass('red-border');
	});
});