import requests
import tkinter as tk
from tkinter import messagebox, Canvas

# Function to fetch weather data
def get_weather(city):
    api_key = "6e8c73c5e20d675b5d7647b6f635830f"  # Replace with your OpenWeatherMap API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        
        if weather_data["cod"] != 200:
            raise ValueError(weather_data.get("message", "Error fetching weather data."))
        
        return {
            "city": weather_data["name"],
            "temperature": weather_data["main"]["temp"],
            "description": weather_data["weather"][0]["description"].capitalize(),
            "humidity": weather_data["main"]["humidity"],
            "wind_speed": weather_data["wind"]["speed"]
        }
    except Exception as e:
        messagebox.showerror("Error", f"Failed to get weather data: {e}")
        return None

# Function to handle button click
def fetch_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    weather = get_weather(city)
    if weather:
        result_label.config(
            text=(
                f"City: {weather['city']}\n"
                f"Temperature: {weather['temperature']}°C\n"
                f"Description: {weather['description']}\n"
                f"Humidity: {weather['humidity']}%\n"
                f"Wind Speed: {weather['wind_speed']} m/s"
            )
        )

# Create the main Tkinter window
app = tk.Tk()
app.title("Weather Forecast")
app.geometry("400x400")

# **Force background to light blue**
app.configure(bg="#87CEEB")  # Sky blue

# Create a canvas for clouds and place it at the top
canvas = Canvas(app, width=400, height=150, bg="#87CEEB", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Function to draw clouds
def draw_cloud(x, y):
    """Draws white clouds on the canvas"""
    canvas.create_oval(x, y, x + 50, y + 30, fill="white", outline="white")
    canvas.create_oval(x + 20, y - 10, x + 70, y + 20, fill="white", outline="white")
    canvas.create_oval(x - 20, y + 10, x + 30, y + 40, fill="white", outline="white")

# Add clouds at different positions
draw_cloud(50, 30)
draw_cloud(200, 50)
draw_cloud(300, 20)

# Input field for city name
city_label = tk.Label(app, text="Enter city name:", bg="#87CEEB", font=("Helvetica", 12, "bold"))
city_label.pack(pady=5)

city_entry = tk.Entry(app, width=30, font=("Helvetica", 12), bg="white", fg="black")
city_entry.pack(pady=5)

# Button to fetch weather
fetch_button = tk.Button(app, text="Get Weather", command=fetch_weather, font=("Helvetica", 12, "bold"), bg="#4682B4", fg="white")
fetch_button.pack(pady=10)

# Label to display weather results
result_label = tk.Label(app, text="", justify="left", bg="#87CEEB", font=("Helvetica", 12))
result_label.pack(pady=10)

# Run the Tkinter main loop
app.mainloop()
