/**
 * Northern Metropolis OSIRIS - Web Server
 * Simple Node.js server for hosting the interactive globe visualization
 * 
 * Usage:
 *   npm install express cors
 *   node server.js
 * 
 * Access at: http://localhost:3000
 */

const express = require('express');
const cors = require('cors');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 3000;
const HOST = process.env.HOST || 'localhost';

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname)));

// Logging middleware
app.use((req, res, next) => {
    console.log(`[${new Date().toISOString()}] ${req.method} ${req.path}`);
    next();
});

// Routes

// Serve main page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Serve globe script
app.get('/globe.js', (req, res) => {
    res.sendFile(path.join(__dirname, 'globe.js'));
});

// API endpoint: City summary
app.get('/api/v1/city', (req, res) => {
    res.json({
        name: 'Northern Metropolis',
        country: 'Hong Kong',
        region: 'New Territories',
        coordinates: {
            latitude: 22.5,
            longitude: 114.1
        },
        total_area_km2: 300,
        target_population: 2500000,
        zones: 4,
        buildings: 9500,
        infrastructure_assets: 7,
        timestamp: new Date().toISOString()
    });
});

// API endpoint: Analytics health report
app.get('/api/v1/analytics/health', (req, res) => {
    res.json({
        timestamp: new Date().toISOString(),
        city_name: 'Northern Metropolis',
        energy: {
            total_consumption_kwh: 5000000,
            average_consumption_kwh: 526315,
            total_renewable_generation_kwh: 2250000,
            renewable_percentage: 45,
            buildings_analyzed: 9500
        },
        occupancy: {
            total_occupancy: 1750000,
            total_capacity: 2500000,
            average_occupancy_percentage: 70,
            buildings_analyzed: 9500
        },
        water: {
            total_consumption_m3: 125000,
            average_consumption_m3: 13.16,
            buildings_analyzed: 9500
        },
        waste: {
            total_waste_kg: 450000,
            average_waste_kg: 47.37,
            buildings_analyzed: 9500
        },
        air_quality: {
            average_aqi: 65,
            median_aqi: 62,
            max_aqi: 150,
            min_aqi: 30,
            poor_air_quality_count: 50,
            moderate_air_quality_count: 4500,
            good_air_quality_count: 4950
        },
        infrastructure: {
            average_health_score: 82.5,
            median_health_score: 85,
            min_health_score: 45,
            max_health_score: 98,
            average_utilization_percentage: 65,
            average_uptime_percentage: 99.2,
            infrastructure_assets_analyzed: 7,
            critical_health_count: 0,
            warning_health_count: 1,
            healthy_count: 6
        },
        thermal_comfort: {
            average_temperature_c: 22.5,
            median_temperature_c: 22,
            max_temperature_c: 28,
            min_temperature_c: 18,
            average_humidity_percentage: 65,
            median_humidity_percentage: 63,
            buildings_analyzed: 9500,
            comfortable_buildings: 7125
        }
    });
});

// API endpoint: Zone details
app.get('/api/v1/zones/:zone_id', (req, res) => {
    const zones = {
        'lok_ma_chau_loop': {
            id: 'lok_ma_chau_loop',
            name: 'Lok Ma Chau Loop',
            type: 'Development Zone',
            location: { latitude: 22.5167, longitude: 114.0167 },
            area_km2: 87,
            population: 195000,
            target_population: 650000,
            buildings: 2500,
            planned_buildings: 2500,
            infrastructure_assets: 2,
            environmental_metrics: {
                air_quality_index: 62,
                temperature: 23,
                humidity_percentage: 65,
                green_space_percentage: 35,
                biodiversity_index: 0.72,
                carbon_emissions_tons: 125000
            }
        },
        'heung_yuen_wai': {
            id: 'heung_yuen_wai',
            name: 'Heung Yuen Wai',
            type: 'Development Zone',
            location: { latitude: 22.4833, longitude: 114.0833 },
            area_km2: 75,
            population: 165000,
            target_population: 550000,
            buildings: 2000,
            planned_buildings: 2000,
            infrastructure_assets: 2,
            environmental_metrics: {
                air_quality_index: 68,
                temperature: 22.8,
                humidity_percentage: 64,
                green_space_percentage: 32,
                biodiversity_index: 0.68,
                carbon_emissions_tons: 110000
            }
        },
        'fanling_sheung_shui': {
            id: 'fanling_sheung_shui',
            name: 'Fanling/Sheung Shui',
            type: 'Development Zone',
            location: { latitude: 22.5, longitude: 114.15 },
            area_km2: 85,
            population: 210000,
            target_population: 700000,
            buildings: 2800,
            planned_buildings: 2800,
            infrastructure_assets: 2,
            environmental_metrics: {
                air_quality_index: 63,
                temperature: 22.2,
                humidity_percentage: 66,
                green_space_percentage: 30,
                biodiversity_index: 0.70,
                carbon_emissions_tons: 140000
            }
        },
        'kwutung_north': {
            id: 'kwutung_north',
            name: 'Kwu Tung North',
            type: 'Development Zone',
            location: { latitude: 22.45, longitude: 114.1167 },
            area_km2: 53,
            population: 180000,
            target_population: 600000,
            buildings: 2200,
            planned_buildings: 2200,
            infrastructure_assets: 1,
            environmental_metrics: {
                air_quality_index: 65,
                temperature: 23.1,
                humidity_percentage: 63,
                green_space_percentage: 28,
                biodiversity_index: 0.65,
                carbon_emissions_tons: 105000
            }
        }
    };

    const zone = zones[req.params.zone_id];
    if (zone) {
        res.json(zone);
    } else {
        res.status(404).json({ error: 'Zone not found' });
    }
});

// API endpoint: Optimization results
app.get('/api/v1/optimization/results', (req, res) => {
    res.json({
        timestamp: new Date().toISOString(),
        overall_optimization_score: 72.5,
        all_constraints_met: false,
        energy: {
            current: 45,
            optimized: 50,
            improvement: 5,
            recommendations: [
                {
                    action: 'Increase renewable capacity',
                    capacity_needed_kw: 250000,
                    priority: 'High',
                    implementation_time_months: 12
                }
            ]
        },
        water: {
            current: 20,
            optimized: 40,
            improvement: 20,
            recommendations: [
                {
                    action: 'Expand water recycling infrastructure',
                    capacity_needed_m3_day: 5000,
                    priority: 'High',
                    implementation_time_months: 18
                }
            ]
        },
        waste: {
            current: 35,
            optimized: 60,
            improvement: 25,
            recommendations: [
                {
                    action: 'Implement comprehensive waste sorting program',
                    target_increase_percentage: 25,
                    priority: 'High',
                    implementation_time_months: 6
                }
            ]
        },
        green_space: {
            current: 31,
            optimized: 30,
            improvement: -1,
            recommendations: []
        }
    });
});

// API endpoint: KPI metrics
app.get('/api/v1/metrics/kpi', (req, res) => {
    res.json({
        timestamp: new Date().toISOString(),
        kpis: {
            renewable_energy_percentage: 45 + Math.random() * 10,
            green_space_percentage: 31 + Math.random() * 5,
            air_quality_index: 65 - Math.random() * 20,
            sustainability_score: 72 + Math.random() * 10,
            livability_index: 78 + Math.random() * 10,
            smart_city_maturity: 65 + Math.random() * 15,
            economic_vitality: 75 + Math.random() * 10
        }
    });
});

// Health check endpoint
app.get('/health', (req, res) => {
    res.json({
        status: 'healthy',
        timestamp: new Date().toISOString(),
        uptime: process.uptime()
    });
});

// 404 handler
app.use((req, res) => {
    res.status(404).json({ error: 'Not found' });
});

// Error handler
app.use((err, req, res, next) => {
    console.error('Error:', err);
    res.status(500).json({ error: 'Internal server error' });
});

// Start server
app.listen(PORT, HOST, () => {
    console.log(`
╔════════════════════════════════════════════════════════════╗
║   Northern Metropolis OSIRIS - Web Server                  ║
╚════════════════════════════════════════════════════════════╝

🌍 Server running at: http://${HOST}:${PORT}
📍 Globe visualization: http://${HOST}:${PORT}/
📊 API endpoints:
   - GET  /api/v1/city
   - GET  /api/v1/analytics/health
   - GET  /api/v1/zones/{zone_id}
   - GET  /api/v1/optimization/results
   - GET  /api/v1/metrics/kpi
   - GET  /health

Press Ctrl+C to stop the server
    `);
});

// Graceful shutdown
process.on('SIGINT', () => {
    console.log('\n\nShutting down gracefully...');
    process.exit(0);
});

process.on('SIGTERM', () => {
    console.log('\n\nShutting down gracefully...');
    process.exit(0);
});
