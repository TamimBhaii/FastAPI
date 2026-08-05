from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello():
    return "Md. Tamim Islam"

@app.get("/about")
def about():
    return "Hello about page"