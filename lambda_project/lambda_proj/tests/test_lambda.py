import json

from hello_world.app import lambda_handler


def test_lambda_handler_success():
    response = lambda_handler("abcd", "abcdefghi")

    assert response["statusCode"] == 200
    assert json.loads(response["body"]) == {
        "message": "Hello World!"
    }


def test_lambda_handler_none_input():
    response = lambda_handler(None, None)

    assert response["statusCode"] == 300
    assert json.loads(response["body"]) == {
        "message": "No World!"
    }


def test_lambda_handler_invalid_length():
    response = lambda_handler("abcdefghi", "abcde")

    assert response["statusCode"] == 400
    assert json.loads(response["body"]) == {
        "message": "Bad World!"
    }