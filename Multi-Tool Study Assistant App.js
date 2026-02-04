// =======================
// Unit Converters
// =======================

const lengthUnits = {
  m: 1, cm: 0.01, mm: 0.001, km: 1000,
  in: 0.0254, ft: 0.3048, yd: 0.9144, mi: 1609.34
};

const weightUnits = {
  kg: 1, g: 0.001, mg: 0.000001,
  lb: 0.453592, oz: 0.0283495, ton: 1000
};

const capacityUnits = {
  ml: 0.001, l: 1, kl: 1000,
  tsp: 0.00492892, tbsp: 0.0147868,
  cup: 0.24, pt: 0.473176,
  qt: 0.946353, gal: 3.78541
};

function convert(unitType) {
  const value = Number(document.getElementById("value").value);
  const from = document.getElementById("from").value;
  const to = document.getElementById("to").value;

  let units;
  if (unitType === "length") units = lengthUnits;
  if (unitType === "weight") units = weightUnits;
  if (unitType === "capacity") units = capacityUnits;

  const result = (value * units[from]) / units[to];
  document.getElementById("output").textContent =
    `${value} ${from} = ${result.toFixed(6)} ${to}`;
}

// =======================
// Calculator
// =======================

function calculate(op) {
  const a = Number(document.getElementById("num1").value);
  const b = Number(document.getElementById("num2").value);
  let result;

  if (op === "+") result = a + b;
  if (op === "-") result = a - b;
  if (op === "*") result = a * b;
  if (op === "/") result = b === 0 ? "Cannot divide by zero" : a / b;

  document.getElementById("calcResult").textContent = result;
}

// =======================
// To-Do List
// =======================

let tasks = [];

function addTask() {
  const task = document.getElementById("taskInput").value;
  if (task === "") return;

  tasks.push(task);
  document.getElementById("taskInput").value = "";
  renderTasks();
}

function renderTasks() {
  const list = document.getElementById("taskList");
  list.innerHTML = "";
  tasks.forEach((task, index) => {
    list.innerHTML += `<li>${task}
      <button onclick="removeTask(${index})">X</button></li>`;
  });
}

function removeTask(index) {
  tasks.splice(index, 1);
  renderTasks();
}

// =======================
// Timer
// =======================

function startTimer() {
  let seconds = Number(document.getElementById("seconds").value);

  const interval = setInterval(() => {
    if (seconds <= 0) {
      clearInterval(interval);
      document.getElementById("timer").textContent = "Time's up!";
      return;
    }
    document.getElementById("timer").textContent = seconds + "s";
    seconds--;
  }, 1000);
}
