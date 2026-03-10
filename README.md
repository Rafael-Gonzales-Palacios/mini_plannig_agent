# 🤖 Agente de Planificación con IA

Este pequeño pryecto me ha servido para entender
de verdad cómo funciona un agente de IA desde cero. Con una idea simple:
darle una lista de tareas a un modelo de lenguaje y que él solo decida
cómo organizarlas en una semana.

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
```
mi-agente-ia/
│
├── src/
│   ├── tasks.py     # Aquí viven las tareas, nada más.
│   ├── agent.py     # Toda la lógica del agente y la llamada al LLM.
│   └── main.py      # El punto de entrada que une todo.
│
├── output/
│   └── weekly_plan.txt  # Se genera automáticamente al ejecutar
│
├── .gitignore
└── README.md
```

La parte que más tiempo me llevó fue el prompt. Aprendí que si no le dices
al modelo exactamente qué formato quieres en la respuesta, cada ejecución
te devuelve algo diferente y eso complica guardar el resultado limpiamente.
Una vez que fijé el formato en el propio prompt, todo funcionó de forma
consistente y correcta.

Para el LLM elegí Groq porque es gratuito y el modelo LLaMA 3 que ofrecen
es más que suficiente para este tipo de tarea.

---