import os
import json
from typing import List, Optional
from pydantic import BaseModel, Field
from enum import Enum

class BimDiscipline(Enum):
    plumbing = 'S - Sanitär'
    network = 'd - Datennetz'
    heating = 'h - Heizung'
    electrical = 'e - Elektro'
    ventilation = 'l - Lüftung'
    architecture = 'a - Architektur'

class KeywordChoice(str, Enum):
    three_dimensional_modeling = "3d modeling"
    four_dimensional_simulation = "4d simulation"
    five_dimensional_cost_estimation = "5d cost estimation"
    six_dimensional_lifecycle_management = "6d lifecycle management"
    adoption = "adoptions"
    agile_bim = "agile bim"
    artificial_intelligence = "artificial intelligence"
    automated_code_checking = "automated code checking"
    automation = "automation"
    big_data_analytics = "big data analytics"
    bim_based_estimating = "bim-based estimating"
    bim_execution_plan = "bim execution plan"
    bim_governance = "bim governance"
    bim_integration = "bim integration"
    bim_maturity = "bim maturity"
    bim_objects = "bim objects"
    bim_process = "bim process"
    bim_quality_assurance = "bim quality assurance"
    bim_requirements = "bim requirements"
    bim_server = "bim server"
    bim_standardization = "bim standardization"
    bim_strategy = "bim strategy"
    bim_tools = "bim tools"
    bim_training = "bim training"
    barriers = "barriers"
    benchmarking = "benchmarking"
    building_energy_modeling = "building energy modeling"
    building_life_cycle = "building life cycle"
    building_physics = "building physics"
    building_smartness = "building smartness"
    built_environment = "built environment"
    case_studies = "case studies"
    cloud_computing = "cloud computing"
    collaborative_environments = "collaborative environments"
    communication = "communication"
    computational_design = "computational design"
    cobie = "construction operations building information exchange"
    construction_scheduling = "construction scheduling"
    construction_site_layout = "construction site layout"
    context_awareness = "context awareness"
    contractual_issues = "contractual issues"
    cost_control = "cost control"
    critical_success_factors = "critical success factors"
    digital_fabrication = "digital fabrication"
    digital_twin = "digital twin"
    disaster_response = "disaster response"
    dispute_resolution = "dispute resolution"
    dynamic_scheduling = "dynamic scheduling"
    education = "education"
    electronic_tendering = "electronic tendering"
    empirical_research = "empirical research"
    energy_analysis = "energy analysis"
    environmental_impacts = "environmental impacts"
    facility_management = "facility management"
    fire_safety = "fire safety"
    gis_integration = "gis integration"
    green_buildings = "green buildings"
    health_and_safety = "health and safety"
    historical_preservation = "historical preservation"
    human_behavior = "human behavior"
    industrialized_construction = "industrialized construction"
    information_management = "information management"
    infrastructure_asset_management = "infrastructure asset management"
    interoperability = "interoperability"
    iot_integration = "iot integration"
    knowledge_sharing = "knowledge sharing"
    lean_construction = "lean construction"
    legal_frameworks = "legal frameworks"
    level_of_development = "level of development"
    level_of_detail = "level of detail"
    level_of_information_need = "level of information need"
    lifetime_costs = "lifetime costs"
    linked_data = "linked data"
    machine_learning = "machine learning"
    manufacturing = "manufacturing"
    materials_management = "materials management"
    mobile_applications = "mobile applications"
    multi_criteria_decision_making = "multi-criteria decision making"
    natural_language_processing = "natural language processing"
    networking = "networking"
    open_bim = "open bim"
    organizational_change = "organizational change"
    owner_involvement = "owner involvement"
    parametric_design = "parametric design"
    performance_measurement = "performance measurement"
    pipeline_simulation = "pipeline simulation"
    policy_implications = "policy implications"
    predictive_maintenance = "predictive maintenance"
    product_data_templates = "product data templates"
    public_procurement = "public procurement"
    radio_frequency_identification = "radio frequency identification"
    reality_capture = "reality capture"
    real_time_monitoring = "real-time monitoring"
    reliability_engineering = "reliability engineering"
    resilience = "resilience"
    return_on_investment = "return on investment"
    reverse_logistics = "reverse logistics"
    risk_assessment = "risk assessment"
    robotics = "robotics"
    maintenance_management = "maintenance management"

# Define the schema for the output.
class Metadata(BaseModel):
    title: str = Field(description='Title of the document')
    summary: str = Field(description='One sentence short summary of the document information')
    disciplines: List[str] = Field(
        default_factory=list,
        description='BIM disciplines the document belongs to',
        example=['S - Sanitär', 'D - Datennetz']
    )
    keywords: List[str] = Field(
        default_factory=list,
        description='List of BIM keywords associated with the document',
        example=['3D Modelling', 'Clash detection']
    )