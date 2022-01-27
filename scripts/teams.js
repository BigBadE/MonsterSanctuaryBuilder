let teams = [];

if(document.cookie !== "") {
    teams = JSON.parse(document.cookie);
}

let activeTeam = [];
let activeElement = null;

if (teams.length > 0) {
    activeTeam = teams[0];
}

let teams_element;
function addTeam() {
    activeTeam = [];
    teams_element.prepend(makeTeamElement(activeTeam));
    teams.push(activeTeam);
}

function loadTeams() {
    teams_element = document.getElementById("teams");
    for(let i = 0; i < teams.length; i++) {
        teams_element.prepend(makeTeamElement(teams[i]));
    }
}

function selectElement(element) {
    if(activeElement != null) {
        activeElement.id = activeElement.id.substr(0, activeElement.id.length - 9);
    }
    element.className += " selected";
    activeElement = element;
    activeTeam = teams[Array.from(element.parentNode.childNodes).indexOf(element)];
}

function makeTeamElement(team) {
    let element = document.getElementById("team-hidden").cloneNode();
    console.log(element + ", " + element.className)
    element.className = element.className.substr(0, element.className.length-7);
    element.onclick = () => selectElement(element);
    return element;
}