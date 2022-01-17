let teams = []

if(document.cookie !== "") {
    teams = JSON.parse(document.cookie)
}

let activeTeam = []
let activeElement = null

if (teams.length > 0) {
    activeTeam = teams[0]
}

let teams_element;
function addTeam() {
    activeTeam = []
    teams_element.appendChild(makeTeamElement(activeTeam))
    teams.add(activeTeam)
}

function loadTeams() {
    teams_element = document.getElementById("teams");
    for(let i = 0; i < teams.length; i++) {
        teams.appendChild(makeTeamElement(teams[i]));
    }
}

function selectElement(element) {
    activeElement.id.substr(activeElement.id.length-9)
    element.class += " selected"
    activeElement = element
    activeTeam = teams[Array.from(element.parentNode.childNodes).indexOf(element)]
}

function makeTeamElement(team) {
    let element = document.getElementById("team-hidden").cloneNode()
    element.class = element.class.substr(element.class.length-7)
    element.onclick = () => selectElement(element)
    return element;
}