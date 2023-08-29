To generate token
-----------------
curl --request POST \
  --url http://localhost:8000/api/user/login \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "user1",
	"password": "password"
}
'

To get logged in user
---------------------
curl --request GET \
  --url http://localhost:8000/api/user/profile \
  --header 'Authorization: Bearer <access_token>'


To list all users
---------------------

- Login through browser (not token auth) http://localhost:8000/api-auth/
- http://localhost:8000/api/user/list
