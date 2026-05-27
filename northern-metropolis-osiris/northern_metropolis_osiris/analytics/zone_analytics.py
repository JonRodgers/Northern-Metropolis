"""
Zone-Level Analytics for Northern Metropolis
Specialized analytics for individual zone performance and development.
"""

from typing import Dict, List, Optional
from datetime import datetime
import statistics


class ZoneAnalytics:
    """
    Analyzes performance metrics at the zone level.
    Tracks development progress, resource consumption, and zone-specific KPIs.
    """

    def __init__(self):
        """Initialize zone analytics"""
        self.created_at = datetime.utcnow()
        self.zone_reports: Dict[str, List[Dict]] = {}

    def analyze_zone_development(self, zone) -> Dict:
        """Analyze development progress for a zone"""
        building_progress = (len(zone.buildings) / zone.planned_buildings * 100) if zone.planned_buildings > 0 else 0
        population_progress = (zone.population / zone.target_population * 100) if zone.target_population > 0 else 0

        return {
            "zone_id": zone.id,
            "zone_name": zone.name,
            "zone_type": zone.zone_type.value,
            "timestamp": datetime.utcnow().isoformat(),
            "development": {
                "building_progress_percentage": round(building_progress, 2),
                "buildings_completed": len(zone.buildings),
                "buildings_planned": zone.planned_buildings,
                "population_progress_percentage": round(population_progress, 2),
                "current_population": zone.population,
                "target_population": zone.target_population,
                "area_km2": zone.area_km2,
                "population_density_per_km2": round(zone.population / zone.area_km2, 2) if zone.area_km2 > 0 else 0,
            },
            "infrastructure": {
                "total_assets": len(zone.infrastructure),
            },
        }

    def analyze_zone_energy(self, zone) -> Dict:
        """Analyze energy consumption and generation for a zone"""
        buildings = zone.buildings.values()
        consumptions = [b.energy_consumption_kwh for b in buildings if hasattr(b, 'energy_consumption_kwh')]
        generations = [b.renewable_energy_generation_kwh for b in buildings if hasattr(b, 'renewable_energy_generation_kwh')]

        analysis = {
            "zone_id": zone.id,
            "zone_name": zone.name,
            "timestamp": datetime.utcnow().isoformat(),
        }

        if consumptions:
            total_consumption = sum(consumptions)
            total_generation = sum(generations)
            analysis["energy"] = {
                "total_consumption_kwh": total_consumption,
                "average_consumption_kwh": round(statistics.mean(consumptions), 2),
                "total_renewable_generation_kwh": total_generation,
                "renewable_percentage": round((total_generation / total_consumption * 100) if total_consumption > 0 else 0, 2),
                "target_renewable_percentage": zone.planned_renewable_energy_percentage,
                "buildings_analyzed": len(consumptions),
            }

        return analysis

    def analyze_zone_water(self, zone) -> Dict:
        """Analyze water consumption for a zone"""
        buildings = zone.buildings.values()
        consumptions = [b.water_consumption_m3 for b in buildings if hasattr(b, 'water_consumption_m3')]

        analysis = {
            "zone_id": zone.id,
            "zone_name": zone.name,
            "timestamp": datetime.utcnow().isoformat(),
        }

        if consumptions:
            analysis["water"] = {
                "total_consumption_m3": round(sum(consumptions), 2),
                "average_consumption_m3": round(statistics.mean(consumptions), 2),
                "per_capita_consumption_m3": round(sum(consumptions) / zone.population, 2) if zone.population > 0 else 0,
                "buildings_analyzed": len(consumptions),
            }

        return analysis

    def analyze_zone_waste(self, zone) -> Dict:
        """Analyze waste generation for a zone"""
        buildings = zone.buildings.values()
        waste_values = [b.waste_generated_kg for b in buildings if hasattr(b, 'waste_generated_kg')]

        analysis = {
            "zone_id": zone.id,
            "zone_name": zone.name,
            "timestamp": datetime.utcnow().isoformat(),
        }

        if waste_values:
            analysis["waste"] = {
                "total_waste_kg": round(sum(waste_values), 2),
                "average_waste_kg": round(statistics.mean(waste_values), 2),
                "per_capita_waste_kg": round(sum(waste_values) / zone.population, 2) if zone.population > 0 else 0,
                "buildings_analyzed": len(waste_values),
            }

        return analysis

    def analyze_zone_occupancy(self, zone) -> Dict:
        """Analyze occupancy patterns for a zone"""
        buildings = zone.buildings.values()
        occupancies = [b.current_occupancy for b in buildings if hasattr(b, 'current_occupancy')]
        capacities = [b.occupancy_capacity for b in buildings if hasattr(b, 'occupancy_capacity')]

        analysis = {
            "zone_id": zone.id,
            "zone_name": zone.name,
            "timestamp": datetime.utcnow().isoformat(),
        }

        if occupancies:
            occupancy_percentages = [
                (occ / cap * 100) if cap > 0 else 0
                for occ, cap in zip(occupancies, capacities)
            ]
            analysis["occupancy"] = {
                "total_occupancy": sum(occupancies),
                "total_capacity": sum(capacities),
                "average_occupancy_percentage": round(statistics.mean(occupancy_percentages), 2),
                "buildings_analyzed": len(occupancies),
            }

        return analysis

    def analyze_zone_environmental(self, zone) -> Dict:
        """Analyze environmental metrics for a zone"""
        metrics = zone.environmental_metrics or {}

        analysis = {
            "zone_id": zone.id,
            "zone_name": zone.name,
            "timestamp": datetime.utcnow().isoformat(),
            "environmental_metrics": metrics,
        }

        return analysis

    def analyze_zone_integration(self, zone) -> Dict:
        """Analyze digital twin integration status for a zone"""
        buildings = zone.buildings.values()
        
        tandem_integrated = sum(1 for b in buildings if hasattr(b, 'tandem_integrated') and b.tandem_integrated)
        unreal_integrated = sum(1 for b in buildings if hasattr(b, 'unreal_integrated') and b.unreal_integrated)
        iot_active = sum(1 for b in buildings if hasattr(b, 'iot_sensors_active') and b.iot_sensors_active)
        bms_connected = sum(1 for b in buildings if hasattr(b, 'bms_connected') and b.bms_connected)

        total_buildings = len(buildings)

        return {
            "zone_id": zone.id,
            "zone_name": zone.name,
            "timestamp": datetime.utcnow().isoformat(),
            "integration": {
                "tandem": {
                    "integrated_buildings": tandem_integrated,
                    "total_buildings": total_buildings,
                    "percentage": round((tandem_integrated / total_buildings * 100) if total_buildings > 0 else 0, 2),
                },
                "unreal": {
                    "integrated_buildings": unreal_integrated,
                    "total_buildings": total_buildings,
                    "percentage": round((unreal_integrated / total_buildings * 100) if total_buildings > 0 else 0, 2),
                },
                "iot_sensors": {
                    "active_buildings": iot_active,
                    "total_buildings": total_buildings,
                    "percentage": round((iot_active / total_buildings * 100) if total_buildings > 0 else 0, 2),
                },
                "bms": {
                    "connected_buildings": bms_connected,
                    "total_buildings": total_buildings,
                    "percentage": round((bms_connected / total_buildings * 100) if total_buildings > 0 else 0, 2),
                },
            },
        }

    def generate_zone_report(self, zone) -> Dict:
        """Generate comprehensive zone report"""
        report = {
            "timestamp": datetime.utcnow().isoformat(),
            "zone_id": zone.id,
            "zone_name": zone.name,
            "development": self.analyze_zone_development(zone),
            "energy": self.analyze_zone_energy(zone),
            "water": self.analyze_zone_water(zone),
            "waste": self.analyze_zone_waste(zone),
            "occupancy": self.analyze_zone_occupancy(zone),
            "environmental": self.analyze_zone_environmental(zone),
            "integration": self.analyze_zone_integration(zone),
        }

        # Store report in history
        if zone.id not in self.zone_reports:
            self.zone_reports[zone.id] = []
        self.zone_reports[zone.id].append(report)

        return report

    def get_zone_kpis(self, zone) -> Dict:
        """Get key performance indicators for a zone"""
        dev_analysis = self.analyze_zone_development(zone)
        energy_analysis = self.analyze_zone_energy(zone)
        water_analysis = self.analyze_zone_water(zone)
        integration_analysis = self.analyze_zone_integration(zone)

        kpis = {
            "zone_id": zone.id,
            "zone_name": zone.name,
            "timestamp": datetime.utcnow().isoformat(),
            "kpis": {
                "development_progress_percentage": dev_analysis["development"]["building_progress_percentage"],
                "population_progress_percentage": dev_analysis["development"]["population_progress_percentage"],
                "renewable_energy_percentage": energy_analysis.get("energy", {}).get("renewable_percentage", 0),
                "tandem_integration_percentage": integration_analysis["integration"]["tandem"]["percentage"],
                "unreal_integration_percentage": integration_analysis["integration"]["unreal"]["percentage"],
                "iot_coverage_percentage": integration_analysis["integration"]["iot_sensors"]["percentage"],
                "bms_coverage_percentage": integration_analysis["integration"]["bms"]["percentage"],
            },
        }

        return kpis

    def compare_zones(self, zones: List) -> Dict:
        """Compare metrics across multiple zones"""
        comparison = {
            "timestamp": datetime.utcnow().isoformat(),
            "zones_compared": len(zones),
            "zones": [],
        }

        for zone in zones:
            zone_data = {
                "zone_id": zone.id,
                "zone_name": zone.name,
                "development_progress": self.analyze_zone_development(zone)["development"]["building_progress_percentage"],
                "population_progress": self.analyze_zone_development(zone)["development"]["population_progress_percentage"],
                "buildings": len(zone.buildings),
                "population": zone.population,
                "area_km2": zone.area_km2,
            }
            comparison["zones"].append(zone_data)

        return comparison

    def __repr__(self) -> str:
        return f"ZoneAnalytics(zones_tracked={len(self.zone_reports)})"
