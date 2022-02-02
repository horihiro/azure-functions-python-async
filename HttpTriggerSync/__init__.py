import logging
import time

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    time.sleep(10)
    return func.HttpResponse(
          "This sync HTTP triggered function executed successfully.",
          status_code=200
    )
