from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.routes import items

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(items.router, prefix="/items", tags=["Items"])

# Serve frontend HTML from /static/index.html at root URL
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# Optional: root redirect (if needed)
@app.get("/api")
async def root():
    return {"message": "Welcome to FastAPI CRUD App"}
