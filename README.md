# Medical Report Analyzer & Preventive Recommender

A web-based application that analyzes patient medical reports (PDFs or text), extracts structured clinical information, and provides actionable preventive healthcare recommendations. This project leverages AI agents for extraction, analysis, and summarization, making it useful for healthcare providers and patients alike.

[![GitHub stars](https://img.shields.io/github/stars/rautaditya2606/healthcare_agent?style=social)](https://github.com/rautaditya2606/healthcare_agent/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/rautaditya2606/healthcare_agent)](https://github.com/rautaditya2606/healthcare_agent/issues)
[![GitHub license](https://img.shields.io/github/license/rautaditya2606/healthcare_agent)](https://github.com/rautaditya2606/healthcare_agent/blob/main/LICENSE)

---

## Features

- **PDF & Text Report Analysis**: Supports both digital PDFs and scanned reports via OCR.
- **Structured Data Extraction**: Extracts diseases, symptoms, vital signs, lab results, medications, and notes.
- **Medical Analysis**: Compares extracted data with a medical knowledge base to identify risks, potential diagnoses, and clinical insights.
- **Preventive Recommendations**: Generates human-readable summaries and actionable guidance for patients.
- **Flask Web UI**: Easy-to-use web interface for uploading reports and viewing analysis.
- **Extensible Architecture**: Built using modular AI agents (Extractor, Analyzer, Recommender) with CrewAI.

---

## Technologies Used

- **Python 3.13**
- **Flask** – Web interface
- **CrewAI** – Agent-based AI workflow
- **pytesseract & pdf2image** – OCR support for scanned PDFs
- **HTML/CSS** – Frontend
- **dotenv** – Environment variable management

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/rautaditya2606/healthcare_agent.git
cd healthcare_agent
```

2. **Set up virtual environment**
```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
# venv\Scripts\activate  # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set your OpenAI API key**
```bash
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

5. **Run the application**
```bash
python app.py
```

6. **Open your browser at http://127.0.0.1:5000** and upload a patient report.

## Usage
1. Upload a PDF or text report.
2. The app extracts clinical data using the Extractor Agent.
3. The Analyzer Agent evaluates risks and potential diagnoses.
4. The Recommender Agent generates human-readable preventive advice.
5. View structured analysis and recommendations directly on the webpage.

## Project Structure
```
healthcare_agent/
│
├── app.py                  # Flask app
├── agents.py               # AI agents (Extractor, Analyzer, Recommender)
├── tools.py                # PDF & OCR tools
├── tasks.py                # CrewAI task definitions
├── templates/
│   └── index.html          # Web UI template
├── static/
│   └── styles.css          # Web UI styles
└── uploads/                # Temporary upload storage
```

## Example Output

### Extracted Data
```
Patient: John Doe
Age: 55
Gender: Male
Medical History: Type 2 Diabetes, Hypertension, High Cholesterol
Current Symptoms: Fatigue, Frequent Urination, Mild Headache
Clinical Measurements: Blood Sugar: 190 mg/dL, Blood Pressure: 145/92 mmHg, Cholesterol: 240 mg/dL
Medications: Metformin, Lisinopril, Atorvastatin
Notes: Difficulty maintaining a balanced diet, occasional dizziness
```

### Recommendations
- Monitor blood sugar daily and adhere to medications.
- Maintain a balanced diet and engage in regular physical activity.
- Monitor blood pressure and cholesterol; consult doctor for medication adjustments.
- Schedule regular follow-ups for HbA1c, lipid profile, and renal function.
- Report new or worsening symptoms promptly.

## Future Enhancements
- Support multiple languages for OCR.
- Table extraction for lab results using Camelot or Tabula.
- Advanced risk scoring and alert system.
- Patient dashboard for historical reports and trends.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <a href="https://github.com/rautaditya2606/healthcare_agent">GitHub Repository</a> | 
  <a href="https://github.com/rautaditya2606/healthcare_agent/issues">Report Issues</a> | 
  <a href="https://github.com/rautaditya2606/healthcare_agent/pulls">Pull Requests</a>
</p>
