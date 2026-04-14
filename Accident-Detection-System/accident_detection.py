import random
import time

def detect_accident():
    # Simulate sensor data
    value = random.randint(0, 100)
    print(f"Sensor Value: {value}")
    
    if value > 90:
        return True
    return False

def send_alert():
    print("\n🚨 Accident Detected!")
    print("📍 Location: Latitude 17.3850, Longitude 78.4867")
    print("📞 Alert sent to emergency contact!")

print("🚗 System Running...\n")

while True:
    if detect_accident():
        send_alert()
        break
    time.sleep(2)