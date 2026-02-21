from fastapi import FastAPI
from datetime import datetime, UTC
app = FastAPI()

@app.get("/")
async def home() -> dict[str, str | float]:
    return {
        "message": "Hello Mother fucker",
        "time": datetime.now(tz=UTC).isoformat(),
        "count": 7, 
    }
