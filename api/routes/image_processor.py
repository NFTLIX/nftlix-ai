from fastapi import APIRouter, UploadFile, File
from services.cartoonization import CartoonizationService
from services.black_and_white import BlackAndWhiteService
from services.nukki import NukkiService
from PIL import Image
import io
import os

router = APIRouter()

cartoonization_service = CartoonizationService()
black_and_white_service = BlackAndWhiteService()
nukki_service = NukkiService()

@router.post("/cartoonization/")
async def cartoonize(image: UploadFile = File(...)):
    image_name = image.filename
    image_bytes = await image.read()
    image = Image.open(io.BytesIO(image_bytes))
    return cartoonization_service.convert(image, image_name)

@router.post("/black-and-white/")
async def black_and_white(image: UploadFile = File(...)):
    image_name = image.filename
    image_bytes = await image.read()
    image = Image.open(io.BytesIO(image_bytes))
    return black_and_white_service.convert(image, image_name)

@router.post("/nukki/")
async def nukki(image: UploadFile = File(...)):
    image_name = image.filename
    image_bytes = await image.read()
    image = Image.open(io.BytesIO(image_bytes))

    # 누끼는 png 확장자에 대해서만 동작
    if image.format != 'PNG':
        base, _ = os.path.splitext(image_name)
        new_name = f"{base}.png"
        image.save(new_name, 'png')

    return nukki_service.convert(image, image_name)