import traceback

from fastapi import Response

from api.main import app, logger
from api.schemas.v2.api_request import APIRequest
from api.schemas.v2.api_response import APIResponse, AnalysisResult

from jpnifcbc.law.standard_methods.law21_1 import ConfirmationV2 as Law21_1_v2
from jpnifcbc.models.building import Building, Storey, Wall, Column, Slab, Roof, Beam, Stair

v2_base_url = 'v2'


@app.post(f"/{v2_base_url}/law/21-1")
def law_21_1(body: APIRequest):
    logger.info("Start Law 21_1")
    message = "Failed"
    result = None
    metadata = None
    try:
        request = body.dict()
        building = Building.from_dict(request["building"])
        storeys = [Storey.from_dict(s) for s in building["storeys"]]
        walls = [Wall.from_dict(w) for w in building["walls"]]
        columns = [Column.from_dict(c) for c in building["columns"]]
        slabs = [Slab.from_dict(s) for s in building["slabs"]]
        beams = [Beam.from_dict(b) for b in building["beams"]]
        roofs = [Roof.from_dict(r) for r in building["roofs"]]
        stairs = [Stair.from_dict(s) for s in building["stairs"]]
        building.building_elements = walls + columns + slabs + beams + roofs + stairs
        building.storeys = storeys
        metadata = request["metadata"]

        conformity_elements, not_conformity_elements, exception_elements = Law21_1_v2.main(
            building=building
        )

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
