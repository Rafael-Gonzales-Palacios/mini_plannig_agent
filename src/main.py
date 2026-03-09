import os
from tasks import tasks
from agent import run_agent

def save_result(result):

    os.makedirs("output", exist_ok=True)
    with open("output/weekly_plan.txt", "w", encoding="UTF-8") as file:
        file.write(result)

    print("Plan guardado correctamente..")

def main():
    print("🤖 Analizando tareas...")
    
    # Llamar al agente
    result = run_agent(tasks)

    # Mostrar los resultados
    print("\n📋RESULTADO:\n")
    print(result)

    # Guardar en archivo
    save_result(result)

if __name__ == "__main__":
    main()