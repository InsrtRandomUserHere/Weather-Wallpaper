import requests
import ctypes
import time

# Image path needs to be full path which is why we need this
path = "C:\\Users\\Username\\Path\\to\\images"
api_link = "https://api.openweathermap.org/data/2.5/YourOwnAPICall"


# Setting the wallpaper
def set_wallpaper(wallpaper_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 0)


# Path of all wallpapers, so we don't have to use a lot of if-statements
assigned_wallpaper = {
    "Thunderstorm": path + "thunderstorm.png",
    "Drizzle": path + "drizzle.png",
    "Rain": path + "raining.png",
    "Clouds": path + "clouds.png",
}

while True:
    data = requests.get(api_link).json()
    weather = data["weather"][0]["main"]

    try:
        set_wallpaper(assigned_wallpaper[weather])

        # If we don't have a wallpaper for a weather, we set it to this
    except KeyError:
        set_wallpaper(path + "unknown.jpg")

    # Run every 10 minutes
    time.sleep(60 * 10)
