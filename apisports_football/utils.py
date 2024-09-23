from typing import Dict

def prepare_params(params: Dict) -> Dict:
    if params is None:
        return {}
    return {k: v for k, v in params.items() if v is not None}
