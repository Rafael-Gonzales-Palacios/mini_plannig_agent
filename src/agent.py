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
        Eres un asistente exeperto en productividad y planificación de tareas.
        Aquí tienes una lista de tareas pendientes:
        {tasks_text}
        Analiza estas tareas y responde EXACTAMENTE en este formato, sin añadir nada más:

        Prioridad:
        1. [tarea más urgente]
        2. [segunda tarea]
        3. [tercera tarea]

        Plan Semanal:
        Lunes: [tasks]
        Martes: [tasks]
        Miércoles: [tasks]

        Reglas IMPORTANTES para el plan:
        - La tarea con prioridad 1 debe programarse el primer día disponible (normalmente el lunes).
        - La planificación debe ser coherente con el orden de prioridad: primero se programan las tareas más urgentes.
        - No contradigas el orden de prioridad en el plan semanal.


        Razón:
        [Explica brevemente por qué has asignado esa prioridad y commo se refleja en el plan]
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