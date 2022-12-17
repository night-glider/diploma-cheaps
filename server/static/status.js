const tick_data = document.getElementById("tick_info")

var requestOptions = {
  method: 'GET',
  redirect: 'follow'
};

function success_load(result) {
  tick_data.innerHTML = `
  Среднее время тика: ${result["avg_tick_time"].toFixed(2)} мс<br>
  Минимальное время тика: ${result["min_tick_time"].toFixed(2)} мс<br>
  Максимальное время тика: ${result["max_tick_time"].toFixed(2)} мс<br>
  Всего прошло тиков: ${result["ticks_elapsed"]} тиков<br>
  `
  console.log(result)
}

function failed_to_load() {
  tick_data.innerHTML = "Не удалось подключиться к серверу"
}

fetch("http://127.0.0.1:5000/tick_data", requestOptions)
  .then(response => response.json())
  .then(result => success_load(result))
  .catch(error => failed_to_load());