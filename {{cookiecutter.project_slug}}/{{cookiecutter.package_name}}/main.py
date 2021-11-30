import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from {{cookiecutter.package_name}}.api.api_v1.api import api_router
from {{cookiecutter.package_name}}.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_PREFIX}/openapi.json")


if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(CORSMiddleware, allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"])

app.include_router(api_router, prefix=settings.API_V1_PREFIX)    

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
