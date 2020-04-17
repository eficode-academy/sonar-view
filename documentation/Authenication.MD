More test and integration with frontend needed

Ref: https://developers.google.com/identity/sign-in/web/backend-auth

1. Frontend: After Google login, fetch Google ID token with google API 
The example login page under `/backend`
```
function onSignIn(googleUser) {
  var id_token = googleUser.getAuthResponse().id_token;
  ...
}
```
Upon login at frontend, google also returns the following info:
```
ID: <User ID>
Full Name: Ruiyang Ding
Given Name: Ruiyang
Family Name: Ding
Image URL: https://lh3.googleusercontent.com/a-/XXX
Email: jane.done@eficode.com
ID Token: <Google ID Token>
```

2.  Frontend: Post to `/google/auth`, attach the token on the request body, type: form, structure: 
```
token= <Google ID Token>
```

3. Backend: Validate the token with Google OAuth API `verify_oauth2_token`, get the user information
``` 
{
"iss": "accounts.google.com",
"azp": "XXX",
"aud": "XXX",
"sub": "XXX",
"hd": "eficode.com",
"email": "XXX",
"email_verified": "true",
"at_hash": "XXX",
"name": "Ruiyang Ding",
"picture": "XXX",
"given_name": "Ruiyang",
"family_name": "Ding",
"locale": "en",
"iat": "1587038471",
"exp": "1587042071",
"jti": "XXX",
"alg": "XXX",
"kid": "XXX",
"typ": "JWT"
}
```
4. Backend: Generate JWT access token, the payload could contains email name return token in the son response
response format:
```
{
    'msg': '....',
    'auth_token': <JWT token>
}
```

5: Frontend:  When accessing to the backend API, attach `Authorization: Bearer <token>` on the header.

6: Backend: Verify the token, identify if the user has read/write right to the database.