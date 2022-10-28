from tokenize import String
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def home(request, *args, **kwargs):
    name = "Augustine"
    backend = True
    age = 25
    bio = "My name is Augustine and i love hannah"

    return Response(
        {
        "SlackUsername":name,
        "backend": backend,
        "Age": age,
        "Bio": bio,
        }
        
    )
        
    