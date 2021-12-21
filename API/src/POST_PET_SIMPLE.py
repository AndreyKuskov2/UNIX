import requests
# "key": "003c6904c7f44a085a12f9bf146415bb3d72270254cfd4dc8e0bd1e2"


# POST PET SIMPLE
post_simple_headers = {
    "auth_key": "197394683a7069e85ca2fb34c04d4009f7d4ce0697c14820b4441c2b",
    "name": "Bob1",
    "animal_type": "German Shepherd",
    "age": '2'
}

post_simple_params = post_simple_headers
create_pet_simple_POST_link = "https://petfriends1.herokuapp.com/api/create_pet_simple"


def post_simple_pet(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers
                             )

    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    print(type(response), type(response.ok))
    return response.ok


print(post_simple_pet(create_pet_simple_POST_link, post_simple_params, post_simple_headers))

