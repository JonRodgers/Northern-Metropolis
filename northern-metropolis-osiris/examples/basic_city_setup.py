"""
Basic City Setup Example
Demonstrates how to initialize and configure the Northern Metropolis digital twin.
"""

from northern_metropolis_osiris.core import (
    NorthernMetropolis,
    CityConfig,
    create_northern_metropolis_zones,
    Building,
    BuildingConfig,
    BuildingType,
    BuildingStatus,
)
from northern_metropolis_osiris.analytics import AnalyticsEngine, EnvironmentalAnalytics
from northern_metropolis_osiris.optimization import OptimizationEngine


def main():
    """Main example function"""
    
    # Create city configuration
    city_config = CityConfig(
        name="Northern Metropolis",
        country="Hong Kong",
        region="New Territories",
        latitude=22.5,
        longitude=114.1,
        total_area_km2=300.0,
        target_population=2500000,
    )
    
    # Initialize city
    city = NorthernMetropolis(city_config)
    print(f"Created city: {city}")
    
    # Create and add zones
    zones = create_northern_metropolis_zones()
    for zone_id, zone in zones.items():
        city.add_zone(zone)
        print(f"Added zone: {zone.name}")
    
    # Create sample buildings
    building_configs = [
        BuildingConfig(
            id="bldg_001",
            name="Central Business Tower",
            building_type=BuildingType.COMMERCIAL,
            latitude=22.5,
            longitude=114.1,
            height_m=250,
            floor_area_m2=150000,
            floors=50,
            construction_year=2024,
            status=BuildingStatus.OPERATIONAL,
            occupancy_capacity=5000,
            energy_rating="A+",
            renewable_energy_capacity_kw=500,
        ),
        BuildingConfig(
            id="bldg_002",
            name="Residential Complex A",
            building_type=BuildingType.RESIDENTIAL,
            latitude=22.51,
            longitude=114.11,
            height_m=120,
            floor_area_m2=80000,
            floors=30,
            construction_year=2024,
            status=BuildingStatus.OPERATIONAL,
            occupancy_capacity=2000,
            energy_rating="A",
            renewable_energy_capacity_kw=300,
        ),
    ]
    
    # Add buildings to first zone
    first_zone_id = list(zones.keys())[0]
    for config in building_configs:
        building = Building(config)
        city.add_building(building, first_zone_id)
        print(f"Added building: {building.name}")
    
    # Update some metrics
    for zone in city.zones.values():
        zone.update_population(int(zone.target_population * 0.3))  # 30% of target
        zone.update_environmental_metrics({
            "air_quality_index": 65,
            "temperature": 24.5,
            "humidity_percentage": 70,
            "green_space_percentage": 25,
            "biodiversity_index": 0.65,
            "carbon_emissions_tons": 100000,
        })
    
    # Update building metrics
    for building in city.buildings.values():
        building.update_occupancy(int(building.occupancy_capacity * 0.7))
        building.update_energy_metrics(
            consumption_kwh=50000,
            generation_kwh=15000,
        )
        building.update_environmental_metrics({
            "water_consumption_m3": 500,
            "waste_generated_kg": 2000,
            "indoor_temperature_c": 22,
            "indoor_humidity_percentage": 55,
            "air_quality_index": 45,
        })
    
    # Generate city metrics
    city_metrics = city.calculate_city_metrics()
    print(f"\nCity Metrics:")
    print(f"  Population: {city_metrics.total_population:,}")
    print(f"  Buildings: {city_metrics.total_buildings}")
    print(f"  Energy Consumption: {city_metrics.total_energy_consumption_mwh:.2f} MWh")
    print(f"  Renewable Energy: {city_metrics.renewable_energy_percentage:.2f}%")
    
    # Run analytics
    analytics_engine = AnalyticsEngine()
    analysis = analytics_engine.generate_city_health_report(city)
    
    print(f"\nCity Health Report:")
    print(f"  Energy Consumption: {analysis['energy']['total_consumption_kwh']:.0f} kWh")
    print(f"  Renewable Percentage: {analysis['energy']['renewable_percentage']:.2f}%")
    print(f"  Average Occupancy: {analysis['occupancy']['average_occupancy_percentage']:.2f}%")
    print(f"  Air Quality Index: {analysis['air_quality']['average_aqi']:.2f}")
    
    # Run optimization
    optimization_engine = OptimizationEngine()
    optimization_result = optimization_engine.multi_objective_optimization(city)
    
    print(f"\nOptimization Results:")
    print(f"  Overall Score: {optimization_result['overall_optimization_score']:.2f}")
    print(f"  All Constraints Met: {optimization_result['all_constraints_met']}")
    
    # Print city summary
    print(f"\nCity Summary:")
    summary = city.get_city_summary()
    print(f"  Name: {summary['name']}")
    print(f"  Zones: {summary['zones']}")
    print(f"  Buildings: {summary['buildings']}")
    print(f"  Infrastructure Assets: {summary['infrastructure_assets']}")
    
    return city


if __name__ == "__main__":
    city = main()
