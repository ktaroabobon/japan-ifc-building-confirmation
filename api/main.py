from pathlib import Path
import shutil
import traceback

from fastapi import FastAPI
import ifcopenshell

from jpnifcbc.law.standard_methods.law21_1 import Confirmation as Law21_1
from schemas.api_request import APIRequest
from schemas.api_response import APIResponse
from operations.file_operation import unzip_str
from operations.object_operation import IfcOpenShellObj

app = FastAPI()


@app.get("/health")
def health_check():
    return {"health check": "ok"}


@app.get("/law/21_1")
def law_21_1(body: APIRequest):
    message = "Failed"
    try:
        request = APIRequest.parse_raw(body)
        ifc = request.ifc
        zipped = request.zipped
        APIResponse.metadata = request.metadata
        if zipped:
            ifc = unzip_str(ifc)

        tmp_dir = Path().resolve() / "tmp"
        if not tmp_dir.exists():
            tmp_dir.mkdir()
        tmp_ifc_path = tmp_dir / "tmp.ifc"
        print(tmp_ifc_path)

        with open(tmp_ifc_path, 'w') as f:
            f.write(ifc)
        print('save tmp file')

        ifc_file = ifcopenshell.open(str(tmp_ifc_path))
        print('open ifc file')

        shutil.rmtree(tmp_dir)
        print('remove tem dir')

        conformity_elements, not_conformity_elements, exception_elements = Law21_1.main(ifc_file=ifc_file)

        APIResponse.result = {
            'conformityElements': IfcOpenShellObj.get_obj_info(conformity_elements),
            'nonConformityElements': IfcOpenShellObj.get_obj_info(not_conformity_elements),
            'exceptionElements': IfcOpenShellObj.get_obj_info(exception_elements)
        }
        message = "Success"

    except Exception as e:
        print(traceback.format_exc())
        message += f"\n{str(e)}"

    APIResponse.message = message
    return APIResponse
