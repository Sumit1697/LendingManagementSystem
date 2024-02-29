from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from LendingLmsHelper import GenericHelper, cifHelper
from Logger import logger


# Create your views here.
class CifApplication(APIView):
    def post(self, request):
        requestheader = request.headers
        requestbody = request.data
        # print(f"Request Headers {requestheader} and body {requestbody}")
        validheader = ['productId', 'Version']
        validbody = ['cif_id', 'external_id', 'email_id', 'mobile_number', 'pan_number', 'date_of_birth', 'profile_type', 'user_address']
        genhelper = GenericHelper(requestheader, requestbody, validheader, validbody)
        isvalidHeader = genhelper.validateRequestHeader()
        if isvalidHeader is True:
            isvalidbody = genhelper.validateRequestBody()
            if isvalidbody is not True:
                return Response(isvalidbody, status=isvalidbody['status'])
            else:
                cifhelper = cifHelper(requestheader, requestbody)
                cifhelper.checkproductconfigdb()
                response = cifhelper.getresponse()
                return Response(response, status = response['status'])
        else:
            return Response(isvalidHeader, status=isvalidHeader['status'])

    def get(self, request):
        requestheader = request.headers
        validheader = ['cifId']
        genhelper = GenericHelper(requestheader, None, validheader, None)
        isvalidheader = genhelper.validateRequestHeader()
        if isvalidheader is True:
            cifhelper = cifHelper(requestheader, None)
            cifhelper.checkcifinfo()
            response = cifhelper.getresponse()
            return Response(response, status=response['status'])
        else:
            return Response(isvalidheader, status=isvalidheader['status'])
