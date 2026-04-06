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

            const submitBtn = form.querySelector("button[type='submit']");

            //changed text for button after submitting an answer
            submitBtn.disabled = true;
            submitBtn.innerText = "Submitting..."

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

                //Daily limit check
                if (data.limit_reached) {
                    const modal = new bootstrap.Modal(document.getElementById("attemptLimitModal"));
                    modal.show();
                    return;
                }

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
                
                const questionId = form.dataset.questionId;

                const questionButton = document.querySelector(
                    `.solve-btn[data-question-id="${questionId}"]`
                );

                if (questionButton) {
                    // disable button
                    questionButton.disabled = true;

                    // remove modal trigger
                    questionButton.removeAttribute("data-bs-toggle");
                    questionButton.removeAttribute("data-bs-target");

                    // New button text
                    questionButton.innerHTML = '<i class="fa-solid fa-check"></i> Answered';

                }

                // close modal after 1s
                setTimeout(() => {
                    const modalElement = form.closest(".modal");
                    const modalInstance = bootstrap.Modal.getInstance(modalElement);
                    modalInstance.hide();
                }, 1000);

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
