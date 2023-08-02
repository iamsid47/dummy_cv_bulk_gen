import openai
import json
from fpdf import FPDF
import time

openai.api_key = "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"

names = [
    "Abigail Smith", "Benjamin Brown", "Christopher Jones", "David Williams", "Emily Anderson",
    "Ethan Davis", "Gabriel Green", "Hannah Hall", "Isabella Jackson", "Jacob White",
    "Joshua Black", "Kevin Carter", "Laura Miller", "Michael Peterson", "Olivia Roberts",
    "Owen Smith", "Peyton Thomas", "Rebecca Walker", "Ryan Young", "Sarah Williams",
    "Samuel Wilson", "Taylor James", "Thomas Johnson", "Victoria Martinez", "William Hernandez",
    "Zachary Perez", "Zoey Garcia", "Ava Lopez", "Brandon Torres", "Camila Rodriguez",
    "Daniel Sanchez", "Emily Alvarez", "Ethan Flores", "Gabriel Garcia", "Hannah Hernandez",
    "Isabella Lopez", "Jacob Martinez", "Kevin Rodriguez", "Liam Torres", "Mia Garcia",
    "Noah Hernandez", "Olivia Lopez", "Owen Martinez", "Peyton Rodriguez", "Rebecca Sanchez",
    "Ryan Torres", "Samuel Alvarez", "Sophia Flores", "Taylor Garcia", "Thomas Hernandez",
    "Victoria Lopez", "William Martinez", "Zachary Rodriguez", "Zoey Sanchez", "Ava Torres",
    "Brandon Alvarez", "Camila Flores", "Daniel Garcia", "Emily Hernandez", "Ethan Lopez",
    "Gabriel Martinez", "Hannah Rodriguez", "Isabella Sanchez", "Jacob Torres", "Kevin Alvarez",
    "Liam Garcia", "Mia Hernandez", "Noah Lopez", "Olivia Martinez", "Owen Rodriguez",
    "Peyton Sanchez", "Rebecca Torres", "Ryan Alvarez", "Samuel Hernandez", "Sophia Lopez",
    "Taylor Martinez", "Thomas Sanchez", "Victoria Torres", "William Alvarez",
    "Zachary Garcia", "Zoey Hernandez", "Ava Lopez", "Brandon Martinez", "Camila Rodriguez",
    "Daniel Sanchez", "Emily Torres", "Ethan Alvarez", "Gabriel Garcia", "Hannah Hernandez",
    "Isabella Lopez", "Jacob Martinez", "Kevin Rodriguez", "Liam Sanchez", "Mia Torres",
    "Noah Alvarez", "Olivia Garcia", "Owen Hernandez", "Peyton Lopez", "Rebecca Martinez",
    "Ryan Sanchez"
]

def generate_resume():
    for name in names[:1]:
        rand_phone = openai.Completion.create(model = "text-davinci-002", prompt="Generate a random phone number of any country:", max_tokens=15)
        time.sleep(20)
        rand_email = openai.Completion.create(model = "text-davinci-002", prompt=f"Generate a random email address with the name {name} :", max_tokens=15)
        time.sleep(20)
        rand_loc = openai.Completion.create(model = "text-davinci-002", prompt="Generate a random address of any country:", max_tokens=15)
        time.sleep(20)
        rand_sum =openai.Completion.create(model = "text-davinci-002", prompt="Generate a work summary for the job post of an Electrical Engineer", max_tokens=256)
        time.sleep(20)
        rand_education =openai.Completion.create(model = "text-davinci-002", prompt="Generate an education background for the job post of an Electrical Engineer", max_tokens=256)
        time.sleep(20)
        rand_skills = openai.Completion.create(model = "text-davinci-002", prompt="Generate a random skill set for the job post of an electrical engineer", max_tokens=128)
        time.sleep(20)
        rand_achieve = openai.Completion.create(model = "text-davinci-002", prompt="Generate random achievements of competition or events", max_tokens=256)
        time.sleep(20)
        rand_work_exp = openai.Completion.create(model = "text-davinci-002", prompt="Generate a random work experience related to electrical engineering", max_tokens=256)
        time.sleep(20)
        rand_proj =openai.Completion.create(model = "text-davinci-002", prompt="Generate random projects idea list with a small description of 50 words or less for electrical engineer background", max_tokens=256)

        resume_content = f"""
        {name["choices"][0]['message']}
        Contact: {rand_phone["choices"][0]['message']} | {rand_email["choices"][0]['message']}
        Location: {rand_loc["choices"][0]['message']}

        Summary:
        {rand_sum["choices"][0]['message']}

        Experience: {rand_work_exp["choices"][0]['message']}

        Education:
        {rand_education["choices"][0]['message']}

        Skills:
        {rand_skills["choices"][0]['message']}

        Achievements: {rand_achieve["choices"][0]['message']}

        Projects: {rand_proj["choices"][0]['message']}
        """

        return resume_content
    

def generate_and_save_resumes():
    for idx, name in enumerate(names[:1]):
        resume_content = generate_resume()
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, resume_content)
        pdf.output(f"resume_{idx}.pdf")
        print(f"Generated resume for {name}")

generate_and_save_resumes()
    