import openai
import random

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