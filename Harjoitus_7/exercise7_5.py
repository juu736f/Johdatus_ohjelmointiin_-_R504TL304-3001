import requests
import json

url = "https://edu.frostbit.fi/api/weather/"
data = sorted(json.loads(requests.get(url).text), key=lambda x: x['wind'], reverse=True)
windByArea = {}
averages = {}

for item in data:
    area = item.get("area")
    wind = item.get("wind")
    if area is not None and wind is not None:
        windByArea.setdefault(area, []).append(wind)

for key, numbers in windByArea.items():
    total_sum = sum(numbers)
    count = len(numbers)
    if count > 0:  # Avoid division by zero if a list is empty
        average = total_sum / count
    else:
        average = 0  
    averages[key] = average
    
areas = list(averages.keys())

print(f"Täällä tuulee eniten: {data[0]["location"]}, {data[0]["wind"]} m/s")
print(f"Täällä tuulee vähiten: {data[-1]["location"]}, {data[-1]["wind"]} m/s")

for i in range(len(areas)):
    print(f"Keskimääräinen tuuli alueella {areas[i]}: {averages[areas[i]]:.1f} m/s")

