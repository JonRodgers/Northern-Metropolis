"""
IoT Connector for Northern Metropolis
Handles real-time sensor data from IoT devices across the city.
"""

from typing import Dict, List, Optional, Any
from datetime import datetime
from .base import BaseConnector, ConnectorStatus


class IoTConnector(BaseConnector):
    """
    Connector for IoT sensor networks.
    Manages real-time data from environmental sensors, building sensors, and infrastructure monitors.
    """

    def __init__(self, connector_id: str = "iot_main", mqtt_broker: str = "localhost", mqtt_port: int = 1883):
        """Initialize IoT connector"""
        super().__init__(connector_id, "IoT")
        self.mqtt_broker = mqtt_broker
        self.mqtt_port = mqtt_port
        self.subscribed_topics: List[str] = []
        self.sensor_data_cache: Dict[str, Any] = {}
        self.mqtt_client = None

    def connect(self) -> bool:
        """Connect to MQTT broker"""
        self.connection_attempts += 1
        try:
            # In production, would use paho-mqtt library
            # import paho.mqtt.client as mqtt
            # self.mqtt_client = mqtt.Client()
            # self.mqtt_client.connect(self.mqtt_broker, self.mqtt_port, 60)
            
            self.set_status(ConnectorStatus.CONNECTED)
            return True
        except Exception as e:
            self.record_error(f"Failed to connect to MQTT broker: {str(e)}")
            return False

    def disconnect(self) -> bool:
        """Disconnect from MQTT broker"""
        try:
            if self.mqtt_client:
                # self.mqtt_client.disconnect()
                pass
            self.set_status(ConnectorStatus.DISCONNECTED)
            return True
        except Exception as e:
            self.record_error(f"Failed to disconnect: {str(e)}")
            return False

    def subscribe_to_topic(self, topic: str) -> bool:
        """Subscribe to MQTT topic"""
        try:
            if topic not in self.subscribed_topics:
                self.subscribed_topics.append(topic)
                # if self.mqtt_client:
                #     self.mqtt_client.subscribe(topic)
            return True
        except Exception as e:
            self.record_error(f"Failed to subscribe to topic {topic}: {str(e)}")
            return False

    def subscribe_to_sensor_topics(self) -> None:
        """Subscribe to all sensor data topics"""
        sensor_topics = [
            "sensors/environmental/air_quality",
            "sensors/environmental/water_quality",
            "sensors/environmental/climate",
            "sensors/environmental/noise",
            "sensors/buildings/energy",
            "sensors/buildings/occupancy",
            "sensors/buildings/hvac",
            "sensors/infrastructure/power_grid",
            "sensors/infrastructure/water_supply",
            "sensors/infrastructure/waste",
            "sensors/traffic/congestion",
            "sensors/traffic/vehicle_count",
        ]

        for topic in sensor_topics:
            self.subscribe_to_topic(topic)

    def send_data(self, data: Dict[str, Any]) -> bool:
        """Send data to IoT system"""
        try:
            # In production, would publish to MQTT topic
            # topic = data.get("topic", "data/output")
            # self.mqtt_client.publish(topic, json.dumps(data))
            
            self.data_points_sent += 1
            return True
        except Exception as e:
            self.record_error(f"Failed to send data: {str(e)}")
            return False

    def receive_data(self) -> Optional[Dict[str, Any]]:
        """Receive data from IoT sensors"""
        try:
            # In production, would receive from MQTT message queue
            # This is a placeholder implementation
            if self.sensor_data_cache:
                self.data_points_received += 1
                return self.sensor_data_cache.pop(next(iter(self.sensor_data_cache)))
            return None
        except Exception as e:
            self.record_error(f"Failed to receive data: {str(e)}")
            return None

    def process_sensor_data(self, sensor_id: str, sensor_type: str, value: float, unit: str) -> Dict:
        """Process incoming sensor data"""
        data = {
            "timestamp": datetime.utcnow().isoformat(),
            "sensor_id": sensor_id,
            "sensor_type": sensor_type,
            "value": value,
            "unit": unit,
        }

        # Cache the data
        self.sensor_data_cache[sensor_id] = data

        return data

    def get_sensor_status(self) -> Dict:
        """Get status of all connected sensors"""
        return {
            "connector_id": self.connector_id,
            "mqtt_broker": self.mqtt_broker,
            "mqtt_port": self.mqtt_port,
            "subscribed_topics": len(self.subscribed_topics),
            "topics": self.subscribed_topics,
            "cached_sensor_data": len(self.sensor_data_cache),
            "connection_health": self.get_connection_health(),
        }

    def simulate_sensor_data(self, zone_id: str) -> None:
        """Simulate sensor data for testing"""
        import random

        sensor_data = {
            "air_quality_index": random.uniform(30, 150),
            "temperature_c": random.uniform(15, 35),
            "humidity_percentage": random.uniform(30, 80),
            "pm25_ug_m3": random.uniform(5, 100),
            "noise_leq_db": random.uniform(40, 80),
            "water_quality_ph": random.uniform(6.5, 8.5),
            "dissolved_oxygen_mg_l": random.uniform(4, 10),
        }

        for sensor_type, value in sensor_data.items():
            sensor_id = f"{zone_id}_{sensor_type}"
            self.process_sensor_data(sensor_id, sensor_type, value, self._get_unit(sensor_type))

    @staticmethod
    def _get_unit(sensor_type: str) -> str:
        """Get unit for sensor type"""
        units = {
            "air_quality_index": "AQI",
            "temperature_c": "°C",
            "humidity_percentage": "%",
            "pm25_ug_m3": "µg/m³",
            "noise_leq_db": "dB",
            "water_quality_ph": "pH",
            "dissolved_oxygen_mg_l": "mg/L",
        }
        return units.get(sensor_type, "")

    def __repr__(self) -> str:
        return (
            f"IoTConnector(id={self.connector_id}, "
            f"broker={self.mqtt_broker}:{self.mqtt_port}, "
            f"topics={len(self.subscribed_topics)})"
        )
