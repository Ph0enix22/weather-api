const searchBtn = document.getElementById('searchBtn');
const cityInput = document.getElementById('cityInput');
const result = document.getElementById('result');
const error = document.getElementById('error');

searchBtn.addEventListener('click', getWeather);

async function getWeather() {
    const city = cityInput.value.trim();

    result.classList.add('hidden');
    error.classList.add('hidden');

    if (!city) {
        error.innerText = "Please enter a city name!";
        error.classList.remove('hidden');
        return;
    }

    try {
        const response = await fetch(`http://127.0.0.1:5000/weather?city=${city}`);
        const data = await response.json();

        if (!response.ok) {
            error.innerText = data.error;
            error.classList.remove('hidden');
            return;
        }

        result.innerHTML = `
            <strong> >> City:</strong> ${data.city} <br>
            <strong> >> Temperature:</strong> ${data.temperature}°C <br>
            <strong> >> Humidity:</strong> ${data.humidity}% <br>
            <strong> >> Condition:</strong> ${data.condition}
        `;
        result.classList.remove('hidden');

    } catch (err) {
        error.innerText = "Network error. Is backend running?";
        error.classList.remove('hidden');
    }
}