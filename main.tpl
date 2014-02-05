%include header
<!--form action="/spara" method="POST">

  <h3>Settu þér sparnaðarmarkmið</h3>

    <div class="textinput">
      <label for="amount">Upphæð:</label>
      <input id="amount" type="text" name="amount" value="" />
    </div>

    <div class="fi_txt">
      <label for="monthlyAmount">Upphæð mánaðarlega:</label>
      <input id="monthlyAmount" type="text" name="monthlyAmount" value="" />
    </div>

    <button type="submit">Reikna</button>

</form-->

<form action="/lan" method="POST">

  <div class="fi_txt">
    <label for="monthlyAmount">Mánaðarlega aukatekjur:</label>
    <input id="monthlyAmount" type="text" name="monthlyAmount" value="" />
  </div>

  <fieldset class="period">
    <h3>Tímabil:</h3>

    <div class="fi_sel">
      <label for="periodYears">Ár:</label>
      <select id="periodYears" name="periodYears">
        %for x in range(0, 41):
          <option>{{x}}</option>
        %end
      </select>
    </div>

    <div class="fi_sel">
      <label for="periodMonths">Mánuðir:</label>
      <select id="periodMonths" name="periodMonths">
        %for x in range(0, 13):
          <option>{{x}}</option>
        %end
      </select>
    </div>

  </fieldset>

  <fieldset class="inflation">
    <h3>Verðbólgutímabil:</h3>

    <div class="row">
      <span>frá</span>
    </div>

    <div class="fi_sel">
      <label for="inflYstart">Ár:</label>
      <select id="inflYstart" name="inflYstart">
        %for x in range(1990, 2014):
        <option>{{x}}</option>
        %end
      </select>
    </div>

    <div class="fi_sel">
      <label for="inflMstart">Mán:</label>
      <select id="inflMstart" name="inflMstart">
        %for x in range(1, 13):
        <option>{{x}}</option>
        %end
      </select>
    </div>

    <span>til</span>

    <div class="fi_sel">
      <label for="inflYend">Ár:</label>
      <select id="inflYend" name="inflYend">
        %for x in range(1990, 2014):
        <option selected>{{x}}</option>
        %end
      </select>
    </div>

    <div class="fi_sel">
      <label for="inflMend">Mán:</label>
      <select id="inflMend" name="inflMend">
        %for x in range(1, 13):
        <option>{{x}}</option>
        %end
      </select>
    </div>

  </fieldset>



  <fieldset class="loan">

    <h3>Lán</h3>

    <div class="fi_txt">
      <label for="lname">Nafn láns:</label>
      <input id="lname" type="text" name="lname" value="" />
    </div>

    <!-- ekki viss hvort við noum þetta -->
    <!--div class="textinput">
      <label for="amount">Eftirstöðvar láns:</label>
      <input id="amount" type="text" name="amount" value="" />
    </div-->

    <div class="textinput numinput">
      <label for="i_rate">Vextir:</label>
      <input id="i_rate" type="tel" name="i_rate" min="0" />
    </div>

    <div class="textinput numinput hashint">
      <label for="term">Lánstími:</label>
      <input id="term" type="tel" name="term" min="0" />
      <span class="hint">í mánuðum</span>
    </div>

    <div class="fi_txt">
      <label for="principle">Höfuðstóll:</label>
      <input id="principle" type="text" name="principle" value="" />
    </div>

    <div class="fi_txt">
      <label for="compoundInt">Vaxtatímabil:</label>
      <input id="compoundInt" type="text" name="compoundInt" value="" />
    </div>

    <fieldset class="fi_rdo">
      <h4>Lán er verðtryggt?</h4>
      <ul>
        <li>
          <input id="verdtryggt" type="radio" name="indexed" value="1" />
          <label for="verdtryggt">Já</label>
        </li>
        <li>
          <input id="overdtryggt" type="radio" name="indexed" value="0" />
          <label for="overdtryggt">Nei</label>
        </li>
      </ul>
    </fieldset>

  </fieldset>

  <a class="addloan" href="/url">Ertu með fleiri lán?</a>

  <input type="hidden" id="numloans" name="numloans" value="1" />

  <button type="submit">Reikna</button>
</form>

%include bottom