# features/steps/api_steps.py
from behave import given, when, then
from utils.excel_reader import read_users_from_excel
from utils.api_client import APIClient
from utils.config import config
from utils.logger import logger
import allure
import json


@given("I have an Excel file with users")
def step_have_excel(context):
    try:
        path = config.excel_path
        context.users = read_users_from_excel(path)
        assert len(context.users) > 0, "No user data found in Excel file"

        logger.info(f"Read {len(context.users)} user records from Excel")

        # Attach sample data to allure report
        sample_data = json.dumps(context.users[:3], indent=2)  # Show first 3 records
        allure.attach(
            sample_data,
            name="sample_excel_data",
            attachment_type=allure.attachment_type.TEXT,
        )
    except Exception as e:
        logger.error(f"Failed to load Excel file: {str(e)}")
        raise


@when("I create users via the API")
def step_create_users(context):
    base = config.api_base_url
    client = APIClient(base)
    context.responses = []
    for i in context.users:
        # Map columns exactly as the API expects; dummyjson is flexible for this assignment
        payload = {
            "firstName": i.get("firstName"),
            "lastName": i.get("lastName"),
            "email": i.get("email"),
            "phone": str(i.get("phone")) if i.get("phone") is not None else None,
        }
        logger.info(f"Creating user {i}: {payload['firstName']} {payload['lastName']}")
        resp = client.create_user(payload)
        assert resp.status_code == 201

        if resp.status_code in [200, 201]:
            body = resp.json()  # Convert response to dict
            logger.info(f"User {i} created successfully. ID: {body.get('id', 'N/A')}")
        else:
            logger.warning(f"User {i} creation failed. Status: {resp.status_code}")

        context.responses.append(resp)


@then("I print the API responses")
def step_print_responses(context):
    for idx, r in enumerate(context.responses, start=1):
        try:
            body = r.json()
        except Exception:
            body = r.text
        logger.info(f"{idx}. status: {r.status_code}, body: {body}")
