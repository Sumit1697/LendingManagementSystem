import time

from Logger import logger
from django.db import connection
from query import Queries
import json

cursor = connection.cursor()


class GenericHelper:
    def __init__(self, requestheader, requestbody, validheaders, validbody):
        self.requestheader = requestheader
        self.requestbody = requestbody
        self.validheaders = validheaders
        self.validbody = validbody
        self.found_keys = []
        logger.info(f"Received Headers for POST Request: {self.requestheader} and Body {self.requestbody}");

    def validateRequestHeader(self):
        try:
            missingoremptyheaders = [key for key in self.validheaders if
                                     key not in self.requestheader or not self.requestheader[key]]
            if missingoremptyheaders:
                responsedata = {
                    "status": 400,
                    "message": f"Bad request {', '.join(missingoremptyheaders)} missing from header"
                }
                logger.error(f"Response: {responsedata}")
                return responsedata
            else:
                logger.info("Headers are Valid")
                return True
        except Exception as e:
            logger.error(f"An Error Occurred at validate Header function {e}")

    def validateRequestBody(self, validbody=None):
        try:
            missingoremptybody = [key for key in self.validbody if
                                  key not in self.requestbody or not self.requestbody[key]]
            if missingoremptybody:
                responsedata = {
                    "status": 400,
                    "message": f"{', '.join(missingoremptybody)} is missing from request body"
                }
                logger.info(f"Response Received: {responsedata}")
                return responsedata
            else:
                return True
        except Exception as e:
            logger.error(f"Error occurred at validate body {e}")

    def validdateRequestBodyofObj(self, request_body, valid_body):
        for keys, values in request_body.items():
            if keys in valid_body:
                self.found_keys.append(keys)
                # print(f"Keys: {keys}")
            elif isinstance(values, dict):
                for sub_keys in values.keys():
                    # print(f"Sub Keys: {sub_keys}")
                    if sub_keys in valid_body and sub_keys not in valid_body:
                        self.found_keys.append(sub_keys)
                    else:
                        self.validdateRequestBodyofObj(values, valid_body)

        return set(self.found_keys)


class cifHelper:
    def __init__(self, requestheader, requestbody):
        self.requestheader = requestheader
        self.requestbody = requestbody
        self.responsedata = None
        # self.checkproductconfigdb()

    def checkproductconfigdb(self):
        try:
            cursor.execute(Queries.GET_PRODUCT_CONFIG, [self.requestheader['productId'], self.requestheader['version']])
            result = cursor.fetchone()
            logger.info(f"Fetched data from product config: {result}")
            alreadyPresent = []
            if result is not None:
                for keys, values in self.requestbody.items():
                    if keys not in ["date_of_birth", "user_address", "profile_type"]:
                        # print(f"Hello: {keys}, {values}")
                        cursor.execute(Queries.GET_CIF_INFORMATION + f"{keys} = %s", [values])
                        if cursor.fetchone() is not None:
                            alreadyPresent.append(keys)
                if (len(alreadyPresent) > 0):
                    self.responsedata = {
                        "status": 409,
                        "message": f"Data is already present for {', '.join(alreadyPresent)}"
                    }
                    logger.error(self.responsedata)
                else:
                    cursor.execute(Queries.INSERT_CIF_DATA, [self.requestbody[values] for values in self.requestbody if
                                                             self.requestbody[values]])
                    self.responsedata = {
                        "status": 200,
                        "message": self.requestbody
                    }
                    logger.info(f"Data inserted Successfully: {self.responsedata}")
            else:
                self.responsedata = {
                    "status": 400,
                    "message": "Product Id or Version is not present"
                }
        except Exception as e:
            logger.error(f"An Error occurred while checking database tables: {e}")
            print(f"An Error occurred while checking db database tables: {e}")

    def getresponse(self):
        if self.responsedata is not None:
            # logger.info(f"API Response: {self.responsedata}")
            return self.responsedata
        else:
            # logger.info(f"API Response: {self.responsedata}")
            return self.responsedata

    def checkcifinfo(self):
        try:
            cursor.execute(Queries.GET_CIF_INFORMATION + "cif_id = %s", [self.requestheader['cifId']])
            result = cursor.fetchone()
            if (result is not None):
                self.responsedata = {
                    "status": 200,
                    "message": {
                        "cif_id": result[1],
                        "external_id": result[2],
                        "email_id": result[3],
                        "phone_number": result[4],
                        "pan_number": result[5],
                        "date_of_birth": result[6],
                        "profile_type": result[7],
                        "user_address": result[8]
                    }
                }
                logger.info(f"Successfully fetch cif info: {self.responsedata}")
            else:
                self.responsedata = {
                    "status": 404,
                    "message": f"Cif info not present for cif_id = {self.requestheader['cifId']}"
                }
                logger.error(self.responsedata)
        except Exception as e:
            logger.error(f"Error occurred while fetching Cif Info from db: {e}")


class onboardingHelper:
    def __init__(self, valid_header, valid_body):
        self.valid_header = valid_header
        self.valid_body = valid_body

        # print(f"Valid Headers: {self.valid_header}, valid body: {self.valid_body}")

    def checkDbAndValidateParameters(self):
        print("Hello from function")