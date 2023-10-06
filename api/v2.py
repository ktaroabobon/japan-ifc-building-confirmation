import traceback

from fastapi import Response

from api.main import app, logger
from api.schemas.v2.api_request import APIRequest
from api.schemas.v2.api_response import APIResponse, AnalysisResult

from jpnifcbc.law.standard_methods.law21_1 import ConfirmationV2 as Law21_1_v2

v2_base_url = 'v2'


@app.post(f"/{v2_base_url}/law/21-1")
def law_21_1(body: APIRequest):
    logger.info("Start Law 21_1")
    message = "Failed"
    result = None
    metadata = None
    try:
        request = body.dict()
        building = request["building"]
        metadata = request["metadata"]

        conformity_elements, not_conformity_elements, exception_elements = Law21_1_v2.main(building)

        result = AnalysisResult(
            conformityElements=[e.export_as_dict() for e in conformity_elements],
            nonConformityElements=[e.export_as_dict() for e in not_conformity_elements],
            exceptionElements=[e.export_as_dict() for e in exception_elements]
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
