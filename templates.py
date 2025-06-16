def generate_resume_prompt(name, role, skills, experience, education, achievements, tone):
    return f"""
You are an expert resume writer.

Write a professional resume in {tone} tone for the following person:

Name: {name}
Role: {role}
Skills: {skills}
Experience: {experience}
Education: {education}
Achievements: {achievements}

Use bullet points for skills and experience. Keep it concise but impactful.
"""

def generate_cover_letter_prompt(name, role, skills, experience, tone):
    return f"""
You are a career consultant.

Write a cover letter in {tone} tone for a candidate applying to the role of {role}.

Candidate's Name: {name}
Relevant Skills: {skills}
Experience: {experience}

Make it personalized, highlight strengths, and end with a positive note.
"""
