document.getElementById("predictForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const payload = {
        gender: gender.value,
        race_ethnicity: race_ethnicity.value,
        parental_level_of_education: parental_level_of_education.value,
        lunch: lunch.value,
        test_preparation_course: test_preparation_course.value,
        reading_score: Number(reading_score.value),
        writing_score: Number(writing_score.value)
    };

    const result = document.getElementById("result");
    result.className = "result hidden";

    try {
        const res = await fetch("/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        const data = await res.json();

        if (!data.success) throw new Error(data.error);

        result.textContent = `Predicted Math Score: ${data.prediction}`;
        result.className = "result success";

    } catch (err) {
        result.textContent = "Prediction failed. Please verify inputs.";
        result.className = "result error";
    }

    result.classList.remove("hidden");
});
