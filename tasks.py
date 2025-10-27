from crewai import Task
from agents import extractor, analyzer, recommender


extract_task = Task(
    description=(
        "Extract and structure medical information from the provided report text. "
        "The report text is available in the 'report_text' input variable. "
        "Identify and list all diseases, symptoms, and key metrics."
    ),
    expected_output=(
        "A structured JSON object with these keys: "
        "'diseases' (list), 'symptoms' (list), and 'metrics' (dict). "
        "Example: { 'diseases': ['Diabetes'], 'symptoms': ['fatigue'], "
        "'metrics': {'blood_sugar': '180 mg/dL'}"
    ),
    agent=extractor,
    context=[]  
)


analyze_task = Task(
    description=(
        "Analyze the extracted medical data. The input will be the output from the extractor. "
        "Focus on identifying patterns, potential diagnoses, and relevant risk factors."
    ),
    expected_output=(
        "A structured analysis including potential diagnoses, risk factors, and key findings. "
        "Format as a JSON object with 'diagnoses', 'risk_factors', and 'findings' keys."
    ),
    agent=analyzer,
    context=[extract_task] 
)


recommend_task = Task(
    description=(
        "Generate clear, actionable recommendations based on the analysis. "
        "The input will be the output from the analyzer."
    ),
    expected_output=(
        "A list of clear, actionable recommendations in order of priority. "
        "Include both immediate and long-term suggestions."
    ),
    agent=recommender,
    context=[analyze_task] 
)