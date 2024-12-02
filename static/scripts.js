function updateTeamOptions() {
    const sport = document.getElementById("sport").value;
    const teamSelectWrapper = document.getElementById("teamSelectWrapper");
    const teamSelect = document.getElementById("teamSelect");
    const standingsDiv = document.getElementById("standings");

    // Clear existing options and standings
    teamSelect.innerHTML = ""; 
    standingsDiv.innerHTML = "";

    if (sport) {
        const teamsBySport = {
            Football: [
                "Arizona Cardinals", "Atlanta Falcons", "Baltimore Ravens", "Buffalo Bills",
                "Carolina Panthers", "Chicago Bears", "Cincinnati Bengals", "Cleveland Browns",
                "Dallas Cowboys", "Denver Broncos", "Detroit Lions", "Green Bay Packers",
                "Houston Texans", "Indianapolis Colts", "Jacksonville Jaguars", "Kansas City Chiefs",
                "Las Vegas Raiders", "Los Angeles Chargers", "Los Angeles Rams", "Miami Dolphins",
                "Minnesota Vikings", "New England Patriots", "New Orleans Saints", "New York Giants",
                "New York Jets", "Philadelphia Eagles", "Pittsburgh Steelers", "San Francisco 49ers",
                "Seattle Seahawks", "Tampa Bay Buccaneers", "Tennessee Titans", "Washington Commanders"
            ],
            Basketball: [
                "Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets", "Chicago Bulls",
                "Cleveland Cavaliers", "Dallas Mavericks", "Denver Nuggets", "Detroit Pistons",
                "Golden State Warriors", "Houston Rockets", "Indiana Pacers", "Los Angeles Clippers",
                "Los Angeles Lakers", "Memphis Grizzlies", "Miami Heat", "Milwaukee Bucks",
                "Minnesota Timberwolves", "New Orleans Pelicans", "New York Knicks", "Oklahoma City Thunder",
                "Orlando Magic", "Philadelphia 76ers", "Phoenix Suns", "Portland Trail Blazers",
                "Sacramento Kings", "San Antonio Spurs", "Toronto Raptors", "Utah Jazz", "Washington Wizards"
            ]
        };

        const teams = teamsBySport[sport] || [];
        const placeholder = document.createElement("option");
        placeholder.value = "";
        placeholder.textContent = "Select a team";
        teamSelect.appendChild(placeholder);

        teams.forEach(team => {
            const option = document.createElement("option");
            option.value = team.toLowerCase().replace(/ /g, "-");
            option.textContent = team;
            teamSelect.appendChild(option);
        });

        teamSelectWrapper.style.display = "block";
    } else {
        teamSelectWrapper.style.display = "none";
    }
}

function addButton() {
    const teamSelectWrapper = document.getElementById("teamSelectWrapper");
    const submitButton = document.getElementById("submitButton");

    if (!submitButton) {
        const button = document.createElement("button");
        button.id = "submitButton";
        button.textContent = "Submit";
        button.type = "button";
        button.onclick = getStandings;
        teamSelectWrapper.appendChild(button);
    }
}

function getStandings(event) {
    if (event) event.preventDefault();

    const teamSelected = document.getElementById('teamSelect');
    const sportSelected = document.getElementById('sport');

    if (!teamSelected.value || !sportSelected.value) {
        alert("Please provide both team and sport.");
        return;
    }

    const team = teamSelected.value;
    const sport = sportSelected.value;

    fetch(`/getStandings?team=${team}&sport=${sport}`)
        .then(response => response.json())
        .then(data => {
            const standingsDiv = document.getElementById('standings');

            if (data.error) {
                standingsDiv.innerHTML = `<p>Error: ${data.error}</p>`;
            } else {
                const { name, record, position } = data.team;
                standingsDiv.innerHTML = `
                    <p><strong>Team:</strong> ${name}</p>
                    <p><strong>Record:</strong> ${record.wins} Wins, ${record.losses} Losses</p>
                    <p><strong>Position:</strong> ${position}</p>
                `;
            }
        })
        .catch(error => {
            console.error("Error fetching data:", error);
            document.getElementById('standings').innerHTML = '<p>Error fetching data from server.</p>';
        });
}
