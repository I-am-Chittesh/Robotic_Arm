import paho.mqtt.client as mqtt
import json
import ssl
import time

# ==========================================
# 1. HiveMQ Cloud Credentials (FILL THESE IN)
# ==========================================
BROKER = "be9133bc31404063a69359a337c31cb3.s1.eu.hivemq.cloud"
PORT = 8883
USERNAME = "arm_admin"
PASSWORD = "Arm_admin123"
TOPIC = "project/arm/commands"

# ==========================================
# 2. MQTT Callbacks
# ==========================================
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("\n[SUCCESS] Connected to HiveMQ Cloud!")
    else:
        print(f"\n[ERROR] Connection failed with code {rc}")

def on_publish(client, userdata, mid, properties=None):
    print("[SENT] Payload successfully published to broker.\n")

# ==========================================
# 3. Setup Client & TLS (Security is required for HiveMQ)
# ==========================================
# Using MQTTv5 which is the latest standard
client = mqtt.Client(client_id="DigitalTwin_Laptop", protocol=mqtt.MQTTv5)
client.on_connect = on_connect
client.on_publish = on_publish

client.tls_set(tls_version=ssl.PROTOCOL_TLS_CLIENT)
client.username_pw_set(USERNAME, PASSWORD)

print("Connecting to Broker...")
client.connect(BROKER, PORT, keepalive=60)
client.loop_start() # Starts a background thread to handle network traffic

time.sleep(2) # Give it a second to establish the handshake

# ==========================================
# 4. The Interactive Simulation Loop
# ==========================================
print("==================================================")
print("DIGITAL TWIN: ARM CONTROLLER SIMULATION")
print("Format: Base,Shoulder,Elbow (e.g., 45,90,180)")
print("Type 'exit' to quit")
print("==================================================")

try:
    while True:
        user_input = input("Enter new arm angles -> ")
        
        if user_input.lower() == 'exit':
            break
            
        try:
            # Parse the input
            angles = user_input.split(',')
            b = int(angles[0].strip())
            s = int(angles[1].strip())
            e = int(angles[2].strip())
            
            # Create the JSON Payload
            payload = {
                "base": b,
                "shoulder": s,
                "elbow": e,
                "timestamp": time.time()
            }
            
            json_payload = json.dumps(payload)
            print(f"Preparing to send: {json_payload}")
            
            # Publish to HiveMQ
            client.publish(TOPIC, json_payload, qos=1)
            
        except Exception as e:
            print("ERRO: Invalid format. Please use Base,Shoulder,Elbow (e.g., 45,90,180)")

except KeyboardInterrupt:
    print("\nShutting down simulation...")
    print("\nDisconnected from HiveMQ Cloud.")

client.loop_stop()
client.disconnect()