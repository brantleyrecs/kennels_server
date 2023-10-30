from .animals_requests import (
  get_all_animals, get_single_animal, get_animal_by_location,
  get_animal_by_status, delete_animal, update_animal, create_animal)
from .location_requests import (
  get_all_locations, get_single_location, delete_location)
from .employee_requests import (
  get_all_employees, get_single_employee, get_employee_by_location, delete_employee)
from .customers_request import (
  get_all_customers, get_single_customer, get_customer_by_email, delete_customer)
