from flask import request # type: ignore
from app.employee import bp
from app.extensions import db
from app.models.employee import Employee
from app.extensions import db
from app.views.base import format_list, format_single

@bp.route('/', methods=['GET', 'POST', 'OPTIONS'])
def index():
    if request.method == 'OPTIONS':
        response = bp.make_default_options_response()
        response.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        return response
    
    if request.method == 'POST':
        data = request.json
        new_employee = Employee(name=data.get('name'),
                            address=data.get('address'),
                            phone=data.get('phone'),)
        db.session.add(new_employee)
        db.session.commit()
        return format_single(new_employee)
    
    employees = Employee.query.all()
    return format_list(employees)

@bp.route('/<int:employee_id>')
def get_by_id(employee_id):
    employee = Employee.query.filter_by(id=employee_id).first()
    return format_single(employee)