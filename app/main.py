from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from controllers.item_routes import router
from database import Base, engine
from domain.exceptions import DomainError, ItemNotFound

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)


@app.exception_handler(ItemNotFound)
def item_not_found_handler(request: Request, exc: ItemNotFound):
    return JSONResponse(status_code=404, content={"detail": str(exc)})


@app.exception_handler(DomainError)
def domain_error_handler(request: Request, exc: DomainError):
    return JSONResponse(status_code=400, content={"detail": str(exc)})
