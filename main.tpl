%include header

  <h1>Sparnaður eða sparnaður</h1>

  <h2>Spara með hefðbundnum hætti eða spara með því að borga meira...ha?</h2>
  <p>Hér geturðu reinka út hvað þú græðir á því að greiða aukalega af lánunum þínum eða hvort það sé bara betra að leggja þessa auka peninga inn á reikning.</p>

  <form action="/lan" method="POST">
    <fieldset class="period">
      <h2>Hversu mikið og hvað lengi?</h2>
      <p>Nú er komið að því að spara eða greiða upp lánið! Hversu mikið geturðu lagt til mánaðarlega og í hvað langan tíma?</p>

      <div class="row">

        <div class="txtinp num w80 req">
          <label for="monthlyAmount">Mánaðarlega upphæð</label>
          <input id="monthlyAmount" type="text" name="monthlyAmount" value="" />
        </div>

        <div class="txtinp num hasops w40 req">
          <label for="periodYears">Ár</label>
          <span class="minus">-</span>
          <input id="periodYears" type="text" name="periodYears" value="0" />
          <span class="plus">+</span>
        </div>

        <div class="txtinp num hasops w40 req">
          <label for="periodMonths">Mánuðir</label>
          <span class="minus">-</span>
          <input id="periodMonths" type="text" name="periodMonths" value="1" />
          <span class="plus">+</span>
        </div>
      </div>

    </fieldset>

    <hr />

    <fieldset class="inflation">
      <h2>Verðbólgutímabil</h2>
      <p>Það eina sem við gerum er að taka meðaltal af verðbólgunni fyrir tíambilið sem þú velur.</p>

      <span>Frá</span>

      <div class="selinp">
        <select id="inflMstart" name="inflMstart">
          %months = ["Janúar", "Febrúar", "Mars", "Apríl", "Maí", "Júní", "Júlí", "Ágúst", "September", "Október", "Nóvember", "December"]
          %for x in range(1, 13):
          <option value="{{x}}">{{months[x-1]}}</option>
          %end
        </select>
      </div>

      <div class="selinp">
        <select id="inflYstart" name="inflYstart">
          %for x in range(1990, 2014):
          <option>{{x}}</option>
          %end
        </select>
      </div>


      <span>Til</span>

      <div class="selinp">
        <select id="inflMend" name="inflMend">
          %for x in range(1, 13):
          <option value="{{x}}">{{months[x-1]}}</option>
          %end
        </select>
      </div>

      <div class="selinp">
        <select id="inflYend" name="inflYend">
          %for x in range(1990, 2014):
          <option selected>{{x}}</option>
          %end
        </select>
      </div>

      <p>Nú nú, heldurðu að þú sért betur til þess fallin(n) að spá fyrir um verðbólguna? Gjörðu svo vel!</p>
      <div class="txtinp num hastype w30">
        <label for="inflation">Verðbólga</label>
        <input id="inflation" type="text" name="inflation" value="" />
        <span class="type"><span>%</span></span>
      </div>

    </fieldset>

    <hr />


    <fieldset class="loan">

      <h2>Lán</h2>
      <p>Segðu mér meira! Hvernig lán ertu með? Ertu með mörg lán?</p>

      <div class="row">
        <div class="txtinp req">
          <label for="lname">Nafn láns</label>
          <input id="lname" type="text" name="lname" value="" />
        </div>

        <div class="txtinp hastype num req">
          <label for="principle">Höfuðstóll</label>
          <input id="principle" type="text" name="principle" value="" />
          <span class="type"><span>kr.</span></span>
        </div>
      </div>

      <div class="row">
        <div class="txtinp num hashint w30 req">
          <label for="term">Lánstími</label>
          <input id="term" type="text" name="term" value="12" />
          <span class="hint"><span>í mánuðum</span></span>
        </div>

        <div class="txtinp num hashint w30 req">
          <label for="compoundInt">Vaxtatímabil</label>
          <input id="compoundInt" type="text" name="compoundInt" value="12" />
          <span class="hint"><span>í mánuðum</span></span>
        </div>

        <div class="txtinp num hasops w30">
          <label for="i_rate">Vextir</label>
          <span class="minus">-</span>
          <input id="i_rate" type="text" name="i_rate" value="1" />
          <span class="plus">+</span>
        </div>
      </div>


      <fieldset class="radioinp">
        <h4>Lán er verðtryggt?</h4>

        <ul>
          <li>
            <input id="verdtryggt" type="radio" name="indexedRadio" value="True" />
            <label for="verdtryggt">Já</label>
          </li>
          <li>
            <input id="overdtryggt" type="radio" name="indexedRadio" value="False" />
            <label for="overdtryggt">Nei</label>
          </li>
        </ul>
        <input type="hidden" id="radioDummy" name="indexed" value="" />
      </fieldset>

    </fieldset>

    <p class="center">Ertu með fleiri lán? <a class="addloan" href="/url">Já! Ég elska lán!</a></p>

    <input type="hidden" id="numloans" name="numloans" value="1" />

    <button type="submit">Og hvað? Hvað sparast mikið?</button>
  </form>


  <h2>Ertu rosa einfalt eintak og ert ekki með nein lán?</h2>
  <p>Settu inn það sparnaðarmarkmið, hvað þú getur sparað mikið á mánuði og við segjum þér hvað það tekur langan tíma að ná markmiðinu!</p>
  <form action="/sparnadur" method="POST">
    <h2>Ertu með sparnaðarmarkmið?</h2>
    <p>Hvað er það? Fyrir hverju æltaru að safna?</p>

    <div class="row">
      <div class="txtinp hastype num req">
        <label for="savingsgoal">Markmið:</label>
        <input id="savingsgoal" type="text" name="savingsgoal" value="" />
        <span class="type">kr.</span>
      </div>

      <div class="txtinp hastype hashint req">
        <label for="savingsAmount">Upphæð:</label>
        <input id="savingsAmount" type="text" name="savingsAmount" value="" />
        <span class="type">kr.</span>
        <span class="hint"><span>mánaðarlega</span></span>
      </div>

      <div class="txtinp num hastyp w30 req">
        <label for="userSavingsInterest">Vextir</label>
        <input id="userSavingsInterest" type="text" name="userSavingsInterest" value="" />
        <span class="type">%</span>
      </div>

    </div>

    <button type="submit">Hvað verð ég lengi að safna?</button>

  </form>

%include bottom