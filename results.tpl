%include header

<!-- this template is for testing purposes as is -->
<div>
    <h2>Hagstæðast er að greiða af láni: {{ loanList[0] }}</h2>
    <p>Við það sparast {{ loanList[1] }} kr.</p>
</div>

  <div class="wrapper">
    <h2>Fyrirsögn</h2>

    <div class="bestloan">
      <p>Með því að greiða aukalega {{mamount}} kr. inn á {{listi af lánum}} á mánuði í {{term}} mánuði getur þú lækkað lánin þínum.</p>
      <ul>
        <li>{{nafnáláni}} um {{upphæð sem lánið lækkar um}}</li>
      </ul>
    </div>

    <div class="bestsaving">
      <p>Með því að leggja fyrir {{mamount}} á mánuði í {{term}} mánuði getur þú sparað {{totalsaved}}.</p>

      <canvas id="canvas" height="450" width="600"></canvas>
    </div>

    <div class="results">
    %if (sparndaru > lowestloan)
    %Það er betra fyrir þig að spara peningana þína heldur en að greiða niður lán
    %else
    %Það er best fyrir þig að greiða niður af einhverju láni.
    </div>

  </div>

%include bottom