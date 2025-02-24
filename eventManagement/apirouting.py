from ninja import NinjaAPI


from eventApp.views.api_event import eventRouter
from eventApp.views.api_user import userRouter
from eventApp.views.api_ticket import ticketRouter
from eventApp.views.api_venue import venueRouter

from ninja import NinjaAPI
# from ninja.security import HttpBearer
# from django.middleware.csrf import get_token

api = NinjaAPI(title="Event API",openapi_extra={"info": {
            "license": {
                "name": "Apache 2.0",
                "url": "http://www.apache.org/licenses/LICENSE-2.0.html"
            }
        },"servers": [{"url": "/api"}],"externalDocs": {
            "description": "Find out more about Swagger",
            "url": "http://swagger.io"
        },"tags": [ {"name": "Event","description": "Event operations","externalDocs": {
        "description": "Find out more",
        "url": "http://swagger.io"
      }},{"name": "User","description": "User operations"},{"name": "Ticket","description": "Ticket operations","externalDocs": {
        "description": "Find out more",
        "url": "http://swagger.io"
      }},{"name": "Venue","description": "Venue operations","externalDocs": {
        "description": "Find out more",
        "url": "http://swagger.io"
      }}]}, version="1.0.0")


# @api.get('/set-csrf-token')
# def get_csrf_token(request):
#     return {'csrf_token':get_token(request)}

api.add_router("/event/",eventRouter)
api.add_router("/user/",userRouter)
api.add_router('/ticket/',ticketRouter)
api.add_router('/venue/',venueRouter)
