from flask import request
import jwt
# This is for saving team scores and shit after quiz completion
# Endpoint: /api/quiz/score
# Type: POST
# Auth: JWT (Handled by login module)
# Request JSON Payload:
# {
#   "score": 8,   // integer — number of correct answers
#   "total": 10   // integer — always 10
# }
# Output/Sent JSON Payload:
# { "message": "Score saved" }
# Authorization: Bearer <token> to be used.
# Let the secret key also be here. I'll implement it as it should be once this shit actually works.
SECRET_KEY = "I don't know what the hell to put here"

def decodejwt(token):
    originalpayload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    return originalpayload

def team_score(payload):
    auth_header = request.headers.get("Authorization") # Extracting the Authorization Header
    if auth_header != None:
        token = auth_header.split(" ")[1]  # strip "Bearer "
    else:
        token = None
    