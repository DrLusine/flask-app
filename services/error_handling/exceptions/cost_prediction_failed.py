from flask import jsonify

class CostPredictionFailed(Exception):
    status_code = 500

    def __init__(self, error_message, response_status_code=None):
        Exception.__init__(self)

        self.error_message = error_message
        if response_status_code is not None:
            self.response_status_code = response_status_code

    def get_http_error_response(self):
        httpErrorResponse = jsonify({"error": { "message": self.error_message }})
        httpErrorResponse.status_code = self.response_status_code
        return httpErrorResponse