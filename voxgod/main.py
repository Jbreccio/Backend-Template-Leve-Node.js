from fastapi import FastAPI
from interfaces.api import router as api_router
from utils.logger import logger

app = FastAPI(
    title="VOXGOD",
    description="IA por voz para comandos de automação e gestão de projetos",
    version="1.0.0",
)

@app.on_event("startup")
async def startup_event():
    logger.info("🚀 VOXGOD iniciado com sucesso!")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("👋 VOXGOD finalizado.")

# Inclui as rotas da API
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
