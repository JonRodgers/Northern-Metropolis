"""
Integration Example
Demonstrates integration with Tandem, Unreal, and IoT systems.
"""

from northern_metropolis_osiris.core import NorthernMetropolis, CityConfig, create_northern_metropolis_zones
from northern_metropolis_osiris.connectors import (
    IoTConnector,
    TandemConnector,
    UnrealConnector,
    EnvironmentalDataConnector,
)


def main():
    """Main integration example"""
    
    # Initialize city
    city_config = CityConfig()
    city = NorthernMetropolis(city_config)
    
    # Create zones
    zones = create_northern_metropolis_zones()
    for zone_id, zone in zones.items():
        city.add_zone(zone)
    
    print("=" * 60)
    print("Northern Metropolis OSIRIS - Integration Example")
    print("=" * 60)
    
    # Initialize IoT Connector
    print("\n1. IoT Connector Setup")
    print("-" * 60)
    iot_connector = IoTConnector(mqtt_broker="mqtt.northern-metropolis.local")
    
    if iot_connector.connect():
        print(f"✓ Connected to IoT broker: {iot_connector.mqtt_broker}")
        iot_connector.subscribe_to_sensor_topics()
        print(f"✓ Subscribed to {len(iot_connector.subscribed_topics)} sensor topics")
        
        # Simulate sensor data
        for zone_id in zones.keys():
            iot_connector.simulate_sensor_data(zone_id)
        print(f"✓ Simulated sensor data for {len(zones)} zones")
        
        print(f"\nIoT Status: {iot_connector.get_sensor_status()}")
    
    # Initialize Tandem Connector
    print("\n2. Autodesk Tandem Connector Setup")
    print("-" * 60)
    tandem_connector = TandemConnector()
    
    if tandem_connector.connect():
        print(f"✓ Connected to Tandem API")
        
        # Register buildings with Tandem
        for building_id, building in city.buildings.items():
            tandem_connector.register_building(
                building_id=building_id,
                building_name=building.name,
                model_url=f"https://models.tandem.autodesk.com/{building_id}",
            )
        
        print(f"✓ Registered {len(city.buildings)} buildings with Tandem")
        
        # Update building properties
        for building_id, building in city.buildings.items():
            tandem_connector.update_building_properties(
                building_id=building_id,
                properties={
                    "energy_consumption_kwh": building.energy_consumption_kwh,
                    "occupancy": building.current_occupancy,
                    "status": building.status.value,
                },
            )
        
        print(f"✓ Updated building properties in Tandem")
        print(f"\nTandem Status: {tandem_connector.get_connected_buildings_summary()}")
    
    # Initialize Unreal Engine Connector
    print("\n3. Unreal Engine Connector Setup")
    print("-" * 60)
    unreal_connector = UnrealConnector(engine_endpoint="localhost:8080")
    
    if unreal_connector.connect():
        print(f"✓ Connected to Unreal Engine at {unreal_connector.engine_endpoint}")
        
        # Load scenes for each zone
        for zone_id, zone in zones.items():
            scene_data = {
                "zone_id": zone_id,
                "zone_name": zone.name,
                "buildings": len(zone.buildings),
                "population": zone.population,
            }
            unreal_connector.load_scene(
                scene_id=zone_id,
                scene_name=f"{zone.name} - 3D Scene",
                scene_data=scene_data,
            )
        
        print(f"✓ Loaded {len(zones)} scenes in Unreal Engine")
        
        # Set visualization parameters
        unreal_connector.set_visualization_parameters({
            "time_of_day": "14:30",
            "weather": "sunny",
            "lighting_quality": "high",
            "render_resolution": "4K",
        })
        
        print(f"✓ Set visualization parameters")
        print(f"\nUnreal Status: {unreal_connector.get_engine_status()}")
    
    # Initialize Environmental Data Connector
    print("\n4. Environmental Data Connector Setup")
    print("-" * 60)
    env_connector = EnvironmentalDataConnector()
    
    if env_connector.connect():
        print(f"✓ Connected to environmental data sources")
        
        # Fetch environmental data for each zone
        for zone_id, zone in zones.items():
            env_data = env_connector.fetch_all_environmental_data(
                zone_id=zone_id,
                latitude=zone.latitude,
                longitude=zone.longitude,
            )
            
            # Update zone with environmental data
            zone.update_environmental_metrics({
                "air_quality_index": env_data["air_quality"]["aqi"],
                "temperature": env_data["weather"]["temperature_c"],
                "humidity_percentage": env_data["weather"]["humidity_percentage"],
                "water_ph": env_data["water_quality"]["ph"],
                "biodiversity_index": env_data["biodiversity"]["biodiversity_index"],
                "carbon_emissions_tons": env_data["carbon"]["total_emissions_tons"],
            })
        
        print(f"✓ Fetched environmental data for {len(zones)} zones")
        print(f"\nEnvironmental Data Status: {env_connector.get_data_source_status()}")
    
    # Summary
    print("\n" + "=" * 60)
    print("Integration Summary")
    print("=" * 60)
    print(f"City: {city.config.name}")
    print(f"Zones: {len(city.zones)}")
    print(f"Buildings: {len(city.buildings)}")
    print(f"\nConnectors Status:")
    print(f"  IoT: {iot_connector.status.value}")
    print(f"  Tandem: {tandem_connector.status.value}")
    print(f"  Unreal: {unreal_connector.status.value}")
    print(f"  Environmental Data: {env_connector.status.value}")
    print("\n" + "=" * 60)
    
    return city


if __name__ == "__main__":
    city = main()
