# Bootstrap

Setup project:

```bash
poetry new meal-planner-proto
cd meal-planner-proto
pyenv local 3.11.4
poetry install
poetry shell
```

Add git:

```bash
git init

# .gitignore
.venv
.env

git add .
git commit -m "init"
git add origin remote ...
git push -u origin main
```

Add deps:

```bash
pip install jupyterlab
pip install langchain
pip install langchain-openai langchain-groq
pip install python-dotenv
```
