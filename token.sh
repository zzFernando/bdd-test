curl -X POST \
   -H 'Content-Type: application/json' \
   -d '{ "username":"fernandosdba@gmail.com", "password":"94084452", "rememberMe":"true" }' \
   'https://api.withleaf.io/api/authenticate'

echo {"id_token":"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJmZXJuYW5kb3NkYmFAZ21haWwuY29tIiwiYXV0aCI6IlJPTEVfVVNFUiIsImV4cCI6MTYyMDYwMTk4NX0.q-VJgbQhi8zeQ_guwHaaAuvAVo96qaKCKC9NwljfXcezuz8fFQjn28Cy3YMH9Ep08QbBVoiKj51mXwP_oYyrAw"}                                                                                                                               