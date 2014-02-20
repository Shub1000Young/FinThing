%include header

<div>

    <h2>Hagstæðasta sparnaðarleiðing</h2>
    <p>Að tímabilinu loknu muntu eiga {{savingsAmount}} kr. miðað við að þú hafir lagt inn á {{accountType}}.</p>


    <h2>Hagstæðasta lánið - {{loan[0].name}}</h2>
    <p>Með því að greiða aukalega inn á <strong>{{loan[0].name}}</strong> sparast {{maxprof}} kr.</p>

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
    </div>

    <h2>En hvað er eginlega best að gera?</h2>
    <p>Þar sem {better} gefur meiri hagnað er best fyrir þig að [insertVariableNameHere]</p>
</div>

%include bottom