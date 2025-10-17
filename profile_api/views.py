from django.http import JsonResponse
from datetime import datetime
import requests

def profile(request):
    """
    return profile data and some random cat fact from an
    external API which outputs an error in the cat_errors.log if
    the API is down
    """
    time = datetime.utcnow().isoformat()
    fact = {"fact": "unable to fetch random cat fact due to an error"}
    try:
        response = requests.get("https://catfact.ninja/fact")
        fact = response.json()
    except Exception as e:
        with open("cat_errors.log", "a") as f:
            f.write(f"ERROR: {e}")

    return JsonResponse(
        {
            "status": "success",
            "user": {
                "email": "pascalswe01@gmail.com",
                "name": "Pascal Ndubi",
                "stack": "Python / Django"
            },
            "timestamp": f"{time}",
            "fact": f"{fact["fact"]}"
        }
    )
