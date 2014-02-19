%include header
<!-- this template is for testing purposes as is -->
<div>
    <p>{{loan[0].name}}</p>
    <p>{{maxprof}}</p>

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

    <canvas id="canvas" height="450" width="800"></canvas>
</div>



  </div>

%include bottom