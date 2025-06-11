from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def entry():
    return "server is up"

@app.post("chat")
def chat():
    pass
    