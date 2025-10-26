from crewai import Task
from agents import extractor
from tools import get_pdf_tool


extract_task = Task(
    description=(
        "Extract and structure medical information from the report. "
        "Identify diseases, symptoms, and key metrics."
    ),
    expected_output=(
        "A structured dictionary with 'diseases', 'symptoms', and 'metrics' keys. "
        "Example: { 'diseases': ['Diabetes'], 'symptoms': ['fatigue'], "
        "'metrics': {'blood_sugar': '180 mg/dL'} }"
    ),
    tools=[],  
    agent=extractor
)
from agents import analyzer

analyze_task = Task(
    description=(
        "Analyze the extracted data from the medical report using the medical knowledge base "
        "or RAG tool to identify patterns, potential diagnoses, and relevant risk factors."
    ),
    expected_output=(
        "A structured analysis array with each disease and its risk status and notes. "
        "Example: [ {'disease': 'Diabetes', 'status': 'High risk', 'notes': 'Blood sugar elevated'} ]"
    ),
    tools=[], 
    agent=analyzer
)
from agents import recommender

recommend_task = Task(
    description=(
        "Generate human-readable summaries and preventive recommendations based on the analyzed data. "
        "Include lifestyle, treatment, or monitoring suggestions."
    ),
    expected_output=(
        "A list of actionable recommendations. "
        "Example: [ 'Monitor blood sugar daily and maintain a balanced diet.', "
        "'Engage in regular physical activity to manage blood pressure.' ]"
    ),
    tools=[], 
    agent=recommender,
    output_file='recommendation.md'
)
