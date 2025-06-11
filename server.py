from fastapi import FastAPI,Query
from .queue.connection import queue
from.queue.worker import process_query

app = FastAPI()

@app.get('/')
def entry():
    return "server is up"

@app.post("/chat")
def chat(
    query: str = Query(...,description="chat_message")
):
    job = queue.enqueue(process_query,query) 
    
    return{'status':"queued","id":job.id}
    
    