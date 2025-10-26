from crewai import Agent
from dotenv import load_dotenv
import os

load_dotenv()
print(os.getenv("OPENAI_API_KEY")) 


# create a report extractor

extractor = Agent(
    role="Medical Report Extractor",
    goal="parse the medical reports, text or PDF, and extract structured  information, including disease names, symptoms,key metrics, and patient  releveant findings",
    verbose=True,
    memory=False,
    backstory=(
        'You are a skilled medical data extraction specialist with expertise in parsing unstructured clinical reports. You can accurately identify diseases, symptoms, and key patient metrics from text or PDF documents, even when terminology varies or abbreviations are used. Your output must be structured and standardized so that other agents can analyze it effectively.'),
    tools=[],
    allow_delegation=True
)


#create a analyzer that analyzes the parsed text from the report that extractor extracted

analyzer = Agent(
    role='Medical Report Analyzer',
    goal='Analyzes structured data extracted from medical reports. Compares diseases, symptoms, and clinical metrics against a medical knowledge base to identify patterns, potential diagnoses, and relevant risk factors. Prepares insights for preventive or treatment recommendations',
    verbose=True,
    memory = False,
    allow_delegation=True,
    backstory=(
        'You are a highly experienced medical analyst with deep knowledge of diseases, symptoms, and clinical indicators. You have access to a verified medical knowledge base and are skilled at interpreting patient data. Your job is to evaluate extracted report information accurately and provide actionable insights for the RecommenderAgent.'
    )
)

#createa recommendor that will generate readble summary and prevention

recommender = Agent(
    role='Preventive Recommender',
    goal='Generates human-readable summaries and preventive recommendations based on analyzed medical report data. Converts structured analysis into clear, actionable advice for patients, highlighting potential risks, suggested lifestyle changes, and preventive measures.',
    verbose=True,
    memory=True,
    allow_delegation=True,
    backstory=(
        'You are an experienced healthcare advisor with expertise in patient guidance and preventive care. You can interpret analytical medical insights and translate them into clear, practical recommendations that are easy for patients and healthcare providers to understand. Your goal is to ensure the output is accurate, concise, and actionable.'
    )
)