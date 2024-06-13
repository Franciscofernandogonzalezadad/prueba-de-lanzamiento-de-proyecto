import sender_stand_request
import data
import pytest


def get_user_body(first_name):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    current_body = data.user_body.copy()
    # Se cambia el valor del parámetro firstName
    current_body["firstName"] = first_name
    # Se devuelve un nuevo diccionario con el valor firstName requerido
    return current_body


# Función de prueba positiva
def positive_assert(first_name):
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body(first_name)
    # El resultado de la solicitud para crear un/a nuevo/a usuario/a se guarda en la variable user_response
    user_response = sender_stand_request.post_new_user(user_body)

    # Comprueba si el código de estado es 201
    assert user_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert user_response.json()["authToken"] != ""

    # El resultado de la solicitud de recepción de datos de la tabla "user_model" se guarda en la variable "users_table_response"
    users_table_response = sender_stand_request.get_users_table()

    # String que debe estar en el cuerpo de respuesta
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    # Comprueba si el usuario o usuaria existe y es único/a
    assert users_table_response.text.count(str_user) == 1


# Prueba 1. Creación de un nuevo usuario o usuaria
# El parámetro "firstName" contiene dos caracteres
def test_create_user_2_letter_in_first_name_get_success_response():
    user_body = get_user_body("Aa")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

    # El resultado de la solicitud de recepción de datos de la tabla "user_model" se guarda en la variable "users_table_response"
    users_table_response = sender_stand_request.get_users_table()
    # El string que debe estar en el cuerpo de la respuesta para recibir datos de la tabla "users" se ve así
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    # Comprueba si el usuario o usuaria existe y es único/a
    assert users_table_response.text.count(str_user) == 1


def test_create_user_15_letter_in_first_name_get_success_response():
    def positive_assert(first_name):
        # El cuerpo de la solicitud actualizada se guarda en la variable user_body
        user_body = get_user_body(first_name)
        # El resultado de la solicitud para crear un/a nuevo/a usuario/a se guarda en la variable user_response
        user_response = sender_stand_request.post_new_user(user_body)

        # Comprueba si el código de estado es 201
        assert user_response.status_code == 201
        # Comprueba que el campo authToken está en la respuesta y contiene un valor
        assert user_response.json()["authToken"] != ""

        # El resultado de la solicitud de recepción de datos de la tabla "user_model" se guarda en la variable "users_table_response"
        users_table_response = sender_stand_request.get_users_table()

        # String que debe estar en el cuerpo de respuesta
        str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
                   + user_body["address"] + ",,," + user_response.json()["authToken"]

        # Comprueba si el usuario o usuaria existe y es único/a
        assert users_table_response.text.count(str_user) == 1
        positive_assert("Aaaaaaaaaaaaaaa")

    # Prueba 1. Creación de un nuevo usuario o usuaria
    # El parámetro "firstName" contiene 1 caracteres


# Prueba 3. Error
# El parámetro "firstName" contiene un carácter
def test_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_symbol("A")


# Función de prueba negativa
def negative_assert_symbol(first_name):
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body(first_name)

    # Comprueba si la variable "response" almacena el resultado de la solicitud.
    response = sender_stand_request.post_new_user(user_body)

    # Comprueba si la respuesta contiene el código 400.
    assert response.status_code == 400

    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400.
    assert response.json()["code"] == 400
    # Comprueba si el atributo "message" en el cuerpo de respuesta se ve así:
    assert response.json()["message"] == "El nombre que ingresaste es incorrecto. " \
                                         "Los nombres solo pueden contener caracteres latinos,  " \
                                         "los nombres deben tener al menos 2 caracteres y no más de 15 caracteres"


def test_create_user_16_letter_in_first_name_get_error_response():
    negative_assert_symbol2("Аааааааааааааааа")

    # Función de prueba negativa


def negative_assert_symbol2(first_name):
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body(first_name)

    # Comprueba si la variable "response" almacena el resultado de la solicitud.
    response = sender_stand_request.post_new_user(user_body)

    # Comprueba si la respuesta contiene el código 400.
    assert response.status_code == 400

    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400.
    assert response.json()["code"] == 400
    # Comprueba si el atributo "message" en el cuerpo de respuesta se ve así:
    assert response.json()["message"] == "El nombre que ingresaste es incorrecto. " \
                                         "Los nombres solo pueden contener caracteres latinos,  " \
                                         "los nombres deben tener al menos 2 caracteres y no más de 15 caracteres"


def test_create_user_has_space_in_first_name_get_error_response():
    negative_assert_symbol("A Aaa")


def negative_assert_symbol3(first_name):
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body(first_name)

    # Comprueba si la variable "response" almacena el resultado de la solicitud.
    response = sender_stand_request.post_new_user(user_body)

    # Comprueba si la respuesta contiene el código 400.
    assert response.status_code == 400

    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400.
    assert response.json()["code"] == 400
    # Comprueba si el atributo "message" en el cuerpo de respuesta se ve así:
    assert response.json()["message"] == "El nombre que ingresaste es incorrecto. " \
                                         "Los nombres solo pueden contener caracteres latinos,  " \
                                         "los nombres deben tener al menos 2 caracteres y no más de 15 caracteres"


def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("№%@")


def negative_assert_symbol4(first_name):
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body(first_name)

    # Comprueba si la variable "response" almacena el resultado de la solicitud.
    response = sender_stand_request.post_new_user(user_body)

    # Comprueba si la respuesta contiene el código 400.
    assert response.status_code == 400
    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400.
    assert response.json()["code"] == 400
    # Comprueba si el atributo "message" en el cuerpo de respuesta se ve así:
    assert response.json()["message"] == "El nombre que ingresaste es incorrecto. " \
                                         "Los nombres solo pueden contener caracteres latinos,  " \
                                         "los nombres deben tener al menos 2 caracteres y no más de 15 caracteres"


def test_create_user_has_number_in_first_name_get_error_response():
    negative_assert_symbol("123")


def test_create_user_empty_first_name_get_error_response():
    negative_assert_symbol("")
    user_body = get_user_body("")


def negative_assert_no_firstname(user_body):
    pass


def negative_assert_no_firstname1(user_body):
    negative_assert_no_firstname(user_body)


def test_create_user_number_type_first_name_get_error_response():
    user_body = get_user_body(12)
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400
