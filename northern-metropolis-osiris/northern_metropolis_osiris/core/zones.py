"""
Zone Management for Northern Metropolis
Defines the four development zones and their characteristics.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime


class ZoneType(Enum):
    """Types of zones in Northern Metropolis"""
    LOK_MA_CHAU_LOOP = "Lok Ma Chau Loop"
    HEUNG_YUEN_WAI = "Heung Yuen Wai"
    FANLING_SHEUNG_SHUI = "Fanling/Sheung Shui"
    KWUTUNG_NORTH = "Kwu Tung North"


@dataclass
class ZoneConfig:
    """Configuration for a zone"""
    id: str
    name: str
    zone_type: ZoneType
    latitude: float
    longitude: float
    area_km2: float
    target_population: int
    planned_buildings: int
    planned_green_space_percentage: float = 30.0
    planned_renewable_energy_percentage: float = 50.0


class Zone:
    """
    Represents a development zone in Northern Metropolis.
    Each zone contains buildings, infrastructure, and environmental data.
    """

    def __init__(self, config: ZoneConfig):
        """Initialize a zone"""
        self.id = config.id
        self.name = config.name
        self.zone_type = config.zone_type
        self.latitude = config.latitude
        self.longitude = config.longitude
        self.area_km2 = config.area_km2
        self.target_population = config.target_population
        self.planned_buildings = config.planned_buildings
        self.planned_green_space_percentage = config.planned_green_space_percentage
        self.planned_renewable_energy_percentage = config.planned_renewable_energy_percentage
        
        self.buildings: Dict[str, 'Building'] = {}
        self.infrastructure: Dict[str, 'Infrastructure'] = {}
        self.population = 0
        self.environmental_metrics: Dict[str, float] = {}
        
        self.created_at = datetime.utcnow()
        self.last_updated = datetime.utcnow()

    def add_building(self, building: 'Building') -> None:
        """Add a building to the zone"""
        self.buildings[building.id] = building
        self.last_updated = datetime.utcnow()

    def remove_building(self, building_id: str) -> bool:
        """Remove a building from the zone"""
        if building_id in self.buildings:
            del self.buildings[building_id]
            self.last_updated = datetime.utcnow()
            return True
        return False

    def add_infrastructure(self, infrastructure: 'Infrastructure') -> None:
        """Add infrastructure to the zone"""
        self.infrastructure[infrastructure.id] = infrastructure
        self.last_updated = datetime.utcnow()

    def remove_infrastructure(self, infrastructure_id: str) -> bool:
        """Remove infrastructure from the zone"""
        if infrastructure_id in self.infrastructure:
            del self.infrastructure[infrastructure_id]
            self.last_updated = datetime.utcnow()
            return True
        return False

    def update_environmental_metrics(self, metrics: Dict[str, float]) -> None:
        """Update environmental metrics for the zone"""
        self.environmental_metrics.update(metrics)
        self.last_updated = datetime.utcnow()

    def update_population(self, population: int) -> None:
        """Update zone population"""
        self.population = population
        self.last_updated = datetime.utcnow()

    def get_zone_summary(self) -> Dict:
        """Get comprehensive zone summary"""
        return {
            "id": self.id,
            "name": self.name,
            "type": self.zone_type.value,
            "location": {
                "latitude": self.latitude,
                "longitude": self.longitude,
            },
            "area_km2": self.area_km2,
            "population": self.population,
            "target_population": self.target_population,
            "buildings": len(self.buildings),
            "planned_buildings": self.planned_buildings,
            "infrastructure_assets": len(self.infrastructure),
            "environmental_metrics": self.environmental_metrics,
            "planned_green_space_percentage": self.planned_green_space_percentage,
            "planned_renewable_energy_percentage": self.planned_renewable_energy_percentage,
            "created_at": self.created_at.isoformat(),
            "last_updated": self.last_updated.isoformat(),
        }

    def get_development_progress(self) -> Dict:
        """Calculate development progress for the zone"""
        building_progress = (len(self.buildings) / self.planned_buildings * 100) if self.planned_buildings > 0 else 0
        population_progress = (self.population / self.target_population * 100) if self.target_population > 0 else 0
        
        return {
            "zone_id": self.id,
            "zone_name": self.name,
            "building_progress_percentage": round(building_progress, 2),
            "population_progress_percentage": round(population_progress, 2),
            "buildings_completed": len(self.buildings),
            "buildings_planned": self.planned_buildings,
            "current_population": self.population,
            "target_population": self.target_population,
        }

    def __repr__(self) -> str:
        return (
            f"Zone(id={self.id}, name={self.name}, "
            f"buildings={len(self.buildings)}, population={self.population})"
        )


# Pre-defined zone configurations for Northern Metropolis
NORTHERN_METROPOLIS_ZONES = {
    "lok_ma_chau_loop": ZoneConfig(
        id="lok_ma_chau_loop",
        name="Lok Ma Chau Loop",
        zone_type=ZoneType.LOK_MA_CHAU_LOOP,
        latitude=22.5167,
        longitude=114.0167,
        area_km2=87.0,
        target_population=650000,
        planned_buildings=2500,
        planned_green_space_percentage=35.0,
        planned_renewable_energy_percentage=55.0,
    ),
    "heung_yuen_wai": ZoneConfig(
        id="heung_yuen_wai",
        name="Heung Yuen Wai",
        zone_type=ZoneType.HEUNG_YUEN_WAI,
        latitude=22.4833,
        longitude=114.0833,
        area_km2=75.0,
        target_population=550000,
        planned_buildings=2000,
        planned_green_space_percentage=32.0,
        planned_renewable_energy_percentage=50.0,
    ),
    "fanling_sheung_shui": ZoneConfig(
        id="fanling_sheung_shui",
        name="Fanling/Sheung Shui",
        zone_type=ZoneType.FANLING_SHEUNG_SHUI,
        latitude=22.5,
        longitude=114.15,
        area_km2=85.0,
        target_population=700000,
        planned_buildings=2800,
        planned_green_space_percentage=30.0,
        planned_renewable_energy_percentage=48.0,
    ),
    "kwutung_north": ZoneConfig(
        id="kwutung_north",
        name="Kwu Tung North",
        zone_type=ZoneType.KWUTUNG_NORTH,
        latitude=22.45,
        longitude=114.1167,
        area_km2=53.0,
        target_population=600000,
        planned_buildings=2200,
        planned_green_space_percentage=28.0,
        planned_renewable_energy_percentage=52.0,
    ),
}


def create_northern_metropolis_zones() -> Dict[str, Zone]:
    """Create all Northern Metropolis zones"""
    zones = {}
    for zone_id, config in NORTHERN_METROPOLIS_ZONES.items():
        zones[zone_id] = Zone(config)
    return zones
