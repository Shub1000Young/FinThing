%include header


%if years == 0:
<h1>Þú verður ekki lengi að þessu!</h1>
%elif 0 < years <= 9:
<h1>Hvað hefurðu mikinn tíma?</h1>
%elif years > 9:
<h1>Vonandi líður tíminn ekki of hægt...</h1>
%end

%monthsString = "mánuði"
%if months == 1:
%monthsString = "mánuð"
%end

<p class="savingsres">Það mun taka þig
%if years > 0:
<strong>{{years}}</strong> ár
%end

%if years > 0 and months > 0:
og
%end

%if months > 0:
<strong>{{months}}</strong>{{monthsString}}
%end

að safna upp í <strong class="pnum">{{total}}</strong> kr., miðað við að þú leggir fyrir <strong class="pnum">{{monthly}}</strong> kr. í hverjum mánuði!
</p>

<img src="static/damoney.gif" alt="Peningar" />



%include bottom