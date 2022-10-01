from pathlib import Path
import requests
import sys

base_dir = Path().resolve()
sys.path.append(base_dir / "operations")

from operations.file_operation import zip_str
from config import API_HOST_URL


def get_test_ifc(zip: bool = False) -> str:
    data_dir = base_dir / "tests" / "data"
    ifc_path = data_dir / 'test.ifc'
    with open(ifc_path) as f:
        ifc_str = f.read()

    if zip:
        ifc_str = zip_str(ifc_str)
    return ifc_str


if __name__ == '__main__':
    print("[START] Test for API")
    ifc_data = get_test_ifc(zip=True)
    print(f"IFC Data: {ifc_data}")

    url = f"{API_HOST_URL}/law/21_1"
    header = {
        'Content-Type': 'application/json'
    }
    params = {
        'ifc': ifc_data,
        'zip': True,
        'metadata': {
            'file_name': 'test.ifc'
        }
    }
    print("Set for request")

    response = requests.get(url=url, json=params, headers=header)
    print("Send request and get response")

    print(f"status code: {response.status_code}")
    print(f"response: {response.text}")

    print("[END] Test for API")
