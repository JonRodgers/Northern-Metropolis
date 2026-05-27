"""
Northern Metropolis City Model
Core city-level data structures and management for the digital twin.
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime
import json

from .zones import Zone, ZoneType
from .buildings import Building
from .infrastructure import Infrastructure


@dataclass
class CityMetrics:
    """Aggregated city-level metrics"""
    timestamp: datetime
    total_population: int = 0
    total_buildings: int = 0
    total_infrastructure_assets: int = 0
    average_air_quality_index: float = 0.0
    average_temperature: float = 0.0
    total_energy_consumption_mwh: float = 0.0
    total_water_consumption_m3: float = 0.0
    total_waste_generated_tons: float = 0.0
    carbon_emissions_tons: float = 0.0
    traffic_congestion_index: float = 0.0
    renewable_energy_percentage: float = 0.0
    green_space_percentage: float = 0.0
    biodiversity_index: float = 0.0


@dataclass
class CityConfig:
    """Configuration for Northern Metropolis city"""
    name: str = "Northern Metropolis"
    country: str = "Hong Kong"
    region: str = "New Territories"
    latitude: float = 22.5
    longitude: float = 114.1
    total_area_km2: float = 300.0
    target_population: int = 2500000
    simulation_timestep_minutes: int = 15
    data_retention_days: int = 365


class NorthernMetropolis:
    """
    Main city model for Northern Metropolis digital twin.
    Manages zones, buildings, infrastructure, and city-wide optimization.
    """

    def __init__(self, config: Optional[CityConfig] = None):
        """Initialize Northern Metropolis city model"""
        self.config = config or CityConfig()
        self.zones: Dict[str, Zone] = {}
        self.buildings: Dict[str, Building] = {}
        self.infrastructure: Dict[str, Infrastructure] = {}
        self.metrics_history: List[CityMetrics] = []
        self.created_at = datetime.utcnow()
        self.last_updated = datetime.utcnow()

    def add_zone(self, zone: Zone) -> None:
        """Add a zone to the city"""
        self.zones[zone.id] = zone
        self.last_updated = datetime.utcnow()

    def add_building(self, building: Building, zone_id: str) -> None:
        """Add a building to a specific zone"""
        if zone_id not in self.zones:
            raise ValueError(f"Zone {zone_id} not found")
        
        self.buildings[building.id] = building
        self.zones[zone_id].add_building(building)
        self.last_updated = datetime.utcnow()

    def add_infrastructure(self, infrastructure: Infrastructure, zone_id: str) -> None:
        """Add infrastructure asset to a zone"""
        if zone_id not in self.zones:
            raise ValueError(f"Zone {zone_id} not found")
        
        self.infrastructure[infrastructure.id] = infrastructure
        self.zones[zone_id].add_infrastructure(infrastructure)
        self.last_updated = datetime.utcnow()

    def get_zone(self, zone_id: str) -> Optional[Zone]:
        """Get zone by ID"""
        return self.zones.get(zone_id)

    def get_building(self, building_id: str) -> Optional[Building]:
        """Get building by ID"""
        return self.buildings.get(building_id)

    def get_infrastructure(self, infrastructure_id: str) -> Optional[Infrastructure]:
        """Get infrastructure by ID"""
        return self.infrastructure.get(infrastructure_id)

    def calculate_city_metrics(self) -> CityMetrics:
        """Calculate aggregated city-level metrics"""
        metrics = CityMetrics(timestamp=datetime.utcnow())
        
        # Aggregate from zones
        for zone in self.zones.values():
            metrics.total_population += zone.population
            metrics.total_buildings += len(zone.buildings)
            metrics.total_infrastructure_assets += len(zone.infrastructure)
            
            # Environmental metrics
            if zone.environmental_metrics:
                metrics.average_air_quality_index += zone.environmental_metrics.get("air_quality_index", 0)
                metrics.average_temperature += zone.environmental_metrics.get("temperature", 0)
                metrics.total_energy_consumption_mwh += zone.environmental_metrics.get("energy_consumption_mwh", 0)
                metrics.total_water_consumption_m3 += zone.environmental_metrics.get("water_consumption_m3", 0)
                metrics.total_waste_generated_tons += zone.environmental_metrics.get("waste_generated_tons", 0)
                metrics.carbon_emissions_tons += zone.environmental_metrics.get("carbon_emissions_tons", 0)
                metrics.traffic_congestion_index += zone.environmental_metrics.get("traffic_congestion_index", 0)
                metrics.renewable_energy_percentage += zone.environmental_metrics.get("renewable_energy_percentage", 0)
                metrics.green_space_percentage += zone.environmental_metrics.get("green_space_percentage", 0)
                metrics.biodiversity_index += zone.environmental_metrics.get("biodiversity_index", 0)
        
        # Average calculations
        num_zones = len(self.zones)
        if num_zones > 0:
            metrics.average_air_quality_index /= num_zones
            metrics.average_temperature /= num_zones
            metrics.traffic_congestion_index /= num_zones
            metrics.renewable_energy_percentage /= num_zones
            metrics.green_space_percentage /= num_zones
            metrics.biodiversity_index /= num_zones
        
        self.metrics_history.append(metrics)
        return metrics

    def get_zone_summary(self, zone_id: str) -> Dict:
        """Get summary information for a zone"""
        zone = self.get_zone(zone_id)
        if not zone:
            return {}
        
        return {
            "id": zone.id,
            "name": zone.name,
            "type": zone.zone_type.value,
            "population": zone.population,
            "area_km2": zone.area_km2,
            "buildings": len(zone.buildings),
            "infrastructure_assets": len(zone.infrastructure),
            "environmental_metrics": zone.environmental_metrics,
        }

    def get_city_summary(self) -> Dict:
        """Get comprehensive city summary"""
        latest_metrics = self.metrics_history[-1] if self.metrics_history else self.calculate_city_metrics()
        
        return {
            "name": self.config.name,
            "country": self.config.country,
            "region": self.config.region,
            "coordinates": {
                "latitude": self.config.latitude,
                "longitude": self.config.longitude,
            },
            "total_area_km2": self.config.total_area_km2,
            "zones": len(self.zones),
            "buildings": len(self.buildings),
            "infrastructure_assets": len(self.infrastructure),
            "metrics": {
                "population": latest_metrics.total_population,
                "air_quality_index": latest_metrics.average_air_quality_index,
                "temperature": latest_metrics.average_temperature,
                "energy_consumption_mwh": latest_metrics.total_energy_consumption_mwh,
                "water_consumption_m3": latest_metrics.total_water_consumption_m3,
                "carbon_emissions_tons": latest_metrics.carbon_emissions_tons,
                "renewable_energy_percentage": latest_metrics.renewable_energy_percentage,
                "green_space_percentage": latest_metrics.green_space_percentage,
                "biodiversity_index": latest_metrics.biodiversity_index,
            },
            "created_at": self.created_at.isoformat(),
            "last_updated": self.last_updated.isoformat(),
        }

    def export_to_json(self) -> str:
        """Export city model to JSON"""
        return json.dumps(self.get_city_summary(), indent=2, default=str)

    def __repr__(self) -> str:
        return (
            f"NorthernMetropolis(zones={len(self.zones)}, "
            f"buildings={len(self.buildings)}, "
            f"infrastructure={len(self.infrastructure)})"
        )
