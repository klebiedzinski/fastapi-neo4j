from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from src.services.employees_service import EmployeesService
import json
employees_router = APIRouter(prefix="/employees", tags=["employees"])

service = EmployeesService()

@employees_router.get("/")
async def get_employees(request: Request):
    sort = request.query_params.get("sort")
    filter = request.query_params.get("filter")
    try:
        response = await service.get_employees(sort, filter)
    except Exception as e:
       return JSONResponse(status_code=404, content=e)
    return JSONResponse(status_code=200, content=response)


@employees_router.post('/')
async def create_employee(request: Request):
    employee = await request.json()
    try:
        response,code = await service.create_employee(employee)
        return Response(content=response,status_code=code)
    except Exception as e:
        response = json.dumps({'message':e.args[0]})
        return JSONResponse(status_code=409,content=response)

@employees_router.put('/{id}')
async def update_employee(request: Request,id:int):
    try:
        employee = await request.json()
        response,code = await service.update_employee(id,employee)
        return JSONResponse(content=response,status_code=code)
    except Exception as e:
        response = json.dumps({'message':e.args[0]})
        return JSONResponse(status_code=404,content=response)

@employees_router.delete('/{id}')
async def delete_employee(id:str):
    response,code = await service.delete_employee(id)
    return JSONResponse(content=response,status_code=code)

@employees_router.get('/{id}/subordinates')
async def get_subordinates(id:str):
    try:
        response = await service.get_subordinates(id)
        return JSONResponse(content=response,status_code=200)
    except Exception as e:
        response = json.dumps({'message':e.args[0]})
        return JSONResponse(status_code=404,content=response)

@employees_router.get('/{id}/department')
async def get_departments_by_employees_id(id:str):
    try:
        response = await service.get_department_by_employees_id(id)
        return JSONResponse(content=response,status_code=200)
    except Exception as e:
        response = json.dumps({'message':e.args[0]})
        return JSONResponse(status_code=404,content=response)

