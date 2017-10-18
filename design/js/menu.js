$(document).ready(function(){

	$(".menu-dropdown-icon").on("click", function(){
		$(".site-navigation").toggleClass("dropdown-open");
		$(".search-section-content").toggleClass("search-open");
	});

});