var body = document.body,
mask = document.createElement("div");

var openModal = function(modal){
	$('#'+modal).fadeIn();
	$(mask).addClass("mask");
	$(body).append($(mask));
};

$(mask).on("click", function(){
	$('#login-modal').fadeOut();
	$(mask).remove();
});