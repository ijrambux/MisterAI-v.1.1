from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from pathlib import Path
from checker import check_account

app = FastAPI()

@app.on_event("startup")
def startup_event():
    print("✅ FastAPI application has started!")

# صفحة البداية تعرض الواجهة الاحترافية
@app.get("/")
def home():
    return FileResponse(Path(__file__).parent.parent / "frontend" / "index.html")

# endpoint للتحقق من حسابات NordVPN
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

