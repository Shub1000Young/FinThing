%include header

<div class="loanResults">

    <h2>Hagstæðasta sparnaðarleiðin</h2>
    <p>Að tímabilinu loknu muntu eiga <span class="pnum">{{savingsAmount}}</span> kr. miðað við að þú hafir lagt inn á {{accountType}}.</p>


    <h2>Hagstæðasta lánið - {{loan[0].name}}</h2>
    <p>Með því að greiða aukalega inn á <strong>{{loan[0].name}}</strong> sparast <span class="pnum">{{maxprofit}}</span> kr.</p>

    <canvas id="canvas" height="450" width="800"></canvas>

    <div class="chartData">
        <ul class="original">
            %for item in chartValues[0]:
                <li>{{item}}</li>
            %end
        </ul>

        <ul class="newlist">
            %for item in chartValues[1]:
                <li>{{item}}</li>
            %end
        </ul>

        <span class="period">{{period}}</span>
        <span class="m_paymnt">{{loan[0].m_paymnt}}</span>
        <span class="principle">{{loan[0].principle}}</span>
    </div>

    <h2>En hvað er eginlega best að gera?</h2>
    %if savingsAmount > maxprofit:
        <p>Þar sem að leggja peninginn fyrir gefur meiri hagnað er best fyrir þig að leggja aukatekjurnar inn á {{accountType}}.</p>
    %else:
        <p>Þar sem að greiða niður lánið gefur meiri hagnað er best fyrir þig að dæla öllum aukatekjunum í {{loan[0].name}}.</p>
    %end
</div>

%include bottom