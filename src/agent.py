# Importar librerias
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def build_prompt(tasks):
    # Necesitamos convertir cada tarea en texto legible
    tasks_text = ""

    for task in tasks:
        tasks_text += f"- Tarea: {task['task']} | Deadline: {task['deadline_days']} días | Duración: {task['duration']} horas\n"

    # Construcción del prompt
    prompt = f"""
        You are an expert assistant in productivity and task planning.
         Here is a list of pending tasks:
        {tasks_text}
        Analyze these tasks and respond EXACTLY in this format, without adding anything else:

        Priority:
        1. [most urgent task]
        2. [second task]
        3. [third task]

        Weekly Plan:
        Monday: [task]
        Tuesday: [task]
        Wednesday: [task]
        Thursday: [task]
        Friday: [task]
        Saturday: [task]
        Sunday: [task]

        IMPORTANT rules for the plan:
        - The task with priority 1 must be scheduled for the first available day (usually Monday).
        - Planning must be consistent with the order of priority: the most urgent tasks are scheduled first.
        - Do not contradict the order of priority in the weekly plan.


        Reason:
        [Briefly explain why you assigned that priority and how it is reflected in the plan]
    """

    return prompt

def call_lm(prompt):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    # Llamado al modelo
    response = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages = [
            {"role": "user", "content": prompt}
        ]
    )

    #Obtener solo el texto
    return response.choices[0].message.content

def run_agent(tasks):
    prompt = build_prompt(tasks)
    result = call_lm(prompt)
    return result