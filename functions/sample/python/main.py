"""IBM Cloud Function that gets all reviews for a dealership

Returns:
    List: List of reviews for the given dealership
"""
from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests


def main(param_dict):
    """Main Function

    Args:
        param_dict (Dict): input paramater

    Returns:
        _type_: _description_ TODO
    """

    try:
        client = Cloudant.iam(
            account_name=param_dict["COUCH_USERNAME"],
            api_key=param_dict["IAM_API_KEY"],
            connect=True,
        )
        print(f"Databases: {client.all_dbs()}")
    except CloudantException as cloudant_exception:
        print("unable to connect")
        return {"error": cloudant_exception}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("connection error")
        return {"error": err}

    return {"dbs": client.all_dbs()}

"""import sys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
def main(dict):
    authenticator = IAMAuthenticator('KNTekC1TCrCpJ8fKGKlYNvLwZepHQeF8U-3zmWU9z_PY')
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url("https://apikey-v2-1nnwkxyh6v74shsolcgiopss2baiz48f7a8pyz3fme9y:94489169cd002b836b63c7e483d97c1b@7ad9f0d9-cba5-4a9c-9891-de7d8475648d-bluemix.cloudantnosqldb.appdomain.cloud")
    response = service.post_find(
    db='reviews',
    selector={'dealership': {'$eq': int(dict["id"])}},
    ).get_result()
    try:
        # result_by_filter=my_database.get_query_result(selector,raw_result=True)
        result= {
        'headers': {'Content-Type':'application/json'},
        'body': {'data':response}
        }
        return result
    except:
        return {
        'statusCode': 404,
        'message': 'Something went wrong'
        }

import sys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
def main(dict):
    authenticator = IAMAuthenticator("KNTekC1TCrCpJ8fKGKlYNvLwZepHQeF8U-3zmWU9z_PY")
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url("https://apikey-v2-1nnwkxyh6v74shsolcgiopss2baiz48f7a8pyz3fme9y:94489169cd002b836b63c7e483d97c1b@7ad9f0d9-cba5-4a9c-9891-de7d8475648d-bluemix.cloudantnosqldb.appdomain.cloud")
    response = service.post_document(db='reviews', document=dict["review"]).get_result()
    try:
    # result_by_filter=my_database.get_query_result(selector,raw_result=True)
        result= {
        'headers': {'Content-Type':'application/json'},
        'body': {'data':response}
        }
        return result
    except:
        return {
        'statusCode': 404,
        'message': 'Something went wrong'
        }"""
        