from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from controllers.character_routes import router as character_router
from controllers.item_routes import router as item_router
from database import Base, engine
from domain.exceptions import DomainError, NotFoundError

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(item_router)
app.include_router(character_router)


@app.exception_handler(NotFoundError)
def not_found_handler(request: Request, exc: NotFoundError):
    return JSONResponse(status_code=404, content={"detail": str(exc)})


@app.exception_handler(DomainError)
def domain_error_handler(request: Request, exc: DomainError):
    return JSONResponse(status_code=400, content={"detail": str(exc)})
