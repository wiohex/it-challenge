import csv
from io import StringIO
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, UploadFile, File

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}
@app.get("/info")
def info():
    return {
        "project": "IT Challenge",
        "level": 1,
        "author": "Egor"
    }

class StatisticsInput(BaseModel):
    values: list[float]
@app.post("/preview")
def preview(data: StatisticsInput):
    values = data.values
    if len(values) == 0:
        raise HTTPException(status_code=400, detail="Список значений пуст")

    count = len(values)
    minimum = min(values)
    maximum = max(values)
    average = sum(values) / count

    return {
        "count": count,
        "min": minimum,
        "max": maximum,
        "mean": average
    }




@app.post("/upload")
async def upload(file: UploadFile = File(), column: str = "age"):
    content = await file.read()
    text = content.decode("utf-8")

    reader = csv.DictReader(StringIO(text))
    rows = list(reader)
    values = []

    for row in rows:
        value = float(row[column])
        values.append(value)

    count = len(values)
    minimum = min(values)
    maximum = max(values)
    mean = sum(values) / count

    return {
        "filename": file.filename,
        "column": column,
        "result": {
            "count": count,
            "min": minimum,
            "max": maximum,
            "mean": mean
        }
    }
