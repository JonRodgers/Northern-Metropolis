#!/usr/bin/env python3
import csv

with open('claases.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['ClassID', 'Theme', 'Class Name', 'Instructor', 'Schedule', 'Location', 'Capacity', 'Status', 'Link to Class', 'Class Description', 'Equipment Requirements'])
    
    for i in range(1, 101):
        section = (i - 1) // 10 + 1
        class_num = (i - 1) % 10 + 1
        class_id = f"S{section:02d}{class_num:02d}"
        
        themes = ["Transportation & Mobility", "Architecture & Structures", "Energy & Power", "Water & Sanitation", 
                  "Materials & Manufacturing", "Communication & Information", "Medicine & Health", 
                  "Environmental & Sustainability", "Space & Exploration", "Future Technologies & Innovation"]
        theme = themes[section - 1]
        
        class_names = [
            "The Telephone to the Smartphone", "Stephenson's Rocket to Tesla's Starship", "The Wright Brothers' First Flight",
            "From Horse Carriages to Electric Vehicles", "The Bicycle Revolution", "Maglev Trains & Hyperloop",
            "The Panama Canal to Modern Waterway Engineering", "From Sailing Ships to Container Vessels",
            "The London Underground to Modern Metro Systems", "Tunneling Through Mountains: From Blasting to Boring Machines",
            "The Eiffel Tower to Modern Skyscrapers", "Roman Arches to Modern Suspension Bridges",
            "The Great Wall of China: Ancient Defense to Modern Barriers", "Domes: From Pantheon to Geodesic Domes",
            "The Crystal Palace to Modern Glass Architecture", "Pyramids: Ancient Engineering Marvels",
            "The Sydney Opera House: Organic Architecture", "Sustainable Architecture: From Vernacular to Green Buildings",
            "The Burj Khalifa: Engineering at the Limit", "Floating Architecture: From Houseboats to Floating Cities",
            "From Candles to Electric Lighting", "Steam Engines to Internal Combustion",
            "Hydroelectric Power: From Water Wheels to Dams", "Wind Power: From Windmills to Modern Turbines",
            "Solar Energy: From Photovoltaic Cells to Solar Cities", "Nuclear Energy: From Discovery to Modern Reactors",
            "Geothermal Energy: Tapping Earth's Heat", "Battery Technology: From Volta to Lithium-Ion",
            "The Grid: From Edison to Smart Grids", "Fusion Energy: The Future of Power",
            "Ancient Aqueducts to Modern Water Systems", "Water Purification: From Boiling to Nanotechnology",
            "Sewage Systems: From Open Drains to Treatment Plants", "Desalination: Creating Fresh Water from the Sea",
            "Dams & Reservoirs: Water Storage Engineering", "Flood Management: From Levees to Smart Systems",
            "Irrigation: From Ancient Channels to Drip Systems", "Wastewater Recycling: From Waste to Resource",
            "Stormwater Management: Urban Water Solutions", "Water Quality Monitoring: From Testing to IoT",
            "Iron to Steel: The Industrial Revolution", "Concrete: From Roman Concrete to High-Performance Mixes",
            "Glass: From Sand to Smart Glass", "Plastics: From Bakelite to Biodegradable Polymers",
            "Ceramics & Composites: Advanced Materials", "Textiles: From Hand Weaving to Smart Fabrics",
            "3D Printing: Additive Manufacturing Revolution", "Nanotechnology: Engineering at the Atomic Scale",
            "Graphene & 2D Materials: The Future of Materials", "Biomaterials: Nature-Inspired Engineering",
            "From Telegraph to Internet", "Radio: From Marconi to Modern Broadcasting",
            "Television: From Mechanical to Digital", "Photography: From Film to Digital Imaging",
            "Computing: From Babbage to Quantum Computers", "The Internet of Things: Connected Everything",
            "Artificial Intelligence: From Logic to Machine Learning", "Cybersecurity: Protecting Digital Infrastructure",
            "Data Science: From Statistics to Big Data", "Virtual & Augmented Reality: Immersive Technology",
            "From Bloodletting to Modern Surgery", "X-Rays to Medical Imaging",
            "Vaccines: From Cowpox to mRNA Technology", "Prosthetics: From Wooden Legs to Bionic Limbs",
            "Pacemakers: Engineering the Heartbeat", "Dialysis: Artificial Kidneys",
            "Dental Technology: From Extraction to Implants", "Genetic Engineering: From Mendel to CRISPR",
            "Telemedicine: Healthcare at a Distance", "Bioprinting: 3D Printing Human Tissue",
            "Air Quality Monitoring: From Smoke to Smart Sensors", "Carbon Capture: From Trees to Technology",
            "Waste Management: From Landfills to Circular Economy", "Renewable Energy Integration: Smart Grids",
            "Biodiversity Monitoring: From Field Surveys to Drones", "Soil Remediation: Cleaning Contaminated Land",
            "Ocean Cleanup: Tackling Plastic Pollution", "Vertical Farming: Growing Food in Cities",
            "Permafrost Monitoring: Climate Change Indicators", "Renewable Materials: From Petroleum to Bioplastics",
            "Rockets: From Fireworks to Reusable Launch Systems", "Satellites: From Sputnik to Mega-Constellations",
            "Space Stations: Living in Orbit", "Lunar Exploration: From Apollo to Artemis",
            "Mars Exploration: The Red Planet", "Telescopes: From Galileo to James Webb",
            "Exoplanet Detection: Finding Worlds Beyond", "Space Propulsion: Beyond Chemical Rockets",
            "Astrobiology: Life Beyond Earth", "Space Tourism: Commercial Spaceflight",
            "Quantum Computing: The Next Computational Revolution", "Blockchain & Distributed Systems",
            "Brain-Computer Interfaces: Mind Control", "Autonomous Systems: Self-Driving Everything",
            "Metamaterials: Engineering Impossible Properties", "Holography: 3D Light Projection",
            "Soft Robotics: Flexible Machines", "Energy Harvesting: Power from Everywhere",
            "Synthetic Biology: Designing Life", "The Metaverse: Virtual Worlds & Digital Existence"
        ]
        
        class_name = class_names[i - 1]
        description = f"Comprehensive STEM class exploring {class_name}. Students engage in hands-on projects, design challenges, and real-world applications. Learn cutting-edge technologies and engineering principles through interactive learning experiences."
        equipment = "Design software, testing equipment, educational materials, analysis tools, simulation software, prototyping materials"
        
        writer.writerow([class_id, theme, class_name, 'TBD', 'TBD', 'TBD', 'TBD', 'Active', 'TBD', description, equipment])

print("CSV file generated successfully!")
