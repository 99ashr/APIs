from fastapi import FastAPI, Form

app = FastAPI(title="Forms")


@app.post('/language/')
async def language(name: str = Form(...), type: str = Form(...)):
    return{"Name": name, "Type": type}
