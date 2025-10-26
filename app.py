from flask import Flask, render_template, request
from crewai import Crew, Process
from agents import extractor, analyzer, recommender
from tools import get_pdf_tool
from tasks import extract_task, analyze_task, recommend_task
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result_text = ''
    if request.method == 'POST' and 'report' in request.files:
        uploaded_file = request.files['report']
        if uploaded_file.filename != '':
            os.makedirs('uploads', exist_ok=True)
            file_path = os.path.join('uploads', uploaded_file.filename)
            uploaded_file.save(file_path)
            
            try:
                pdf_tool = get_pdf_tool(file_path)
                extracted_text = pdf_tool.run()
                
                crew = Crew(
                    agents=[extractor, analyzer, recommender],
                    tasks=[extract_task, analyze_task, recommend_task],
                    process=Process.sequential,
                    memory=False,
                    cache=False
                )
                
                result = crew.kickoff(inputs={'report_text': extracted_text})
                
                if isinstance(result, list):
                    result_text = '<ul>' + ''.join([f'<li>{rec}</li>' for rec in result]) + '</ul>'
                else:
                    result_text = str(result)
                    
            except Exception as e:
                result_text = f"Error processing file: {str(e)}"
            finally:
                if os.path.exists(file_path):
                    os.remove(file_path)
    
    return render_template('index.html', result=result_text)

if __name__ == '__main__':
    app.run(debug=True)