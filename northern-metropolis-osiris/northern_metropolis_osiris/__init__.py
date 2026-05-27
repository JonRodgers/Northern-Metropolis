"""
Northern Metropolis OSIRIS - AI-Powered Smart City Digital Twin
A comprehensive platform for optimizing urban systems in the Northern Metropolis development.
"""

__version__ = "0.1.0"
__author__ = "Northern Metropolis Development Team"
__description__ = "AI-powered digital twin for smart city optimization"

from .core.city import NorthernMetropolis
from .core.zones import Zone, ZoneType
from .core.buildings import Building, BuildingType
from .core.infrastructure import Infrastructure, InfrastructureType

__all__ = [
    "NorthernMetropolis",
    "Zone",
    "ZoneType",
    "Building",
    "BuildingType",
    "Infrastructure",
    "InfrastructureType",
]
