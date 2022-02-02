import logging
import asyncio

import azure.functions as func


async def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    await asyncio.sleep(10)
    return func.HttpResponse(
          "This async HTTP triggered function executed successfully.",
          status_code=200
    )
