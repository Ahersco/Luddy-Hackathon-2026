async function submitScore() {
    const user = document.getElementById("user").value;
    const score = document.getElementById("score").value;

    await fetch(`/add?username=${user}&score=${score}`, {
        method: "POST"
    });

    loadLeaderboard();
}

async function loadLeaderboard() {
    const res = await fetch("/leaderboard");
    const data = await res.json();

    const list = document.getElementById("leaderboard");
    list.innerHTML = "";

    data.forEach(entry => {
        const li = document.createElement("li");
        li.textContent = `${entry.username}: ${entry.score}`;
        list.appendChild(li);
    });
}