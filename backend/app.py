from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests
import strawberry
from strawberry.flask.views import GraphQLView
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)

load_dotenv()
API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@strawberry.type
class WeatherType:
    temperature: float
    humidity: int
    condition: str

@strawberry.type
class Query:
    @strawberry.field
    def weather(self, city: str) -> WeatherType:
        response = requests.get(BASE_URL, params={"q": city, "appid": API_KEY, "units": "metric"})
        data = response.json()
        return WeatherType(
            temperature=data["main"]["temp"],
            humidity=data["main"]["humidity"],
            condition=data["weather"][0]["description"]
        )

schema = strawberry.Schema(query=Query)

@app.route('/health', methods=['GET'])
def health_check():
    return {"status": "ok"}

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')

    if not city:
        return jsonify({"error": "City is required"}), 400
    
    response = requests.get(BASE_URL, params={"q": city, "appid": API_KEY, "units": "metric"})

    if response.status_code == 404:
        return jsonify({"error": "City not found"}), 404
    
    if response.status_code != 200:
        return jsonify({"error": "External API failure"}), 502
    
    data = response.json()

    return jsonify({
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "condition": data["weather"][0]["description"]
    })

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql_view', schema=schema))

if __name__ == '__main__':
    app.run(debug=True)