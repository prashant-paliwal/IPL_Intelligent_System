let score = 0;
let wickets = 0;
let balls = 0;

async function sendEvent() {

    const runs = Math.floor(Math.random() * 7);

    if (runs === 0 && Math.random() > 0.7) {
        wickets += 1;
    } else {
        score += runs;
    }

    balls += 1;

    const res = await fetch("/event", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            runs: runs,
            batsman: "Kohli",
            bowler: "Bumrah"
        })
    });

    const data = await res.json();

    document.getElementById("score").innerText =
        `${score}/${wickets}`;

    document.getElementById("over").innerText =
        `${(balls/6).toFixed(1)} overs`;

    document.getElementById("output").innerHTML = `
        <div class="card">
            <div class="title">🎙 Commentary</div>
            <div class="text">${data.commentary}</div>
        </div>

        <div class="card">
            <div class="title">📊 Analysis</div>
            <div class="text">${data.analysis}</div>
        </div>

        <div class="card">
            <div class="title">🔥 Hype</div>
            <div class="text hype">${data.hype}</div>
        </div>

        <div class="card">
            <div class="title">📈 Prediction</div>
            <div class="text prediction">
                Win: ${data.prediction.win_probability}<br>
                Next: ${data.prediction.next_ball}
            </div>
        </div>
    `;
}