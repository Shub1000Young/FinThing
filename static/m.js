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
            .find('.radioinp input[type="radio"]')
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
            .find('input[type="text"], #radioDummy')
                .each(function () {
                    $(this).val('');
                  });

        //Setjum nýja lánið okkar inn í DOM-ið.
        fieldsetClone.insertBefore(linkParent);
    });


    bdy.on('change', '.radioinp input', function (e) {
        var radioBtn = $(this),
            radioParent = radioBtn.parents('.radioinp'),
            radioDummy = radioParent.find('#radioDummy');

        radioDummy.val(radioBtn.val())
      });

    //Bindum smell á fjarlægja hnapp til þess að fjarlægja lán.
    $(bdy).on('click', '.rmloan', function (e) {
        e.preventDefault();
        $(this).parents('fieldset').remove();
    });

    //Komum í veg fyrir að formi sé submittað ef nauðsynlegir reitir eru ekki útfylltir
    $('form').on('submit', function (e) {
        var theForm = $(this),
            canSubmit = true;

        theForm.find('.req')
            .each(function () {
                var req = $(this),
                    input = req.find('input');

                if(input.val().length == 0)
                {
                    req.addClass('error');
                    canSubmit = false;
                }
                else
                {
                    req.removeClass('error');
                }
              });

        if (!canSubmit)
        {
            ;;;alert( 'Ertu viss um að þú hafir fyllt allt út?' );
        }

        return canSubmit;
      });

    //Komum í veg fyrir að hægt sé að setja annað en tölustafi og punkt í textareitinn.
    $('.num').on('keydown', function(e) {
        var key = e.keyCode,
            //allowedKeys = [8, 18, 9, 35, 36, 37, 39, 18, 190, 16, 46];
            allowedKeys = [
                  8, // BACKSPACE
                  9, // TAB
                 18, //
                 35, //
                 36, //
                 37, // LEFT
                 39, // RIGHT
                 46, // DEL
                 48, // 0
                 49, // 1
                 50, // 2
                 51, // 3
                 52, // 4
                 53, // 5
                 54, // 6
                 55, // 7
                 56, // 8
                 57, // 9
                 96, // 0 (numpad)
                 97, // 1 (numpad)
                 98, // 2 (numpad)
                 99, // 3 (numpad)
                100, // 4 (numpad)
                101, // 5 (numpad)
                102, // 6 (numpad)
                103, // 7 (numpad)
                104, // 8 (numpad)
                105, // 9 (numpad)
                190  // .
              ];

        if( allowedKeys.indexOf( key ) == -1 && isNaN( String.fromCharCode( key ) ) )
        {
            return false;
        }
    });

    //Prettyfy tölur
    $('.pnum').prettynumber();

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

    //Gögn fyrir línurit hefur verið prentað út sem HTML notum JS hérna til að "veiða" gögnin.
    var originalNode = $('.original li'),
        newlistNode = $('.newlist li'),
        periodNode = parseInt($('.period').text(), 10),
        m_paymnt = parseInt($('.m_paymnt').text(), 10),
        periodData = [],
        originalData = [],
        newlistData = [];

        for (var i=0; i<periodNode; i++)
        {
          periodData[i] = i + '';
        }

        for (var i=0; i<originalNode.length; i++)
        {
            newlistData[i] = parseInt(newlistNode.eq(i).text());
            originalData[i] = parseInt(originalNode.eq(i).text());
        }

    //Setjum upplýsingar línurits í lineChartData hlutinn
    var lineChartData = {
            labels : periodData,
            datasets : [
            {
              fillColor : "rgba(220,220,220,0.5)",
              strokeColor : "rgba(220,220,220,1)",
              pointColor : "rgba(220,220,220,1)",
              pointStrokeColor : "#fff",
              data : originalData
            },
            {
              fillColor : "rgba(151,187,205,0.5)",
              strokeColor : "rgba(151,187,205,1)",
              pointColor : "rgba(151,187,205,1)",
              pointStrokeColor : "#fff",
              data : newlistData
            }
            ]
            };

    //stillingahlutur fyrir línuritið
    var options = {
        scaleOverride: true,
        scaleSteps : periodNode,
        scaleStepWidth : m_paymnt,
        scaleStartValue : 0,
        bezierCurve: false
    }

    //teiknum loks línuritið
    var canvas = document.getElementById("canvas");
    if (canvas)
    {
        new Chart(canvas.getContext("2d")).Line(lineChartData, options);
    }
})($);