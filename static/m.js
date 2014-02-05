(function() {

var $ = jQuery,
    bdy = $('body');

    //Bindum smell á fjarlægja hnapp til þess að fjarlægja lán.
    $('.addloan').on('click', function (e) {
        e.preventDefault();

        var link = $(this),
            fieldset = link.parents('form').find('.loan:first'),
            fieldsetClone = fieldset.clone();

        fieldsetClone.append('<a class="rmloan" href="#rmloan">Fjarlægja</a>')

        fieldsetClone.find('input')
            .each(function () {
                $(this).val("");
              });

        fieldsetClone.insertBefore(link);
    });

    //Bindum smell á fjarlægja hnapp til þess að fjarlægja lán.
    $(bdy).on('click', '.rmloan', function (e) {
        $(this).parents('fieldset').remove();
    });

})($);