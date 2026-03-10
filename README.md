# 🤖 Mini Task Plannig Agent 

A small Python-based agent that analyzes a list of tasks, prioritizes them, and generates a weekly plan using a language model powered by Groq.

## 📂 Project Structure

```
prueba_dq/
├── src/
│   ├── tasks.py        # Input task list stored as a list of dictionaries
│   ├── agent.py        # Agent logic and LLM interactions
│   └── main.py         # Program entry point
├── output/
├── weekly_plan.txt     # Generated output after execution
├── .gitignore
└── README.md
```
---

## ⚙️ Requirements

- A free account on [Groq](https://console.groq.com) to obtain your API key.

---

## 🚀 Installation

**1. Clone the repository**
```bash
git clone https://github.com/Rafael-Gonzales-Palacios/mini_plannig_agent.git
cd mini_plannig_agent
```

**2. Create a virtual environment**

It is recommended to use a virtual environment to isolate project dependencies.

```bash
python3 -m venv venv
```

Activate the environment:

Windows
```bash
venv\Scripts\activate
```

macOS / Linux:
```bash
source venv/bin/activate
```

---

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

---

**4. Configure environment variables**

```bash
cp .env.example .env
```

---

## ▶️ Running the project
```bash
python src/main.py
```

The program will display the plan in the console and automatically save it to `output/weekly_plan.txt`.

---

## 📋 Example Output
```
Priority:
1. Read a book
2. Go to the gym
3. Study Python

Weekly Plan:
Monday: Read a book
Tuesday: Go to the gym
Wednesday: Study Python

Reasoning:
The presentation is prioritized because it has the closest deadline.
```

---

## 🧠 Technical Decisions

- **Groq + LLaMA 3** as the LLM due to being free and powerful enough for this task.
- **Separación en módulos** to keep the code clean and ensure each file has a single responsibility.
- **Prompt estructurado** to guarantee predictable and consistent output formatting.

---

## What does it actually do?

You provide a list of tasks with deadlines and estimated durations.
The agent prioritizes them, builds a weekly plan, and explains the reasoning behind its decisions.
The final result is saved to a text file so you can refer to it anytime

---

## How I structured it and why

I chose to split the code into three files with clear responsibilities instead of putting everything in one place.
Even for a small project, this makes maintenance easier—if I need to modify something, I know exactly where to look without risking breaking unrelated parts.

---

The most time-consuming part was designing the prompt. I learned that if you don’t explicitly define the output format, the model produces different structures each time, which makes saving the result messy. Once I enforced the format inside the prompt, everything became consistent and reliable.
I selected Groq because it’s free and the LLaMA 3 model they provide is more than enough for this type of task.

---

## 📈 Potential Improvements

- Allow interactive task input from the terminal.
- Add automated tests for the `build_prompt` function.
- Validate task fields before sending them to the LLM.
- Allow selecting the LLM model via configuration.
- Export the weekly plan in PDF format.

---
