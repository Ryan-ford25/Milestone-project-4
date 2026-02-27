document.addEventListener("DOMContentLoaded", function() {

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            document.cookie.split(';').forEach(cookie => {
                cookie = cookie.trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.slice(name.length + 1));
                }
            });
        }
        return cookieValue;
    }

    const csrftoken = getCookie('csrftoken');

    document.querySelectorAll(".quiz-form").forEach(form => {
        form.addEventListener("submit", function(e) {
            e.preventDefault();

            const selected = form.querySelector("input[name='answer']:checked");
            if (!selected) return;

            fetch(form.dataset.url, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrftoken
                },
                body: new URLSearchParams({ answer: selected.value })
            })
            .then(response => response.json())
            .then(data => {
                const correctAnswer = data.correct_answer;
                const allOptions = form.querySelectorAll(".form-check");

                allOptions.forEach(option => {
                    const input = option.querySelector("input");
                    option.classList.remove("bg-success", "bg-danger", "text-white");

                    // highlight correct
                    if (input.value === correctAnswer) {
                        option.classList.add("bg-success", "text-white");
                    }

                    // highlight wrong selection
                    if (input.checked && !data.correct) {
                        option.classList.add("bg-danger", "text-white");
                    }

                    input.disabled = true; // prevent changing answer
                });

                fetch('/user/points-json/')
                    .then(response => response.json())
                    .then(stats => {
                        document.querySelectorAll("#points-today").forEach(el => el.innerText = stats.points_today);
                        document.querySelectorAll("#points-week").forEach(el => el.innerText = stats.points_week);
                        document.querySelectorAll("#points-month").forEach(el => el.innerText = stats.points_month);
                        document.querySelectorAll("#accuracy").forEach(el => el.innerText = stats.accuracy);
                    });
            });
        });
    });

});
