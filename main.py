import logging
from fastapi import FastAPI, Request
import uvicorn
from api.routes.image_processor import router as image_processor_router
from exceptions.image_exception import ImageException
from fastapi.responses import JSONResponse

# 로그 처리
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log')
    ]
)

logger = logging.getLogger(__name__)
app = FastAPI()

app.include_router(image_processor_router, prefix="/api/v1")

@app.exception_handler(ImageException)
async def image_exception_handler(request: Request, e: ImageException):
    logger.error(f"An error occurred: {e}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "error": {
                "image_name": e.image_name,
                "message": e.message
            }
        }
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
