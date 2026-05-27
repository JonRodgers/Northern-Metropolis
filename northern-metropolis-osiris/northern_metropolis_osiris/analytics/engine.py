"""
Analytics Engine for Northern Metropolis
Core analytics processing and aggregation.
"""

from typing import Dict, List, Optional, Tuple
from datetime import datetime, timedelta
import statistics


class AnalyticsEngine:
    """
    Main analytics engine for processing city-wide metrics and generating insights.
    """

    def __init__(self):
        """Initialize analytics engine"""
        self.created_at = datetime.utcnow()
        self.last_analysis = None
        self.analysis_cache: Dict = {}

    def analyze_energy_consumption(self, buildings: List) -> Dict:
        """Analyze city-wide energy consumption patterns"""
        if not buildings:
            return {}

        consumptions = [b.energy_consumption_kwh for b in buildings if hasattr(b, 'energy_consumption_kwh')]
        generations = [b.renewable_energy_generation_kwh for b in buildings if hasattr(b, 'renewable_energy_generation_kwh')]

        if not consumptions:
            return {}

        return {
            "total_consumption_kwh": sum(consumptions),
            "average_consumption_kwh": statistics.mean(consumptions),
            "median_consumption_kwh": statistics.median(consumptions),
            "max_consumption_kwh": max(consumptions),
            "min_consumption_kwh": min(consumptions),
            "std_dev_consumption": statistics.stdev(consumptions) if len(consumptions) > 1 else 0,
            "total_renewable_generation_kwh": sum(generations),
            "renewable_percentage": (sum(generations) / sum(consumptions) * 100) if sum(consumptions) > 0 else 0,
            "buildings_analyzed": len(consumptions),
        }

    def analyze_occupancy_patterns(self, buildings: List) -> Dict:
        """Analyze occupancy patterns across buildings"""
        if not buildings:
            return {}

        occupancies = [b.current_occupancy for b in buildings if hasattr(b, 'current_occupancy')]
        capacities = [b.occupancy_capacity for b in buildings if hasattr(b, 'occupancy_capacity')]

        if not occupancies:
            return {}

        occupancy_percentages = [
            (occ / cap * 100) if cap > 0 else 0
            for occ, cap in zip(occupancies, capacities)
        ]

        return {
            "total_occupancy": sum(occupancies),
            "total_capacity": sum(capacities),
            "average_occupancy_percentage": statistics.mean(occupancy_percentages),
            "median_occupancy_percentage": statistics.median(occupancy_percentages),
            "max_occupancy_percentage": max(occupancy_percentages),
            "min_occupancy_percentage": min(occupancy_percentages),
            "buildings_analyzed": len(occupancies),
        }

    def analyze_water_consumption(self, buildings: List) -> Dict:
        """Analyze water consumption patterns"""
        if not buildings:
            return {}

        consumptions = [b.water_consumption_m3 for b in buildings if hasattr(b, 'water_consumption_m3')]

        if not consumptions:
            return {}

        return {
            "total_consumption_m3": sum(consumptions),
            "average_consumption_m3": statistics.mean(consumptions),
            "median_consumption_m3": statistics.median(consumptions),
            "max_consumption_m3": max(consumptions),
            "min_consumption_m3": min(consumptions),
            "buildings_analyzed": len(consumptions),
        }

    def analyze_waste_generation(self, buildings: List) -> Dict:
        """Analyze waste generation patterns"""
        if not buildings:
            return {}

        waste = [b.waste_generated_kg for b in buildings if hasattr(b, 'waste_generated_kg')]

        if not waste:
            return {}

        return {
            "total_waste_kg": sum(waste),
            "average_waste_kg": statistics.mean(waste),
            "median_waste_kg": statistics.median(waste),
            "max_waste_kg": max(waste),
            "min_waste_kg": min(waste),
            "buildings_analyzed": len(waste),
        }

    def analyze_air_quality(self, buildings: List) -> Dict:
        """Analyze air quality across buildings"""
        if not buildings:
            return {}

        aqi_values = [b.air_quality_index for b in buildings if hasattr(b, 'air_quality_index')]

        if not aqi_values:
            return {}

        return {
            "average_aqi": statistics.mean(aqi_values),
            "median_aqi": statistics.median(aqi_values),
            "max_aqi": max(aqi_values),
            "min_aqi": min(aqi_values),
            "buildings_analyzed": len(aqi_values),
            "poor_air_quality_count": sum(1 for aqi in aqi_values if aqi > 150),
            "moderate_air_quality_count": sum(1 for aqi in aqi_values if 50 < aqi <= 150),
            "good_air_quality_count": sum(1 for aqi in aqi_values if aqi <= 50),
        }

    def analyze_infrastructure_health(self, infrastructure: List) -> Dict:
        """Analyze overall infrastructure health"""
        if not infrastructure:
            return {}

        health_scores = [infra.calculate_health_score() for infra in infrastructure]
        utilizations = [infra.current_utilization for infra in infrastructure]
        uptimes = [infra.uptime_percentage for infra in infrastructure]

        if not health_scores:
            return {}

        return {
            "average_health_score": statistics.mean(health_scores),
            "median_health_score": statistics.median(health_scores),
            "min_health_score": min(health_scores),
            "max_health_score": max(health_scores),
            "average_utilization_percentage": statistics.mean(utilizations),
            "average_uptime_percentage": statistics.mean(uptimes),
            "infrastructure_assets_analyzed": len(health_scores),
            "critical_health_count": sum(1 for score in health_scores if score < 50),
            "warning_health_count": sum(1 for score in health_scores if 50 <= score < 80),
            "healthy_count": sum(1 for score in health_scores if score >= 80),
        }

    def analyze_thermal_comfort(self, buildings: List) -> Dict:
        """Analyze thermal comfort conditions"""
        if not buildings:
            return {}

        temperatures = [b.indoor_temperature_c for b in buildings if hasattr(b, 'indoor_temperature_c')]
        humidities = [b.indoor_humidity_percentage for b in buildings if hasattr(b, 'indoor_humidity_percentage')]

        if not temperatures:
            return {}

        return {
            "average_temperature_c": statistics.mean(temperatures),
            "median_temperature_c": statistics.median(temperatures),
            "max_temperature_c": max(temperatures),
            "min_temperature_c": min(temperatures),
            "average_humidity_percentage": statistics.mean(humidities),
            "median_humidity_percentage": statistics.median(humidities),
            "buildings_analyzed": len(temperatures),
            "comfortable_buildings": sum(
                1 for t, h in zip(temperatures, humidities)
                if 20 <= t <= 26 and 30 <= h <= 60
            ),
        }

    def generate_city_health_report(self, city) -> Dict:
        """Generate comprehensive city health report"""
        all_buildings = list(city.buildings.values())
        all_infrastructure = list(city.infrastructure.values())

        report = {
            "timestamp": datetime.utcnow().isoformat(),
            "city_name": city.config.name,
            "energy": self.analyze_energy_consumption(all_buildings),
            "occupancy": self.analyze_occupancy_patterns(all_buildings),
            "water": self.analyze_water_consumption(all_buildings),
            "waste": self.analyze_waste_generation(all_buildings),
            "air_quality": self.analyze_air_quality(all_buildings),
            "infrastructure": self.analyze_infrastructure_health(all_infrastructure),
            "thermal_comfort": self.analyze_thermal_comfort(all_buildings),
        }

        self.last_analysis = report
        return report

    def get_optimization_recommendations(self, analysis_report: Dict) -> List[Dict]:
        """Generate optimization recommendations based on analysis"""
        recommendations = []

        # Energy recommendations
        if analysis_report.get("energy", {}).get("renewable_percentage", 0) < 50:
            recommendations.append({
                "category": "Energy",
                "priority": "High",
                "recommendation": "Increase renewable energy generation capacity",
                "current_value": analysis_report.get("energy", {}).get("renewable_percentage", 0),
                "target_value": 50,
            })

        # Occupancy recommendations
        avg_occupancy = analysis_report.get("occupancy", {}).get("average_occupancy_percentage", 0)
        if avg_occupancy > 90:
            recommendations.append({
                "category": "Occupancy",
                "priority": "Medium",
                "recommendation": "Consider capacity expansion in high-occupancy buildings",
                "current_value": avg_occupancy,
                "target_value": 80,
            })

        # Air quality recommendations
        avg_aqi = analysis_report.get("air_quality", {}).get("average_aqi", 0)
        if avg_aqi > 100:
            recommendations.append({
                "category": "Air Quality",
                "priority": "High",
                "recommendation": "Implement air quality improvement measures",
                "current_value": avg_aqi,
                "target_value": 50,
            })

        # Infrastructure recommendations
        critical_infra = analysis_report.get("infrastructure", {}).get("critical_health_count", 0)
        if critical_infra > 0:
            recommendations.append({
                "category": "Infrastructure",
                "priority": "Critical",
                "recommendation": f"Address {critical_infra} critical infrastructure issues",
                "current_value": critical_infra,
                "target_value": 0,
            })

        return recommendations

    def __repr__(self) -> str:
        return f"AnalyticsEngine(created_at={self.created_at.isoformat()})"
