import json
from pathlib import Path
import requests
import sys
import logging
import base64
import gzip

logging.basicConfig(level=logging.INFO)
base_dir = Path().resolve()
sys.path.append(base_dir / "operations")

from operations.file_operation import zip_str
import config


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
    url = f"{config.API_HOST_URL}/health"
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.get(url=url, headers=headers)

    logger.info("Send request and get response")

    logger.info(f"status code: {response.status_code}")
    logger.info(f"response: {response.text}")

    logger.info("[END] Test for health check")


def test_for_health_check_with_params(logger: logging.Logger = logging.getLogger(__name__)):
    logger.info("[START] Test for health check with params")
    url = f"{config.API_HOST_URL}/health/params"
    data = {
        'ifc': 'test',
        'zipped': True,
    }
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.post(url=url, data=json.dumps(data), headers=headers)
    logger.info("Send request and get response")

    logger.info(f"status code: {response.status_code}")
    logger.info(f"response: {response.text}")

    logger.info("[END] Test for health check with params")


def test_for_law21_1(logger: logging.Logger = logging.getLogger(__name__)):
    logger.info("[START] Test for API")
    ifc_data = get_test_ifc(zip=True)

    url = f"{config.API_HOST_URL}/law/21-1"
    headers = {
        'Content-Type': 'application/json',
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

    response = requests.post(url=url, data=json.dumps(data), headers=headers)
    logger.info("Send request and get response")

    logger.info(f"status code: {response.status_code}")
    logger.debug(f"response: {response.text}")

    logger.info("[END] Test for API")


def test_zip():
    target = base_dir / "tests" / "data" / "test.txt"
    # target = base_dir / "tests" / "data" / "test_base64.txt"
    with target.open('rb') as f:
        decompressed_value = f.read()
    print(decompressed_value[:10])
    # value = gzip.decompress(base64.b64decode(decompressed_value))
    value = gzip.decompress(decompressed_value)

    save_data_path = base_dir / "tests" / "data" / "test_ifc.txt"
    with save_data_path.open('w') as f:
        f.write(value.decode(encoding='utf-8'))


def make_sample():
    target = base_dir / "tests" / "data" / "test.ifc"
    with target.open('r') as f:
        original_data = f.read()
    compressed_data = gzip.compress(original_data.encode(encoding='utf-8'))
    print(compressed_data[:10])
    compressed_base64_data = base64.b64encode(compressed_data)
    save_path = base_dir / "tests" / "data" / "sample.txt"
    with save_path.open('wb') as f:
        f.write(compressed_data)

    ifc_data = compressed_base64_data.decode(encoding='utf-8')
    save_base64_path = base_dir / "tests" / "data" / "sample_base64.txt"
    with save_base64_path.open('w') as f:
        f.write(ifc_data)

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


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.info("Start test")
    # test_for_health_check(logger)
    # test_for_health_check_with_params(logger)
    # test_for_law21_1(logger)
    # test_zip()
    make_sample()
    logger.info("End test")
