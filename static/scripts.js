function updateTeamOptions() {
    const sport = document.getElementById("sport").value;
    const teamSelectWrapper = document.getElementById("teamSelectWrapper");
    const teamSelect = document.getElementById("teamSelect");
    const standingsDiv = document.getElementById("standings");
    teamSelect.innerHTML = ""; // Clear existing options
    standingsDiv.innerHTML = ""; // Clear previous standings

    if (sport === "Football") {
        const teams = ["", "Arizona Cardinals", "Atlanta Falcons", "Baltimore Ravens", "Buffalo Bills", "Carolina Panthers", "Chicago Bears", "Cincinnati Bengals", "Cleveland Browns", "Dallas Cowboys", "Denver Broncos", "Detroit Lions", "Green Bay Packers", "Houston Texans", "Indianapolis Colts", "Jacksonville Jaguars", "Kansas City Chiefs", "Las Vegas Raiders", "Los Angeles Chargers", "Los Angeles Rams", "Miami Dolphins", "Minnesota Vikings", "New England Patriots", "New Orleans Saints", "New York Giants", "New York Jets", "Philadelphia Eagles", "Pittsburgh Steelers", "San Francisco 49ers", "Seattle Seahawks", "Tampa Bay Buccaneers", "Tennessee Titans", "Washington Commanders"];
        
        teams.forEach(team => {
            const option = document.createElement("option");
            option.value = team.toLowerCase().replace(/ /g, "-");
            option.textContent = team;
            teamSelect.appendChild(option);
        });
        teamSelectWrapper.style.display = "block"; // Show the team selection menu
    } else if (sport === "Basketball") {
        const teams = [" ", "Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets",
                        "Chicago Bulls", "Cleveland Cavaliers", "Dallas Mavericks", "Denver Nuggets",
                        "Detroit Pistons", "Golden State Warriors", "Houston Rockets", "Indiana Pacers",
                        "Los Angeles Clippers", "Los Angeles Lakers", "Memphis Grizzlies", "Miami Heat",
                        "Milwaukee Bucks", "Minnesota Timberwolves", "New Orleans Pelicans", "New York Knicks",
                        "Oklahoma City Thunder", "Orlando Magic", "Philadelphia 76ers", "Phoenix Suns",
                        "Portland Trail Blazers", "Sacramento Kings", "San Antonio Spurs", "Toronto Raptors",
                        "Utah Jazz", "Washington Wizards"];
        teams.forEach(team => {
            const option = document.createElement("option");
            option.value = team.toLowerCase().replace(/ /g, "-");
            option.textContent = team;
            teamSelect.appendChild(option);
        });
        teamSelectWrapper.style.display = "block"; // Show the team selection menu
    } else {
        teamSelectWrapper.style.display = "none"; // Hide the team selection menu if not football
    }
}

function addButton() {
    const submitButton = document.getElementById("submitButton");
    if (!submitButton) {
        const button = document.createElement("button");
        button.id = "submitButton";
        button.textContent = "Submit";
        button.type = "button"; // Prevent form submission on click
        button.onclick = getStandings; // Trigger getStandings function
        document.getElementById("teamSelectWrapper").appendChild(button); // Append button to the wrapper
    }
}

function getStandings(event) {
    event.preventDefault(); // Prevent form from submitting traditionally

    const teamSelected = document.getElementById('teamSelect').value;
    const sportSelected = document.getElementById('sport').value;

    // Ensure the team and sport are selected
    if (!teamSelected || !sportSelected) {
    alert("Please provide both team and sport.");
    return;
    }

    const team = teamSelected;  
    const sport = sportSelected; 

    // Build the request URL
    const url = `http://localhost:5000/getStandings?team=${team}&sport=${sport}`;

    // Fetch data from the Flask backend
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Server error: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            if (data.error) {
                document.getElementById('standings').innerHTML = `<p>Error: ${data.error}</p>`;
            } else {
                // If data is available, display player names (or whatever is relevant)
                document.getElementById('standings').innerHTML = `
                    <h2>Roster</h2>
                    <ul>
                        ${data.athletes ? data.athletes.map(player => `<li>${player.displayName}</li>`).join("") : '<li>No players found</li>'}
                    </ul>
                `;
            }
        })
        .catch(error => {
            console.error("Error fetching data:", error);
            document.getElementById('standings').innerHTML = '<p>Error fetching data from server.</p>';
        });
        }



function displayData(rosterData, scheduleData) {
    const standingsDiv = document.getElementById("standings");

    // Roster Display
    const rosterHTML = rosterData.athletes.map(player => `
        <li>${player.fullName} (${player.position.displayName})</li>
    `).join("");

    // Schedule Display
    const scheduleHTML = scheduleData.events.map(event => `
        <li>${event.name} on ${new Date(event.date).toLocaleDateString()}</li>
    `).join("");

    standingsDiv.innerHTML = `
        <h3>Roster</h3>
        <ul>${rosterHTML}</ul>
        <h3>Schedule</h3>
        <ul>${scheduleHTML}</ul>
    `;
}