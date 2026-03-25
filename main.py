import requests

# -----------------------------------------
# HIGH-RAIN & FLOOD-PRONE CITY LIST
# -----------------------------------------
cities = {
    "Auto Rain City (Recommended)": "Cherrapunji",
    "World's Wettest (India)": "Mawsynram",
    "Kerala Rain": "Kochi",
    "North East Rain": "Shillong",
    "Hill Rain": "Darjeeling",
    "Metro Rain": "Mumbai",
    "Coastal Flood City": "Chennai",
    "Eastern Flood City": "Kolkata",
    "Assam Flood City": "Guwahati",
    "Bangladesh Flood City": "Dhaka",
    "Indonesia Storm City": "Jakarta",
    "Philippines Flood City": "Manila",
    "Thailand Rain": "Bangkok",
    "UK Drizzle": "London",
    "USA Rain": "Seattle",
    "Your Custom Location": "CUSTOM"
}

# -----------------------------------------
# GET WEATHER + ALERTS
# -----------------------------------------
def get_weather(city):
    city_query = city.replace(" ", "+")
    URL = f"https://wttr.in/{city_query}?format=j1"

    try:
        data = requests.get(URL).json()

        # Current conditions
        current = data["current_condition"][0]
        desc = current["weatherDesc"][0]["value"]
        rainfall_mm = float(current.get("precipMM", 0))

        print(f"\n📍 Location: {city}")
        print(f"🌤 Current Weather: {desc}")
        print(f"🌧 Rainfall (mm): {rainfall_mm}")

        # ---------- RAIN ALERT ----------
        rain_keywords = ["rain", "drizzle", "thunder", "storm"]

        if any(k in desc.lower() for k in rain_keywords) or rainfall_mm > 1:
            print("\n⚠️ RAIN ALERT!")
            print("🌧 Rain expected soon. Farmers should avoid irrigation.")
        else:
            print("\n✅ No rain expected. Irrigation is safe.")

        # ---------- FLOOD ALERT ----------
        hourly = data["weather"][0]["hourly"]
        heavy_rain_hours = sum(
            1 for hour in hourly if float(hour["precipMM"]) > 10
        )

        if ("storm" in desc.lower() or "thunder" in desc.lower()
            or rainfall_mm > 20 or heavy_rain_hours >= 3):

            print("\n🚨 FLOOD WARNING!")
            print("⚡ Heavy rainfall / storm detected.")
            print("🌊 Flood risk possible in low-lying areas.")
        else:
            print("\n🟢 No flood risk detected.")

        print("\n-----------------------------------------")

    except Exception as e:
        print("❌ Error fetching weather:", e)

# -----------------------------------------
# USER MENU (NUMBERS + CITY NAME SUPPORTED)
# -----------------------------------------
def main():
    print("\n=========== WEATHER & FLOOD ALERT SYSTEM ===========")
    print("Choose a city by NUMBER or NAME, or press ENTER for Auto Rain City:\n")

    # Show numbered list
    for i, (label, city) in enumerate(cities.items(), start=1):
        print(f"{i}. {label} — {city}")

    user_input = input("\nEnter choice number or city name (or press ENTER): ").strip()

    # AUTO CITY
    if user_input == "":
        city = "Cherrapunji"
        print("\nUsing Auto Rain City: Cherrapunji")

    # USER ENTERED A CITY NAME
    elif not user_input.isdigit():
        city = user_input.title()  # Convert "london" → "London"

        # If not in our predefined list
        if city not in cities.values():
            print("\nUsing custom city:", city)

    # USER ENTERED A NUMBER
    else:
        num = int(user_input)
        selected_label = list(cities.keys())[num - 1]
        city = cities[selected_label]

        if city == "CUSTOM":
            city = input("Enter your custom location: ").strip()

    # FETCH WEATHER
    get_weather(city)

# Run program
main()

