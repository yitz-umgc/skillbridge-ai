from fastapi import APIRouter, HTTPException

from .schemas import EmployeeCreate, EmployeeResponse


router = APIRouter(
    prefix="/employees",
    tags=["employees"],
)

employees: list[dict] = []


@router.post("/", response_model=EmployeeResponse, status_code=201)
def create_employee(employee: EmployeeCreate):
    new_employee = {
        "id": len(employees) + 1,
        **employee.model_dump(),
    }

    employees.append(new_employee)
    return new_employee


@router.get("/", response_model=list[EmployeeResponse])
def get_employees():
    return employees


@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee(employee_id: int):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee

    raise HTTPException(
        status_code=404,
        detail="Employee not found",
    )
