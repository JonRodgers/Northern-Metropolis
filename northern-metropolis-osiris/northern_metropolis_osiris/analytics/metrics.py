"""
Metrics Calculator for Northern Metropolis
Calculates KPIs, sustainability metrics, and performance indicators.
"""

from typing import Dict, List, Optional, Tuple
from datetime import datetime
import statistics


class MetricsCalculator:
    """
    Calculates various metrics and KPIs for the Northern Metropolis digital twin.
    Includes sustainability metrics, efficiency ratios, and performance indicators.
    """

    def __init__(self):
        """Initialize metrics calculator"""
        self.created_at = datetime.utcnow()
        self.calculation_history: List[Dict] = []

    def calculate_energy_efficiency_ratio(self, total_consumption_kwh: float, renewable_generation_kwh: float) -> float:
        """Calculate energy efficiency ratio (renewable/total)"""
        if total_consumption_kwh == 0:
            return 0.0
        return (renewable_generation_kwh / total_consumption_kwh) * 100

    def calculate_carbon_intensity(self, carbon_emissions_tons: float, gdp_or_population: float) -> float:
        """Calculate carbon intensity (emissions per unit of GDP or population)"""
        if gdp_or_population == 0:
            return 0.0
        return carbon_emissions_tons / gdp_or_population

    def calculate_water_stress_index(self, water_consumption_m3: float, water_availability_m3: float) -> float:
        """Calculate water stress index"""
        if water_availability_m3 == 0:
            return 0.0
        return (water_consumption_m3 / water_availability_m3) * 100

    def calculate_waste_diversion_rate(self, waste_diverted_kg: float, total_waste_kg: float) -> float:
        """Calculate waste diversion rate (recycled/composted percentage)"""
        if total_waste_kg == 0:
            return 0.0
        return (waste_diverted_kg / total_waste_kg) * 100

    def calculate_green_space_ratio(self, green_space_area_km2: float, total_area_km2: float) -> float:
        """Calculate green space ratio"""
        if total_area_km2 == 0:
            return 0.0
        return (green_space_area_km2 / total_area_km2) * 100

    def calculate_walkability_score(self, pedestrian_infrastructure_km: float, total_area_km2: float) -> float:
        """Calculate walkability score based on pedestrian infrastructure density"""
        if total_area_km2 == 0:
            return 0.0
        density = pedestrian_infrastructure_km / total_area_km2
        # Normalize to 0-100 scale (assuming 50 km/km2 is excellent)
        return min(100.0, (density / 50) * 100)

    def calculate_transit_accessibility(self, transit_stops: int, population: int) -> float:
        """Calculate transit accessibility (people per transit stop)"""
        if transit_stops == 0:
            return 0.0
        return population / transit_stops

    def calculate_building_energy_performance(self, consumption_kwh: float, floor_area_m2: float) -> float:
        """Calculate building energy performance (kWh per m2)"""
        if floor_area_m2 == 0:
            return 0.0
        return consumption_kwh / floor_area_m2

    def calculate_occupancy_efficiency(self, current_occupancy: int, capacity: int) -> float:
        """Calculate occupancy efficiency percentage"""
        if capacity == 0:
            return 0.0
        return (current_occupancy / capacity) * 100

    def calculate_infrastructure_resilience_score(self, uptime_percentage: float, redundancy_factor: float) -> float:
        """Calculate infrastructure resilience score"""
        # Weighted combination of uptime and redundancy
        return (uptime_percentage * 0.7) + (redundancy_factor * 30)

    def calculate_air_quality_health_impact(self, aqi: float) -> Dict[str, any]:
        """Calculate health impact based on air quality index"""
        health_impacts = {
            "aqi": aqi,
            "category": self._get_aqi_category(aqi),
            "health_risk": self._get_health_risk(aqi),
            "vulnerable_population_risk": self._get_vulnerable_risk(aqi),
        }
        return health_impacts

    def calculate_thermal_comfort_index(self, temperature_c: float, humidity_percentage: float) -> float:
        """Calculate thermal comfort index (0-100)"""
        # Optimal range: 20-26°C, 30-60% humidity
        temp_score = 100 - abs(temperature_c - 23) * 5  # Peak at 23°C
        humidity_score = 100 - abs(humidity_percentage - 45) * 2  # Peak at 45%
        
        # Weighted average
        comfort_index = (temp_score * 0.6 + humidity_score * 0.4)
        return max(0.0, min(100.0, comfort_index))

    def calculate_sustainability_index(self, metrics: Dict) -> float:
        """
        Calculate overall sustainability index (0-100).
        Combines multiple environmental and social metrics.
        """
        components = []
        weights = []

        # Energy sustainability (20%)
        if "renewable_energy_percentage" in metrics:
            components.append(metrics["renewable_energy_percentage"])
            weights.append(0.20)

        # Water sustainability (15%)
        if "water_recycling_percentage" in metrics:
            components.append(metrics["water_recycling_percentage"])
            weights.append(0.15)

        # Waste management (15%)
        if "waste_diversion_rate" in metrics:
            components.append(metrics["waste_diversion_rate"])
            weights.append(0.15)

        # Green space (15%)
        if "green_space_percentage" in metrics:
            components.append(metrics["green_space_percentage"])
            weights.append(0.15)

        # Air quality (15%)
        if "air_quality_score" in metrics:
            components.append(metrics["air_quality_score"])
            weights.append(0.15)

        # Biodiversity (10%)
        if "biodiversity_index" in metrics:
            components.append(metrics["biodiversity_index"] * 100)  # Normalize to 0-100
            weights.append(0.10)

        if not components:
            return 0.0

        # Weighted average
        total_weight = sum(weights)
        weighted_sum = sum(c * w for c, w in zip(components, weights))
        
        return weighted_sum / total_weight if total_weight > 0 else 0.0

    def calculate_livability_index(self, metrics: Dict) -> float:
        """
        Calculate livability index (0-100).
        Combines housing, safety, healthcare, education, and environmental factors.
        """
        components = []
        weights = []

        # Housing affordability (20%)
        if "housing_affordability_ratio" in metrics:
            # Lower ratio is better (inverse scoring)
            affordability_score = max(0, 100 - metrics["housing_affordability_ratio"])
            components.append(affordability_score)
            weights.append(0.20)

        # Safety (20%)
        if "crime_rate_per_100k" in metrics:
            # Lower crime is better
            safety_score = max(0, 100 - (metrics["crime_rate_per_100k"] / 100))
            components.append(safety_score)
            weights.append(0.20)

        # Healthcare access (15%)
        if "healthcare_accessibility_score" in metrics:
            components.append(metrics["healthcare_accessibility_score"])
            weights.append(0.15)

        # Education (15%)
        if "education_quality_score" in metrics:
            components.append(metrics["education_quality_score"])
            weights.append(0.15)

        # Environmental quality (15%)
        if "environmental_quality_score" in metrics:
            components.append(metrics["environmental_quality_score"])
            weights.append(0.15)

        # Walkability (15%)
        if "walkability_score" in metrics:
            components.append(metrics["walkability_score"])
            weights.append(0.15)

        if not components:
            return 0.0

        total_weight = sum(weights)
        weighted_sum = sum(c * w for c, w in zip(components, weights))
        
        return weighted_sum / total_weight if total_weight > 0 else 0.0

    def calculate_smart_city_maturity(self, metrics: Dict) -> float:
        """
        Calculate smart city maturity level (0-100).
        Based on digital integration, IoT coverage, and data analytics capabilities.
        """
        components = []
        weights = []

        # IoT sensor coverage (25%)
        if "iot_coverage_percentage" in metrics:
            components.append(metrics["iot_coverage_percentage"])
            weights.append(0.25)

        # Building management system integration (20%)
        if "bms_integration_percentage" in metrics:
            components.append(metrics["bms_integration_percentage"])
            weights.append(0.20)

        # Digital twin coverage (20%)
        if "digital_twin_coverage_percentage" in metrics:
            components.append(metrics["digital_twin_coverage_percentage"])
            weights.append(0.20)

        # Real-time data availability (15%)
        if "real_time_data_percentage" in metrics:
            components.append(metrics["real_time_data_percentage"])
            weights.append(0.15)

        # Analytics and AI capability (20%)
        if "analytics_capability_score" in metrics:
            components.append(metrics["analytics_capability_score"])
            weights.append(0.20)

        if not components:
            return 0.0

        total_weight = sum(weights)
        weighted_sum = sum(c * w for c, w in zip(components, weights))
        
        return weighted_sum / total_weight if total_weight > 0 else 0.0

    def calculate_economic_vitality_index(self, metrics: Dict) -> float:
        """
        Calculate economic vitality index (0-100).
        Based on employment, business diversity, and economic growth.
        """
        components = []
        weights = []

        # Employment rate (25%)
        if "employment_rate_percentage" in metrics:
            components.append(metrics["employment_rate_percentage"])
            weights.append(0.25)

        # Business diversity (20%)
        if "business_diversity_score" in metrics:
            components.append(metrics["business_diversity_score"])
            weights.append(0.20)

        # GDP growth (20%)
        if "gdp_growth_percentage" in metrics:
            # Normalize to 0-100 (assuming 10% is excellent)
            gdp_score = min(100, metrics["gdp_growth_percentage"] * 10)
            components.append(gdp_score)
            weights.append(0.20)

        # Innovation index (20%)
        if "innovation_score" in metrics:
            components.append(metrics["innovation_score"])
            weights.append(0.20)

        # Startup ecosystem (15%)
        if "startup_ecosystem_score" in metrics:
            components.append(metrics["startup_ecosystem_score"])
            weights.append(0.15)

        if not components:
            return 0.0

        total_weight = sum(weights)
        weighted_sum = sum(c * w for c, w in zip(components, weights))
        
        return weighted_sum / total_weight if total_weight > 0 else 0.0

    @staticmethod
    def _get_aqi_category(aqi: float) -> str:
        """Get AQI category"""
        if aqi <= 50:
            return "Good"
        elif aqi <= 100:
            return "Moderate"
        elif aqi <= 150:
            return "Unhealthy for Sensitive Groups"
        elif aqi <= 200:
            return "Unhealthy"
        elif aqi <= 300:
            return "Very Unhealthy"
        else:
            return "Hazardous"

    @staticmethod
    def _get_health_risk(aqi: float) -> str:
        """Get health risk level"""
        if aqi <= 50:
            return "None"
        elif aqi <= 100:
            return "Low"
        elif aqi <= 150:
            return "Moderate"
        elif aqi <= 200:
            return "High"
        else:
            return "Very High"

    @staticmethod
    def _get_vulnerable_risk(aqi: float) -> str:
        """Get risk level for vulnerable populations"""
        if aqi <= 50:
            return "None"
        elif aqi <= 100:
            return "Low"
        elif aqi <= 150:
            return "High"
        else:
            return "Very High"

    def record_calculation(self, metric_name: str, value: float, metadata: Optional[Dict] = None) -> None:
        """Record a metric calculation"""
        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "metric_name": metric_name,
            "value": value,
            "metadata": metadata or {},
        }
        self.calculation_history.append(record)

    def __repr__(self) -> str:
        return f"MetricsCalculator(calculations_recorded={len(self.calculation_history)})"
