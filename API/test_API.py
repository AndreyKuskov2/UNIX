import pytest
import requests

# POST PET SIMPLE
post_simple_headers = {
    "auth_key": "197394683a7069e85ca2fb34c04d4009f7d4ce0697c14820b4441c2b",
    "name": "Bombastic",
    "animal_type": "Big Bad Boy",
    "age": '6'
}
post_simple_params = post_simple_headers
create_pet_simple_POST_link = "https://petfriends1.herokuapp.com/api/create_pet_simple"

# API KEY
get_key_headers = {
    "email": "kuskov-2002@mail.ru",
    "password": "12345"
}
get_key_params = get_key_headers
api_key_link = "https://petfriends1.herokuapp.com/api/key"

# PETS LIST
get_headers_my_pets = {
    "auth_key ": "197394683a7069e85ca2fb34c04d4009f7d4ce0697c14820b4441c2b",
    "filter": "my_pets"
}
get_params_my_pets = get_headers_my_pets
my_pets_link = "https://petfriends1.herokuapp.com/api/pets?filter=my_pets"

# NEW PET
post_new_pet_headers = {
    "auth_key": "197394683a7069e85ca2fb34c04d4009f7d4ce0697c14820b4441c2b",
    "name": "Tonny Montana",
    "animal_type": "monkey",
    "age": '4',
    "pet_photo": ""
}
post_new_pet_params = post_new_pet_headers
new_pet_POST_link = "https://petfriends1.herokuapp.com/api/pets"

# SET PHOTO
post_set_photo_headers = {
    "auth_key": "197394683a7069e85ca2fb34c04d4009f7d4ce0697c14820b4441c2b",
    "pet_id": "526c71d9-3787-4b72-b04f-da90293b869b"
}
post_set_photo_params = post_set_photo_headers
set_photo_POST_link = "https://petfriends1.herokuapp.com/api/pets/set_photo/" + "526c71d9-3787-4b72-b04f-da90293b869b"

# DELETE
delete_pet_headers = {
    "auth_key": "197394683a7069e85ca2fb34c04d4009f7d4ce0697c14820b4441c2b",
    "pet_id": "0f1b6134-dbdb-4fee-8f47-3e213895cb42"
}
delete_pet_params = delete_pet_headers
DELETE_pet_link = "https://petfriends1.herokuapp.com/api/pets/" + "0f1b6134-dbdb-4fee-8f47-3e213895cb42"

# PUT INFO
put_info_headers = {
    "auth_key": "197394683a7069e85ca2fb34c04d4009f7d4ce0697c14820b4441c2b",
    "pet_id": "9c565e54-5271-4c95-9615-61f2d0bc509e"
}
put_info_params = put_info_headers
put_info_link = "https://petfriends1.herokuapp.com/api/pets/" + "9c565e54-5271-4c95-9615-61f2d0bc509e"


# ФИКСТУРЫ
@pytest.fixture
def post_simple_pet(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers
                             )
    return response.ok


@pytest.fixture
def get_api_key(link, params, headers):
    response = requests.get(link,
                            params=params,
                            headers=headers
                            )
    if response.status_code == 200:
        return True


@pytest.fixture
def get_pets_list(link, params, headers):
    response = requests.get(link,
                            params=params,
                            headers=headers
                            )
    if response.status_code == 200:
        return True


@pytest.fixture
def post_new_pet(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers,
                             files={"pet_photo": open('monkey.jpg', 'rb')}
                             )
    return response.ok


@pytest.fixture
def post_set_photo(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers,
                             files={"pet_photo": open('dog.jpg', 'rb')}
                             )
    return response.ok


@pytest.fixture
def delete_pet(link, del_params, del_headers):
    response = requests.delete(link,
                               params=del_params,
                               headers=del_headers
                               )
    if response.status_code == 200:
        return True


@pytest.fixture
def put_pet_info():
    response = requests.put(put_info_link,
                            params=put_info_params,
                            headers=put_info_headers
                            )
    return response.ok


@pytest.mark.parametrize('link, params, header, expected_result',
                         [ 
                             (create_pet_simple_POST_link, post_simple_params, post_simple_headers, True),

                             (new_pet_POST_link, post_new_pet_params, post_new_pet_headers, False),


                             pytest.param(set_photo_POST_link, post_set_photo_params, post_set_photo_headers, True,
                                          marks=pytest.mark.xfail),
                         ]
                         )
def test_post(link, params, header, expected_result):
    response = requests.post(link,
                             params=params,
                             headers=header
                             )
    assert response.ok == expected_result


@pytest.mark.parametrize('link, params, header, expected_result',
                         [  # get_api_key
                             (api_key_link, get_key_params, get_key_headers, True),

                             # get_my_pets_list
                             (my_pets_link, get_params_my_pets, get_headers_my_pets, True)
                         ]
                         )
def test_get(link, params, header, expected_result):
    response = requests.get(link,
                            params=params,
                            headers=header
                            )
    assert response.ok == expected_result


@pytest.mark.parametrize('link, params, header, expected_result',
                         [
                             (DELETE_pet_link, delete_pet_params, delete_pet_headers, True)
                         ]
                         )
def test_delete(link, params, header, expected_result):
    response = requests.delete(link,
                               params=params,
                               headers=header
                               )
    assert response.ok == expected_result


def test_put(put_pet_info):
    assert put_pet_info == True
