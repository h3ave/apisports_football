from typing import Callable, Dict, List


def dict_to_query_params(params: Dict) -> str:
    if not isinstance(params, Dict):
        return ''
    lowercase_params = {key: str(value).lower() if isinstance(
        value, bool) else value for key, value in params.items()}
    return '&'.join(f'{key}={value}' for key, value in lowercase_params.items())


def get_api_method(api_wrapper, method_names: List) -> Callable:
    if hasattr(api_wrapper, method_names[0]):
        if len(method_names) == 1:
            endpoint = getattr(api_wrapper, method_names[0])
            method = endpoint().get
        else:
            endpoint = getattr(api_wrapper, method_names[0])
            method = getattr(endpoint(), '_'.join(method_names[1:]))
        return method
    return None
