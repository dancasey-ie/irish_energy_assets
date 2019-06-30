// Controls initial state of collapse Divs relative to screen resolution
var setDivsState = function () {
    if ($(window).width() < 576) {
        $(function () {
            $('.collapse_xs').removeClass('in');
            $('.collapse_xs').parent().find(".fa-minus").removeClass("fa-minus").addClass("fa-plus");

        });
    }
    else if ($(window).width() < 768) {
        $(function () {
            $('.collapse_sm').removeClass('in');
            $('.collapse_sm').parent().find(".fa-minus").removeClass("fa-minus").addClass("fa-plus");

        });
    }

    else
        $(function () {

            $('.collapse_xs').addClass('in');
            $('.collapse_sm').addClass('in');
            $('.collapse_xs').parent().find(".fa-plus").removeClass("fa-plus").addClass("fa-minus");
            $('.collapse_sm').parent().find(".fa-plus").removeClass("fa-plus").addClass("fa-minus");

        });
};

$(document).ready(setDivsState);

$('.collapse').on('shown.bs.collapse', function () {
    $(this).parent().find(".fa-plus").removeClass("fa-plus").addClass("fa-minus");
}).on('hidden.bs.collapse', function () {
    $(this).parent().find(".fa-minus").removeClass("fa-minus").addClass("fa-plus");
});
