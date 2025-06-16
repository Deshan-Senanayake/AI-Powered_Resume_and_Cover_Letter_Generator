from transformers import pipeline
from templates import generate_resume_prompt, generate_cover_letter_prompt

generator = pipeline("text-generation", model="gpt2")

def generate_text(prompt):
    output = generator(prompt, max_length=500, do_sample=True, temperature=0.7)
    return output[0]["generated_text"]

def get_resume_and_cover_letter(name, role, skills, experience, education, achievements, tone):
    resume_prompt = generate_resume_prompt(name, role, skills, experience, education, achievements, tone)
    cover_prompt = generate_cover_letter_prompt(name, role, skills, experience, tone)

    resume = generate_text(resume_prompt)
    cover_letter = generate_text(cover_prompt)

    return resume.strip(), cover_letter.strip()
