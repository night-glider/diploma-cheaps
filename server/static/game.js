let button = document.getElementById("get_map");
let map_id = document.getElementById("map_id");
let output = document.getElementById("output");
let refresh_rate = document.getElementById("refresh_interval")
let refresh_button = document.getElementById("refresh_button")
let ship_id = document.getElementById("ship_id")
let get_code_button = document.getElementById("get_code_button")
let send_code_button = document.getElementById("send_code_button")


function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function refresh_map() {
    let url = "maps?id=" + map_id.value;

    fetch(url)
    .then((response) => response.text())
    .then((result) => {
        result = result.replaceAll("\\n", "|<br>|")
        result = result.replaceAll("\"", "")
        output.innerHTML = result;
    })
}

async function infinite_refresh() {
    while (true) {
        refresh_map();
        await sleep( Number(refresh_rate.value) );
    }
}

function get_code() {
    let url = "ship_code?id=" + ship_id.value;
    fetch(url)
    .then((response) => response.text())
    .then((result) => {
        editor.setValue(result);
    })
}

function send_code() {
    let myHeaders = new Headers();
    myHeaders.append("Content-Type", "text/plain");

    let raw = editor.getValue();

    var requestOptions = {
      method: 'POST',
      headers: myHeaders,
      body: raw,
      redirect: 'follow'
    };

    let url = "ship_code?id=" + ship_id.value;

    fetch(url, requestOptions)
      .then(response => response.text())
      .then(result => {
        alert(result)
      })
}


button.onclick = function() {
	refresh_map();
}

refresh_button.onclick = function() {
    infinite_refresh();
}

get_code_button.onclick = function() {
    get_code();
}

send_code_button.onclick = function() {
    send_code()
}

