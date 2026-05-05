let interval = null;
let isRunning = false;

async function playBall() {
    try {
        const res = await fetch("/event", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({})
        });

        const data = await res.json();

        // --- STATE (from backend) ---
        document.getElementById("score").innerText =
            `${data.state.score}/${data.state.wickets}`;

        document.getElementById("over").innerText =
            `${data.state.over} overs`;

        // --- METRICS ---
        document.getElementById("rr").innerText =
            data.features?.run_rate?.toFixed(2) || "0.00";

        document.getElementById("pressure").innerText =
            data.features?.pressure || "-";

        document.getElementById("win").innerText =
            data.prediction?.win_probability || "-";

        // --- ANIMATION (fade) ---
        const commentaryEl = document.getElementById("commentary");
        commentaryEl.style.opacity = 0;

        setTimeout(() => {
            commentaryEl.innerText = data.commentary;
            commentaryEl.style.opacity = 1;
        }, 200);

        document.getElementById("analysis").innerText =
            data.analysis || "-";

        document.getElementById("hype").innerText =
            data.hype || "-";

        document.getElementById("prediction").innerText =
            `Next: ${data.prediction?.next_ball || "-"}`;

    } catch (err) {
        console.error(err);
    }
}

function startMatch() {
    if (isRunning) return;

    isRunning = true;

    interval = setInterval(() => {
        playBall();
    }, 1500); // every 1.5 sec
}

function stopMatch() {
    clearInterval(interval);
    isRunning = false;
}