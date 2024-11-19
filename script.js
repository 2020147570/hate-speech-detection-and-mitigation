document.getElementById("process-button").addEventListener("click", async () => {
    const url = document.getElementById("url-input").value.trim();
    const resultDiv = document.getElementById("processed-divs");

    resultDiv.textContent = "로딩 중 . . .";

    if (!url.startsWith("https://everytime.kr/")) {
        resultDiv.textContent = "[404 에러]: 유효한 에브리타임 게시글 주소를 입력하세요.";
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:3000/index.html", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ url }),
        });

        if (!response.ok) {
            if (response.status === 404) {
                resultDiv.textContent = `[${response.status} 에러]: 유효한 에브리타임 게시글 주소를 입력하세요.`;
            } else {
                resultDiv.textContent = `[${response.status} 에러]: ${response.statusText}`;
            }
            return;
        }

        const data = await response.json();
        resultDiv.textContent = data.processed_divs;
    } catch (error) {
        resultDiv.textContent = `[에러]: ${error}`;
    }
});
