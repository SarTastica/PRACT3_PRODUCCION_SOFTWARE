from datetime import date
import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from core.expense_service import ExpenseService
from core.in_memory_expense_repository import InMemoryExpenseRepository

scenarios("./expense_management.feature")

@pytest.fixture
def context():
    repo = InMemoryExpenseRepository()
    service = ExpenseService(repo)
    return {"service": service, "db": repo}

@given(parsers.parse("un gestor de gastos vacío"))
def empty_manager(context):
    pass

@given(parsers.parse("un gestor con un gasto de {amount:d} euros"))
def manager_with_one_expense(context, amount):
    context["service"].create_expense(
        title="Gasto inicial", amount=amount, description="", expense_date=date.today()
    )


@when(parsers.parse("añado un gasto de {amount:d} euros llamado {title}"))
def add_expense(context, amount, title):
    context["service"].create_expense(
        title=title.strip('"'), amount=amount, description="", expense_date=date.today()
    )

@when(parsers.parse("elimino el gasto con id {expense_id:d}"))
def remove_expense(context, expense_id):
    context["service"].remove_expense(expense_id)

@when(parsers.parse("calculo el total por mes"))
def calculate_month_totals(context):
    context["totals"] = context["service"].total_by_month()

@when(parsers.parse("actualizo el gasto con id {expense_id:d} con el nombre {new_title}"))
def update_expense_title(context, expense_id, new_title):
    context["service"].update_expense(expense_id=expense_id, title=new_title.strip('"'))


@then(parsers.parse("el total de dinero gastado debe ser {total:d} euros"))
def check_total(context, total):
    assert context["service"].total_amount() == total

@then(parsers.parse("{month_key} debe sumar {expected_total:d} euros"))
def check_month_total(context, month_key, expected_total):
    total_actual = context["totals"].get(month_key.strip('"'), 0)
    assert total_actual == expected_total

@then(parsers.parse("debe haber {expenses:d} gastos registrados"))
def check_expenses_length(context, expenses):
    total = len(context["db"].list_all())
    assert total == expenses

@then(parsers.parse("el gasto con id {expense_id:d} debe llamarse {expected_title}"))
def check_expense_title(context, expense_id, expected_title):
    expense = context["db"].get_by_id(expense_id)
    assert expense.title == expected_title.strip('"')