from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if response is not None:
        # Standardize the error format for the frontend
        response.data = {
            'status': 'error',
            'code': response.status_code,
            'message': response.data.get('detail', 'An error occurred.'),
            'errors': response.data if response.status_code != 404 else None
        }

    return response
