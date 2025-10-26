from flask import Flask, render_template, request
from crewai import Crew, Process
from agents import extractor, analyzer, recommender
from tools import get_pdf_tool
from tasks import extract_task, analyze_task, recommend_task
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

UPLOAD_DIR = 'uploads'
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    
    if request.method == 'POST':
        uploaded_file = request.files.get('report')
        if not uploaded_file or not uploaded_file.filename.endswith('.pdf'):
            return render_template('index.html', result="Please upload a valid PDF file.")
        
        file_path = os.path.join(UPLOAD_DIR, uploaded_file.filename)
        uploaded_file.save(file_path)
        
        try:
            extracted_text = get_pdf_tool(file_path).run()
            crew = Crew(
                agents=[extractor, analyzer, recommender],
                tasks=[extract_task, analyze_task, recommend_task],
                process=Process.sequential,
                memory=False,
                cache=False
            )
            result = crew.kickoff(inputs={'report_text': extracted_text})
            if isinstance(result, list):
                result = '<ul>' + ''.join(f'<li>{r}</li>' for r in result) + '</ul>'
        except Exception as e:
            result = f"Error: {e}"
        finally:
            os.remove(file_path)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
