from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from checker import check_account

app = FastAPI()

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>NordVPN Checker</title>
</head>
<body>
    <h1>NordVPN Account Checker</h1>
    <form action="/check" method="post" enctype="multipart/form-data">
        <label>Upload combolist (nord.txt):</label>
        <input type="file" name="file" required><br><br>
        <button type="submit">Start Checking</button>
    </form>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def home():
    return html_content

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
