from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def main():
    return {"Class":"Thursday"}

@app.get("/location")
def main():
    return {"City":"Karachi"}