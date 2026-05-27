#!/usr/bin/env python3
import csv

with open('training.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['TrainingID', 'Theme', 'Course Name', 'Instructor', 'Schedule', 'Location', 'Capacity', 'Status', 'Link to Course', 'Course Description', 'Equipment Requirements'])
    
    # Theme 1: AI & Business Development (T0101-T0110)
    for i in range(1, 11):
        course_id = f'T010{i}'
        courses_t1 = [
            ('AI Fundamentals for AECO Professionals', 'Comprehensive introduction to artificial intelligence applications in architecture, engineering, and construction. Learn machine learning basics, neural networks, and practical AI implementations for project optimization, cost estimation, and risk management.', 'Laptops, AI software, case studies, datasets, Python environment'),
            ('Machine Learning for Construction Analytics', 'Advanced machine learning techniques for analyzing construction data. Predictive modeling for project timelines, resource allocation, and quality control. Real-world case studies from major construction projects.', 'Python, Jupyter notebooks, ML libraries, construction datasets, analysis tools'),
            ('AI-Powered Project Management Systems', 'Implementing AI systems for project scheduling, budget forecasting, and resource optimization. Integration with existing project management platforms. ROI analysis and implementation strategies.', 'Project management software, AI tools, integration platforms, case studies'),
            ('Natural Language Processing for Construction Documents', 'NLP applications for automated document analysis, contract review, and specification extraction. Reduce manual document processing time by 80%. Practical implementation using Python and NLP libraries.', 'Python, NLP libraries, document samples, processing tools, case studies'),
            ('Computer Vision for Site Monitoring', 'Computer vision technology for automated site monitoring, progress tracking, and safety compliance. Real-time analysis of construction site images and videos. Integration with drone footage and security cameras.', 'Python, OpenCV, drone footage, cameras, analysis software, case studies'),
            ('Generative AI for Design and Planning', 'Leveraging generative AI for architectural design, space planning, and construction sequencing. ChatGPT and advanced language models for design assistance. Ethical considerations and best practices.', 'Generative AI tools, design software, case studies, ethical frameworks'),
            ('AI-Driven Cost Estimation and Budgeting', 'Machine learning models for accurate cost estimation. Historical data analysis and predictive budgeting. Reducing cost overruns through AI-powered forecasting and contingency planning.', 'Cost estimation software, historical data, ML tools, analysis platforms'),
            ('Business Development Strategy in the AI Era', 'Strategic planning for AECO companies to leverage AI for competitive advantage. Market analysis, service innovation, and revenue optimization. Building AI-ready organizational culture.', 'Business strategy frameworks, market analysis tools, case studies, planning software'),
            ('AI Ethics and Responsible Implementation', 'Ethical considerations in AI deployment. Bias detection and mitigation. Regulatory compliance and responsible AI practices. Building trust with stakeholders through transparent AI implementation.', 'Ethics frameworks, compliance guidelines, case studies, assessment tools'),
            ('AI ROI Measurement and Performance Metrics', 'Measuring return on investment for AI implementations. Key performance indicators for AI projects. Cost-benefit analysis and business case development. Demonstrating value to stakeholders.', 'Analytics tools, KPI frameworks, case studies, measurement software'),
        ]
        name, desc, equip = courses_t1[i-1]
        writer.writerow([course_id, 'AI & Business Development', name, 'Industry Expert', 'TBD', 'TBD', 'TBD', 'Active', 'TBD', desc, equip])
    
    # Theme 2: BIM & Digital Twin (T0201-T0210)
    for i in range(1, 11):
        course_id = f'T020{i}'
        courses_t2 = [
            ('BIM Fundamentals and Best Practices', 'Comprehensive introduction to Building Information Modeling. BIM standards, workflows, and collaboration. Implementation strategies for small to large organizations. Industry standards and best practices.', 'BIM software, standards documentation, case studies, collaboration tools'),
            ('Advanced BIM Modeling Techniques', 'Advanced BIM modeling for complex projects. Parametric design, family creation, and custom workflows. Optimization for performance and collaboration. Real-world project examples.', 'BIM software, design tools, parametric libraries, case studies'),
            ('BIM for Facility Management', 'Leveraging BIM data for facility management operations. Asset tracking, maintenance scheduling, and space utilization. Integration with FM systems and IoT sensors. Lifecycle management.', 'BIM software, FM systems, IoT integration, case studies, management tools'),
            ('Digital Twin Technology and Applications', 'Creating and managing digital twins of buildings and infrastructure. Real-time monitoring and simulation. Predictive maintenance and performance optimization. Integration with IoT and sensors.', 'Digital twin platforms, IoT sensors, simulation software, case studies'),
            ('BIM to Digital Twin Workflow', 'Seamless transition from BIM models to operational digital twins. Data enrichment and real-time synchronization. Continuous model updates and lifecycle management. Implementation strategies.', 'BIM software, digital twin platforms, integration tools, case studies'),
            ('IFC and Open Standards in BIM', 'Industry Foundation Classes (IFC) standards and open BIM workflows. Interoperability between different software platforms. Data exchange and quality assurance. Future of open standards.', 'IFC tools, validation software, standards documentation, case studies'),
            ('COBIE and Data Handover', 'Construction Operations Building Information Exchange (COBie) standards. Structured data handover from design to operations. Compliance with client requirements and standards. Automated COBie generation.', 'COBie tools, spreadsheet templates, validation software, case studies'),
            ('BIM Coordination and Clash Detection', 'Coordinating multi-discipline BIM models. Automated clash detection and resolution. Workflow optimization and conflict management. Reducing rework and construction delays.', 'BIM software, clash detection tools, coordination platforms, case studies'),
            ('BIM for Construction Planning and Sequencing', '4D BIM for construction sequencing and scheduling. Visualizing construction sequences and logistics. Resource planning and site layout optimization. Improving project efficiency.', 'BIM software, 4D tools, scheduling software, visualization platforms'),
            ('BIM Governance and Standards Implementation', 'Establishing BIM governance frameworks and standards. Organizational BIM strategy and implementation roadmap. Quality assurance and compliance monitoring. Building BIM maturity.', 'Governance frameworks, standards documentation, implementation guides, case studies'),
        ]
        name, desc, equip = courses_t2[i-1]
        writer.writerow([course_id, 'BIM & Digital Twin', name, 'Industry Expert', 'TBD', 'TBD', 'TBD', 'Active', 'TBD', desc, equip])
    
    # Theme 3: Smart Cities & IoT (T0301-T0310)
    for i in range(1, 11):
        course_id = f'T030{i}'
        courses_t3 = [
            ('Smart City Fundamentals and Vision', 'Understanding smart city concepts and technologies. Urban challenges and technology solutions. Sustainable development and quality of life improvements. Global smart city examples and lessons learned.', 'Case studies, frameworks, planning tools, documentation'),
            ('IoT Sensors and Microcontrollers', 'Introduction to IoT sensors and microcontroller platforms. Arduino, Raspberry Pi, and industrial IoT devices. Sensor selection and deployment strategies. Data collection and transmission.', 'Arduino kits, sensors, microcontrollers, development boards, documentation'),
            ('IoT Networks and Connectivity', 'IoT communication protocols and networks. WiFi, Bluetooth, LoRaWAN, and 5G for IoT. Network design and optimization. Security and reliability considerations.', 'Network equipment, protocol documentation, simulation tools, case studies'),
            ('Building Automation and Smart Buildings', 'Automated building systems for energy efficiency and comfort. HVAC, lighting, and security automation. Integration with BIM and digital twins. Smart building standards and certifications.', 'Building automation software, control systems, sensors, case studies'),
            ('Smart Infrastructure and Utilities', 'Smart water, energy, and waste management systems. Real-time monitoring and optimization. Reducing resource consumption and environmental impact. Integration with city-wide systems.', 'Monitoring systems, control software, sensors, case studies'),
            ('Data Analytics for Smart Cities', 'Analyzing IoT data for city-wide insights. Real-time dashboards and predictive analytics. Urban planning and resource optimization. Data visualization and decision support.', 'Analytics platforms, visualization tools, datasets, case studies'),
            ('Cybersecurity for IoT and Smart Cities', 'Security challenges in IoT deployments. Protecting smart city infrastructure from cyber threats. Encryption, authentication, and access control. Compliance and standards.', 'Security tools, encryption software, testing platforms, case studies'),
            ('Smart Mobility and Transportation', 'Connected vehicles and autonomous transportation systems. Traffic management and congestion reduction. Integration with urban planning. Sustainability and emissions reduction.', 'Mobility platforms, traffic management software, case studies'),
            ('Citizen Engagement and Smart City Services', 'Digital platforms for citizen engagement and service delivery. Mobile applications and smart city services. Community participation and feedback mechanisms. Building livable smart cities.', 'Mobile platforms, engagement tools, case studies, frameworks'),
            ('Smart City Implementation and Governance', 'Planning and implementing smart city initiatives. Governance structures and stakeholder management. Funding and financing strategies. Measuring success and impact.', 'Implementation frameworks, governance guides, case studies, planning tools'),
        ]
        name, desc, equip = courses_t3[i-1]
        writer.writerow([course_id, 'Smart Cities & IoT', name, 'Industry Expert', 'TBD', 'TBD', 'TBD', 'Active', 'TBD', desc, equip])
    
    # Theme 4: Industry 4.0 & Automation (T0401-T0410)
    for i in range(1, 11):
        course_id = f'T040{i}'
        courses_t4 = [
            ('Industry 4.0 Fundamentals', 'Understanding Industry 4.0 and digital transformation. Connected systems, data analytics, and automation. Impact on construction and manufacturing. Organizational readiness and change management.', 'Case studies, frameworks, documentation, assessment tools'),
            ('Robotics in Construction', 'Robotic systems for construction automation. Bricklaying, concrete placement, and structural assembly robots. Safety, efficiency, and quality improvements. ROI and implementation challenges.', 'Robot demonstrations, case studies, technical documentation, videos'),
            ('Drones and Aerial Technology', 'Drone applications in construction and surveying. Aerial photography, mapping, and inspection. Regulatory compliance and safety protocols. Integration with BIM and digital twins.', 'Drone equipment, flight simulators, case studies, regulatory guides'),
            ('3D Printing and Additive Manufacturing', '3D printing technology for construction components and buildings. Material selection and structural design. Cost and time savings. Future of construction manufacturing.', '3D printers, materials, design software, case studies'),
            ('Prefabrication and Modular Construction', 'Off-site manufacturing and modular construction strategies. Quality control and standardization. Supply chain optimization. Reducing on-site labor and schedule.', 'Manufacturing systems, case studies, design tools, documentation'),
            ('Wearable Technology and Safety', 'Wearable devices for worker safety and productivity. Real-time monitoring and alert systems. Health and safety compliance. Integration with site management systems.', 'Wearable devices, monitoring software, case studies, safety protocols'),
            ('Augmented Reality for Construction', 'AR applications for construction visualization and guidance. On-site navigation and assembly instructions. Quality control and inspection. Training and skill development.', 'AR software, mobile devices, case studies, development tools'),
            ('Digital Supply Chain Management', 'Digitizing supply chain for construction materials and equipment. Real-time tracking and inventory management. Supplier integration and collaboration. Reducing waste and delays.', 'Supply chain software, tracking systems, case studies, integration tools'),
            ('Predictive Maintenance and Asset Management', 'Predictive maintenance using IoT sensors and analytics. Equipment health monitoring and failure prevention. Extending asset lifespan and reducing downtime. Integration with digital twins.', 'Monitoring systems, analytics software, sensors, case studies'),
            ('Digital Transformation Strategy for AECO', 'Developing digital transformation roadmaps for AECO companies. Technology selection and implementation planning. Organizational change and workforce development. Measuring digital maturity.', 'Strategy frameworks, assessment tools, case studies, planning guides'),
        ]
        name, desc, equip = courses_t4[i-1]
        writer.writerow([course_id, 'Industry 4.0 & Automation', name, 'Industry Expert', 'TBD', 'TBD', 'TBD', 'Active', 'TBD', desc, equip])
    
    # Theme 5: Programming & Python (T0501-T0510)
    for i in range(1, 11):
        course_id = f'T050{i}'
        courses_t5 = [
            ('Python Fundamentals for AECO Professionals', 'Introduction to Python programming for construction and engineering applications. Variables, data types, and control structures. Practical examples and hands-on exercises. Building automation scripts.', 'Python IDE, documentation, tutorials, practice exercises'),
            ('Data Analysis with Python', 'Using Python for construction data analysis. Pandas, NumPy, and data manipulation libraries. Statistical analysis and visualization. Real-world project data examples.', 'Python, Jupyter, libraries, datasets, visualization tools'),
            ('Python for BIM Automation', 'Automating BIM workflows with Python. Revit API and IFC file manipulation. Batch processing and model generation. Improving productivity and reducing manual work.', 'Python, BIM software APIs, documentation, case studies'),
            ('Web Development for Construction Applications', 'Building web applications for construction management. Flask and Django frameworks. Database design and integration. Deploying applications to the cloud.', 'Python frameworks, web development tools, databases, hosting platforms'),
            ('Python for IoT and Sensor Data', 'Processing IoT sensor data with Python. Real-time data collection and analysis. Integration with databases and visualization tools. Building monitoring systems.', 'Python, IoT libraries, sensors, databases, visualization tools'),
            ('Machine Learning with Python', 'Machine learning libraries and frameworks in Python. Scikit-learn, TensorFlow, and PyTorch. Building predictive models for construction applications. Model evaluation and optimization.', 'Python, ML libraries, datasets, Jupyter notebooks, case studies'),
            ('Python for Computational Design', 'Parametric design and generative algorithms with Python. Grasshopper and Rhino integration. Creating complex geometries and design variations. Optimization and performance analysis.', 'Python, Grasshopper, Rhino, design tools, case studies'),
            ('Testing and Debugging Python Code', 'Writing reliable and maintainable Python code. Unit testing and test-driven development. Debugging techniques and tools. Code quality and best practices.', 'Python, testing frameworks, debugging tools, documentation'),
            ('Python Documentation and Collaboration', 'Writing clear documentation for Python projects. Code commenting and docstrings. Collaboration tools and version control. Building professional Python projects.', 'Documentation tools, version control, collaboration platforms, guides'),
            ('Advanced Python Topics', 'Advanced Python concepts and patterns. Object-oriented programming and design patterns. Performance optimization and profiling. Building scalable applications.', 'Python, advanced libraries, optimization tools, case studies'),
        ]
        name, desc, equip = courses_t5[i-1]
        writer.writerow([course_id, 'Programming & Python', name, 'Industry Expert', 'TBD', 'TBD', 'TBD', 'Active', 'TBD', desc, equip])
    
    # Theme 6: Computational Design (T0601-T0610)
    for i in range(1, 11):
        course_id = f'T060{i}'
        courses_t6 = [
            ('Parametric Design Fundamentals', 'Introduction to parametric design and generative algorithms. Grasshopper and visual programming. Creating flexible and adaptable designs. Optimization and performance analysis.', 'Grasshopper, Rhino, design tools, tutorials, case studies'),
            ('Algorithmic Thinking for Designers', 'Developing algorithmic thinking and problem-solving skills. Breaking down complex design problems. Creating reusable design components. Scaling design solutions.', 'Design tools, programming concepts, case studies, exercises'),
            ('Advanced Grasshopper Techniques', 'Advanced Grasshopper scripting and custom components. Data trees and complex workflows. Performance optimization. Building professional design tools.', 'Grasshopper, Rhino, scripting tools, documentation, case studies'),
            ('Generative Design and Optimization', 'Generative design for exploring design possibilities. Multi-objective optimization. Structural and environmental performance. AI-assisted design exploration.', 'Generative design software, optimization tools, case studies'),
            ('Computational Geometry and Topology', 'Mathematical foundations of computational design. Geometric algorithms and transformations. Topology and spatial relationships. Advanced geometric modeling.', 'Computational geometry libraries, mathematics tools, case studies'),
            ('Scripting in Design Software', 'Python and C# scripting in design software. Revit API and Rhino Python. Automating design workflows. Building custom tools and plugins.', 'Design software, scripting languages, APIs, documentation'),
            ('Data-Driven Design', 'Using data to inform design decisions. Analyzing performance metrics and feedback. Iterative design improvement. Evidence-based design practices.', 'Data analysis tools, visualization software, case studies'),
            ('Computational Fabrication', 'Designing for digital fabrication and 3D printing. Optimizing designs for manufacturing constraints. Material efficiency and waste reduction. From digital to physical.', 'CAM software, fabrication equipment, design tools, case studies'),
            ('Machine Learning for Design', 'Applying machine learning to design problems. Training models on design data. Predictive design and pattern recognition. AI-assisted creativity.', 'ML libraries, design software, datasets, case studies'),
            ('Computational Design Portfolio and Practice', 'Building a computational design portfolio. Documenting design processes and results. Professional practice and business models. Advancing the field of computational design.', 'Portfolio tools, documentation platforms, case studies, guides'),
        ]
        name, desc, equip = courses_t6[i-1]
        writer.writerow([course_id, 'Computational Design', name, 'Industry Expert', 'TBD', 'TBD', 'TBD', 'Active', 'TBD', desc, equip])
    
    # Theme 7: Standards & Compliance (T0701-T0710)
    for i in range(1, 11):
        course_id = f'T070{i}'
        courses_t7 = [
            ('ISO 19650 Information Management', 'ISO 19650 standards for information management in construction. Organizational information requirements and asset information requirements. Implementing information management systems. Compliance and auditing.', 'ISO standards, documentation, implementation guides, case studies'),
            ('ISO 19650 Part 1: Concepts and Principles', 'Deep dive into ISO 19650-1 concepts and principles. Information management framework. Roles and responsibilities. Building information management culture.', 'ISO standards, documentation, training materials, case studies'),
            ('ISO 19650 Part 2: Delivery Phase', 'ISO 19650-2 for delivery phase information management. Project information requirements and execution plans. Collaborative workflows and data exchange. Quality assurance.', 'ISO standards, templates, software tools, case studies'),
            ('ISO 19650 Part 3: Operational Phase', 'ISO 19650-3 for operational phase information management. Asset information requirements and handover. Facility management integration. Lifecycle information management.', 'ISO standards, FM systems, documentation, case studies'),
            ('IFC Standards and Open BIM', 'Industry Foundation Classes (IFC) standards and open BIM. Data exchange and interoperability. IFC schema and implementation. Quality assurance and validation.', 'IFC tools, validation software, standards documentation, case studies'),
            ('COBie Data Standards', 'Construction Operations Building Information Exchange (COBie) standards. Structured data handover requirements. COBie generation and validation. Client compliance.', 'COBie tools, spreadsheet templates, validation software, case studies'),
            ('IDS Information Delivery Specification', 'Information Delivery Specification (IDS) for defining information requirements. Creating and validating IDS documents. Ensuring data quality and completeness. Integration with BIM workflows.', 'IDS tools, validation software, documentation, case studies'),
            ('Building Codes and Compliance', 'Building codes and regulatory compliance in design and construction. Code checking and compliance verification. Digital tools for code compliance. International standards and variations.', 'Code databases, compliance software, documentation, case studies'),
            ('Sustainability Standards and Certifications', 'LEED, BREEAM, and other sustainability certifications. Environmental performance standards. Measuring and reporting sustainability metrics. Green building practices.', 'Certification frameworks, assessment tools, documentation, case studies'),
            ('Data Privacy and Security Standards', 'GDPR, CCPA, and data privacy regulations. Protecting sensitive project and personal information. Cybersecurity standards and best practices. Compliance and audit trails.', 'Privacy frameworks, security tools, documentation, case studies'),
        ]
        name, desc, equip = courses_t7[i-1]
        writer.writerow([course_id, 'Standards & Compliance', name, 'Industry Expert', 'TBD', 'TBD', 'TBD', 'Active', 'TBD', desc, equip])
    
    # Theme 8: Cost, Quantity & Risk Management (T0801-T0810)
    for i in range(1, 11):
        course_id = f'T080{i}'
        courses_t8 = [
            ('Advanced Cost Estimation Techniques', 'Mastering cost estimation from conceptual to detailed design phases. Parametric cost modeling and historical data analysis. Managing cost uncertainty and contingency planning. Real-world case studies and benchmarking.', 'Cost estimation software, historical databases, analysis tools, case studies'),
            ('Quantity Surveying in the Digital Age', 'Modern quantity surveying practices leveraging BIM and digital tools. Automated quantity extraction and bill of quantities generation. Reducing errors and improving accuracy. Integration with cost management systems.', 'BIM software, QS tools, automation platforms, case studies'),
            ('Value Engineering and Cost Optimization', 'Strategic value engineering to maximize project value. Identifying cost reduction opportunities without compromising quality. Life cycle costing and total cost of ownership. Stakeholder engagement and decision-making.', 'VE frameworks, analysis tools, case studies, decision support software'),
            ('Risk Management Framework and Strategy', 'Comprehensive risk management from identification through mitigation. Risk registers and probability-impact matrices. Monte Carlo simulation for cost and schedule risk. Building organizational risk culture.', 'Risk management software, simulation tools, templates, case studies'),
            ('Schedule Risk and Time Management', 'Managing schedule risk and uncertainty. Critical path analysis and schedule compression. Resource leveling and optimization. Predictive scheduling using historical data and AI.', 'Scheduling software, risk analysis tools, historical data, case studies'),
            ('Quality Risk and Defect Management', 'Quality assurance and defect prevention strategies. Root cause analysis and corrective actions. Building quality culture and continuous improvement. Reducing rework and warranty costs.', 'Quality management systems, inspection tools, case studies, frameworks'),
            ('Financial Risk and Cash Flow Management', 'Managing financial risks in construction projects. Cash flow forecasting and working capital management. Payment terms and contract risk allocation. Protecting profitability and financial health.', 'Financial modeling software, cash flow tools, contract templates, case studies'),
            ('Insurance and Liability Management', 'Understanding insurance requirements and coverage. Managing liability and claims. Professional indemnity and project insurance. Risk transfer strategies and cost implications.', 'Insurance frameworks, contract templates, case studies, legal guidance'),
            ('Earned Value Management', 'Earned value management for integrated cost and schedule control. Performance measurement and variance analysis. Forecasting final costs and completion dates. Stakeholder reporting and transparency.', 'EVM software, project management tools, templates, case studies'),
            ('Contingency Planning and Resilience', 'Building resilient projects through contingency planning. Scenario analysis and stress testing. Adaptive management and flexibility. Learning from disruptions and building organizational resilience.', 'Scenario planning tools, simulation software, case studies, frameworks'),
        ]
        name, desc, equip = courses_t8[i-1]
        writer.writerow([course_id, 'Cost, Quantity & Risk', name, 'Industry Expert', 'TBD', 'TBD', 'TBD', 'Active', 'TBD', desc, equip])
    
    # Theme 9: Resource Management & Entrepreneurship (T0901-T0910)
    for i in range(1, 11):
        course_id = f'T090{i}'
        courses_t9 = [
            ('Strategic Resource Planning', 'Optimizing resource allocation across multiple projects. Capacity planning and workforce forecasting. Skills matrix and competency development. Building high-performing teams.', 'Resource management software, planning tools, case studies, frameworks'),
            ('Talent Development and Leadership', 'Developing talent within AECO organizations. Mentoring and coaching strategies. Building leadership pipelines. Creating learning cultures and continuous improvement.', 'Leadership frameworks, training programs, case studies, assessment tools'),
            ('Entrepreneurship in AECO', 'Starting and scaling AECO businesses. Business model innovation and value creation. Funding and financing strategies. Building sustainable enterprises.', 'Business planning tools, case studies, funding guides, mentorship resources'),
            ('Strategic Partnerships and Alliances', 'Building strategic partnerships for competitive advantage. Joint ventures and collaboration models. Managing partner relationships and shared value creation. Expanding market reach and capabilities.', 'Partnership frameworks, case studies, negotiation guides, legal templates'),
            ('Innovation Management and R&D', 'Managing innovation in AECO organizations. Research and development strategies. Commercializing innovations and new technologies. Building innovation culture and processes.', 'Innovation frameworks, case studies, R&D tools, commercialization guides'),
            ('Organizational Change Management', 'Leading organizational change in digital transformation. Change communication and stakeholder engagement. Managing resistance and building adoption. Measuring change success.', 'Change management frameworks, communication tools, case studies, assessment tools'),
            ('Performance Management and KPIs', 'Establishing performance management systems. Defining KPIs and metrics for AECO organizations. Data-driven decision making and continuous improvement. Balanced scorecard approach.', 'Performance management software, KPI frameworks, dashboards, case studies'),
            ('Diversity, Equity and Inclusion', 'Building diverse and inclusive AECO organizations. Recruitment and retention strategies. Creating inclusive cultures and addressing bias. Measuring and reporting on DEI metrics.', 'DEI frameworks, assessment tools, case studies, training programs'),
            ('Sustainability and Corporate Responsibility', 'Integrating sustainability into business strategy. Environmental, social, and governance (ESG) reporting. Building sustainable value and stakeholder trust. Circular economy principles.', 'Sustainability frameworks, ESG tools, case studies, reporting standards'),
            ('Future-Ready Organizations', 'Preparing AECO organizations for the future. Scenario planning and strategic foresight. Building adaptive capacity and resilience. Continuous learning and evolution.', 'Foresight frameworks, scenario planning tools, case studies, strategic guides'),
        ]
        name, desc, equip = courses_t9[i-1]
        writer.writerow([course_id, 'Resource Management & Entrepreneurship', name, 'Industry Expert', 'TBD', 'TBD', 'TBD', 'Active', 'TBD', desc, equip])
    
    # Theme 10: Drones & Robotics (T1001-T1010)
    for i in range(1, 11):
        course_id = f'T100{i}'
        courses_t10 = [
            ('Drone Fundamentals and Operations', 'Introduction to drone technology and operations. Types of drones and their applications. Flight planning and safety protocols. Regulatory compliance and certifications.', 'Drone equipment, flight simulators, regulatory guides, case studies'),
            ('Advanced Drone Surveying and Mapping', 'Professional drone surveying and mapping techniques. Photogrammetry and LiDAR technology. Creating accurate site models and orthomosaics. Integration with BIM and GIS.', 'Drones, surveying software, processing tools, case studies'),
            ('Drone Inspection and Monitoring', 'Using drones for building and infrastructure inspection. Thermal imaging and defect detection. Condition assessment and monitoring. Safety and quality improvements.', 'Drones, thermal cameras, inspection software, case studies'),
            ('Robotics Fundamentals and Applications', 'Introduction to robotics in construction. Types of construction robots and their capabilities. Programming and control systems. Safety and human-robot collaboration.', 'Robot demonstrations, programming tools, case studies, technical documentation'),
            ('Autonomous Construction Robots', 'Autonomous systems for construction tasks. Path planning and obstacle avoidance. Machine vision and sensor integration. Real-world deployment challenges and solutions.', 'Robot systems, sensors, programming tools, case studies'),
            ('Robotic Process Automation', 'Automating repetitive construction processes. Bricklaying, concrete placement, and assembly robots. Productivity gains and quality improvements. ROI and implementation strategies.', 'Robot systems, case studies, technical documentation, videos'),
            ('Drone and Robot Integration with BIM', 'Integrating drone and robot data with BIM models. Real-time site monitoring and model updates. Digital twin creation and management. Improving project visibility and control.', 'Drones, robots, BIM software, integration tools, case studies'),
            ('Safety and Compliance for Drones and Robots', 'Safety protocols and best practices for drone and robot operations. Regulatory compliance and certifications. Insurance and liability considerations. Building safe work environments.', 'Safety frameworks, regulatory guides, insurance information, case studies'),
            ('Future of Autonomous Construction', 'Emerging technologies in autonomous construction. AI and machine learning for autonomous systems. Fully autonomous construction sites. Challenges and opportunities ahead.', 'Research papers, case studies, technology demonstrations, future scenarios'),
            ('Drone and Robot Business Models', 'Building businesses around drone and robot services. Service offerings and pricing strategies. Market opportunities and competitive landscape. Scaling operations and growth strategies.', 'Business planning tools, case studies, market analysis, entrepreneurship guides'),
        ]
        name, desc, equip = courses_t10[i-1]
        writer.writerow([course_id, 'Drones & Robotics', name, 'Industry Expert', 'TBD', 'TBD', 'TBD', 'Active', 'TBD', desc, equip])

print('Training CSV generated successfully with 100 premium CPD courses!')
