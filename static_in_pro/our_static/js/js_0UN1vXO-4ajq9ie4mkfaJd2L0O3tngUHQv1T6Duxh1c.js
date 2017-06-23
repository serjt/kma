(function ($) {
    Drupal.behaviors.joinandpay = {
	attach: function(context, settings) {
	    
	    $("#process-msg").html('<img src="/sites/default/modules/ama_join/images/ajax-loader.gif" /><h1>Processing your request.</h1><div>This may take up to 60 seconds. Please do not click any button during this time.</div>');
	    $("#process-msg").hide();

	    //$(".example8").colorbox({width:"50%", inline:true, href:"#inline_example1"});

	    $('#submit-wrapper button.form-submit:not(.japo-processed)', context).each(function() {
		$(this).addClass('japo-processed');
		$(this).click(function () {	    
		    $("#process-msg").show();
		    console.debug('Hello from processing msg');
		});
	    });
	    
	    // var state = $('#edit-state', context).val();
	    // //console.debug(state);
	    // if (state == 'WA' || state == 'VIC' || state == 'ACT') {
	    //     $('input#submit-join', context).hide();
	    // } else {
	    // 	$('input#submit-join', context).show();
	    // }
	    
	    // $('#state_info:not(.japo-processed)', context).each(function() {
	    // 	$(this).addClass('japo-processed');
	    // 	$(this).click(function() {
	    // 	    $('#state_info_text').toggle();
	    // 	});
	    // });
	    
	    // $('#category_info:not(.japo-processed)', context).each(function() {
	    // 	$(this).addClass('japo-processed');
	    // 	$(this).click(function() {
	    // 	    $('#category_info_text').toggle();
	    // 	});
	    // });
	}
    };
})(jQuery);
;
