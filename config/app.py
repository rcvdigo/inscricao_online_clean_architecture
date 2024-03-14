from typing import Dict


def config() -> Dict[str, Dict[str, str]]:
    return {
        'db': {
            'host': 'localhost',
            'user': 'root',
            'password': 'root',
            'database': 'clean_arch'
        }
    }
