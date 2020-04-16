from fastapi import FastAPI, HTTPException, Request, File, UploadFile, Depends, Response
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import qrcode
import io

# init
app = FastAPI()

class Request(BaseModel):
    url: str

# create qr code
@app.post('/api/v1/qr')
async def create_qr(req: Request, type: str = 'img'):
    img = qrcode.make(req.url)
    output = io.BytesIO()
    img.save(output, format='JPEG', quality=100)
    output.seek(0)
    return StreamingResponse(output, media_type="image/jpeg",
        headers={'Content-Disposition': 'inline; filename="qr.jpg"'})
    
