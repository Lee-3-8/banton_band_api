import uvicorn
from api import groove
from fastapi import FastAPI

if __name__ == "__main__":
    app = FastAPI()
    app.include_router(groove.router)
    uvicorn.run(app, host="127.0.0.1", port=8000)
