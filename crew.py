# from crewai import Crew, Process
# from agents import extractor, analyzer, recommender
# from tools import pdf_tool
# from tasks  import extract_task, analyze_task, recommend_task

# crew = Crew(
#     agents=[extractor, analyzer, recommender],
#     tasks=[extract_task, analyze_task, recommend_task],
#     process=Process.sequential,
#     memory=False,
#     cache=False
# )

# result = crew.kickoff(inputs={'report_text': '/home/adityaraut/Downloads/test.pdf'})