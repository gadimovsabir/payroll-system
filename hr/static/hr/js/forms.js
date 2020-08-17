"use strict";

const SELECT_FIELDS = `<select>
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
<select></select>`;

const MONTH_NAMES = [
  "Yanvar",
  "Fevral",
  "Mart",
  "Aprel",
  "May",
  "İyun",
  "İyul",
  "Avqust",
  "Sentyabr",
  "Oktyabr",
  "Noyabr",
  "Dekabr"
];

const TABLE_HEAD = `<tr>
  <th>BE</th>
  <th>ÇA</th>
  <th>Ç</th>
  <th>CA</th>
  <th>C</th>
  <th>Ş</th>
  <th>B</th>
</tr>`;

const dateFields = document.querySelectorAll(".date-field");
const calendarFields = document.querySelectorAll(".calendar-field");
let today = new Date();
let openedCalendar;

for (let field of dateFields) {
  field.hidden = true;
  let parentField = field.parentElement;
  parentField.insertAdjacentHTML("afterbegin", SELECT_FIELDS);
  let [dayField, monthField, yearField] = parentField.children;

  for (let year = 0; year < 100; year++) {
    let option = document.createElement("option");
    option.value = today.getFullYear() - year;
    option.textContent = today.getFullYear() - year;
    yearField.append(option);
  }

  if (field.value) {
    dayField.value = field.value.slice(0, 2);
    monthField.value = field.value.slice(3, 5);
    yearField.value = field.value.slice(6);  
  } else {
    field.value = "1.1." + today.getFullYear();
  }

  parentField.onchange = function() {
    field.value = `${dayField.value}.${monthField.value}.${yearField.value}`;
  }
}

for (let field of calendarFields) {
  field.addEventListener("click", openCalendar);
}


function openCalendar(event) {
  if (openedCalendar) {
    openedCalendar.container.remove();
    openedCalendar.field.addEventListener("click", openCalendar);
  }

  let calendarContainer = document.createElement("div");
  let targetCoordinates = event.target.getBoundingClientRect();
  calendarContainer.style.left = targetCoordinates.x + "px";
  calendarContainer.style.top = targetCoordinates.bottom + window.pageYOffset + "px";
  calendarContainer.className = "calendar-container";
  event.target.parentElement.append(calendarContainer);
  openedCalendar = {
    container: calendarContainer,
    field: event.target
  };

  calendarContainer.innerHTML = `
    <div class="row calendar-head">
      <div onclick="createCalendar(-1, arguments[0])">
        <img class="arrows" src="/static/hr/img/left-arrow-icon.svg">
      </div>
      <div id="selected-month"></div>
      <div onclick="createCalendar(1, arguments[0])">
        <img class="arrows" src="/static/hr/img/right-arrow-icon.svg">
      </div>
    </div>
    <table class="calendar-table"></table>`;
    
  calendarContainer.onclick = setDate;
  event.target.removeEventListener("click", openCalendar);
  createCalendar(0, event);
}


function createCalendar(n, event) {
  let selectedMonth = document.querySelector("#selected-month");
  let date;

  if (selectedMonth.textContent) {
    let index = selectedMonth.textContent.indexOf(" ");
    date = new Date(
      selectedMonth.textContent.slice(index + 1),
      MONTH_NAMES.indexOf(selectedMonth.textContent.slice(0, index)) + n
    ); 
  } else {
    today = new Date();
    date = new Date(today.getFullYear(), today.getMonth());  
  }

  let month = date.getMonth();
  let calendarRows = "<tr>";
  selectedMonth.textContent = MONTH_NAMES[month] + " " + date.getFullYear();

  for (let i = 0; i < getDay(date); i++) {
    calendarRows += '<td></td>';
  }

  while (date.getMonth() == month) {
    calendarRows += "<td>" + date.getDate() + '</td>';

    if (getDay(date) % 7 == 6) {
      calendarRows += '</tr><tr>';
    }

    date.setDate(date.getDate() + 1);
  }

  if (getDay(date) != 0) {
    for (let i = getDay(date); i < 7; i++) {
      calendarRows += '<td></td>';
    }
  }

  calendarRows += '</tr>';
  let calendarTable = document.querySelector(".calendar-table"); 
  calendarTable.innerHTML = TABLE_HEAD + calendarRows;
  event.stopPropagation();
};


function setDate(event) {
  if (event.target.nodeName != "TD" || !event.target.textContent) {
    event.stopPropagation();
    return;
  }
  
  let selectedMonth = document.querySelector("#selected-month");
  let index = selectedMonth.textContent.indexOf(" ");
  let monthNumber = MONTH_NAMES.indexOf(selectedMonth.textContent.slice(0, index)) + 1;
  let year = selectedMonth.textContent.slice(index + 1); 
  openedCalendar.field.value = `${event.target.textContent}.${monthNumber}.${year}`;
  openedCalendar.container.remove();
  openedCalendar.field.addEventListener("click", openCalendar);
  openedCalendar = null;
};


function getDay(date) {
  let day = date.getDay();
  return (day == 0) ? 6 : day - 1;
}


document.addEventListener("click", function() {
  if (openedCalendar) {
    openedCalendar.container.remove();
    openedCalendar.field.addEventListener("click", openCalendar);
  }
});