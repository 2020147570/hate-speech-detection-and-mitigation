import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
from flask_cors import CORS
from hate_speech_mitigation.mitigate_hate_speech import mitigate_hate_speech


app = Flask(__name__)
CORS(app)


@app.route('/process', methods=['POST'])
def process_webpage():
    data = request.json
    url = data.get('url')

    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({'processed_divs': ''}), 400

    soup = BeautifulSoup(response.text, "html.parser")

    wrap_divs = soup.find_all("div", class_="wrap") # Everytime post divs
    processed_divs = []

    for div in wrap_divs:
        paragraphs = div.find_all("p", class_="large")
        
        for p in paragraphs: # For each text
            original_text = p.get_text(strip=True)
            transformed_text = mitigate_hate_speech(hate_speech=original_text) # Hate speech mitigation
            p.string = transformed_text

        processed_divs.append(str(div))

    return jsonify({'processed_divs': "\n\n".join(processed_divs)})


if __name__ == "__main__":
    app.run(debug=True)
