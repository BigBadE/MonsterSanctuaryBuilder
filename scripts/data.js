let monsterSkills;
let monsterShifts;
let monsterList;

getData('data/skills.json', response => {
    monsterSkills = JSON.parse(response)
})

getData('data/shifts.json', response => {
    monsterShifts = JSON.parse(response)
})

getData('data/monsters.json', response => {
    monsterList = JSON.parse(response)
})

function getData(path, dataHandler) {
    let xhr = new XMLHttpRequest();
    xhr.open("GET", './' + path);
    xhr.responseType = "blob"; //force the HTTP response, response-type header to be blob
    xhr.onload = function()
    {
        dataHandler(xhr.response);
    }
    xhr.send();
}