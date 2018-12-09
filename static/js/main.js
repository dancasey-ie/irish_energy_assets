// Controls initial state of collapse Divs relative to screen resolution
var setDivsState = function () {
    if ($(window).width() < 576) {
        $(function () {
            $('.collapse_xs').removeClass('in');
        });
    }
    else if ($(window).width() < 768) {
        $(function () {
            $('.collapse_sm').removeClass('in');
        });
    }

    else
        $(function () {

            $('.collapse_xs').addClass('in');
            $('.collapse_sm').addClass('in');
        });
    }

$(document).ready(setDivsState);

$('.collapse').on('shown.bs.collapse', function () {
    $(this).parent().find(".fa-plus").removeClass("fa-plus").addClass("fa-minus");
}).on('hidden.bs.collapse', function () {
    $(this).parent().find(".fa-minus").removeClass("fa-minus").addClass("fa-plus");
});
