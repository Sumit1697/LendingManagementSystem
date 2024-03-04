from rest_framework.views import APIView
from rest_framework.response import Response
from LendingLmsHelper import GenericHelper, onboardingHelper



class AccountOnborading(APIView):
    def post(self, request):
        request_headers = request.headers
        request_body = request.data
        valid_headers = ['productId', 'version', 'cifId', 'externalId']
        valid_body = ['lenderId','email','annual_income','phone','credit_score','loan_amount', 'term_months', 'interest_rate']
        genhelper = GenericHelper(request_headers, request_body, valid_headers, valid_body)
        is_valid_header = genhelper.validateRequestHeader()
        if is_valid_header is not True:
            return Response(is_valid_header, status=is_valid_header['status'])
        else:
            is_valid_body = genhelper.validdateRequestBodyofObj(request_body, valid_body)
            if set(is_valid_body) != set(valid_body):
                missing_body = list(set(is_valid_body) - set(valid_body))
                responseData = {
                    "status":400,
                    "message": f"Missing Mandatory Field {', '.join(missing_body)} from request body"
                }
                return Response(responseData, status=responseData['status'])
            else:
                onboardinghelper = onboardingHelper(request_headers, request_body)
                onboardinghelper.checkDbAndValidateParameters()

        return Response("Hi", status = 200)
