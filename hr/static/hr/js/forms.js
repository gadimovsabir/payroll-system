"use strict";

let HTMLText = `<select>
  <option value="01">1</option>
  <option value="02">2</option>
  <option value="03">3</option>
  <option value="04">4</option>
  <option value="05">5</option>
  <option value="06">6</option>
  <option value="07">7</option>
  <option value="08">8</option>
  <option value="09">9</option>
  <option value="10">10</option>
  <option value="11">11</option>
  <option value="12">12</option>
  <option value="13">13</option>
  <option value="14">14</option>
  <option value="15">15</option>
  <option value="16">16</option>
  <option value="17">17</option>
  <option value="18">18</option>
  <option value="19">19</option>
  <option value="20">20</option>
  <option value="21">21</option>
  <option value="22">22</option>
  <option value="23">23</option>
  <option value="24">24</option>
  <option value="25">25</option>
  <option value="26">26</option>
  <option value="27">27</option>
  <option value="28">28</option>
  <option value="29">29</option>
  <option value="30">30</option>
  <option value="31">31</option>
</select>
<select>
  <option value="01">Yanvar</option>
  <option value="02">Fevral</option>
  <option value="03">Mart</option>
  <option value="04">Aprel</option>
  <option value="05">May</option>
  <option value="06">İyun</option>
  <option value="07">İyul</option>
  <option value="08">Avqust</option>
  <option value="09">Sentyabr</option>
  <option value="10">Oktyabr</option>
  <option value="11">Noyabr</option>
  <option value="12">Dekabr</option>
</select>
<select></select>`

let dateFields = document.querySelectorAll(".date-field");
let date = new Date();

for (let field of dateFields) {
  field.hidden = true;
  let parentField = field.parentElement;
  parentField.insertAdjacentHTML("afterbegin", HTMLText);
  let [selectDay, selectMonth, selectYear] = parentField.children;

  for (let year = 0; year < 100; year++) {
    let option = document.createElement("option");
    option.value = date.getFullYear() - year;
    option.textContent = date.getFullYear() - year;
    selectYear.append(option);
  }

  if (field.value) {
    selectDay.value = field.value.slice(0, 2);
    selectMonth.value = field.value.slice(3, 5);
    selectYear.value = field.value.slice(6);  
  } else {
    field.value = "1.1." + date.getFullYear();
  }

  parentField.onchange = function() {
    field.value = `${selectDay.value}.${selectMonth.value}.${selectYear.value}`;
  }
}
