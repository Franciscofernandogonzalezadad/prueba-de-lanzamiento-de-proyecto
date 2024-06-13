
    # Guarda el resultado de llamar a la función a la variable "response"

    response1 = sender_stand_request.post_new_user(data.user_body)

    # Comprueba si la respuesta contiene el código 400


assert response.status_code == 400

assert response.json()["code"] == 400

# Comprueba si el atributo "message" en el cuerpo de respuesta se ve así:
assert response.json()["message"] == "No se enviaron todos los parámetros requeridos"


# Prueba 8. Error
# La solicitud no contiene el parámetro "firstName"
def test_create_user_no_first_name_get_error_response():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "user_body"
    # De lo contrario, se podrían perder los datos del diccionario de origen
    user_body = data.user_body.copy()
    # El parámetro "firstName" se elimina de la solicitud
    user_body.pop("firstName")
    # Comprueba la respuesta
    negative_assert_no_firstname(user_body)

    # Función de prueba negativa
    # La respuesta contiene el siguiente mensaje de error: "No se han enviado todos los parámetros requeridos"


Prueba
9.
Error


# El parámetro "firstName" contiene un string vacío
def test_create_user_empty_first_name_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body("")
    # Comprueba la respuesta
    negative_assert_no_firstname(user_body)
