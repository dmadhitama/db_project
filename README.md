# Test an API build and call

## Run the database using PGVector docker
Run this:
```bash
cd pgvector/
docker compose up -d
```

## Store a username to the database
To store a username to the database using `curl` to endpoint `/users/`:
```bash
curl -X POST http://127.0.0.1:8000/users/ \
     -H "Content-Type: application/json" \
     -d '{"usernames": "dom law"}'
```

To retrieve a username from its user id using `curl`:
```bash
curl -X GET http://127.0.0.1:8000/users/3

Result:
{"usernames":"dom law","id":3}
```

## Store a post to the database
To store a post to the database using `curl` to endpoint `/posts/`:
```bash
curl -X POST http://127.0.0.1:8000/posts/ \
     -H "Content-Type: application/json" \
     -d '{"title": "ABCD", "content": "Ini adalah abjad", "user_id": 22}'
```

To retrieve a username from its user id using `curl`:
```bash
curl -X GET http://127.0.0.1:8000/posts/1

Result:
{"title":"ABCD","content":"Ini adalah abjad","user_id":2,"id":1}
```

### Detailed description
It is possible to check the detailed of API request parameters using endpoints `/docs` using Swagger documentation and run the API request using it.