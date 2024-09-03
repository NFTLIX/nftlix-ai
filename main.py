from fastapi import FastAPI
import uvicorn
from api.routes.image_processor import router as image_processor_router

app = FastAPI()

app.include_router(image_processor_router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
