import gradio as gr
from generator import get_resume_and_cover_letter

def generate_all(name, role, skills, experience, education, achievements, tone):
    resume, cover, resume_file, cover_file = get_resume_and_cover_letter(
        name, role, skills, experience, education, achievements, tone
    )
    return resume, cover, resume_file, cover_file

iface = gr.Interface(
    fn=generate_all,
    inputs=[
        gr.Textbox(label="Full Name"),
        gr.Textbox(label="Job Role"),
        gr.Textbox(label="Skills (comma-separated)"),
        gr.Textbox(label="Experience Summary"),
        gr.Textbox(label="Education Background"),
        gr.Textbox(label="Achievements"),
        gr.Dropdown(choices=["formal", "enthusiastic", "creative"], label="Tone")
    ],
    outputs=[
        gr.Textbox(label="Generated Resume", lines=15),
        gr.Textbox(label="Generated Cover Letter", lines=15),
        gr.File(label="Download Resume as PDF"),
        gr.File(label="Download Cover Letter as PDF")
    ],
    title="AI-Powered Resume & Cover Letter Generator with PDF"
)

iface.launch()
