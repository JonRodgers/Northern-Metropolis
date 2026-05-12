# ISO 19650 Compliance Framework & Implementation Checklist

**Document Version:** 1.0  
**Last Updated:** 2026-04-11  
**Scope:** Multi-disciplinary Construction Project Compliance (Architecture, Structural Engineering, Building Services)

---

## TABLE OF CONTENTS

1. [ISO 19650 Standards Overview](#iso-19650-standards-overview)
2. [Project Information Requirements](#project-information-requirements)
3. [Organizational & Team Structure](#organizational--team-structure)
4. [File & Folder Naming Conventions](#file--folder-naming-conventions)
5. [Shared Coordinate System Requirements](#shared-coordinate-system-requirements)
6. [Information Delivery Specification (IDS)](#information-delivery-specification-ids)
7. [BIM Execution Plan (BEP)](#bim-execution-plan-bep)
8. [Discipline-Specific Compliance Checklists](#discipline-specific-compliance-checklists)
9. [Discipline Coordination & Interface Management](#discipline-coordination--interface-management)
10. [Data Drop Procedures](#data-drop-procedures)
11. [IFC & COBie Requirements](#ifc--cobie-requirements)
12. [Quality Assurance & Validation](#quality-assurance--validation)
13. [Handover & Asset Management](#handover--asset-management)
14. [Information Management Processes](#information-management-processes)
15. [Compliance Verification Checklist](#compliance-verification-checklist)

---

## ISO 19650 STANDARDS OVERVIEW

### Part 1: Concepts and Principles
- Framework for information management in BIM
- Definition of roles, responsibilities, and competencies
- Information requirements and delivery framework

### Part 2: Information Delivery
- Processes and procedures for information delivery
- Team member appointment and information management roles
- Information requirements and delivery specifications

### Part 3: Information Delivery Specification
- Development of information delivery specifications
- Technical aspects of information exchange
- Data formats and standards

### Part 5: Security-Minded Approach
- Information security management
- Data protection and access control
- Cybersecurity requirements

---

## PROJECT INFORMATION REQUIREMENTS

### 1. Employer's Information Requirements (EIR)

**Document:** `[PROJECT_CODE]_EIR_v[VERSION].pdf`

**Mandatory Content:**
- [ ] Project objectives and success criteria
- [ ] Required information outputs at each project stage
- [ ] Information standards and formats required
- [ ] Data drop schedules and milestones
- [ ] Security requirements and data classification
- [ ] Asset information requirements (for operational phase)
- [ ] Compliance with local regulations and standards
- [ ] Handover and asset management requirements

**Disciplines Involved:** All (Architecture, Structure, Building Services)

### 2. Project Information Requirements (PIR)

**Document:** `[PROJECT_CODE]_PIR_v[VERSION].pdf`

**Mandatory Content:**
- [ ] Detailed breakdown of information requirements by discipline
- [ ] Specific information needs for each project phase
- [ ] Coordination requirements between disciplines
- [ ] Quality standards and accuracy requirements
- [ ] Clash detection and resolution protocols
- [ ] Information exchange frequency and format
- [ ] Responsibility matrix for information delivery

**Disciplines Involved:** All

---

## ORGANIZATIONAL & TEAM STRUCTURE

### 1. Information Management Team Roles

#### Lead Information Manager (LIM)
- **Responsibility:** Overall information management strategy and compliance
- **Reporting:** Project Director/Client
- **Key Tasks:**
  - [ ] Develop and maintain BIM Execution Plan
  - [ ] Oversee information delivery schedules
  - [ ] Manage information security and access
  - [ ] Coordinate between disciplines
  - [ ] Ensure ISO 19650 compliance

#### Discipline Information Managers (DIM)

**Architecture DIM**
- [ ] Manage architectural information delivery
- [ ] Coordinate with structural and services
- [ ] Maintain architectural standards
- [ ] Quality assurance of architectural models

**Structural Engineering DIM**
- [ ] Manage structural information delivery
- [ ] Coordinate structural-architectural interface
- [ ] Maintain structural standards
- [ ] Quality assurance of structural models

**Building Services DIM**
- [ ] Manage MEP information delivery
- [ ] Coordinate services-architectural interface
- [ ] Maintain services standards
- [ ] Quality assurance of services models

#### BIM Coordinator
- [ ] Day-to-day model coordination
- [ ] Clash detection and reporting
- [ ] Model federation and management
- [ ] Data exchange and format conversion

#### Information Security Officer
- [ ] Data protection and access control
- [ ] Cybersecurity compliance
- [ ] Information classification and handling
- [ ] Audit and compliance monitoring

### 2. Responsibility Matrix (RACI)

**Template:** `[PROJECT_CODE]_RACI_Matrix_v[VERSION].xlsx`

| Task | Architecture | Structure | Building Services | LIM | BIM Coord |
|------|--------------|-----------|-------------------|-----|-----------|
| Model Creation | R | R | R | A | C |
| Coordination | C | C | C | A | R |
| Clash Detection | C | C | C | A | R |
| Data Drops | R | R | R | A | S |
| IFC Export | R | R | R | A | C |
| COBie Delivery | C | C | C | R | S |
| Quality Assurance | R | R | R | A | C |

**Legend:** R=Responsible, A=Accountable, C=Consulted, S=Supporter

---

## FILE & FOLDER NAMING CONVENTIONS

### 1. Project Folder Structure

```
[PROJECT_CODE]_[PROJECT_NAME]_BIM/
│
├── 00_ADMINISTRATION/
│   ├── 00_EIR_PIR/
│   │   ├── [PROJECT_CODE]_EIR_v[VERSION].pdf
│   │   ├── [PROJECT_CODE]_PIR_v[VERSION].pdf
│   │   └── [PROJECT_CODE]_IDS_v[VERSION].pdf
│   ├── 01_BEP/
│   │   ├── [PROJECT_CODE]_BEP_v[VERSION].pdf
│   │   └── [PROJECT_CODE]_BEP_Appendices_v[VERSION].pdf
│   ├── 02_RACI/
│   │   └── [PROJECT_CODE]_RACI_Matrix_v[VERSION].xlsx
│   ├── 03_STANDARDS/
│   │   ├── [PROJECT_CODE]_Naming_Conventions_v[VERSION].pdf
│   │   ├── [PROJECT_CODE]_Coordinate_System_v[VERSION].pdf
│   │   └── [PROJECT_CODE]_Data_Dictionary_v[VERSION].xlsx
│   └── 04_MEETING_MINUTES/
│       └── [PROJECT_CODE]_BIM_Coordination_Minutes_[DATE].pdf
│
├── 01_MODELS/
│   ├── 01_ARCHITECTURE/
│   │   ├── WORKING/
│   │   │   ├── [PROJECT_CODE]_ARC_[PHASE]_v[VERSION].rvt
│   │   │   ├── [PROJECT_CODE]_ARC_[PHASE]_v[VERSION].ifc
│   │   │   └── [PROJECT_CODE]_ARC_[PHASE]_v[VERSION].nwd
│   │   ├── ISSUED/
│   │   │   ├── [PROJECT_CODE]_ARC_[PHASE]_v[VERSION]_ISSUED.rvt
│   │   │   └── [PROJECT_CODE]_ARC_[PHASE]_v[VERSION]_ISSUED.ifc
│   │   └── ARCHIVE/
│   │
│   ├── 02_STRUCTURE/
│   │   ├── WORKING/
│   │   │   ├── [PROJECT_CODE]_STR_[PHASE]_v[VERSION].rvt
│   │   │   ├── [PROJECT_CODE]_STR_[PHASE]_v[VERSION].ifc
│   │   │   └── [PROJECT_CODE]_STR_[PHASE]_v[VERSION].nwd
│   │   ├── ISSUED/
│   │   └── ARCHIVE/
│   │
│   ├── 03_BUILDING_SERVICES/
│   │   ├── 03A_MECHANICAL/
│   │   │   ├── WORKING/
│   │   │   ├── ISSUED/
│   │   │   └── ARCHIVE/
│   │   ├── 03B_ELECTRICAL/
│   │   │   ├── WORKING/
│   │   │   ├── ISSUED/
│   │   │   └── ARCHIVE/
│   │   └── 03C_PLUMBING/
│   │       ├── WORKING/
│   │       ├── ISSUED/
│   │       └── ARCHIVE/
│   │
│   ├── 04_FEDERATED/
│   │   ├── [PROJECT_CODE]_FED_[PHASE]_v[VERSION].nwd
│   │   ├── [PROJECT_CODE]_FED_[PHASE]_v[VERSION].ifc
│   │   └── ARCHIVE/
│   │
│   └── 05_REFERENCE/
│       ├── [PROJECT_CODE]_SURVEY_[DATE].dwg
│       └── [PROJECT_CODE]_SITE_PLAN_[DATE].dwg
│
├── 02_COORDINATION/
│   ├── 01_CLASH_REPORTS/
│   │   ├── [PROJECT_CODE]_CLASH_REPORT_[PHASE]_v[VERSION].pdf
│   │   ├── [PROJECT_CODE]_CLASH_REPORT_[PHASE]_v[VERSION].xlsx
│   │   └── [PROJECT_CODE]_CLASH_RESOLUTION_LOG_[PHASE]_v[VERSION].xlsx
│   ├── 02_COORDINATION_DRAWINGS/
│   │   ├── [PROJECT_CODE]_COORD_[PHASE]_[LEVEL]_v[VERSION].pdf
│   │   └── [PROJECT_CODE]_COORD_[PHASE]_[SECTION]_v[VERSION].pdf
│   └── 03_INTERFACE_AGREEMENTS/
│       ├── [PROJECT_CODE]_ARC_STR_Interface_v[VERSION].pdf
│       ├── [PROJECT_CODE]_ARC_MEP_Interface_v[VERSION].pdf
│       └── [PROJECT_CODE]_STR_MEP_Interface_v[VERSION].pdf
│
├── 03_DATA_DROPS/
│   └── [PROJECT_CODE]_DATA_DROP_[PHASE]_[DATE]_v[VERSION]/
│       ├── MODELS/
│       ├── COBIE/
│       ├── DOCUMENTATION/
│       └── METADATA/
│
├── 04_QUALITY_ASSURANCE/
│   ├── 01_MODEL_AUDITS/
│   ├── 02_IFC_VALIDATION/
│   └── 03_COBIE_VALIDATION/
│
├── 05_INFORMATION_SECURITY/
│   ├── [PROJECT_CODE]_Data_Classification_v[VERSION].pdf
│   ├── [PROJECT_CODE]_Access_Control_Matrix_v[VERSION].xlsx
│   └── [PROJECT_CODE]_Information_Security_Log_[DATE].xlsx
│
└── 06_HANDOVER/
    ├── [PROJECT_CODE]_Asset_Information_[DATE].xlsx
    ├── [PROJECT_CODE]_COBie_Final_[DATE].xlsx
    └── [PROJECT_CODE]_As_Built_Models_[DATE]/
```

### 2. File Naming Convention Rules

**Format:** `[PROJECT_CODE]_[DISCIPLINE]_[PHASE]_[CONTENT]_v[VERSION].[EXTENSION]`

**Components:**

| Component | Format | Example | Notes |
|-----------|--------|---------|-------|
| PROJECT_CODE | 4-6 chars | PROJ01, LC001 | Unique project identifier |
| DISCIPLINE | 3-4 chars | ARC, STR, MEP, MECH, ELEC, PLMB | Architecture, Structure, Mechanical, Electrical, Plumbing |
| PHASE | 2-3 chars | SD, DD, CD, TEN, CON, AS | Scheme Design, Detailed Design, Construction Documents, Tender, Construction, As-Built |
| CONTENT | Descriptive | FLOOR_PLAN, SECTION, DETAIL | Clear description of content |
| VERSION | v[NUMBER] | v01, v02, v10 | Sequential numbering, zero-padded |
| EXTENSION | File type | .rvt, .ifc, .dwg, .pdf | Native or export format |

**Examples:**
- `PROJ01_ARC_DD_FLOOR_PLAN_v03.rvt`
- `PROJ01_STR_CD_FOUNDATION_DETAIL_v02.ifc`
- `PROJ01_MEP_MECH_DD_DUCTWORK_v01.rvt`
- `PROJ01_FED_CD_v04.nwd`

### 3. Revision Numbering Protocol

- **v01-v09:** Design development iterations
- **v10-v19:** Tender/Coordination phase
- **v20-v29:** Construction phase
- **v30+:** As-built and post-construction

---

## SHARED COORDINATE SYSTEM REQUIREMENTS

### 1. Coordinate System Definition

**Document:** `[PROJECT_CODE]_Coordinate_System_v[VERSION].pdf`

**Mandatory Specifications:**

#### Horizontal Datum
- [ ] Coordinate system type (e.g., UTM, Local Grid, Project-Specific)
- [ ] Projection system and parameters
- [ ] False Easting and False Northing values
- [ ] Rotation angle from true north (if applicable)
- [ ] Accuracy specification (±[X]mm)

#### Vertical Datum
- [ ] Vertical reference point (e.g., Mean Sea Level, Ordnance Datum)
- [ ] Benchmark location and elevation
- [ ] Elevation reference for all models
- [ ] Accuracy specification (±[X]mm)

#### Project Origin
- [ ] Project origin coordinates (Easting, Northing, Elevation)
- [ ] Location of origin point on site
- [ ] Relationship to site survey data
- [ ] Relationship to reference drawings

### 2. Discipline-Specific Coordinate Requirements

#### Architecture
- [ ] All models created in shared coordinate system
- [ ] Site survey data imported and locked
- [ ] Reference levels established and shared
- [ ] Grid lines aligned with structural grid
- [ ] Coordinate system verified before design commencement

#### Structural Engineering
- [ ] Structural grid established in shared coordinates
- [ ] Foundation coordinates verified against survey
- [ ] Column centerlines aligned with architectural grid
- [ ] Structural levels match architectural levels
- [ ] Coordinate system locked and protected

#### Building Services (MEP)
- [ ] All equipment located in shared coordinates
- [ ] Ductwork, piping, and cable routes in shared coordinates
- [ ] Equipment centerlines aligned with structural grid
- [ ] Vertical distribution aligned with architectural levels
- [ ] Coordinate system verified before routing commencement

### 3. Coordinate System Verification Protocol

**Document:** `[PROJECT_CODE]_Coordinate_Verification_[DATE].pdf`

**Verification Steps:**
- [ ] Survey data imported and verified
- [ ] Project origin coordinates confirmed
- [ ] Vertical datum confirmed
- [ ] All discipline models checked for coordinate alignment
- [ ] Grid lines verified for alignment
- [ ] Reference levels verified for consistency
- [ ] Clash detection run to verify alignment
- [ ] Verification report signed off by LIM

**Frequency:** Before each design phase commencement and before data drops

---

## INFORMATION DELIVERY SPECIFICATION (IDS)

**Document:** `[PROJECT_CODE]_IDS_v[VERSION].pdf`

### 1. Information Delivery Schedule

| Phase | Milestone | Delivery Date | Deliverable | Format | Responsible |
|-------|-----------|---------------|-------------|--------|-------------|
| SD | Concept | [DATE] | Architectural Concept Model | IFC 2x3 | Architecture |
| SD | Concept | [DATE] | Structural Concept Model | IFC 2x3 | Structure |
| DD | Design | [DATE] | Detailed Architectural Model | IFC 4 | Architecture |
| DD | Design | [DATE] | Detailed Structural Model | IFC 4 | Structure |
| DD | Design | [DATE] | MEP Coordination Model | IFC 4 | Building Services |
| CD | Documentation | [DATE] | Construction Documents | IFC 4 + PDF | All |
| CD | Documentation | [DATE] | COBie Data | COBie 2.4 | All |
| TEN | Tender | [DATE] | Tender Models | IFC 4 | All |
| CON | Construction | [DATE] | As-Built Models | IFC 4 | All |
| CON | Handover | [DATE] | Asset Information | COBie 2.4 | All |

### 2. Information Requirements by Discipline

#### Architecture

**Scheme Design (SD):**
- [ ] Site context and massing model
- [ ] Building envelope and floor plates
- [ ] Gross floor areas
- [ ] Key architectural elements (walls, doors, windows)
- [ ] Spatial organization and circulation
- [ ] Preliminary material specifications

**Detailed Design (DD):**
- [ ] Complete architectural model with all spaces
- [ ] Detailed wall, floor, and roof construction
- [ ] Door and window schedules with specifications
- [ ] Finishes and material specifications
- [ ] Architectural details and sections
- [ ] Accessibility compliance information

**Construction Documents (CD):**
- [ ] As-built architectural model
- [ ] Complete construction details
- [ ] Specification data linked to model elements
- [ ] Maintenance and cleaning access information
- [ ] Asset information for handover

#### Structural Engineering

**Scheme Design (SD):**
- [ ] Structural grid and column layout
- [ ] Foundation strategy and preliminary sizing
- [ ] Structural system description
- [ ] Key structural elements (columns, beams, walls)
- [ ] Preliminary material specifications

**Detailed Design (DD):**
- [ ] Complete structural model with all elements
- [ ] Detailed member sizing and reinforcement
- [ ] Connection details and specifications
- [ ] Material specifications and grades
- [ ] Structural analysis results summary
- [ ] Temporary works strategy

**Construction Documents (CD):**
- [ ] As-built structural model
- [ ] Complete construction details
- [ ] Specification data linked to model elements
- [ ] Maintenance and inspection access information
- [ ] Asset information for handover

#### Building Services (MEP)

**Mechanical - Scheme Design (SD):**
- [ ] HVAC system strategy and zoning
- [ ] Main plant room location and sizing
- [ ] Preliminary ductwork routing
- [ ] Key equipment (chillers, boilers, AHUs)
- [ ] Preliminary material specifications

**Mechanical - Detailed Design (DD):**
- [ ] Complete ductwork model with sizing
- [ ] All mechanical equipment with specifications
- [ ] Ductwork connections and fittings
- [ ] Insulation and fire rating specifications
- [ ] Control system strategy
- [ ] Maintenance access requirements

**Electrical - Scheme Design (SD):**
- [ ] Electrical distribution strategy
- [ ] Main switchroom location and sizing
- [ ] Preliminary cable routing
- [ ] Key equipment (transformers, panels)
- [ ] Preliminary material specifications

**Electrical - Detailed Design (DD):**
- [ ] Complete cable tray and conduit routing
- [ ] All electrical equipment with specifications
- [ ] Cable schedules and sizing
- [ ] Lighting and power outlet locations
- [ ] Control system strategy
- [ ] Maintenance access requirements

**Plumbing - Scheme Design (SD):**
- [ ] Water supply and drainage strategy
- [ ] Main plant room location and sizing
- [ ] Preliminary piping routing
- [ ] Key equipment (pumps, tanks, treatment)
- [ ] Preliminary material specifications

**Plumbing - Detailed Design (DD):**
- [ ] Complete piping model with sizing
- [ ] All plumbing equipment with specifications
- [ ] Pipe connections and fittings
- [ ] Insulation and fire rating specifications
- [ ] Maintenance access requirements
- [ ] Backflow prevention strategy

---

## BIM EXECUTION PLAN (BEP)

**Document:** `[PROJECT_CODE]_BEP_v[VERSION].pdf`

### 1. BEP Core Sections

**Section 1: Project Overview**
- [ ] Project name, location, and code
- [ ] Project description and scope
- [ ] Project phases and timeline
- [ ] Key stakeholders and contacts
- [ ] Project objectives and success criteria

**Section 2: Information Management Strategy**
- [ ] Information management approach
- [ ] Information standards and formats
- [ ] Data exchange protocols
- [ ] Information security strategy
- [ ] Compliance requirements

**Section 3: Roles and Responsibilities**
- [ ] Organizational structure
- [ ] Role definitions and responsibilities
- [ ] Competency requirements
- [ ] Training and development plan

**Section 4: Information Standards**
- [ ] File naming conventions
- [ ] Folder structure
- [ ] Data formats and standards
- [ ] Classification systems
- [ ] Property sets and parameters

**Section 5: Collaboration and Communication**
- [ ] Coordination procedures
- [ ] Meeting schedule and protocols
- [ ] Issue resolution process
- [ ] Change management procedure
- [ ] Communication channels and tools

**Section 6: Quality Assurance**
- [ ] Quality standards and criteria
- [ ] Model audit procedures
- [ ] Clash detection and resolution
- [ ] Data validation procedures
- [ ] Sign-off procedures

**Section 7: Information Security**
- [ ] Data classification
- [ ] Access control procedures
- [ ] Backup and recovery procedures
- [ ] Cybersecurity requirements
- [ ] Compliance with regulations

---

## DISCIPLINE-SPECIFIC COMPLIANCE CHECKLISTS

### ARCHITECTURE DISCIPLINE COMPLIANCE

#### Pre-Project Setup
- [ ] Coordinate system established and documented
- [ ] Survey data imported and verified
- [ ] Reference levels created and shared
- [ ] Grid lines established and aligned with structure
- [ ] Project template configured with correct standards
- [ ] Family library established and shared
- [ ] View templates created for consistency
- [ ] Sheet templates created for documentation

#### Scheme Design Phase (SD)
- [ ] Site context model created
- [ ] Building massing model developed
- [ ] Floor plates defined with gross areas
- [ ] Key architectural elements modeled
- [ ] Spatial organization documented
- [ ] Preliminary material specifications assigned
- [ ] Model exported to IFC 2x3 format
- [ ] Model validated against IFC schema
- [ ] Coordinate system verification completed
- [ ] Data drop checklist completed
- [ ] Transmittal document prepared

#### Detailed Design Phase (DD)
- [ ] All spaces defined with correct classification
- [ ] Space properties populated (area, volume, height)
- [ ] All walls modeled with correct construction
- [ ] All doors scheduled with specifications
- [ ] All windows scheduled with specifications
- [ ] All finishes specified and linked to model
- [ ] Accessibility compliance verified
- [ ] Architectural details created
- [ ] Section drawings generated
- [ ] Elevation drawings generated
- [ ] Model exported to IFC 4 format
- [ ] IFC validation report completed
- [ ] COBie data populated for all assets
- [ ] Clash detection run with structure and MEP
- [ ] Clash resolution documented
- [ ] Coordination drawings prepared
- [ ] Data drop checklist completed
- [ ] Transmittal document prepared

#### Construction Documents Phase (CD)
- [ ] As-built model updated with all changes
- [ ] Construction details finalized
- [ ] Specification data linked to all elements
- [ ] Maintenance and cleaning access documented
- [ ] Asset information completed for handover
- [ ] Model exported to IFC 4 format
- [ ] Final IFC validation completed
- [ ] Final COBie data validated
- [ ] As-built drawings prepared
- [ ] Handover documentation prepared
- [ ] Data drop checklist completed
- [ ] Final transmittal document prepared

#### Quality Assurance (Architecture)
- [ ] Model audit completed (geometry, properties, standards)
- [ ] IFC export validation completed
- [ ] COBie data validation completed
- [ ] Coordinate system verification completed
- [ ] Clash detection and resolution verified
- [ ] Documentation completeness verified
- [ ] Sign-off obtained from Architecture DIM

---

### STRUCTURAL ENGINEERING DISCIPLINE COMPLIANCE

#### Pre-Project Setup
- [ ] Coordinate system established and documented
- [ ] Survey data imported and verified
- [ ] Structural grid created in shared coordinates
- [ ] Reference levels created and aligned with architecture
- [ ] Project template configured with correct standards
- [ ] Family library established and shared
- [ ] View templates created for consistency
- [ ] Sheet templates created for documentation

#### Scheme Design Phase (SD)
- [ ] Structural grid established and documented
- [ ] Column layout defined
- [ ] Foundation strategy documented
- [ ] Structural system description prepared
- [ ] Key structural elements modeled
- [ ] Preliminary member sizing completed
- [ ] Preliminary material specifications assigned
- [ ] Model exported to IFC 2x3 format
- [ ] Model validated against IFC schema
- [ ] Coordinate system verification completed
- [ ] Grid alignment with architecture verified
- [ ] Data drop checklist completed
- [ ] Transmittal document prepared

#### Detailed Design Phase (DD)
- [ ] All structural members modeled with correct properties
- [ ] Member sizing finalized
- [ ] Reinforcement scheduled and specified
- [ ] Connection details created
- [ ] Material specifications finalized
- [ ] Structural analysis results documented
- [ ] Temporary works strategy documented
- [ ] Structural details created
- [ ] Section drawings generated
- [ ] Elevation drawings generated
- [ ] Model exported to IFC 4 format
- [ ] IFC validation report completed
- [ ] COBie data populated for all assets
- [ ] Clash detection run with architecture and MEP
- [ ] Clash resolution documented
- [ ] Coordination drawings prepared
- [ ] Interface agreements signed (ARC-STR, STR-MEP)
- [ ] Data drop checklist completed
- [ ] Transmittal document prepared

#### Construction Documents Phase (CD)
- [ ] As-built model updated with all changes
- [ ] Construction details finalized
- [ ] Specification data linked to all elements
- [ ] Maintenance and inspection access documented
- [ ] Asset information completed for handover
- [ ] Model exported to IFC 4 format
- [ ] Final IFC validation completed
- [ ] Final COBie data validated
- [ ] As-built drawings prepared
- [ ] Handover documentation prepared
- [ ] Data drop checklist completed
- [ ] Final transmittal document prepared

#### Quality Assurance (Structure)
- [ ] Model audit completed (geometry, properties, standards)
- [ ] IFC export validation completed
- [ ] COBie data validation completed
- [ ] Coordinate system verification completed
- [ ] Grid alignment verification completed
- [ ] Clash detection and resolution verified
- [ ] Documentation completeness verified
- [ ] Sign-off obtained from Structural DIM

---

### BUILDING SERVICES (MEP) DISCIPLINE COMPLIANCE

#### Pre-Project Setup
- [ ] Coordinate system established and documented
- [ ] Survey data imported and verified
- [ ] Reference levels created and aligned with architecture
- [ ] Equipment zones defined
- [ ] Project template configured with correct standards
- [ ] Family library established and shared (MECH, ELEC, PLMB)
- [ ] View templates created for consistency
- [ ] Sheet templates created for documentation

#### Mechanical Systems - Scheme Design Phase (SD)
- [ ] HVAC system strategy documented
- [ ] Zoning strategy defined
- [ ] Main plant room location identified
- [ ] Preliminary equipment sizing completed
- [ ] Preliminary ductwork routing planned
- [ ] Key equipment modeled
- [ ] Preliminary material specifications assigned
- [ ] Model exported to IFC 2x3 format
- [ ] Model validated against IFC schema
- [ ] Coordinate system verification completed
- [ ] Data drop checklist completed
- [ ] Transmittal document prepared

#### Mechanical Systems - Detailed Design Phase (DD)
- [ ] Complete ductwork model created
- [ ] Ductwork sizing finalized
- [ ] All mechanical equipment modeled with specifications
- [ ] Equipment connections detailed
- [ ] Insulation specifications assigned
- [ ] Fire rating specifications assigned
- [ ] Control system strategy documented
- [ ] Maintenance access requirements documented
- [ ] Mechanical details created
- [ ] Section drawings generated
- [ ] Model exported to IFC 4 format
- [ ] IFC validation report completed
- [ ] COBie data populated for all equipment
- [ ] Clash detection run with architecture and structure
- [ ] Clash resolution documented
- [ ] Coordination drawings prepared
- [ ] Interface agreements signed (ARC-MEP, STR-MEP)
- [ ] Data drop checklist completed
- [ ] Transmittal document prepared

#### Electrical Systems - Scheme Design Phase (SD)
- [ ] Electrical distribution strategy documented
- [ ] Main switchroom location identified
- [ ] Preliminary equipment sizing completed
- [ ] Preliminary cable routing planned
- [ ] Key equipment modeled
- [ ] Preliminary material specifications assigned
- [ ] Model exported to IFC 2x3 format
- [ ] Model validated against IFC schema
- [ ] Coordinate system verification completed
- [ ] Data drop checklist completed
- [ ] Transmittal document prepared

#### Electrical Systems - Detailed Design Phase (DD)
- [ ] Complete cable tray and conduit routing created
- [ ] Cable sizing finalized
- [ ] All electrical equipment modeled with specifications
- [ ] Equipment connections detailed
- [ ] Cable schedules completed
- [ ] Lighting and power outlet locations defined
- [ ] Control system strategy documented
- [ ] Maintenance access requirements documented
- [ ] Electrical details created
- [ ] Section drawings generated
- [ ] Model exported to IFC 4 format
- [ ] IFC validation report completed
- [ ] COBie data populated for all equipment
- [ ] Clash detection run with architecture and structure
- [ ] Clash resolution documented
- [ ] Coordination drawings prepared
- [ ] Data drop checklist completed
- [ ] Transmittal document prepared

#### Plumbing Systems - Scheme Design Phase (SD)
- [ ] Water supply and drainage strategy documented
- [ ] Main plant room location identified
- [ ] Preliminary equipment sizing completed
- [ ] Preliminary piping routing planned
- [ ] Key equipment modeled
- [ ] Preliminary material specifications assigned
- [ ] Model exported to IFC 2x3 format
- [ ] Model validated against IFC schema
- [ ] Coordinate system verification completed
- [ ] Data drop checklist completed
- [ ] Transmittal document prepared

#### Plumbing Systems - Detailed Design Phase (DD)
- [ ] Complete piping model created
- [ ] Piping sizing finalized
- [ ] All plumbing equipment modeled with specifications
- [ ] Equipment connections detailed
- [ ] Insulation specifications assigned
- [ ] Fire rating specifications assigned
- [ ] Backflow prevention strategy documented
- [ ] Maintenance access requirements documented
- [ ] Plumbing details created
- [ ] Section drawings generated
- [ ] Model exported to IFC 4 format
- [ ] IFC validation report completed
- [ ] COBie data populated for all equipment
- [ ] Clash detection run with architecture and structure
- [ ] Clash resolution documented
- [ ] Coordination drawings prepared
- [ ] Data drop checklist completed
- [ ] Transmittal document prepared

#### MEP Construction Documents Phase (CD)
- [ ] As-built models updated with all changes
- [ ] Construction details finalized
- [ ] Specification data linked to all elements
- [ ] Maintenance and service access documented
- [ ] Asset information completed for handover
- [ ] Models exported to IFC 4 format
- [ ] Final IFC validation completed
- [ ] Final COBie data validated
- [ ] As-built drawings prepared
- [ ] Handover documentation prepared
- [ ] Data drop checklist completed
- [ ] Final transmittal document prepared

#### Quality Assurance (MEP)
- [ ] Model audit completed (geometry, properties, standards)
- [ ] IFC export validation completed
- [ ] COBie data validation completed
- [ ] Coordinate system verification completed
- [ ] Clash detection and resolution verified
- [ ] Documentation completeness verified
- [ ] Sign-off obtained from Building Services DIM

---

## DISCIPLINE COORDINATION & INTERFACE MANAGEMENT

### 1. Coordination Meeting Protocol

**Frequency:** Weekly during design phases, bi-weekly during construction

**Attendees:**
- [ ] Lead Information Manager
- [ ] Architecture DIM
- [ ] Structural Engineering DIM
- [ ] Building Services DIM
- [ ] BIM Coordinator
- [ ] Project Manager

**Meeting Agenda:**
- [ ] Model status updates from each discipline
- [ ] Clash detection and resolution review
- [ ] Coordination drawing review
- [ ] Interface agreement updates
- [ ] Data drop schedule confirmation
- [ ] Quality assurance status
- [ ] Issues and risks discussion
- [ ] Action items and responsibilities

**Documentation:**
- [ ] Meeting minutes prepared within 24 hours
- [ ] Action items tracked and assigned
- [ ] Decisions documented and distributed
- [ ] Minutes filed in `00_ADMINISTRATION/04_MEETING_MINUTES/`

### 2. Clash Detection and Resolution Protocol

**Clash Detection Process:**
- [ ] Federated model created from all discipline models
- [ ] Clash detection run using approved software
- [ ] Clash report generated with severity classification
- [ ] Clashes categorized (Hard, Soft, Warning)
- [ ] Clashes assigned to responsible discipline
- [ ] Resolution timeline established

**Clash Resolution:**
- [ ] Hard clashes resolved before data drop
- [ ] Soft clashes reviewed and documented
- [ ] Resolution documented in clash log
- [ ] Updated models provided by responsible discipline
- [ ] Clash detection re-run to verify resolution
- [ ] Clash resolution report prepared

### 3. Interface Agreements

**Architecture-Structure Interface Agreement**
- [ ] Structural grid alignment with architectural grid
- [ ] Reference level alignment
- [ ] Column locations and centerlines
- [ ] Beam soffit elevations
- [ ] Opening locations and sizes
- [ ] Load-bearing wall locations
- [ ] Structural penetrations through floors
- [ ] Temporary support requirements
- [ ] Maintenance access coordination

**Architecture-MEP Interface Agreement**
- [ ] Equipment room locations and sizing
- [ ] Ductwork routing and clearances
- [ ] Piping routing and clearances
- [ ] Cable tray routing and clearances
- [ ] Ceiling heights and soffit clearances
- [ ] Wall penetrations and sleeves
- [ ] Floor penetrations and sleeves
- [ ] Maintenance access requirements
- [ ] Vibration isolation requirements

**Structure-MEP Interface Agreement**
- [ ] Equipment support requirements
- [ ] Structural penetrations for ductwork/piping
- [ ] Vibration isolation requirements
- [ ] Roof-mounted equipment coordination
- [ ] Temporary support requirements
- [ ] Maintenance access coordination
- [ ] Load requirements for equipment

---

## DATA DROP PROCEDURES

### 1. Data Drop Schedule

**Mandatory Data Drops:**

| Phase | Milestone | Date | Deliverables | Format |
|-------|-----------|------|--------------|--------|
| SD | Concept Review | [DATE] | ARC, STR, MEP Models | IFC 2x3 |
| DD | 50% Design | [DATE] | ARC, STR, MEP Models | IFC 4 |
| DD | 100% Design | [DATE] | ARC, STR, MEP, FED Models + COBie | IFC 4 + XLSX |
| CD | 50% Documentation | [DATE] | ARC, STR, MEP, FED Models + COBie | IFC 4 + XLSX |
| CD | 100% Documentation | [DATE] | ARC, STR, MEP, FED Models + COBie | IFC 4 + XLSX |
| TEN | Tender | [DATE] | ARC, STR, MEP, FED Models | IFC 4 |
| CON | Monthly | [DATE] | As-Built Models + COBie Updates | IFC 4 + XLSX |
| CON | Final Handover | [DATE] | As-Built Models + Final COBie | IFC 4 + XLSX |

### 2. Data Drop Package Contents

**Required Contents:**
```
MODELS/
├── [PROJECT_CODE]_ARC_[PHASE]_v[VERSION].ifc
├── [PROJECT_CODE]_STR_[PHASE]_v[VERSION].ifc
├── [PROJECT_CODE]_MEP_MECH_[PHASE]_v[VERSION].ifc
├── [PROJECT_CODE]_MEP_ELEC_[PHASE]_v[VERSION].ifc
├── [PROJECT_CODE]_MEP_PLMB_[PHASE]_v[VERSION].ifc
└── [PROJECT_CODE]_FED_[PHASE]_v[VERSION].ifc

COBIE/
└── [PROJECT_CODE]_COBie_[PHASE]_v[VERSION].xlsx

DOCUMENTATION/
├── [PROJECT_CODE]_Data_Drop_Transmittal_[DATE].pdf
├── [PROJECT_CODE]_Data_Drop_Checklist_[DATE].pdf
├── [PROJECT_CODE]_Clash_Report_[PHASE]_v[VERSION].pdf
└── [PROJECT_CODE]_Coordination_Drawings_[PHASE]_v[VERSION].pdf
```

### 3. Data Drop Checklist

**Pre-Drop Verification:**
- [ ] All models updated to latest version
- [ ] Coordinate system verified in all models
- [ ] All clashes resolved or documented
- [ ] All properties populated correctly
- [ ] All IFC exports validated
- [ ] All COBie data validated
- [ ] File naming conventions verified
- [ ] File sizes optimized
- [ ] Backup copies created
- [ ] Virus scan completed

**IFC Validation:**
- [ ] IFC schema validation passed
- [ ] All required entities present
- [ ] All properties correctly mapped
- [ ] Coordinate system correctly defined
- [ ] Units correctly specified
- [ ] No orphaned objects
- [ ] File integrity verified

**COBie Validation:**
- [ ] All required sheets present
- [ ] All mandatory fields populated
- [ ] No duplicate entries
- [ ] All references valid
- [ ] Data consistency verified
- [ ] Spelling and formatting checked

**Sign-Off:**
- [ ] Architecture DIM sign-off
- [ ] Structural DIM sign-off
- [ ] Building Services DIM sign-off
- [ ] Lead Information Manager approval
- [ ] Client acceptance (if required)

---

## IFC & COBie REQUIREMENTS

### 1. IFC (Industry Foundation Classes) Specifications

**IFC Version:** IFC 4 (or IFC 2x3 for compatibility)

**Required IFC Entities by Discipline:**

**Architecture:**
- [ ] IfcBuilding
- [ ] IfcBuildingStorey
- [ ] IfcSpace
- [ ] IfcWall
- [ ] IfcDoor
- [ ] IfcWindow
- [ ] IfcSlab
- [ ] IfcRoof
- [ ] IfcFurniture
- [ ] IfcCovering (finishes)

**Structure:**
- [ ] IfcBuilding
- [ ] IfcBuildingStorey
- [ ] IfcColumn
- [ ] IfcBeam
- [ ] IfcWall (structural)
- [ ] IfcSlab
- [ ] IfcFooting
- [ ] IfcMember (secondary members)
- [ ] IfcPlate (connections)

**Building Services:**
- [ ] IfcBuilding
- [ ] IfcBuildingStorey
- [ ] IfcDuctSegment
- [ ] IfcPipeSegment
- [ ] IfcCableSegment
- [ ] IfcFlowTerminal (outlets, diffusers)
- [ ] IfcFlowController (dampers, valves)
- [ ] IfcFlowMovingDevice (fans, pumps)
- [ ] IfcFlowStorageDevice (tanks, accumulators)
- [ ] IfcFlowTreatmentDevice (filters, heat exchangers)

**IFC Export Checklist:**
- [ ] All required entities present
- [ ] All properties correctly mapped
- [ ] All relationships correctly defined
- [ ] Coordinate system correctly defined
- [ ] Units correctly specified
- [ ] Classification system applied
- [ ] IFC file validated against schema
- [ ] File size optimized (remove unused data)

### 2. COBie (Construction Operations Building Information Exchange)

**COBie Version:** COBie 2.4 (UK Standard)

**Required COBie Sheets:**

| Sheet | Content | Responsible |
|-------|---------|-------------|
| Project | Project information | LIM |
| Facility | Building and facility information | Architecture |
| Floor | Floor information | Architecture |
| Space | Space information | Architecture |
| Zone | Zone information | All |
| Type | Asset type information | All |
| Component | Component/asset information | All |
| System | System information | All |
| Assembly | Assembly information | All |
| Connection | Connection information | All |
| Spare | Spare parts information | All |
| Resource | Resource information | All |
| Job | Maintenance job information | All |
| Attribute | Attribute information | All |
| Document | Document information | All |
| Coordinate | Coordinate information | All |

**COBie Mandatory Fields (All Assets):**
- [ ] Asset Name
- [ ] Asset Type
- [ ] Manufacturer
- [ ] Model Number
- [ ] Serial Number
- [ ] Installation Date
- [ ] Warranty Start Date
- [ ] Warranty End Date
- [ ] Location (Space/Zone)
- [ ] Coordinates (X, Y, Z)
- [ ] Asset Description
- [ ] Asset Category
- [ ] Asset Subcategory

---

## QUALITY ASSURANCE & VALIDATION

### 1. Model Audit Procedures

**Audit Frequency:**
- [ ] Weekly during design phases
- [ ] Bi-weekly during construction
- [ ] Before each data drop

**Audit Checklist - Architecture:**
- [ ] All spaces defined with correct classification
- [ ] All doors and windows scheduled
- [ ] All finishes specified
- [ ] All properties populated
- [ ] Coordinate system correct
- [ ] Reference levels correct
- [ ] Grid alignment verified
- [ ] No orphaned objects
- [ ] No duplicate elements
- [ ] Naming conventions followed
- [ ] IFC export validated

**Audit Checklist - Structure:**
- [ ] All members modeled with correct properties
- [ ] All connections detailed
- [ ] All materials specified
- [ ] All reinforcement scheduled
- [ ] Coordinate system correct
- [ ] Reference levels correct
- [ ] Grid alignment verified
- [ ] No orphaned objects
- [ ] No duplicate elements
- [ ] Naming conventions followed
- [ ] IFC export validated

**Audit Checklist - MEP:**
- [ ] All equipment modeled with specifications
- [ ] All ductwork/piping sized
- [ ] All connections detailed
- [ ] All materials specified
- [ ] Coordinate system correct
- [ ] Reference levels correct
- [ ] No orphaned objects
- [ ] No duplicate elements
- [ ] Naming conventions followed
- [ ] IFC export validated

### 2. IFC Validation Procedures

**IFC Validation Checklist:**
- [ ] File opens without errors
- [ ] Schema validation passed
- [ ] All required entities present
- [ ] All properties correctly mapped
- [ ] Coordinate system correctly defined
- [ ] Units correctly specified
- [ ] Classification system applied
- [ ] No orphaned objects
- [ ] File size optimized
- [ ] Checksums verified

### 3. COBie Validation Procedures

**COBie Validation Checklist:**
- [ ] All required sheets present
- [ ] All mandatory fields populated
- [ ] No duplicate entries
- [ ] All references valid
- [ ] Data consistency verified
- [ ] Spelling and formatting correct
- [ ] Coordinates verified
- [ ] Relationships verified
- [ ] Documents referenced correctly

---

## HANDOVER & ASSET MANAGEMENT

### 1. Handover Documentation

**Required Deliverables:**
- [ ] As-built BIM models (IFC 4 format)
- [ ] Final COBie data (COBie 2.4 format)
- [ ] Asset information spreadsheet
- [ ] Maintenance manuals index
- [ ] Equipment schedules
- [ ] System descriptions
- [ ] Operating procedures
- [ ] Maintenance schedules
- [ ] Spare parts lists
- [ ] Service contact information
- [ ] Warranty information
- [ ] As-built drawings (PDF)

### 2. Asset Information Requirements

**Asset Categories:**

**Mechanical Equipment:**
- [ ] Chillers and boilers
- [ ] Air handling units
- [ ] Fans and pumps
- [ ] Ductwork and piping
- [ ] Valves and dampers
- [ ] Insulation and fire protection
- [ ] Controls and sensors

**Electrical Equipment:**
- [ ] Transformers
- [ ] Switchboards and panels
- [ ] Cable trays and conduits
- [ ] Cables and wiring
- [ ] Lighting fixtures
- [ ] Power outlets
- [ ] Controls and sensors

**Plumbing Equipment:**
- [ ] Pumps and tanks
- [ ] Pipes and fittings
- [ ] Valves and strainers
- [ ] Water treatment equipment
- [ ] Backflow prevention devices
- [ ] Insulation and fire protection
- [ ] Controls and sensors

**Architectural Elements:**
- [ ] Doors and windows
- [ ] Finishes and coverings
- [ ] Furniture and fittings
- [ ] Accessibility features
- [ ] Safety equipment

### 3. COBie Final Delivery

**Completion Requirements:**
- [ ] All assets included
- [ ] All mandatory fields completed
- [ ] All optional fields populated where applicable
- [ ] All relationships defined
- [ ] All documents referenced
- [ ] All coordinates verified
- [ ] Data validated and error-free
- [ ] Signed off by all disciplines

---

## INFORMATION MANAGEMENT PROCESSES

### 1. Model Management Process

**Model Creation:**
- [ ] New model created from approved template
- [ ] Coordinate system set to shared origin
- [ ] Reference levels created and linked
- [ ] Grid lines created and aligned
- [ ] Survey data imported and locked
- [ ] Naming conventions applied
- [ ] Properties configured
- [ ] View templates applied

**Model Updates:**
- [ ] Changes documented in change log
- [ ] Version number incremented
- [ ] Previous version archived
- [ ] Updated model validated
- [ ] Coordination team notified
- [ ] Clash detection re-run if necessary

**Model Archiving:**
- [ ] Previous versions moved to ARCHIVE folder
- [ ] Naming convention includes version number
- [ ] Archive folder organized by phase
- [ ] Backup copies created
- [ ] Retention policy followed

### 2. Data Exchange Process

**IFC Export:**
- [ ] Model prepared for export
- [ ] Unused objects removed
- [ ] Properties verified
- [ ] Coordinate system verified
- [ ] IFC export settings configured
- [ ] File exported to IFC format
- [ ] File validated against schema
- [ ] File size optimized
- [ ] Checksum calculated
- [ ] File stored in correct location

**COBie Export:**
- [ ] Model data extracted
- [ ] COBie template populated
- [ ] All mandatory fields completed
- [ ] Data validated
- [ ] File saved in correct format
- [ ] Checksum calculated
- [ ] File stored in correct location

### 3. Information Security Process

**Access Control:**
- [ ] User access levels defined
- [ ] Access control matrix maintained
- [ ] Passwords changed regularly
- [ ] Access logs reviewed monthly
- [ ] Unauthorized access prevented
- [ ] Audit trail maintained

**Data Protection:**
- [ ] Data classified by sensitivity
- [ ] Sensitive data encrypted
- [ ] Backup copies created regularly
- [ ] Backup copies stored securely
- [ ] Recovery procedures tested
- [ ] Disaster recovery plan maintained

**Cybersecurity:**
- [ ] Antivirus software installed and updated
- [ ] Firewall configured and monitored
- [ ] Security patches applied promptly
- [ ] Intrusion detection enabled
- [ ] Security incidents reported and logged
- [ ] Security training provided to all staff

---

## COMPLIANCE VERIFICATION CHECKLIST

### Pre-Project Compliance

- [ ] EIR document prepared and approved
- [ ] PIR document prepared and approved
- [ ] IDS document prepared and approved
- [ ] BEP document prepared and approved
- [ ] Coordinate system defined and documented
- [ ] File naming conventions established
- [ ] Folder structure created
- [ ] Team roles and responsibilities assigned
- [ ] RACI matrix completed
- [ ] Information security plan prepared
- [ ] Backup and recovery procedures established
- [ ] Software and hardware requirements confirmed
- [ ] Training completed for all team members

### Scheme Design Phase Compliance

- [ ] Coordinate system verified in all models
- [ ] All models created in shared coordinates
- [ ] Preliminary information delivered on schedule
- [ ] IFC exports validated
- [ ] Data drop checklist completed
- [ ] Transmittal document prepared
- [ ] Meeting minutes documented
- [ ] No critical issues outstanding

### Detailed Design Phase Compliance

- [ ] All models updated with detailed information
- [ ] All properties populated correctly
- [ ] Clash detection completed
- [ ] Clash resolution documented
- [ ] Coordination drawings prepared
- [ ] Interface agreements signed
- [ ] IFC exports validated
- [ ] COBie data populated
- [ ] Data drop checklist completed
- [ ] Transmittal document prepared
- [ ] Meeting minutes documented
- [ ] Quality assurance completed

### Construction Documents Phase Compliance

- [ ] All models finalized
- [ ] All properties verified
- [ ] Final clash detection completed
- [ ] Final coordination drawings prepared
- [ ] Final IFC exports validated
- [ ] Final COBie data validated
- [ ] Data drop checklist completed
- [ ] Transmittal document prepared
- [ ] Quality assurance completed
- [ ] Sign-offs obtained from all disciplines

### Construction Phase Compliance

- [ ] As-built models updated monthly
- [ ] COBie data updated with actual information
- [ ] Monthly data drops completed
- [ ] Coordination meetings held
- [ ] Issues tracked and resolved
- [ ] Quality assurance ongoing
- [ ] Final handover documentation prepared

### Handover Compliance

- [ ] As-built models finalized
- [ ] Final COBie data completed
- [ ] Asset information spreadsheet completed
- [ ] Maintenance manuals indexed
- [ ] Equipment schedules provided
- [ ] Operating procedures documented
- [ ] Maintenance schedules provided
- [ ] Spare parts lists provided
- [ ] Service contact information provided
- [ ] Warranty information provided
- [ ] Final sign-offs obtained
- [ ] Handover meeting completed

---

## SIGN-OFF AND APPROVAL

**Document Prepared By:** [NAME, TITLE, DATE]

**Reviewed By:** [NAME, TITLE, DATE]

**Approved By:** [NAME, TITLE, DATE]

**Client Acceptance:** [NAME, TITLE, DATE]

---

**END OF DOCUMENT**

*This framework is based on ISO 19650 standards and represents best practices for BIM information management in construction projects. All requirements are mandatory unless explicitly marked as optional. Project-specific modifications must be documented and approved by the Lead Information Manager.*