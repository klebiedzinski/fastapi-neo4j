from fastapi import FastAPI
from src.config.db_connector import driver
from src.controllers.employees_controller import employees_router

app = FastAPI()

app.include_router(employees_router)











if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)


