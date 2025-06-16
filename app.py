import gradio as gr
from generator import get_resume_and_cover_letter

def generate_all(name, role, skills, experience, education, achievements, tone):
    resume, cover = get_resume_and_cover_letter(name, role, skills, experience, education, achievements, tone)
    return resume, cover

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
        gr.Textbox(label="Generated Cover Letter", lines=15)
    ],
    title="AI-Powered Resume & Cover Letter Generator"
)

iface.launch()
