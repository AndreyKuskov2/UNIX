import requests

post_set_photo_headers = {
    "auth_key": "197394683a7069e85ca2fb34c04d4009f7d4ce0697c14820b4441c2b",
    "pet_id": "7bbc9f4e-450e-476d-bc7a-f29a50c66d07"
}

post_set_photo_params = post_set_photo_headers
set_photo_POST_link = "https://petfriends1.herokuapp.com/api/pets/set_photo/" + post_set_photo_headers['pet_id']


def post_set_photo(link, post_params, post_headers):
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


print(post_set_photo(set_photo_POST_link, post_set_photo_params, post_set_photo_headers))
