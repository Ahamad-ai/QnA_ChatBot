async function sendMessage() {
    const apiKey = document.getElementById("apiKey").value.trim();
    const model = document.getElementById("model").value;
    const temperature = parseFloat(document.getElementById("temperature").value);
    const maxTokens = parseInt(document.getElementById("maxTokens").value);
    const question = document.getElementById("userInput").value.trim();
    const responseDiv = document.getElementById("response");

    if (!question || !apiKey) {
        responseDiv.innerHTML = "<p style='color:red;'>Please enter your question or API key or both.</p>";
        return;
    }

    responseDiv.innerHTML = "<em>Thinking...</em>";

    try {
        const res = await fetch("https://api.openai.com/v1/chat/completions", {
            method: "POST",
            headers: {
                "Authorization": `Bearer ${apiKey}`,
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                model: model,
                messages: [
                    {
                        role: "system",
                        content: "You are a helpful assistant. Format your answers in Markdown with headings, bold text, and bullet points."
                    },
                    {
                        role: "user",
                        content: question
                    }
                ],
                temperature: temperature,
                max_tokens: maxTokens
            })
        });

        const data = await res.json();

        if (data.error) {
            responseDiv.innerHTML = `<p style="color:red;"><strong>Error:</strong> ${data.error.message}</p>`;
        } else {
            const markdown = data.choices?.[0]?.message?.content || "No response received.";
            responseDiv.innerHTML = marked.parse(markdown);
        }
    } catch (err) {
        responseDiv.innerHTML = `<p style="color:red;"><strong>Error:</strong> ${err.message}</p>`;
    }
}

function updateTemperature() {
    document.getElementById("tempValue").innerText = document.getElementById("temperature").value;
}

function updateMaxTokens() {
    document.getElementById("tokenValue").innerText = document.getElementById("maxTokens").value;
}

// Initialize values on page load
window.onload = function () {
    updateTemperature();
    updateMaxTokens();
};
