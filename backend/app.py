from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from checker import check_account
from pathlib import Path

app = FastAPI()

# إرسال صفحة HTML من frontend
@app.get("/")
def home():
    return FileResponse(Path(__file__).parent.parent / "frontend" / "index.html")

@app.post("/check")
async def check(file: UploadFile = File(...)):
    content = await file.read()
    lines = content.decode().splitlines()
    results = []
    for line in lines:
        if ":" not in line:
            continue
        username, password = line.split(":", 1)
        status = check_account(username, password)
        results.append(f"{username}:{password} - {'Valid' if status else 'Invalid'}")
    return {"results": results}
