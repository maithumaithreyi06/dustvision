import joblib

model = joblib.load("model.pkl")

dust = float(input("Enter Dust Level: "))
temp = float(input("Enter Temperature: "))
humidity = float(input("Enter Humidity: "))

result = model.predict([[dust, temp, humidity]])

if result[0] == 1:
    print("⚠ Sandstorm Likely")
else:
    print("✅ Weather Normal")