$(document).ready(function() {
	$("#content_dialer").show();	
	$("#content_contacts").hide();	
	$("#content_add_contact").hide();	
	
	$("#tab_dialer").addClass("current-tab");
	$("#tab_contacts").removeClass("current-tab");
	$("#tab_add_contact").removeClass("current-tab");
});

$("#tab_dialer").click(function() {
	$("#content_dialer").show();	
	$("#content_contacts").hide();	
	$("#content_add_contact").hide();	
	
	$("#tab_dialer").addClass("current-tab");
	$("#tab_contacts").removeClass("current-tab");
	$("#tab_add_contact").removeClass("current-tab");
});

$("#tab_contacts").click(function() {
	$("#content_dialer").hide();	
	$("#content_contacts").show();
	$("#content_add_contact").hide();		
	
	$("#tab_dialer").removeClass("current-tab");
	$("#tab_contacts").addClass("current-tab");
	$("#tab_add_contact").removeClass("current-tab");
});

$("#tab_add_contact").click(function() {
	$("#content_dialer").hide();	
	$("#content_contacts").hide();
	$("#content_add_contact").show();		
	
	$("#tab_dialer").removeClass("current-tab");
	$("#tab_contacts").removeClass("current-tab");
	$("#tab_add_contact").addClass("current-tab");
});

/* fancy dialing functions */
$("#dialer_pad button").click(function() {
	$("#number_input").val($("#number_input").val() + this.innerText);
})

$("#button_dialer_clear").click(function() {
	$("#number_input").val("");
})
