var base = {

    // use for reload div
    reloadData : function(division){
        $.get(location.href, function(data) {
            $(`${division}`).html($(data).find(`${division}`).html());
        });
    },

    // use for replace div with new one
    replaceDiv : function(division, htmlData){
        $(`${division}`).html($(htmlData).find(`${division}`).html());

    }
}