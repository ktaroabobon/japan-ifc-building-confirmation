from pathlib import Path
import shutil
import traceback
from logging import getLogger
import json

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
import ifcopenshell

from jpnifcbc.law.standard_methods.law21_1 import Confirmation as Law21_1
from schemas.api_request import APIRequest, HealthAPIRequest
from schemas.api_response import APIResponse, AnalysisResult
from operations.file_operation import gunzip_str
from operations.object_operation import IfcOpenShellObj

base_dir = Path().resolve()

logger = getLogger('uvicorn')

app = FastAPI()

origins = [
    "http://localhost:5173",
    "https://ktaroabobon.github.io",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    body = {"health check": "ok"}
    return Response(content=json.dumps(body))


@app.post("/health/params")
def health_check_with_params(body: HealthAPIRequest):
    logger.info("this is health check with params")
    return Response(content=json.dumps(body.dict()))


@app.post("/law/21-1")
def law_21_1(body: APIRequest):
    logger.info("Start Law 21_1")
    message = "Failed"
    result = None
    metadata = None
    try:
        request = body.dict()
        ifc = request["ifc"]
        zipped = request["zipped"]
        metadata = request["metadata"]
        if zipped:
            ifc = gunzip_str(ifc)

        tmp_dir = base_dir / "tmp"
        if not tmp_dir.exists():
            tmp_dir.mkdir()
        tmp_ifc_path = tmp_dir / "tmp.ifc"
        logger.debug(f'write ifc file to {tmp_ifc_path}')

        with open(tmp_ifc_path, 'w') as f:
            f.write(ifc)
        logger.debug('save tmp file')

        ifc_file = ifcopenshell.open(str(tmp_ifc_path))
        logger.debug('open ifc file')

        shutil.rmtree(tmp_dir)
        logger.debug('remove tmp dir')

        conformity_elements, not_conformity_elements, exception_elements = Law21_1.main(ifc_file=ifc_file)

        result = AnalysisResult(
            conformityElements=IfcOpenShellObj.get_obj_info(conformity_elements),
            nonConformityElements=IfcOpenShellObj.get_obj_info(not_conformity_elements),
            exceptionElements=IfcOpenShellObj.get_obj_info(exception_elements)
        )
        message = "Success"
        logger.debug("Success Law 21_1")

    except Exception as e:
        logger.error(traceback.format_exc())
        message += f"\n{str(e)}"

    logger.debug(f"message: {message}")
    logger.debug(f"result: {result}")
    logger.debug(f"metadata: {metadata}")
    response = APIResponse(
        message=message,
        result=result,
        metadata=metadata
    )

    logger.info("End Law 21_1")
    return Response(content=response.json())
