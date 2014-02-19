(function() {

var $ = jQuery,
    bdy = $('body');


    //Bindum smell á hnapp til þess að bæta við láni.
    $('.addloan').on('click', function (e) {
        e.preventDefault();

        var link = $(this),
            linkParent = link.parents('p'),
            fieldset = link.parents('form').find('.loan:first'),
            fieldsetClone = fieldset.clone(),
            numLoans = link.parents('form').find('.loan').length;

        fieldsetClone
            .append('<a class="rmloan" href="#rmloan">Úps, ég er ekki með svona mörg lán!</a>');

        //Bætum við tölu aftan við "Lán" fyrirsögnina okkar í fieldsettinu.
        fieldsetClone
            .each(function () {
                var heading = $(this).find('h2');
                heading.text(heading.text() + ' ' + numLoans);
              });

        //Breytum for attr á label
        fieldsetClone
            .find('.radioinp label')
                .each(function () {
                    var label = $(this),
                        currId = label.attr('for');

                    label.attr('for', currId + numLoans);
                  });

        //Breytum name og id á input
        fieldsetClone
            .find('.radioinp input')
                .each(function () {
                    var radio = $(this),
                        currId = radio.attr('id'),
                        name = radio.attr('name');

                    radio.attr('id', currId + numLoans);
                    radio.attr('name', name + numLoans);
                    radio.prop('checked', false);
                  });

        //Hreinsum textareiti
        fieldsetClone
            .find('input[type="text"]')
                .each(function () {
                    $(this).val('');
                  });

        //Setjum nýja lánið okkar inn í DOM-ið.
        fieldsetClone.insertBefore(linkParent);
    });


    bdy.on('change', '.radioinp input', function (e) {
        var allRadios = $('.radioinp input:checked'),
            allRadioValues = [];

        allRadios.each(function () {
            allRadioValues.push($(this).val())
          });

        //$('#radioDummy').val()
      });

    //Bindum smell á fjarlægja hnapp til þess að fjarlægja lán.
    $(bdy).on('click', '.rmloan', function (e) {
        $(this).parents('fieldset').remove();
    });

    //Komum í veg fyrir að hægt sé að setja annað en tölustafi og punkt í textareitinn.
    $('.num').on('keydown', function(e) {
        var key = e.keyCode,
            allowedKeys = [8, 18, 9, 35, 36, 37, 39, 18, 190, 16, 46];

        if( allowedKeys.indexOf( key ) == -1 && isNaN( String.fromCharCode( key ) ) )
        {
            return false;
        }
    });

    //Bindum smelli á plús/mínus hnappa til að hækka/lækka gildi í tölureitum.
    $('.num').each(function() {
        var num = $(this),
            parent = num.parents('fieldset'),
            buttons = $(this).find('.plus, .minus');

        buttons.on('click', function() {
            var button = $(this),
                bparent = button.parents('.num'),
                input = bparent.find('input'),
                val = parseFloat(input.val(), 10);

            if( button.is('.minus') )
            {
                val >= 1 ? input.val(val - 1) : '';
            }
            else {
                input.val(val + 1);

                //if we're incrementing the period part (years/months)
                //we want to increment the year ticker once we reach 12 months
                if(parent.is('.period') && val === 12)
                {
                    var years = parseInt(parent.find('#periodYears').val(), 10);
                    parent.find('#periodYears').val(years + 1);
                    input.val(0);
                }
            }
        });

    });

})($);