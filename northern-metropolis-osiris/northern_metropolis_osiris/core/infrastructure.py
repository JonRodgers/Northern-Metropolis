"""
Infrastructure Management for Northern Metropolis
Defines critical infrastructure assets and their operational metrics.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum
from datetime import datetime


class InfrastructureType(Enum):
    """Types of infrastructure in Northern Metropolis"""
    POWER_GRID = "Power Grid"
    WATER_SUPPLY = "Water Supply"
    WASTEWATER = "Wastewater"
    TRANSPORTATION = "Transportation"
    TELECOMMUNICATIONS = "Telecommunications"
    WASTE_MANAGEMENT = "Waste Management"
    RENEWABLE_ENERGY = "Renewable Energy"
    DISTRICT_COOLING = "District Cooling"
    DISTRICT_HEATING = "District Heating"
    SMART_LIGHTING = "Smart Lighting"
    ENVIRONMENTAL_MONITORING = "Environmental Monitoring"
    FLOOD_MANAGEMENT = "Flood Management"


class InfrastructureStatus(Enum):
    """Status of infrastructure"""
    PLANNED = "Planned"
    UNDER_CONSTRUCTION = "Under Construction"
    OPERATIONAL = "Operational"
    MAINTENANCE = "Maintenance"
    DECOMMISSIONED = "Decommissioned"


@dataclass
class InfrastructureConfig:
    """Configuration for infrastructure asset"""
    id: str
    name: str
    infrastructure_type: InfrastructureType
    latitude: float
    longitude: float
    capacity: float
    capacity_unit: str
    status: InfrastructureStatus = InfrastructureStatus.PLANNED
    installation_year: int = 2024
    expected_lifespan_years: int = 30
    maintenance_interval_days: int = 90


class Infrastructure:
    """
    Represents critical infrastructure in Northern Metropolis.
    Tracks operational status, capacity utilization, and maintenance schedules.
    """

    def __init__(self, config: InfrastructureConfig):
        """Initialize infrastructure asset"""
        self.id = config.id
        self.name = config.name
        self.infrastructure_type = config.infrastructure_type
        self.latitude = config.latitude
        self.longitude = config.longitude
        self.capacity = config.capacity
        self.capacity_unit = config.capacity_unit
        self.status = config.status
        self.installation_year = config.installation_year
        self.expected_lifespan_years = config.expected_lifespan_years
        self.maintenance_interval_days = config.maintenance_interval_days
        
        # Operational metrics
        self.current_utilization = 0.0
        self.efficiency_percentage = 100.0
        self.uptime_percentage = 99.9
        self.last_maintenance = datetime.utcnow()
        self.next_maintenance = datetime.utcnow()
        
        # Health metrics
        self.health_score = 100.0
        self.alerts: List[Dict] = []
        self.performance_history: List[Dict] = []
        
        self.created_at = datetime.utcnow()
        self.last_updated = datetime.utcnow()

    def update_status(self, status: InfrastructureStatus) -> None:
        """Update infrastructure status"""
        self.status = status
        self.last_updated = datetime.utcnow()

    def update_utilization(self, utilization: float) -> None:
        """Update current utilization percentage"""
        self.current_utilization = max(0.0, min(100.0, utilization))
        self.last_updated = datetime.utcnow()

    def update_efficiency(self, efficiency: float) -> None:
        """Update efficiency percentage"""
        self.efficiency_percentage = max(0.0, min(100.0, efficiency))
        self.last_updated = datetime.utcnow()

    def update_uptime(self, uptime: float) -> None:
        """Update uptime percentage"""
        self.uptime_percentage = max(0.0, min(100.0, uptime))
        self.last_updated = datetime.utcnow()

    def record_maintenance(self) -> None:
        """Record maintenance completion"""
        self.last_maintenance = datetime.utcnow()
        # Schedule next maintenance
        from datetime import timedelta
        self.next_maintenance = self.last_maintenance + timedelta(days=self.maintenance_interval_days)
        self.last_updated = datetime.utcnow()

    def add_alert(self, severity: str, message: str) -> None:
        """Add an alert for this infrastructure"""
        alert = {
            "timestamp": datetime.utcnow().isoformat(),
            "severity": severity,
            "message": message,
        }
        self.alerts.append(alert)
        self.last_updated = datetime.utcnow()

    def calculate_health_score(self) -> float:
        """Calculate overall health score (0-100)"""
        # Health score based on efficiency, uptime, and utilization
        efficiency_weight = 0.4
        uptime_weight = 0.4
        utilization_weight = 0.2
        
        # Penalize if over-utilized
        utilization_score = 100.0 if self.current_utilization <= 80 else (100 - (self.current_utilization - 80) * 2)
        
        health = (
            (self.efficiency_percentage * efficiency_weight) +
            (self.uptime_percentage * uptime_weight) +
            (utilization_score * utilization_weight)
        )
        
        self.health_score = max(0.0, min(100.0, health))
        return self.health_score

    def is_maintenance_due(self) -> bool:
        """Check if maintenance is due"""
        return datetime.utcnow() >= self.next_maintenance

    def get_infrastructure_summary(self) -> Dict:
        """Get comprehensive infrastructure summary"""
        return {
            "id": self.id,
            "name": self.name,
            "type": self.infrastructure_type.value,
            "status": self.status.value,
            "location": {
                "latitude": self.latitude,
                "longitude": self.longitude,
            },
            "capacity": {
                "value": self.capacity,
                "unit": self.capacity_unit,
            },
            "operational": {
                "utilization_percentage": round(self.current_utilization, 2),
                "efficiency_percentage": round(self.efficiency_percentage, 2),
                "uptime_percentage": round(self.uptime_percentage, 2),
                "health_score": round(self.calculate_health_score(), 2),
            },
            "maintenance": {
                "last_maintenance": self.last_maintenance.isoformat(),
                "next_maintenance": self.next_maintenance.isoformat(),
                "maintenance_due": self.is_maintenance_due(),
                "interval_days": self.maintenance_interval_days,
            },
            "lifecycle": {
                "installation_year": self.installation_year,
                "expected_lifespan_years": self.expected_lifespan_years,
                "age_years": datetime.utcnow().year - self.installation_year,
            },
            "alerts": len(self.alerts),
            "recent_alerts": self.alerts[-5:] if self.alerts else [],
            "created_at": self.created_at.isoformat(),
            "last_updated": self.last_updated.isoformat(),
        }

    def record_performance_snapshot(self) -> None:
        """Record a snapshot of current performance"""
        snapshot = {
            "timestamp": datetime.utcnow().isoformat(),
            "utilization_percentage": self.current_utilization,
            "efficiency_percentage": self.efficiency_percentage,
            "uptime_percentage": self.uptime_percentage,
            "health_score": self.health_score,
        }
        self.performance_history.append(snapshot)

    def __repr__(self) -> str:
        return (
            f"Infrastructure(id={self.id}, name={self.name}, "
            f"type={self.infrastructure_type.value}, status={self.status.value})"
        )


# Pre-defined critical infrastructure for Northern Metropolis
CRITICAL_INFRASTRUCTURE_TEMPLATES = {
    "power_grid_main": InfrastructureConfig(
        id="power_grid_main",
        name="Main Power Grid Distribution",
        infrastructure_type=InfrastructureType.POWER_GRID,
        latitude=22.5,
        longitude=114.1,
        capacity=2000.0,
        capacity_unit="MW",
        installation_year=2024,
        expected_lifespan_years=40,
        maintenance_interval_days=180,
    ),
    "water_supply_main": InfrastructureConfig(
        id="water_supply_main",
        name="Main Water Supply Network",
        infrastructure_type=InfrastructureType.WATER_SUPPLY,
        latitude=22.5,
        longitude=114.1,
        capacity=500.0,
        capacity_unit="ML/day",
        installation_year=2024,
        expected_lifespan_years=50,
        maintenance_interval_days=90,
    ),
    "renewable_solar": InfrastructureConfig(
        id="renewable_solar",
        name="Solar Farm Array",
        infrastructure_type=InfrastructureType.RENEWABLE_ENERGY,
        latitude=22.48,
        longitude=114.12,
        capacity=500.0,
        capacity_unit="MW",
        installation_year=2024,
        expected_lifespan_years=25,
        maintenance_interval_days=180,
    ),
    "renewable_wind": InfrastructureConfig(
        id="renewable_wind",
        name="Wind Turbine Farm",
        infrastructure_type=InfrastructureType.RENEWABLE_ENERGY,
        latitude=22.52,
        longitude=114.08,
        capacity=300.0,
        capacity_unit="MW",
        installation_year=2024,
        expected_lifespan_years=25,
        maintenance_interval_days=90,
    ),
    "district_cooling": InfrastructureConfig(
        id="district_cooling",
        name="District Cooling System",
        infrastructure_type=InfrastructureType.DISTRICT_COOLING,
        latitude=22.5,
        longitude=114.1,
        capacity=1000.0,
        capacity_unit="MW_cooling",
        installation_year=2024,
        expected_lifespan_years=30,
        maintenance_interval_days=60,
    ),
    "smart_lighting": InfrastructureConfig(
        id="smart_lighting",
        name="Smart Street Lighting Network",
        infrastructure_type=InfrastructureType.SMART_LIGHTING,
        latitude=22.5,
        longitude=114.1,
        capacity=50000.0,
        capacity_unit="fixtures",
        installation_year=2024,
        expected_lifespan_years=15,
        maintenance_interval_days=180,
    ),
    "environmental_monitoring": InfrastructureConfig(
        id="environmental_monitoring",
        name="Environmental Monitoring Network",
        infrastructure_type=InfrastructureType.ENVIRONMENTAL_MONITORING,
        latitude=22.5,
        longitude=114.1,
        capacity=500.0,
        capacity_unit="sensors",
        installation_year=2024,
        expected_lifespan_years=10,
        maintenance_interval_days=30,
    ),
}


def create_critical_infrastructure() -> Dict[str, Infrastructure]:
    """Create all critical infrastructure assets"""
    infrastructure = {}
    for infra_id, config in CRITICAL_INFRASTRUCTURE_TEMPLATES.items():
        infrastructure[infra_id] = Infrastructure(config)
    return infrastructure
