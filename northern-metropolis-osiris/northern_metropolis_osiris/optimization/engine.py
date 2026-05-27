"""
Optimization Engine for Northern Metropolis
Core optimization algorithms and decision support.
"""

from typing import Dict, List, Optional, Tuple
from datetime import datetime
from dataclasses import dataclass


@dataclass
class OptimizationResult:
    """Result of an optimization run"""
    timestamp: datetime
    optimization_type: str
    current_value: float
    optimized_value: float
    improvement_percentage: float
    recommendations: List[Dict]
    constraints_met: bool


class OptimizationEngine:
    """
    Main optimization engine for Northern Metropolis.
    Coordinates multi-objective optimization across energy, traffic, and sustainability.
    """

    def __init__(self):
        """Initialize optimization engine"""
        self.created_at = datetime.utcnow()
        self.optimization_history: List[OptimizationResult] = []
        self.active_optimizations: Dict[str, bool] = {}

    def optimize_energy_distribution(self, zones: List, target_renewable_percentage: float = 50.0) -> OptimizationResult:
        """
        Optimize energy distribution across zones.
        Balances renewable generation with demand.
        """
        total_consumption = sum(
            sum(b.energy_consumption_kwh for b in zone.buildings.values())
            for zone in zones
        )
        total_generation = sum(
            sum(b.renewable_energy_generation_kwh for b in zone.buildings.values())
            for zone in zones
        )

        current_renewable_percentage = (total_generation / total_consumption * 100) if total_consumption > 0 else 0
        
        recommendations = []
        if current_renewable_percentage < target_renewable_percentage:
            deficit = target_renewable_percentage - current_renewable_percentage
            additional_capacity_needed = (total_consumption * deficit) / 100
            
            recommendations.append({
                "action": "Increase renewable capacity",
                "capacity_needed_kw": additional_capacity_needed,
                "priority": "High" if deficit > 20 else "Medium",
            })

        improvement = target_renewable_percentage - current_renewable_percentage
        
        result = OptimizationResult(
            timestamp=datetime.utcnow(),
            optimization_type="Energy Distribution",
            current_value=current_renewable_percentage,
            optimized_value=target_renewable_percentage,
            improvement_percentage=improvement,
            recommendations=recommendations,
            constraints_met=current_renewable_percentage >= target_renewable_percentage,
        )

        self.optimization_history.append(result)
        return result

    def optimize_water_usage(self, zones: List, target_recycling_percentage: float = 40.0) -> OptimizationResult:
        """
        Optimize water usage and recycling across zones.
        """
        total_consumption = sum(
            sum(b.water_consumption_m3 for b in zone.buildings.values())
            for zone in zones
        )
        
        # Estimate current recycling (placeholder)
        current_recycling_percentage = 20.0
        
        recommendations = []
        if current_recycling_percentage < target_recycling_percentage:
            deficit = target_recycling_percentage - current_recycling_percentage
            additional_recycling_needed = (total_consumption * deficit) / 100
            
            recommendations.append({
                "action": "Expand water recycling infrastructure",
                "capacity_needed_m3_day": additional_recycling_needed,
                "priority": "High",
            })

        improvement = target_recycling_percentage - current_recycling_percentage
        
        result = OptimizationResult(
            timestamp=datetime.utcnow(),
            optimization_type="Water Usage",
            current_value=current_recycling_percentage,
            optimized_value=target_recycling_percentage,
            improvement_percentage=improvement,
            recommendations=recommendations,
            constraints_met=current_recycling_percentage >= target_recycling_percentage,
        )

        self.optimization_history.append(result)
        return result

    def optimize_waste_management(self, zones: List, target_diversion_rate: float = 60.0) -> OptimizationResult:
        """
        Optimize waste management and diversion rates.
        """
        total_waste = sum(
            sum(b.waste_generated_kg for b in zone.buildings.values())
            for zone in zones
        )
        
        # Estimate current diversion rate (placeholder)
        current_diversion_rate = 35.0
        
        recommendations = []
        if current_diversion_rate < target_diversion_rate:
            deficit = target_diversion_rate - current_diversion_rate
            
            recommendations.append({
                "action": "Implement comprehensive waste sorting program",
                "target_increase_percentage": deficit,
                "priority": "High",
            })
            
            recommendations.append({
                "action": "Expand composting facilities",
                "estimated_capacity_tons_day": (total_waste / 1000) * (deficit / 100),
                "priority": "Medium",
            })

        improvement = target_diversion_rate - current_diversion_rate
        
        result = OptimizationResult(
            timestamp=datetime.utcnow(),
            optimization_type="Waste Management",
            current_value=current_diversion_rate,
            optimized_value=target_diversion_rate,
            improvement_percentage=improvement,
            recommendations=recommendations,
            constraints_met=current_diversion_rate >= target_diversion_rate,
        )

        self.optimization_history.append(result)
        return result

    def optimize_green_space(self, zones: List, target_green_percentage: float = 30.0) -> OptimizationResult:
        """
        Optimize green space allocation across zones.
        """
        total_area = sum(zone.area_km2 for zone in zones)
        current_green_area = sum(
            zone.area_km2 * (zone.environmental_metrics.get("green_space_percentage", 0) / 100)
            for zone in zones
        )
        
        current_green_percentage = (current_green_area / total_area * 100) if total_area > 0 else 0
        
        recommendations = []
        if current_green_percentage < target_green_percentage:
            deficit = target_green_percentage - current_green_percentage
            additional_area_needed = (total_area * deficit) / 100
            
            recommendations.append({
                "action": "Expand green space",
                "area_needed_km2": additional_area_needed,
                "priority": "High",
            })

        improvement = target_green_percentage - current_green_percentage
        
        result = OptimizationResult(
            timestamp=datetime.utcnow(),
            optimization_type="Green Space",
            current_value=current_green_percentage,
            optimized_value=target_green_percentage,
            improvement_percentage=improvement,
            recommendations=recommendations,
            constraints_met=current_green_percentage >= target_green_percentage,
        )

        self.optimization_history.append(result)
        return result

    def multi_objective_optimization(self, city) -> Dict:
        """
        Perform multi-objective optimization across all domains.
        Returns balanced recommendations considering trade-offs.
        """
        zones = list(city.zones.values())
        
        energy_result = self.optimize_energy_distribution(zones)
        water_result = self.optimize_water_usage(zones)
        waste_result = self.optimize_waste_management(zones)
        green_result = self.optimize_green_space(zones)
        
        # Calculate overall optimization score
        all_constraints_met = all([
            energy_result.constraints_met,
            water_result.constraints_met,
            waste_result.constraints_met,
            green_result.constraints_met,
        ])
        
        average_improvement = (
            energy_result.improvement_percentage +
            water_result.improvement_percentage +
            waste_result.improvement_percentage +
            green_result.improvement_percentage
        ) / 4
        
        return {
            "timestamp": datetime.utcnow().isoformat(),
            "overall_optimization_score": average_improvement,
            "all_constraints_met": all_constraints_met,
            "energy": {
                "current": energy_result.current_value,
                "optimized": energy_result.optimized_value,
                "improvement": energy_result.improvement_percentage,
                "recommendations": energy_result.recommendations,
            },
            "water": {
                "current": water_result.current_value,
                "optimized": water_result.optimized_value,
                "improvement": water_result.improvement_percentage,
                "recommendations": water_result.recommendations,
            },
            "waste": {
                "current": waste_result.current_value,
                "optimized": waste_result.optimized_value,
                "improvement": waste_result.improvement_percentage,
                "recommendations": waste_result.recommendations,
            },
            "green_space": {
                "current": green_result.current_value,
                "optimized": green_result.optimized_value,
                "improvement": green_result.improvement_percentage,
                "recommendations": green_result.recommendations,
            },
        }

    def get_optimization_summary(self) -> Dict:
        """Get summary of all optimizations performed"""
        if not self.optimization_history:
            return {"message": "No optimizations performed yet"}

        total_improvements = sum(opt.improvement_percentage for opt in self.optimization_history)
        average_improvement = total_improvements / len(self.optimization_history)
        constraints_met_count = sum(1 for opt in self.optimization_history if opt.constraints_met)

        return {
            "total_optimizations": len(self.optimization_history),
            "average_improvement_percentage": round(average_improvement, 2),
            "constraints_met_percentage": round((constraints_met_count / len(self.optimization_history) * 100), 2),
            "optimization_types": list(set(opt.optimization_type for opt in self.optimization_history)),
            "last_optimization": self.optimization_history[-1].timestamp.isoformat() if self.optimization_history else None,
        }

    def __repr__(self) -> str:
        return f"OptimizationEngine(optimizations_performed={len(self.optimization_history)})"
