"""
Building Management for Northern Metropolis
Defines building types, properties, and energy/environmental characteristics.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime


class BuildingType(Enum):
    """Types of buildings in Northern Metropolis"""
    RESIDENTIAL = "Residential"
    COMMERCIAL = "Commercial"
    INDUSTRIAL = "Industrial"
    INSTITUTIONAL = "Institutional"
    MIXED_USE = "Mixed Use"
    HOSPITALITY = "Hospitality"
    HEALTHCARE = "Healthcare"
    EDUCATION = "Education"
    TRANSPORTATION = "Transportation"
    UTILITY = "Utility"


class BuildingStatus(Enum):
    """Status of building development"""
    PLANNED = "Planned"
    UNDER_CONSTRUCTION = "Under Construction"
    OPERATIONAL = "Operational"
    RENOVATION = "Renovation"
    DECOMMISSIONED = "Decommissioned"


@dataclass
class BuildingConfig:
    """Configuration for a building"""
    id: str
    name: str
    building_type: BuildingType
    latitude: float
    longitude: float
    height_m: float
    floor_area_m2: float
    floors: int
    construction_year: int
    status: BuildingStatus = BuildingStatus.PLANNED
    occupancy_capacity: int = 0
    energy_rating: str = "TBD"
    renewable_energy_capacity_kw: float = 0.0
    water_recycling_capacity_m3_day: float = 0.0


class Building:
    """
    Represents a building in Northern Metropolis.
    Tracks energy consumption, occupancy, environmental impact, and integration with digital twin.
    """

    def __init__(self, config: BuildingConfig):
        """Initialize a building"""
        self.id = config.id
        self.name = config.name
        self.building_type = config.building_type
        self.latitude = config.latitude
        self.longitude = config.longitude
        self.height_m = config.height_m
        self.floor_area_m2 = config.floor_area_m2
        self.floors = config.floors
        self.construction_year = config.construction_year
        self.status = config.status
        self.occupancy_capacity = config.occupancy_capacity
        self.energy_rating = config.energy_rating
        self.renewable_energy_capacity_kw = config.renewable_energy_capacity_kw
        self.water_recycling_capacity_m3_day = config.water_recycling_capacity_m3_day
        
        # Real-time metrics
        self.current_occupancy = 0
        self.energy_consumption_kwh = 0.0
        self.renewable_energy_generation_kwh = 0.0
        self.water_consumption_m3 = 0.0
        self.waste_generated_kg = 0.0
        self.indoor_temperature_c = 22.0
        self.indoor_humidity_percentage = 50.0
        self.air_quality_index = 50
        
        # Integration flags
        self.tandem_integrated = False
        self.unreal_integrated = False
        self.iot_sensors_active = False
        self.bms_connected = False
        
        self.created_at = datetime.utcnow()
        self.last_updated = datetime.utcnow()
        self.metrics_history: List[Dict] = []

    def update_status(self, status: BuildingStatus) -> None:
        """Update building status"""
        self.status = status
        self.last_updated = datetime.utcnow()

    def update_occupancy(self, occupancy: int) -> None:
        """Update current occupancy"""
        if occupancy > self.occupancy_capacity:
            occupancy = self.occupancy_capacity
        self.current_occupancy = occupancy
        self.last_updated = datetime.utcnow()

    def update_energy_metrics(self, consumption_kwh: float, generation_kwh: float = 0.0) -> None:
        """Update energy consumption and generation"""
        self.energy_consumption_kwh = consumption_kwh
        self.renewable_energy_generation_kwh = generation_kwh
        self.last_updated = datetime.utcnow()

    def update_environmental_metrics(self, metrics: Dict[str, float]) -> None:
        """Update environmental metrics"""
        if "water_consumption_m3" in metrics:
            self.water_consumption_m3 = metrics["water_consumption_m3"]
        if "waste_generated_kg" in metrics:
            self.waste_generated_kg = metrics["waste_generated_kg"]
        if "indoor_temperature_c" in metrics:
            self.indoor_temperature_c = metrics["indoor_temperature_c"]
        if "indoor_humidity_percentage" in metrics:
            self.indoor_humidity_percentage = metrics["indoor_humidity_percentage"]
        if "air_quality_index" in metrics:
            self.air_quality_index = metrics["air_quality_index"]
        
        self.last_updated = datetime.utcnow()

    def set_tandem_integration(self, integrated: bool) -> None:
        """Set Autodesk Tandem integration status"""
        self.tandem_integrated = integrated
        self.last_updated = datetime.utcnow()

    def set_unreal_integration(self, integrated: bool) -> None:
        """Set Unreal Engine integration status"""
        self.unreal_integrated = integrated
        self.last_updated = datetime.utcnow()

    def set_iot_sensors(self, active: bool) -> None:
        """Set IoT sensors active status"""
        self.iot_sensors_active = active
        self.last_updated = datetime.utcnow()

    def set_bms_connection(self, connected: bool) -> None:
        """Set Building Management System connection status"""
        self.bms_connected = connected
        self.last_updated = datetime.utcnow()

    def calculate_energy_efficiency(self) -> float:
        """Calculate energy efficiency ratio (generation/consumption)"""
        if self.energy_consumption_kwh == 0:
            return 0.0
        return (self.renewable_energy_generation_kwh / self.energy_consumption_kwh) * 100

    def calculate_occupancy_percentage(self) -> float:
        """Calculate occupancy percentage"""
        if self.occupancy_capacity == 0:
            return 0.0
        return (self.current_occupancy / self.occupancy_capacity) * 100

    def get_building_summary(self) -> Dict:
        """Get comprehensive building summary"""
        return {
            "id": self.id,
            "name": self.name,
            "type": self.building_type.value,
            "status": self.status.value,
            "location": {
                "latitude": self.latitude,
                "longitude": self.longitude,
            },
            "dimensions": {
                "height_m": self.height_m,
                "floor_area_m2": self.floor_area_m2,
                "floors": self.floors,
            },
            "construction_year": self.construction_year,
            "energy_rating": self.energy_rating,
            "occupancy": {
                "current": self.current_occupancy,
                "capacity": self.occupancy_capacity,
                "percentage": round(self.calculate_occupancy_percentage(), 2),
            },
            "energy": {
                "consumption_kwh": self.energy_consumption_kwh,
                "renewable_generation_kwh": self.renewable_energy_generation_kwh,
                "renewable_capacity_kw": self.renewable_energy_capacity_kw,
                "efficiency_percentage": round(self.calculate_energy_efficiency(), 2),
            },
            "environmental": {
                "water_consumption_m3": self.water_consumption_m3,
                "water_recycling_capacity_m3_day": self.water_recycling_capacity_m3_day,
                "waste_generated_kg": self.waste_generated_kg,
                "indoor_temperature_c": self.indoor_temperature_c,
                "indoor_humidity_percentage": self.indoor_humidity_percentage,
                "air_quality_index": self.air_quality_index,
            },
            "integrations": {
                "tandem": self.tandem_integrated,
                "unreal": self.unreal_integrated,
                "iot_sensors": self.iot_sensors_active,
                "bms": self.bms_connected,
            },
            "created_at": self.created_at.isoformat(),
            "last_updated": self.last_updated.isoformat(),
        }

    def record_metrics_snapshot(self) -> None:
        """Record a snapshot of current metrics"""
        snapshot = {
            "timestamp": datetime.utcnow().isoformat(),
            "occupancy": self.current_occupancy,
            "energy_consumption_kwh": self.energy_consumption_kwh,
            "renewable_generation_kwh": self.renewable_energy_generation_kwh,
            "water_consumption_m3": self.water_consumption_m3,
            "waste_generated_kg": self.waste_generated_kg,
            "indoor_temperature_c": self.indoor_temperature_c,
            "air_quality_index": self.air_quality_index,
        }
        self.metrics_history.append(snapshot)

    def __repr__(self) -> str:
        return (
            f"Building(id={self.id}, name={self.name}, "
            f"type={self.building_type.value}, status={self.status.value})"
        )
