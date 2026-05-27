"""
Environmental Analytics for Northern Metropolis
Specialized analytics for environmental metrics from ENV-Twin.md
"""

from typing import Dict, List, Optional
from datetime import datetime
import statistics


class EnvironmentalAnalytics:
    """
    Analyzes environmental metrics specific to Northern Metropolis.
    Integrates with ENV-Twin.md metrics: air quality, water quality, climate, noise, biodiversity, carbon.
    """

    def __init__(self):
        """Initialize environmental analytics"""
        self.created_at = datetime.utcnow()
        self.metrics_history: List[Dict] = []

    def analyze_air_quality(self, zones: List) -> Dict:
        """
        Analyze air quality metrics across zones.
        Metrics: PM2.5, PM10, NO2, O3, SO2, CO
        """
        aqi_values = []
        pm25_values = []
        pm10_values = []
        no2_values = []
        o3_values = []

        for zone in zones:
            metrics = zone.environmental_metrics or {}
            if "air_quality_index" in metrics:
                aqi_values.append(metrics["air_quality_index"])
            if "pm25_ug_m3" in metrics:
                pm25_values.append(metrics["pm25_ug_m3"])
            if "pm10_ug_m3" in metrics:
                pm10_values.append(metrics["pm10_ug_m3"])
            if "no2_ppb" in metrics:
                no2_values.append(metrics["no2_ppb"])
            if "o3_ppb" in metrics:
                o3_values.append(metrics["o3_ppb"])

        analysis = {
            "zones_analyzed": len(zones),
            "timestamp": datetime.utcnow().isoformat(),
        }

        if aqi_values:
            analysis["aqi"] = {
                "average": round(statistics.mean(aqi_values), 2),
                "median": round(statistics.median(aqi_values), 2),
                "min": min(aqi_values),
                "max": max(aqi_values),
                "status": self._get_aqi_status(statistics.mean(aqi_values)),
            }

        if pm25_values:
            analysis["pm25_ug_m3"] = {
                "average": round(statistics.mean(pm25_values), 2),
                "median": round(statistics.median(pm25_values), 2),
                "min": round(min(pm25_values), 2),
                "max": round(max(pm25_values), 2),
                "who_guideline": 15.0,
                "exceeds_guideline": statistics.mean(pm25_values) > 15.0,
            }

        if pm10_values:
            analysis["pm10_ug_m3"] = {
                "average": round(statistics.mean(pm10_values), 2),
                "median": round(statistics.median(pm10_values), 2),
                "min": round(min(pm10_values), 2),
                "max": round(max(pm10_values), 2),
                "who_guideline": 45.0,
                "exceeds_guideline": statistics.mean(pm10_values) > 45.0,
            }

        return analysis

    def analyze_water_quality(self, zones: List) -> Dict:
        """
        Analyze water quality metrics across zones.
        Metrics: pH, dissolved oxygen, turbidity, conductivity, temperature
        """
        ph_values = []
        do_values = []
        turbidity_values = []
        conductivity_values = []
        temp_values = []

        for zone in zones:
            metrics = zone.environmental_metrics or {}
            if "water_ph" in metrics:
                ph_values.append(metrics["water_ph"])
            if "dissolved_oxygen_mg_l" in metrics:
                do_values.append(metrics["dissolved_oxygen_mg_l"])
            if "turbidity_ntu" in metrics:
                turbidity_values.append(metrics["turbidity_ntu"])
            if "conductivity_us_cm" in metrics:
                conductivity_values.append(metrics["conductivity_us_cm"])
            if "water_temperature_c" in metrics:
                temp_values.append(metrics["water_temperature_c"])

        analysis = {
            "zones_analyzed": len(zones),
            "timestamp": datetime.utcnow().isoformat(),
        }

        if ph_values:
            analysis["ph"] = {
                "average": round(statistics.mean(ph_values), 2),
                "median": round(statistics.median(ph_values), 2),
                "min": round(min(ph_values), 2),
                "max": round(max(ph_values), 2),
                "optimal_range": "6.5-8.5",
                "in_range": all(6.5 <= ph <= 8.5 for ph in ph_values),
            }

        if do_values:
            analysis["dissolved_oxygen_mg_l"] = {
                "average": round(statistics.mean(do_values), 2),
                "median": round(statistics.median(do_values), 2),
                "min": round(min(do_values), 2),
                "max": round(max(do_values), 2),
                "minimum_healthy": 5.0,
                "healthy": all(do >= 5.0 for do in do_values),
            }

        if turbidity_values:
            analysis["turbidity_ntu"] = {
                "average": round(statistics.mean(turbidity_values), 2),
                "median": round(statistics.median(turbidity_values), 2),
                "min": round(min(turbidity_values), 2),
                "max": round(max(turbidity_values), 2),
            }

        return analysis

    def analyze_climate_conditions(self, zones: List) -> Dict:
        """
        Analyze climate conditions across zones.
        Metrics: temperature, humidity, precipitation, wind speed
        """
        temp_values = []
        humidity_values = []
        precip_values = []
        wind_values = []

        for zone in zones:
            metrics = zone.environmental_metrics or {}
            if "temperature" in metrics:
                temp_values.append(metrics["temperature"])
            if "humidity_percentage" in metrics:
                humidity_values.append(metrics["humidity_percentage"])
            if "precipitation_mm" in metrics:
                precip_values.append(metrics["precipitation_mm"])
            if "wind_speed_kmh" in metrics:
                wind_values.append(metrics["wind_speed_kmh"])

        analysis = {
            "zones_analyzed": len(zones),
            "timestamp": datetime.utcnow().isoformat(),
        }

        if temp_values:
            analysis["temperature_c"] = {
                "average": round(statistics.mean(temp_values), 2),
                "median": round(statistics.median(temp_values), 2),
                "min": round(min(temp_values), 2),
                "max": round(max(temp_values), 2),
            }

        if humidity_values:
            analysis["humidity_percentage"] = {
                "average": round(statistics.mean(humidity_values), 2),
                "median": round(statistics.median(humidity_values), 2),
                "min": round(min(humidity_values), 2),
                "max": round(max(humidity_values), 2),
            }

        if precip_values:
            analysis["precipitation_mm"] = {
                "total": round(sum(precip_values), 2),
                "average": round(statistics.mean(precip_values), 2),
                "max": round(max(precip_values), 2),
            }

        if wind_values:
            analysis["wind_speed_kmh"] = {
                "average": round(statistics.mean(wind_values), 2),
                "median": round(statistics.median(wind_values), 2),
                "max": round(max(wind_values), 2),
            }

        return analysis

    def analyze_noise_levels(self, zones: List) -> Dict:
        """
        Analyze noise pollution levels across zones.
        Metrics: Leq (equivalent continuous sound level), Lmax, Lmin
        """
        leq_values = []
        lmax_values = []
        lmin_values = []

        for zone in zones:
            metrics = zone.environmental_metrics or {}
            if "noise_leq_db" in metrics:
                leq_values.append(metrics["noise_leq_db"])
            if "noise_lmax_db" in metrics:
                lmax_values.append(metrics["noise_lmax_db"])
            if "noise_lmin_db" in metrics:
                lmin_values.append(metrics["noise_lmin_db"])

        analysis = {
            "zones_analyzed": len(zones),
            "timestamp": datetime.utcnow().isoformat(),
        }

        if leq_values:
            avg_leq = statistics.mean(leq_values)
            analysis["leq_db"] = {
                "average": round(avg_leq, 2),
                "median": round(statistics.median(leq_values), 2),
                "min": round(min(leq_values), 2),
                "max": round(max(leq_values), 2),
                "who_guideline": 55.0,
                "exceeds_guideline": avg_leq > 55.0,
                "status": self._get_noise_status(avg_leq),
            }

        if lmax_values:
            analysis["lmax_db"] = {
                "average": round(statistics.mean(lmax_values), 2),
                "max": round(max(lmax_values), 2),
            }

        return analysis

    def analyze_biodiversity(self, zones: List) -> Dict:
        """
        Analyze biodiversity metrics across zones.
        Metrics: species count, habitat quality, green space percentage
        """
        biodiversity_indices = []
        species_counts = []
        green_space_percentages = []

        for zone in zones:
            metrics = zone.environmental_metrics or {}
            if "biodiversity_index" in metrics:
                biodiversity_indices.append(metrics["biodiversity_index"])
            if "species_count" in metrics:
                species_counts.append(metrics["species_count"])
            if "green_space_percentage" in metrics:
                green_space_percentages.append(metrics["green_space_percentage"])

        analysis = {
            "zones_analyzed": len(zones),
            "timestamp": datetime.utcnow().isoformat(),
        }

        if biodiversity_indices:
            analysis["biodiversity_index"] = {
                "average": round(statistics.mean(biodiversity_indices), 2),
                "median": round(statistics.median(biodiversity_indices), 2),
                "min": round(min(biodiversity_indices), 2),
                "max": round(max(biodiversity_indices), 2),
                "target": 0.8,
            }

        if species_counts:
            analysis["species_count"] = {
                "total": sum(species_counts),
                "average_per_zone": round(statistics.mean(species_counts), 0),
                "max": max(species_counts),
            }

        if green_space_percentages:
            analysis["green_space_percentage"] = {
                "average": round(statistics.mean(green_space_percentages), 2),
                "median": round(statistics.median(green_space_percentages), 2),
                "min": round(min(green_space_percentages), 2),
                "max": round(max(green_space_percentages), 2),
                "target": 30.0,
            }

        return analysis

    def analyze_carbon_emissions(self, zones: List) -> Dict:
        """
        Analyze carbon emissions and carbon footprint.
        Metrics: total emissions, per capita emissions, emissions by sector
        """
        total_emissions = []
        per_capita_emissions = []
        energy_emissions = []
        transport_emissions = []
        waste_emissions = []

        for zone in zones:
            metrics = zone.environmental_metrics or {}
            if "carbon_emissions_tons" in metrics:
                total_emissions.append(metrics["carbon_emissions_tons"])
            if "carbon_per_capita_kg" in metrics:
                per_capita_emissions.append(metrics["carbon_per_capita_kg"])
            if "energy_sector_emissions_tons" in metrics:
                energy_emissions.append(metrics["energy_sector_emissions_tons"])
            if "transport_sector_emissions_tons" in metrics:
                transport_emissions.append(metrics["transport_sector_emissions_tons"])
            if "waste_sector_emissions_tons" in metrics:
                waste_emissions.append(metrics["waste_sector_emissions_tons"])

        analysis = {
            "zones_analyzed": len(zones),
            "timestamp": datetime.utcnow().isoformat(),
        }

        if total_emissions:
            analysis["total_emissions_tons"] = {
                "total": round(sum(total_emissions), 2),
                "average_per_zone": round(statistics.mean(total_emissions), 2),
                "max": round(max(total_emissions), 2),
            }

        if per_capita_emissions:
            analysis["per_capita_emissions_kg"] = {
                "average": round(statistics.mean(per_capita_emissions), 2),
                "median": round(statistics.median(per_capita_emissions), 2),
                "target": 2000.0,
            }

        if energy_emissions or transport_emissions or waste_emissions:
            analysis["emissions_by_sector"] = {
                "energy_tons": round(sum(energy_emissions), 2) if energy_emissions else 0,
                "transport_tons": round(sum(transport_emissions), 2) if transport_emissions else 0,
                "waste_tons": round(sum(waste_emissions), 2) if waste_emissions else 0,
            }

        return analysis

    def generate_environmental_report(self, zones: List) -> Dict:
        """Generate comprehensive environmental report"""
        report = {
            "timestamp": datetime.utcnow().isoformat(),
            "zones_analyzed": len(zones),
            "air_quality": self.analyze_air_quality(zones),
            "water_quality": self.analyze_water_quality(zones),
            "climate": self.analyze_climate_conditions(zones),
            "noise": self.analyze_noise_levels(zones),
            "biodiversity": self.analyze_biodiversity(zones),
            "carbon": self.analyze_carbon_emissions(zones),
        }

        self.metrics_history.append(report)
        return report

    @staticmethod
    def _get_aqi_status(aqi: float) -> str:
        """Get air quality status based on AQI value"""
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
    def _get_noise_status(leq: float) -> str:
        """Get noise status based on Leq value"""
        if leq <= 50:
            return "Quiet"
        elif leq <= 55:
            return "Acceptable"
        elif leq <= 65:
            return "Noisy"
        elif leq <= 75:
            return "Very Noisy"
        else:
            return "Extremely Noisy"

    def __repr__(self) -> str:
        return f"EnvironmentalAnalytics(reports_generated={len(self.metrics_history)})"
