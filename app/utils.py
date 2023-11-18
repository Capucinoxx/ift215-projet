from functools import wraps
from typing import List, Callable, Any

from flask import jsonify, request
from flask_login import LoginManager

login_manager = LoginManager()


def check_required_json_data(keys: List[str]) -> Callable:
    """
    Decorator to check if the request contains the required JSON data.
    If request method is GET, the function is called without any checks.

    Args:
        keys: The required keys in the JSON data
    """

    def decorator(route_fct: Callable) -> Callable:
        @wraps(route_fct)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if request.method == 'GET':
                return route_fct(*args, **kwargs)

            data = request.json
            if not data or not all(key in data for key in keys):
                return jsonify({'error': 'Missing required data'}), 400
            return route_fct(*args, **kwargs)

        return wrapper

    return decorator
