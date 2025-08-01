from flask import Flask, request
import requests

app = Flask(__name__)

API_KEY = "6334d03cdf640172aed41e5faec45008"

@app.route("/get-weather", methods=["GET"])
def get_weather():
    city = request.args.get("city", default="Oisterwijk", type=str)
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ro"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        descriere = data['weather'][0]['description']
        temperatura = data['main']['temp']
        return {
            "oras": city,
            "temperatura": temperatura,
            "descriere": descriere
        }
    else:
        return {"error": "Nu am putut obține vremea"}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
