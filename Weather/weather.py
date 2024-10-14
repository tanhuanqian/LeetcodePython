from flask import Flask, jsonify

app = Flask(__name__)

# Hardcoded weather data
weather_data = {
    "city": "Kuala Lumpur",
    "temperature": 30,
    "condition": "Sunny",
    "humidity": 70
}

@app.route('/', methods=['GET'])
def get_weather():
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)
