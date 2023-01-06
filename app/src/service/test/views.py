import json
from django.http import HttpResponse, HttpRequest, JsonResponse, HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from service.commom.response import SuccessJsonResponse, FailureJsonResponse
from service.commom.constants import POST_METHOD, GET_METHOD
from service.test.models import Test
from service.test.utils import extract_questions_from_list
from mongoengine.errors import ValidationError, DoesNotExist


def register_test(test_body: bytes) -> JsonResponse:
    """Verifies the HTTP Request method and calls the appropriate method to handle the request:
        Returning all the tests items on database;
        Or creates a new one
    
    Args:
        test_body (bytes): The request body bytes having the test attributes

    Raises:
        Exception (There is no object to be added): In case request data is empty
        Exception (Test questions must be a list): In case question type is wrong

    Returns:
        response (FailureJsonResponse | SuccessJsonResponse): response having the method result
    """
    test_dict = json.loads(test_body.decode("utf-8"))
    if not test_dict:
        raise Exception('There is no object to be added')

    questions_list = test_dict.get('questions')
    if not isinstance(questions_list, list):
        raise Exception('Test questions must be a list')
    
    test = Test(
        name = test_dict.get('name'),
        summary = test_dict.get('summary'),
        type = test_dict.get('type'),
        duration = test_dict.get('duration'),
        level = test_dict.get('level'),
        audience = test_dict.get('audience'),
        language = test_dict.get('language'),
        skills = test_dict.get('skills')
    )
    questions = extract_questions_from_list(questions_list)
    test.questions = questions

    test.save()

    return SuccessJsonResponse()


def list_all_tests() -> JsonResponse:
    itens = Test.objects.to_json()
    result = {'itens': json.loads(itens)}
    return SuccessJsonResponse(result)


def get_test_by_id(id: str) -> JsonResponse:
    try:
        test = Test.objects.get(pk=id)
    except (ValidationError, DoesNotExist) as e:
        return FailureJsonResponse('Item not found')
    
    result = {'item': json.loads(test.to_json())}
    return SuccessJsonResponse(result)


### URL ENTRIES
@csrf_exempt
def index(request: HttpRequest) -> HttpResponse:
    """Verifies the HTTP Request method and calls the appropriate method to handle the request:
        Returning all the tests items on database;
        Or creates a new one
    
    Args:
        request (HttpRequest): The django-built HTTP request object

    Returns:
        response (HttpResponseBadRequest | FailureJsonResponse | SuccessJsonResponse):
            reponse containing the items or the reason if something goes wrong
    """
    try:
        if request.method == POST_METHOD:
            return register_test(request.body)
        elif request.method == GET_METHOD:
            return list_all_tests()
        else:
            return HttpResponseBadRequest()
    except Exception as e:
        return FailureJsonResponse(str(e))


@csrf_exempt
def detail(request: HttpRequest, test_id: str):
    """Gets the detail of a specific test
    
    Args:
        request (HttpRequest): The django-built HTTP request object

    Returns:
        response (HttpResponseBadRequest | FailureJsonResponse | SuccessJsonResponse):
            reponse containing the items or the reason if something goes wrong
    """
    try:
        if request.method != GET_METHOD:
            return HttpResponseBadRequest()
        
        return get_test_by_id(test_id)
    except Exception as e:
        return FailureJsonResponse(str(e))
