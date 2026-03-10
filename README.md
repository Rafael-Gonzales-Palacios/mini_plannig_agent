# 🤖 Mini Agente de Planificación de Tareas 

Un pequeño agente en Python que se encarga de analizar una lista de tareas, luego las prioriza
y genera un plan semanal utilizando un modelo de lenguaje a través de Groq.

## 📂 Estructura del proyecto

```
prueba_dq/
├── src/
│   ├── tasks.py        # Lista de tareas de entrada en una lista de diccionarios
│   ├── agent.py        # Lógica del agente y llamadas al LLM
│   └── main.py         # Punto de entrada del programa
├── output/
├── weekly_plan.txt     # Resultado generado al ejecutar
├── .gitignore
└── README.md
```
---

## ⚙️ Requisitos

- Una cuenta gratuita en [Groq](https://console.groq.com) para obtener tu API_KEY

---

## 🚀 Instalación

**1. Clona el repositorio**
```bash
git clone https://github.com/Rafael-Gonzales-Palacios/mini_plannig_agent.git
cd mini_plannig_agent
```

**2. Instala las dependecias**
```bash
pip install groq python-dotenv
```
o
```bash
pip install requirements.txt
```

**3. Configurar varibles de entorno**
Crea un archivo .env y añade tu API_KEY
```bash
GROQ_API_KEY = "aquí tu API key real"
```

---

## ▶️ Ejecución
```bash
python src/main.py
```

El programa mostrará el plan en consola y lo guardará automáticamente en `output/weekly_plan.txt`.

---

## 📋 Ejemplo de salida
```
Prioridad:
1. Leer un libro
2. Ir al gimnasio
3. Estudiar Python

Plan semanal:
Lunes: Leer un libro
Martes: Ir al gimnasio
Miércoles: Estudiar Python

Razón:
La presentación se prioriza porque tiene el deadline más cercano.
```

---

## 🧠 Decisiones técnicas

- **Groq + LLaMA 3** como LLM por ser gratuito y suficientemente potente para esta tarea
- **Separación en módulos** para mantener el código limpio y cada archivo con una sola responsabilidad
- **Prompt estructurado** para garantizar un formato de salida predecible y consistente

---

## ¿Qué hace exactamente?

Le pasas una lista de tareas con su deadline y cuánto tiempo te llevan,
y el agente se encarga de priorizarlas, montar un plan semanal y explicarte
por qué ha tomado esas decisiones. El resultado lo guarda en un archivo
de texto para que lo tengas siempre a mano.

---

## Cómo lo estructuré y por qué

Decidí separar el código en tres archivos con responsabilidades claras,
en lugar de meterlo todo en uno. Al principio puede parecer exagerado para
un proyecto pequeño, pero para mi es mejor ya que si quiero modificar o buscar algo
voy directamente a un archivo especifico sin romper el resto.

---

La parte que más tiempo me llevó fue el prompt. Aprendí que si no le dices
al modelo exactamente qué formato quieres en la respuesta, cada ejecución
te devuelve algo diferente y eso complica guardar el resultado limpiamente.
Una vez que fijé el formato en el propio prompt, todo funcionó de forma
consistente y correcta.

Para el LLM elegí Groq porque es gratuito y el modelo LLaMA 3 que ofrecen
es más que suficiente para este tipo de tarea.

---

## 📈 Mejoras con más tiempo

- Permitir introducir tareas desde la terminal de forma interactiva
- Añadir tests automáticos para la función `build_prompt`
- Validar que las tareas tienen todos los campos necesarios antes de enviarlas al LLM
- Permitir elegir el modelo de LLM desde configuración
- Exportar el plan también en formato PDF

---
