# Northern Metropolis OSIRIS - Deployment Guide

## Quick Start

### Prerequisites
- Python 3.8+
- Docker & Docker Compose (for containerized deployment)
- Git
- 4GB RAM minimum
- 10GB disk space

### Local Development Setup

```bash
# 1. Clone the repository
git clone https://github.com/JonRodgers/Northern-Metropolis.git
cd northern-metropolis-osiris

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Install in development mode
pip install -e .

# 6. Run example
python examples/basic_city_setup.py
```

### Docker Deployment

```bash
# 1. Build and start all services
docker-compose up -d

# 2. Check service status
docker-compose ps

# 3. View logs
docker-compose logs -f osiris-api

# 4. Access services
# API: http://localhost:8000
# Grafana: http://localhost:3000 (admin/admin)
# Prometheus: http://localhost:9090
# MQTT: localhost:1883
# PostgreSQL: localhost:5432
# Redis: localhost:6379
```

## Project Structure Overview

```
northern-metropolis-osiris/
├── northern_metropolis_osiris/          # Main Python package
│   ├── core/                            # City models (4 zones, buildings, infrastructure)
│   ├── analytics/                       # Analytics engines (energy, environmental, metrics)
│   ├── optimization/                    # Optimization algorithms (traffic, energy, sustainability)
│   └── connectors/                      # External integrations (IoT, Tandem, Unreal, Environmental)
├── examples/                            # Example scripts
├── tests/                               # Unit tests (to be added)
├── docs/                                # Documentation (to be added)
├── setup.py                             # Package configuration
├── requirements.txt                     # Python dependencies
├── Dockerfile                           # Docker image definition
├── docker-compose.yml                   # Multi-container setup
├── README.md                            # Project overview
├── PROJECT_STATUS.md                    # Development status
└── DEPLOYMENT_GUIDE.md                  # This file
```

## Module Descriptions

### Core Module (`northern_metropolis_osiris/core/`)
Defines the fundamental city models:
- **city.py:** NorthernMetropolis class managing zones, buildings, infrastructure
- **zones.py:** 4 development zones with realistic parameters
- **buildings.py:** Building models with energy/environmental tracking
- **infrastructure.py:** Critical infrastructure assets (power, water, renewable energy, etc.)

### Analytics Module (`northern_metropolis_osiris/analytics/`)
Provides comprehensive analytics:
- **engine.py:** Main analytics engine for multi-metric analysis
- **environmental.py:** Environmental metrics (air, water, climate, noise, biodiversity, carbon)
- **zone_analytics.py:** Zone-level performance analysis
- **metrics.py:** KPI calculations (sustainability, livability, smart city maturity)

### Optimization Module (`northern_metropolis_osiris/optimization/`)
Implements optimization algorithms:
- **engine.py:** Multi-objective optimization coordinator
- **traffic.py:** Traffic flow and mobility optimization
- **energy.py:** Energy efficiency and renewable optimization
- **sustainability.py:** Circular economy and environmental optimization

### Connectors Module (`northern_metropolis_osiris/connectors/`)
Integrates external systems:
- **base.py:** Abstract base connector class
- **iot.py:** IoT sensor networks (MQTT protocol)
- **tandem.py:** Autodesk Tandem building models
- **unreal.py:** Unreal Engine 3D visualization
- **environmental.py:** Environmental data sources

## Configuration

### Environment Variables
Create `.env` file in project root:

```env
# Database
DATABASE_URL=postgresql://osiris:password@localhost:5432/northern_metropolis

# Cache
REDIS_URL=redis://localhost:6379

# IoT
MQTT_BROKER=localhost
MQTT_PORT=1883

# Logging
LOG_LEVEL=INFO

# API
API_HOST=0.0.0.0
API_PORT=8000
```

### Zone Configuration
Zones are pre-configured with realistic parameters:

| Zone | Area (km²) | Target Population | Buildings | Green Space |
|------|-----------|------------------|-----------|------------|
| Lok Ma Chau Loop | 87 | 650,000 | 2,500 | 35% |
| Heung Yuen Wai | 75 | 550,000 | 2,000 | 32% |
| Fanling/Sheung Shui | 85 | 700,000 | 2,800 | 30% |
| Kwu Tung North | 53 | 600,000 | 2,200 | 28% |

## Running Examples

### Basic City Setup
```bash
python examples/basic_city_setup.py
```
Demonstrates:
- City initialization
- Zone creation
- Building addition
- Metrics calculation
- Analytics generation
- Optimization execution

### Integration Example
```bash
python examples/integration_example.py
```
Demonstrates:
- IoT connector setup
- Tandem integration
- Unreal Engine connection
- Environmental data fetching
- Multi-system synchronization

## API Endpoints (Planned)

Once API module is implemented:

```
GET  /api/v1/city                    # Get city summary
GET  /api/v1/zones                   # List all zones
GET  /api/v1/zones/{zone_id}         # Get zone details
GET  /api/v1/buildings               # List buildings
GET  /api/v1/buildings/{building_id} # Get building details
GET  /api/v1/analytics/health        # City health report
GET  /api/v1/optimization/results    # Optimization results
POST /api/v1/optimization/run        # Run optimization
WS   /ws/realtime                    # WebSocket for real-time updates
```

## Monitoring & Logging

### Prometheus Metrics
Access at `http://localhost:9090`
- City metrics
- Building metrics
- Infrastructure health
- API performance

### Grafana Dashboards
Access at `http://localhost:3000`
- City overview
- Zone performance
- Energy consumption
- Environmental metrics
- Infrastructure status

### Application Logs
```bash
# View logs
docker-compose logs -f osiris-api

# Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
```

## Database Management

### PostgreSQL
```bash
# Connect to database
psql -h localhost -U osiris -d northern_metropolis

# Useful commands
\dt                    # List tables
\d table_name          # Describe table
SELECT * FROM table;   # Query data
```

### Redis Cache
```bash
# Connect to Redis
redis-cli

# Useful commands
KEYS *                 # List all keys
GET key_name           # Get value
FLUSHDB                # Clear database
```

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=northern_metropolis_osiris

# Run specific test file
pytest tests/test_core.py

# Run with verbose output
pytest -v
```

## Code Quality

```bash
# Format code
black northern_metropolis_osiris/

# Lint code
flake8 northern_metropolis_osiris/

# Type checking
mypy northern_metropolis_osiris/

# Sort imports
isort northern_metropolis_osiris/
```

## Troubleshooting

### Port Already in Use
```bash
# Find process using port
lsof -i :8000

# Kill process
kill -9 <PID>
```

### Database Connection Error
```bash
# Check PostgreSQL is running
docker-compose ps postgres

# Restart PostgreSQL
docker-compose restart postgres
```

### MQTT Connection Issues
```bash
# Check Mosquitto is running
docker-compose ps mosquitto

# Test MQTT connection
mosquitto_sub -h localhost -t "test"
```

### Memory Issues
```bash
# Increase Docker memory limit
# Edit docker-compose.yml and add:
# services:
#   osiris-api:
#     mem_limit: 2g
```

## Performance Optimization

### Database
- Add indexes on frequently queried columns
- Use connection pooling
- Archive old metrics data

### Caching
- Enable Redis caching for analytics results
- Cache zone summaries
- Cache optimization results

### API
- Implement pagination for large datasets
- Use compression for responses
- Add rate limiting

## Security Considerations

### Before Production
- [ ] Change default passwords
- [ ] Enable HTTPS/TLS
- [ ] Implement authentication (JWT)
- [ ] Add API rate limiting
- [ ] Enable CORS properly
- [ ] Validate all inputs
- [ ] Use environment variables for secrets
- [ ] Enable database encryption
- [ ] Set up firewall rules
- [ ] Regular security audits

### Secrets Management
```bash
# Use environment variables
export DATABASE_PASSWORD="secure_password"

# Or use .env file (add to .gitignore)
echo "DATABASE_PASSWORD=secure_password" >> .env
```

## Scaling Considerations

### Horizontal Scaling
- Use load balancer (nginx, HAProxy)
- Run multiple API instances
- Use shared database and cache

### Vertical Scaling
- Increase container memory limits
- Optimize database queries
- Use connection pooling

### Data Management
- Implement data archiving
- Use time-series database for metrics
- Partition large tables

## Backup & Recovery

### Database Backup
```bash
# Backup PostgreSQL
docker-compose exec postgres pg_dump -U osiris northern_metropolis > backup.sql

# Restore from backup
docker-compose exec -T postgres psql -U osiris northern_metropolis < backup.sql
```

### Volume Backup
```bash
# Backup Docker volumes
docker run --rm -v nm-osiris-postgres_data:/data -v $(pwd):/backup \
  alpine tar czf /backup/postgres_backup.tar.gz /data
```

## Updating & Maintenance

### Update Dependencies
```bash
# Check for updates
pip list --outdated

# Update specific package
pip install --upgrade package_name

# Update all packages
pip install --upgrade -r requirements.txt
```

### Database Migrations
```bash
# Create migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

## Support & Resources

- **Documentation:** See `docs/` directory
- **Examples:** See `examples/` directory
- **Issues:** GitHub Issues
- **Contributing:** See `CONTRIBUTING.md`

## Next Steps

1. **API Implementation:** Implement FastAPI server and REST endpoints
2. **Database Integration:** Add SQLAlchemy models and migrations
3. **Testing:** Write comprehensive unit and integration tests
4. **Documentation:** Expand API and architecture documentation
5. **Advanced Features:** Add ML models, real-time simulation, advanced visualization

## License

MIT License - See LICENSE file

---

**Last Updated:** 2026-05-27  
**Version:** 0.1.0  
**Status:** Ready for GitHub Push ✅
