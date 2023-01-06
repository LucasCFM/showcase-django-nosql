import json
from django.http import JsonResponse


class SuccessJsonResponse(JsonResponse):

    def __init__(self, data: dict = None) -> None:
        if not data:
            super().__init__({'success': True})
            return

        data['success'] = True
        super().__init__(data)


class FailureJsonResponse(JsonResponse):

    def __init__(self, reason: str) -> None:
        if not reason:
            raise Exception('Failure response must have a reason')

        data = {
            'success': False,
            'reason': reason
        }
        super().__init__(data)
