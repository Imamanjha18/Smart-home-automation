import paho.mqtt.client as mqtt
import json

# MQTT client instance
client = None

# Callback when connecting to the MQTT broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker successfully")
        # Subscribe to all device topics
        client.subscribe("home/#")
    else:
        print(f"Failed to connect to MQTT broker with result code {rc}")

# Callback when receiving a message from the broker
def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")
    
    # In a real implementation, you would update the database here
    # For now, we'll just print the message

# Initialize MQTT client
def connect_mqtt(broker_url, broker_port):
    global client
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    
    try:
        client.connect(broker_url, broker_port, 60)
        client.loop_start()
        print("MQTT client connected and loop started")
        return True
    except Exception as e:
        print(f"Failed to connect to MQTT broker: {e}")
        return False

def publish_message(topic, message):
    if client and client.is_connected():
        client.publish(topic, message)
        print(f"Published message to {topic}: {message}")
        return True
    else:
        print(f"Simulating MQTT publish to {topic}: {message}")
        # In a real scenario, you would update the device state through MQTT
        # For simulation, we'll just print the message
        return False