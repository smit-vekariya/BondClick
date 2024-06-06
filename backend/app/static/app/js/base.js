var base = {
    reloadData : function(division){
        $.get(location.href, function(data) {
            $(`${division}`).html($(data).find(`${division}`).html());
        });
    }
}