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
        Lunes: [task]
        Martes: [task]
        Miércoles: [task]

        Razón:
        [Explica brevemente por qué has asignado esa prioridad]
    """

    return prompt