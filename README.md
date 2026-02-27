# Weather API Project

A full-stack weather application built with Python (Flask) on the backend and HTML/CSS/JavaScript on the frontend.

## Project Overview
This project fetches live weather data from OpenWeatherMap and exposes it through a custom REST API and GraphQL endpoint. The frontend communicates with the backend to display weather information.

## REST Endpoints

### Health Check
```
GET /health
```
Response: 
```json
{ "status": "OK" }
```

### Get Weather
```
GET /weather?city=CityName
```
Response:
```json
{
  "city": "London",
  "temperature": 11.5,
  "humidity": 80,
  "condition": "overcast clouds"
}
```

## Error Responses
- 400 — Missing city parameter
- 404 — City not found
- 502 — External API failure

## GraphQL Endpoint
```
POST /graphql
```

Example query:
```graphql
query {
  weather(city: "London") {
    temperature
    humidity
    condition
  }
}
```

## Frontend
Simple HTML/CSS/JavaScript page that fetches weather data from the backend using the Fetch API.

## Frontend-Backend Flow
1. User types city name in the browser
2. JavaScript sends GET request to /weather
3. Flask backend calls OpenWeatherMap API
4. Backend returns clean JSON response
5. JavaScript displays data on the page