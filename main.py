from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

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

