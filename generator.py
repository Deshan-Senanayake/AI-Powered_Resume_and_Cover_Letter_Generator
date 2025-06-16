from transformers import pipeline
from templates import generate_resume_prompt, generate_cover_letter_prompt
from pdf_utils import save_as_pdf

generator = pipeline("text-generation", model="gpt2")

def generate_text(prompt):
    output = generator(prompt, max_length=500, do_sample=True, temperature=0.7)
    return output[0]["generated_text"]

def get_resume_and_cover_letter(name, role, skills, experience, education, achievements, tone):
    resume_prompt = generate_resume_prompt(name, role, skills, experience, education, achievements, tone)
    cover_prompt = generate_cover_letter_prompt(name, role, skills, experience, tone)

    resume = generate_text(resume_prompt).strip()
    cover = generate_text(cover_prompt).strip()

    resume_file = save_as_pdf(resume, "resume", "Generated Resume")
    cover_file = save_as_pdf(cover, "cover_letter", "Generated Cover Letter")

    return resume, cover, resume_file, cover_file
