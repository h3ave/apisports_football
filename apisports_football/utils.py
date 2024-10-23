from typing import Dict

def prepare_params(params: Dict) -> Dict:
    if params is None:
        return {}
    result = {}
    for k, v in params.items():
        if v is not None:
            if isinstance(v, bool):
                result[k] = str(v).lower()
            else:
                result[k] = v
    return result
