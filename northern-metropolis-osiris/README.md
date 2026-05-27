# Northern Metropolis OSIRIS AI
## Smart City Digital Twin for Hong Kong's Northern Metropolis Development

**Version:** 1.0.0  
**Status:** Initial Development  
**Last Updated:** 2026-05-27

---

## Overview

Northern Metropolis OSIRIS is a customized implementation of the OSIRIS AI framework specifically designed for Hong Kong's Northern Metropolis smart city development initiative. This project provides city-scale optimization, real-time analytics, and decision support for the 900+ km² development spanning four major zones:

- **Lok Ma Chau Loop** (87 km², 400K population)
- **Heung Yuen Wai** (150 km², 700K population)
- **Fanling/Sheung Shui** (200 km², 500K population)
- **Kwu Tung North** (150 km², 400K population)

### Key Features

✅ **City-Scale Optimization**
- Traffic signal timing optimization
- Energy load distribution optimization
- Cross-zone resource allocation
- Sustainability target tracking

✅ **Real-Time Analytics**
- Environmental monitoring (air, water, climate, noise, biodiversity)
- Zone-specific metrics
- Infrastructure performance tracking
- Sustainability metrics

✅ **Multi-Agent Simulation**
- Traffic flow simulation
- Pedestrian movement simulation
- Building energy consumption simulation
- Crowd dynamics

✅ **Integration Capabilities**
- Autodesk Tandem integration (building-level data)
- Unreal Engine integration (3D visualization)
- IoT sensor network integration (1M+ sensors)
- REST APIs and WebSocket support

✅ **Decision Support**
- AI-powered recommendations
- Policy impact analysis
- Scenario simulation
- What-if analysis

---

## Quick Start

### Prerequisites

- Python 3.8+
- PostgreSQL 12+
- Redis 6+
- Docker & Docker Compose (optional)

### Installation

```bash
# Clone the repository
git clone https://github.com/JonRodgers/Northern-Metropolis.git
cd northern-metropolis-osiris

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

### Basic Usage

```python
from northern_metropolis_osiris.core import NorthernMetropolis
from northern_metropolis_osiris.analytics import NorthernMetropolisAnalytics
from northern_metropolis_osiris.optimization import NorthernMetropolisOptimizer

# Create city
city = NorthernMetropolis()

# Create analytics engine
analytics = NorthernMetropolisAnalytics(city)

# Calculate metrics
metrics = analytics.calculate_city_metrics()
print(f"City Metrics: {metrics}")

# Create optimizer
optimizer = NorthernMetropolisOptimizer(city)

# Optimize traffic
traffic_opt = optimizer.optimize_cross_zone_traffic()
print(f"Traffic Optimization: {traffic_opt}")
```

### Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up -d

# Access API at http://localhost:8000
# Access Dashboard at http://localhost:3000
```

---

## Project Structure

```
northern-metropolis-osiris/
├── README.md
├── LICENSE
├── setup.py
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
├── .gitignore
├── .github/
│   └── workflows/
│       ├── tests.yml
│       └── deploy.yml
├── docs/
│   ├── ARCHITECTURE.md
│   ├── ZONES.md
│   ├── METRICS.md
│   ├── API.md
│   └── INTEGRATION.md
├── northern_metropolis_osiris/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── city.py
│   │   ├── zones.py
│   │   ├── buildings.py
│   │   └── infrastructure.py
│   ├── connectors/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── iot.py
│   │   ├── tandem.py
│   │   ├── unreal.py
│   │   └── environmental.py
│   ├── analytics/
│   │   ├── __init__.py
│   │   ├── engine.py
│   │   ├── environmental.py
│   │   ├── zone_analytics.py
│   │   └── metrics.py
│   ├── optimization/
│   │   ├── __init__.py
│   │   ├── engine.py
│   │   ├── traffic.py
│   │   ├── energy.py
│   │   └── sustainability.py
│   ├── simulation/
│   │   ├── __init__.py
│   │   ├── engine.py
│   │   ├── agents.py
│   │   └── physics.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── server.py
│   │   ├── routes.py
│   │   └── websocket.py
│   ├── dashboard/
│   │   ├── __init__.py
│   │   └── app.py
│   └── utils/
│       ├── __init__.py
│       ├── config.py
│       ├── logging.py
│       └── database.py
├── config/
│   ├── default.yaml
│   ├── development.yaml
│   ├── production.yaml
│   └── zones/
│       ├── lok_ma_chau.yaml
│       ├── heung_yuen_wai.yaml
│       ├── fanling_sheung_shui.yaml
│       └── kwu_tung_north.yaml
├── examples/
│   ├── basic_city.py
│   ├── zone_optimization.py
│   ├── cross_zone_analysis.py
│   └── env_twin_integration.py
├── tests/
│   ├── __init__.py
│   ├── test_core.py
│   ├── test_analytics.py
│   ├── test_optimization.py
│   └── test_integration.py
└── scripts/
    ├── setup_database.py
    ├── import_env_twin_data.py
    └── deploy.sh
```

---

## Development Roadmap

### Phase 1: Foundation (Week 1-2) ✅
- [x] Project structure setup
- [x] Core city and zone models
- [x] Basic configuration system
- [x] README and documentation

### Phase 2: Core Modules (Week 3-4)
- [ ] Analytics engine implementation
- [ ] Environmental metrics integration
- [ ] Zone-specific analytics
- [ ] Unit tests

### Phase 3: Optimization (Week 5-6)
- [ ] Traffic optimization module
- [ ] Energy optimization module
- [ ] Sustainability optimization
- [ ] Performance testing

### Phase 4: Integration (Week 7-8)
- [ ] Tandem connector
- [ ] Unreal Engine connector
- [ ] IoT connector
- [ ] Integration testing

### Phase 5: API & Dashboard (Week 9-10)
- [ ] REST API implementation
- [ ] WebSocket support
- [ ] Dashboard UI
- [ ] Documentation

---

## Configuration

### Main Configuration (config/default.yaml)

```yaml
city:
  name: "Northern Metropolis"
  id: "northern_metropolis"
  location:
    latitude: 22.5
    longitude: 114.0
  area_km2: 900
  planned_population: 2500000

zones:
  - name: "Lok Ma Chau Loop"
    id: "lok_ma_chau"
    area_km2: 87
    planned_population: 400000
    planned_buildings: 5000
  
  - name: "Heung Yuen Wai"
    id: "heung_yuen_wai"
    area_km2: 150
    planned_population: 700000
    planned_buildings: 8000
  
  - name: "Fanling/Sheung Shui"
    id: "fanling_sheung_shui"
    area_km2: 200
    planned_population: 500000
    planned_buildings: 6000
  
  - name: "Kwu Tung North"
    id: "kwu_tung_north"
    area_km2: 150
    planned_population: 400000
    planned_buildings: 5000

sustainability_targets:
  carbon_neutral_year: 2050
  renewable_energy_target: 60
  green_space_target: 30
  waste_diversion_target: 90

data_sources:
  iot:
    broker_url: "mqtt.northern-metropolis.local"
    port: 1883
  
  tandem:
    url: "https://tandem.autodesk.com/api"
    project_id: "northern_metropolis"
  
  unreal:
    url: "http://localhost"
    port: 8080
```

---

## API Endpoints

### Analytics Endpoints

```
GET  /api/v1/metrics/city          - Get city-wide metrics
GET  /api/v1/metrics/zones         - Get zone-specific metrics
GET  /api/v1/metrics/environmental - Get environmental metrics
GET  /api/v1/metrics/sustainability - Get sustainability metrics
```

### Optimization Endpoints

```
POST /api/v1/optimize/traffic      - Optimize traffic
POST /api/v1/optimize/energy       - Optimize energy
POST /api/v1/optimize/sustainability - Optimize sustainability
```

### Simulation Endpoints

```
POST /api/v1/simulate/traffic      - Simulate traffic
POST /api/v1/simulate/energy       - Simulate energy
POST /api/v1/simulate/scenario     - Simulate scenario
```

---

## Integration

### Autodesk Tandem Integration

```python
from northern_metropolis_osiris.connectors import TandemConnector

connector = TandemConnector(
    tandem_url="https://tandem.autodesk.com/api",
    api_key="your_api_key",
    project_id="northern_metropolis"
)

buildings = connector.fetch_buildings()
```

### Unreal Engine Integration

```python
from northern_metropolis_osiris.connectors import UnrealConnector

connector = UnrealConnector(
    unreal_url="localhost",
    port=8080
)

connector.connect()
connector.send_data({
    'type': 'city_metrics',
    'data': metrics
})
```

### IoT Integration

```python
from northern_metropolis_osiris.connectors import IoTConnector

connector = IoTConnector(
    broker_url="mqtt.northern-metropolis.local",
    port=1883
)

connector.connect()
connector.subscribe("sensors/+/data")
```

---

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

```bash
# Clone repository
git clone https://github.com/JonRodgers/Northern-Metropolis.git
cd northern-metropolis-osiris

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Run linting
flake8 northern_metropolis_osiris
black northern_metropolis_osiris
```

---

## License

Apache License 2.0 - See [LICENSE](LICENSE) file for details

---

## Contact & Support

- **Project Lead:** Jon Rodgers
- **GitHub:** https://github.com/JonRodgers/Northern-Metropolis
- **Issues:** https://github.com/JonRodgers/Northern-Metropolis/issues
- **Discussions:** https://github.com/JonRodgers/Northern-Metropolis/discussions

---

## Acknowledgments

- Based on [OSIRIS AI](https://github.com/simplifaisoul/osiris) framework
- Inspired by smart city initiatives in Singapore, Dubai, and Barcelona
- Environmental metrics from Northern Metropolis ENV-Twin project
- Integration with Autodesk Tandem and Unreal Engine

---

**Last Updated:** 2026-05-27  
**Status:** Initial Development Phase  
**Next Milestone:** Phase 2 - Core Modules Implementation
