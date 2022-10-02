import json
from pathlib import Path
import requests
import sys
import logging

logging.basicConfig(level=logging.INFO)
base_dir = Path().resolve()
sys.path.append(base_dir / "operations")

from operations.file_operation import zip_str, unzip_str
from config import API_HOST_URL


def get_test_ifc(zip: bool = False) -> str:
    data_dir = base_dir / 'tests' / "data"
    ifc_path = data_dir / 'test.ifc'
    with open(ifc_path) as f:
        ifc_str = f.read()

    if zip:
        ifc_str = zip_str(ifc_str)
    return ifc_str


def test_for_health_check(logger: logging.Logger = logging.getLogger(__name__)):
    logger.info("[START] Test for health check")
    url = f"{API_HOST_URL}/health"
    response = requests.get(url=url)
    logger.info("Send request and get response")

    logger.info(f"status code: {response.status_code}")
    logger.info(f"response: {response.text}")

    logger.info("[END] Test for health check")


def test_for_health_check_with_params(logger: logging.Logger = logging.getLogger(__name__)):
    logger.info("[START] Test for health check with params")
    url = f"{API_HOST_URL}/health/params"
    data = {
        'ifc': 'test',
        'zipped': True,
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.get(url=url, data=json.dumps(data), headers=headers)
    logger.info("Send request and get response")

    logger.info(f"status code: {response.status_code}")
    logger.info(f"response: {response.text}")

    logger.info("[END] Test for health check with params")


def test_for_law21_1(logger: logging.Logger = logging.getLogger(__name__)):
    logger.info("[START] Test for API")
    ifc_data = get_test_ifc(zip=True)

    url = f"{API_HOST_URL}/law/21-1"
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'ifc': ifc_data,
        'zipped': True,
        'metadata': {
            'file_name': 'test.ifc'
        }
    }
    post_data_file_path = base_dir / "tests" / "data" / "post_data.json"
    with post_data_file_path.open('w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    logger.info("Set for request")

    response = requests.get(url=url, data=json.dumps(data), headers=headers)
    logger.info("Send request and get response")

    logger.info(f"status code: {response.status_code}")
    logger.debug(f"response: {response.text}")

    logger.info("[END] Test for API")


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    # test_for_health_check(logger)
    # test_for_health_check_with_params(logger)
    test_for_law21_1(logger=logger)
