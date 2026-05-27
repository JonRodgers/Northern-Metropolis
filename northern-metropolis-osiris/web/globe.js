// Northern Metropolis OSIRIS - Interactive Globe Visualization
// Three.js based 3D globe with Northern Metropolis boundary and KPI metrics

class NorthernMetropolisGlobe {
    constructor() {
        this.scene = null;
        this.camera = null;
        this.renderer = null;
        this.controls = null;
        this.globe = null;
        this.nmBoundary = null;
        this.autoRotate = false;
        this.viewMode = 'globe';
        this.showBoundaries = true;
        this.showHeatmap = false;

        // Northern Metropolis coordinates (Hong Kong)
        this.nmCenter = { lat: 22.5, lon: 114.1 };
        this.nmBounds = {
            north: 22.55,
            south: 22.45,
            east: 114.15,
            west: 114.05
        };

        // Wait for libraries to load before initializing
        this.waitForLibraries();
    }

    waitForLibraries() {
        console.log('Waiting for Three.js and OrbitControls to load...');
        
        // Check if libraries are available
        if (typeof THREE === 'undefined') {
            console.warn('THREE.js not loaded yet, retrying...');
            setTimeout(() => this.waitForLibraries(), 100);
            return;
        }

        // Check for OrbitControls - it should be available globally after the script loads
        if (typeof OrbitControls === 'undefined') {
            console.warn('OrbitControls not loaded yet, retrying...');
            setTimeout(() => this.waitForLibraries(), 100);
            return;
        }

        console.log('Libraries loaded successfully, initializing globe...');
        this.init();
    }

    init() {
        try {
            console.log('Initializing Northern Metropolis Globe...');
            this.setupScene();
            this.createGlobe();
            this.createNorthernMetropolisBoundary();
            this.setupControls();
            this.setupEventListeners();
            this.animate();
            this.hideLoading();
            console.log('Globe initialized successfully');
        } catch (error) {
            console.error('Error initializing globe:', error);
            this.showError('Failed to initialize globe: ' + error.message);
        }
    }

    setupScene() {
        // Get canvas
        const canvas = document.getElementById('globe-canvas');
        if (!canvas) {
            throw new Error('Canvas element not found');
        }

        // Scene
        this.scene = new THREE.Scene();
        this.scene.background = new THREE.Color(0x0a0e27);
        this.scene.fog = new THREE.Fog(0x0a0e27, 100, 1000);

        // Camera
        const width = window.innerWidth;
        const height = window.innerHeight;
        this.camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 10000);
        this.camera.position.z = 2.5;

        // Renderer
        this.renderer = new THREE.WebGLRenderer({ 
            canvas: canvas,
            antialias: true,
            alpha: true,
            precision: 'highp'
        });
        this.renderer.setSize(width, height);
        this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        this.renderer.shadowMap.enabled = true;
        this.renderer.shadowMap.type = THREE.PCFShadowShadowMap;

        // Lighting
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
        this.scene.add(ambientLight);

        const directionalLight = new THREE.DirectionalLight(0xffffff, 0.9);
        directionalLight.position.set(5, 3, 5);
        directionalLight.castShadow = true;
        directionalLight.shadow.mapSize.width = 2048;
        directionalLight.shadow.mapSize.height = 2048;
        this.scene.add(directionalLight);

        // Stars background
        this.createStarfield();

        // Handle window resize
        window.addEventListener('resize', () => this.onWindowResize());
    }

    createStarfield() {
        const starGeometry = new THREE.BufferGeometry();
        const starCount = 1000;
        const positions = new Float32Array(starCount * 3);

        for (let i = 0; i < starCount * 3; i += 3) {
            positions[i] = (Math.random() - 0.5) * 2000;
            positions[i + 1] = (Math.random() - 0.5) * 2000;
            positions[i + 2] = (Math.random() - 0.5) * 2000;
        }

        starGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
        const starMaterial = new THREE.PointsMaterial({ 
            color: 0xffffff, 
            size: 2,
            sizeAttenuation: true
        });
        const stars = new THREE.Points(starGeometry, starMaterial);
        this.scene.add(stars);
    }

    createGlobe() {
        // Create sphere geometry
        const geometry = new THREE.SphereGeometry(1, 64, 64);

        // Create canvas texture for globe
        const canvas = document.createElement('canvas');
        canvas.width = 2048;
        canvas.height = 1024;
        const ctx = canvas.getContext('2d');

        // Draw globe texture
        this.drawGlobeTexture(ctx, canvas.width, canvas.height);

        const texture = new THREE.CanvasTexture(canvas);
        texture.magFilter = THREE.LinearFilter;
        texture.minFilter = THREE.LinearMipmapLinearFilter;

        const material = new THREE.MeshPhongMaterial({ 
            map: texture,
            shininess: 5,
            emissive: 0x111111
        });

        this.globe = new THREE.Mesh(geometry, material);
        this.globe.castShadow = true;
        this.globe.receiveShadow = true;
        this.scene.add(this.globe);

        // Add atmosphere glow
        const atmosphereGeometry = new THREE.SphereGeometry(1.02, 64, 64);
        const atmosphereMaterial = new THREE.MeshBasicMaterial({
            color: 0x64c8ff,
            transparent: true,
            opacity: 0.1,
            side: THREE.BackSide
        });
        const atmosphere = new THREE.Mesh(atmosphereGeometry, atmosphereMaterial);
        this.scene.add(atmosphere);

        console.log('Globe created successfully');
    }

    drawGlobeTexture(ctx, width, height) {
        // Ocean blue
        ctx.fillStyle = '#1a4d7a';
        ctx.fillRect(0, 0, width, height);

        // Land masses (simplified)
        ctx.fillStyle = '#2d5a3d';
        
        // Asia
        ctx.fillRect(width * 0.5, height * 0.3, width * 0.3, height * 0.3);
        
        // Africa
        ctx.fillRect(width * 0.4, height * 0.4, width * 0.2, height * 0.3);
        
        // Europe
        ctx.fillRect(width * 0.35, height * 0.2, width * 0.15, height * 0.15);
        
        // Americas
        ctx.fillRect(width * 0.05, height * 0.2, width * 0.2, height * 0.4);

        // Grid lines
        ctx.strokeStyle = 'rgba(100, 200, 255, 0.1)';
        ctx.lineWidth = 1;

        // Latitude lines
        for (let lat = -80; lat <= 80; lat += 20) {
            const y = height * (0.5 - lat / 180);
            ctx.beginPath();
            ctx.moveTo(0, y);
            ctx.lineTo(width, y);
            ctx.stroke();
        }

        // Longitude lines
        for (let lon = -180; lon <= 180; lon += 20) {
            const x = width * (0.5 + lon / 360);
            ctx.beginPath();
            ctx.moveTo(x, 0);
            ctx.lineTo(x, height);
            ctx.stroke();
        }

        // Highlight Hong Kong region
        const hkX = width * (0.5 + 114.1 / 360);
        const hkY = height * (0.5 - 22.5 / 180);
        ctx.fillStyle = 'rgba(255, 200, 0, 0.3)';
        ctx.beginPath();
        ctx.arc(hkX, hkY, 30, 0, Math.PI * 2);
        ctx.fill();

        // Label
        ctx.fillStyle = '#ffc800';
        ctx.font = 'bold 16px Arial';
        ctx.fillText('Hong Kong', hkX - 40, hkY - 40);
    }

    createNorthernMetropolisBoundary() {
        // Convert lat/lon to 3D coordinates
        const points = this.generateBoundaryPoints();
        
        // Create line geometry
        const geometry = new THREE.BufferGeometry();
        geometry.setAttribute('position', new THREE.BufferAttribute(points, 3));

        const material = new THREE.LineBasicMaterial({
            color: 0x64c8ff,
            linewidth: 3,
            fog: false
        });

        this.nmBoundary = new THREE.Line(geometry, material);
        this.scene.add(this.nmBoundary);

        // Add zone markers
        this.addZoneMarkers();
        
        console.log('Northern Metropolis boundary created');
    }

    generateBoundaryPoints() {
        const points = [];
        const radius = 1.01;

        // Create a rectangular boundary around Northern Metropolis
        const corners = [
            { lat: this.nmBounds.north, lon: this.nmBounds.west },
            { lat: this.nmBounds.north, lon: this.nmBounds.east },
            { lat: this.nmBounds.south, lon: this.nmBounds.east },
            { lat: this.nmBounds.south, lon: this.nmBounds.west },
            { lat: this.nmBounds.north, lon: this.nmBounds.west }
        ];

        // Add intermediate points for smooth lines
        for (let i = 0; i < corners.length - 1; i++) {
            const start = corners[i];
            const end = corners[i + 1];
            
            for (let t = 0; t <= 1; t += 0.05) {
                const lat = start.lat + (end.lat - start.lat) * t;
                const lon = start.lon + (end.lon - start.lon) * t;
                const pos = this.latLonToXYZ(lat, lon, radius);
                points.push(pos.x, pos.y, pos.z);
            }
        }

        return new Float32Array(points);
    }

    latLonToXYZ(lat, lon, radius = 1) {
        const phi = (90 - lat) * Math.PI / 180;
        const theta = (lon + 180) * Math.PI / 180;

        return {
            x: -radius * Math.sin(phi) * Math.cos(theta),
            y: radius * Math.cos(phi),
            z: radius * Math.sin(phi) * Math.sin(theta)
        };
    }

    addZoneMarkers() {
        const zones = [
            { name: 'Lok Ma Chau Loop', lat: 22.5167, lon: 114.0167, color: 0xff6b6b },
            { name: 'Heung Yuen Wai', lat: 22.4833, lon: 114.0833, color: 0xffd93d },
            { name: 'Fanling/Sheung Shui', lat: 22.5, lon: 114.15, color: 0x6bcf7f },
            { name: 'Kwu Tung North', lat: 22.45, lon: 114.1167, color: 0x4a90e2 }
        ];

        zones.forEach(zone => {
            const pos = this.latLonToXYZ(zone.lat, zone.lon, 1.05);
            
            // Create marker sphere
            const geometry = new THREE.SphereGeometry(0.03, 16, 16);
            const material = new THREE.MeshBasicMaterial({ color: zone.color });
            const marker = new THREE.Mesh(geometry, material);
            
            marker.position.set(pos.x, pos.y, pos.z);
            marker.userData = { name: zone.name, lat: zone.lat, lon: zone.lon };
            
            this.scene.add(marker);
        });

        console.log('Zone markers added');
    }

    setupControls() {
        // Use the global OrbitControls class
        if (typeof OrbitControls === 'undefined') {
            throw new Error('OrbitControls library not loaded');
        }

        this.controls = new OrbitControls(this.camera, this.renderer.domElement);
        this.controls.enableDamping = true;
        this.controls.dampingFactor = 0.05;
        this.controls.autoRotate = false;
        this.controls.autoRotateSpeed = 2;
        this.controls.enableZoom = true;
        this.controls.enablePan = true;
        this.controls.minDistance = 1.5;
        this.controls.maxDistance = 5;
        
        console.log('OrbitControls initialized successfully');
    }

    setupEventListeners() {
        // View mode buttons
        const btnGlobe = document.getElementById('btn-globe');
        const btnZones = document.getElementById('btn-zones');
        const btnMetrics = document.getElementById('btn-metrics');
        
        if (btnGlobe) btnGlobe.addEventListener('click', () => this.setViewMode('globe'));
        if (btnZones) btnZones.addEventListener('click', () => this.setViewMode('zones'));
        if (btnMetrics) btnMetrics.addEventListener('click', () => this.setViewMode('metrics'));

        // Visualization buttons
        const btnBoundaries = document.getElementById('btn-boundaries');
        const btnHeatmap = document.getElementById('btn-heatmap');
        const btnReset = document.getElementById('btn-reset');
        
        if (btnBoundaries) btnBoundaries.addEventListener('click', () => this.toggleBoundaries());
        if (btnHeatmap) btnHeatmap.addEventListener('click', () => this.toggleHeatmap());
        if (btnReset) btnReset.addEventListener('click', () => this.resetView());

        // Interaction buttons
        const btnZoomNM = document.getElementById('btn-zoom-nm');
        const btnRotate = document.getElementById('btn-rotate');
        
        if (btnZoomNM) btnZoomNM.addEventListener('click', () => this.zoomToNorthernMetropolis());
        if (btnRotate) btnRotate.addEventListener('click', () => this.toggleAutoRotate());

        // Mouse move for tooltip
        this.renderer.domElement.addEventListener('mousemove', (e) => this.onMouseMove(e));
    }

    setViewMode(mode) {
        this.viewMode = mode;
        
        // Update button states
        document.querySelectorAll('.controls-panel button').forEach(btn => {
            btn.classList.remove('active');
        });
        
        if (mode === 'globe') {
            const btn = document.getElementById('btn-globe');
            if (btn) btn.classList.add('active');
            this.resetView();
        } else if (mode === 'zones') {
            const btn = document.getElementById('btn-zones');
            if (btn) btn.classList.add('active');
            this.zoomToNorthernMetropolis();
        } else if (mode === 'metrics') {
            const btn = document.getElementById('btn-metrics');
            if (btn) btn.classList.add('active');
            this.zoomToNorthernMetropolis();
        }
    }

    toggleBoundaries() {
        this.showBoundaries = !this.showBoundaries;
        if (this.nmBoundary) {
            this.nmBoundary.visible = this.showBoundaries;
        }
        const btn = document.getElementById('btn-boundaries');
        if (btn) btn.classList.toggle('active');
    }

    toggleHeatmap() {
        this.showHeatmap = !this.showHeatmap;
        const btn = document.getElementById('btn-heatmap');
        if (btn) btn.classList.toggle('active');
    }

    resetView() {
        this.camera.position.z = 2.5;
        if (this.controls) {
            this.controls.target.set(0, 0, 0);
            this.controls.autoRotate = false;
        }
        this.autoRotate = false;
    }

    zoomToNorthernMetropolis() {
        const nmPos = this.latLonToXYZ(this.nmCenter.lat, this.nmCenter.lon, 1);
        const direction = new THREE.Vector3(nmPos.x, nmPos.y, nmPos.z).normalize();
        
        this.camera.position.copy(direction.multiplyScalar(1.8));
        if (this.controls) {
            this.controls.target.copy(direction.multiplyScalar(1));
            this.controls.update();
        }
    }

    toggleAutoRotate() {
        this.autoRotate = !this.autoRotate;
        if (this.controls) {
            this.controls.autoRotate = this.autoRotate;
        }
        const btn = document.getElementById('btn-rotate');
        if (btn) btn.classList.toggle('active');
    }

    onMouseMove(event) {
        const rect = this.renderer.domElement.getBoundingClientRect();
        const x = (event.clientX - rect.left) / rect.width * 2 - 1;
        const y = -(event.clientY - rect.top) / rect.height * 2 + 1;

        const raycaster = new THREE.Raycaster();
        raycaster.setFromCamera(new THREE.Vector2(x, y), this.camera);

        const objects = this.scene.children.filter(obj => 
            obj.geometry && 
            obj.geometry.type === 'SphereGeometry' && 
            obj.userData && 
            obj.userData.name
        );
        const intersects = raycaster.intersectObjects(objects);

        const tooltip = document.getElementById('tooltip');
        
        if (intersects.length > 0 && tooltip) {
            const zone = intersects[0].object.userData;
            tooltip.innerHTML = `<strong>${zone.name}</strong><br>Lat: ${zone.lat.toFixed(4)}<br>Lon: ${zone.lon.toFixed(4)}`;
            tooltip.classList.add('visible');
            tooltip.style.left = event.clientX + 10 + 'px';
            tooltip.style.top = event.clientY + 10 + 'px';
        } else if (tooltip) {
            tooltip.classList.remove('visible');
        }
    }

    onWindowResize() {
        const width = window.innerWidth;
        const height = window.innerHeight;

        this.camera.aspect = width / height;
        this.camera.updateProjectionMatrix();
        this.renderer.setSize(width, height);
    }

    updateKPIs() {
        // Simulate KPI updates
        const kpis = {
            renewable: Math.floor(Math.random() * 30 + 40),
            green: Math.floor(Math.random() * 10 + 28),
            aqi: Math.floor(Math.random() * 40 + 50),
            sustainability: Math.floor(Math.random() * 20 + 65)
        };

        const renewableEl = document.getElementById('kpi-renewable');
        const greenEl = document.getElementById('kpi-green');
        const aqiEl = document.getElementById('kpi-aqi');
        const sustainabilityEl = document.getElementById('kpi-sustainability');

        if (renewableEl) renewableEl.textContent = kpis.renewable;
        if (greenEl) greenEl.textContent = kpis.green;
        if (aqiEl) aqiEl.textContent = kpis.aqi;
        if (sustainabilityEl) sustainabilityEl.textContent = kpis.sustainability;
    }

    animate() {
        requestAnimationFrame(() => this.animate());

        // Rotate globe slightly
        if (this.globe && !this.autoRotate) {
            this.globe.rotation.y += 0.0001;
        }

        if (this.controls) {
            this.controls.update();
        }

        if (this.renderer && this.scene && this.camera) {
            this.renderer.render(this.scene, this.camera);
        }

        // Update KPIs periodically
        if (Math.random() < 0.01) {
            this.updateKPIs();
        }
    }

    hideLoading() {
        const loading = document.getElementById('loading');
        if (loading) {
            setTimeout(() => {
                loading.style.opacity = '0';
                loading.style.pointerEvents = 'none';
                setTimeout(() => {
                    loading.style.display = 'none';
                }, 300);
            }, 1000);
        }
    }

    showError(message) {
        const loading = document.getElementById('loading');
        if (loading) {
            loading.innerHTML = `<div class="loading-text" style="color: #ff6b6b;">Error: ${message}</div>`;
        }
    }
}

// Initialize globe when page loads
window.addEventListener('load', () => {
    console.log('Page loaded, initializing globe...');
    try {
        new NorthernMetropolisGlobe();
    } catch (error) {
        console.error('Failed to initialize globe:', error);
        const loading = document.getElementById('loading');
        if (loading) {
            loading.innerHTML = `<div class="loading-text" style="color: #ff6b6b;">Error: ${error.message}</div>`;
        }
    }
});

// Fallback initialization
document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM loaded');
    if (!window.globe) {
        console.log('Initializing globe from DOMContentLoaded...');
        try {
            window.globe = new NorthernMetropolisGlobe();
        } catch (error) {
            console.error('Failed to initialize globe:', error);
        }
    }
});
