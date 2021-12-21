import requests

post_new_pet_headers = {
    "auth_key": "197394683a7069e85ca2fb34c04d4009f7d4ce0697c14820b4441c2b",
    "name": "LION",
    "animal_type": "KIT",
    "age": '4',
    "pet_photo": ""
}

post_new_pet_params = post_new_pet_headers
new_pet_POST_link = "https://petfriends1.herokuapp.com/api/pets"


def post_new_pet(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers,
                             files={"pet_photo": open('8.jpg', 'rb')}
                             )
    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(post_new_pet(new_pet_POST_link, post_new_pet_params, post_new_pet_headers))
