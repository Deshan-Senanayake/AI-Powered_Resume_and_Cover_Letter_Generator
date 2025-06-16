============================        AI-Powered Resume & Cover Letter Generator              ===========================


What It Does:
Takes user input (job role, experience, skills) and generates a tailored resume and cover letter using a pre-trained LLM.


Why It’s Impressive:

  Solves a real-world problem
  
  Demonstrates prompt engineering and automation
  
  Easy to deploy on Gradio or Streamlit for demo


Tech Stack:

  Python, Gradio, Hugging Face Transformers (GPT2 or Mistral)


Optional: Save outputs as PDFs using fpdf or pdfkit


==================================         Overview of What I Built              ===================================

What It Does:
An app that asks the user for:

  Full Name
  
  Job Role
  
  Skills
  
  Experience
  
  Education
  
  Achievements

Tone (formal, enthusiastic, creative)


And generates:

  A tailored resume
  
  A professional cover letter

===============       Install required libraries          ==================


pip install gradio transformers

pip install torch

pip install "huggingface_hub[hf_xet]"



===============          Folder Structure         =============================


ai_resume_generator/

├── app.py

├── generator.py

├── templates.py

├── venv/ (optional)
