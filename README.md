# Project-openwheatherapi_with_container
# Weather Forecast Checker

The **Weather Forecast Checker** is a containerized web application designed to fetch and display real-time weather information for user-specified locations. It is built using modern web technologies and showcases a microservices architecture powered by **Docker**.

---

## Features

- **Real-Time Weather Data**:
  Fetches live weather information (e.g., temperature, conditions) from the [OpenWeatherMap API](https://openweathermap.org/).
  
- **User-Friendly Interface**:
  A simple HTML interface allows users to input city names or ZIP codes and view weather data dynamically.

- **Containerized Architecture**:
  Backend (FastAPI) and frontend (Nginx) services are containerized for scalability, portability, and ease of deployment.

- **Error Handling**:
  Robust mechanisms for managing invalid user inputs, API errors, and connectivity issues.

- **Extensible Design**:
  Modular architecture allows for future enhancements like caching, user authentication, or additional data layers.

---

## Architecture

### Components

1. **Frontend**:
   - Serves the static HTML file for user interaction.
   - Routes API requests to the backend using **Nginx** as a reverse proxy.

2. **Backend**:
   - Built with **FastAPI**, it processes location inputs and fetches weather data from the OpenWeatherMap API.
   - Validates inputs and handles errors gracefully.

3. **Docker Networking**:
   - Frontend and backend containers communicate securely via a custom Docker network.

### Workflow

1. User enters a location in the web interface.
2. Nginx forwards the request to the FastAPI backend.
3. FastAPI fetches the weather data from OpenWeatherMap.
4. The response flows back through Nginx to the frontend, displaying the weather data to the user.

---

## Prerequisites

- **Docker** and **Docker Compose** installed on your system.
- An API key from [OpenWeatherMap](https://openweathermap.org/).

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/weather-forecast-checker.git
   cd weather-forecast-checker
