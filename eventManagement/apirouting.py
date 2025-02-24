from ninja import NinjaAPI


from eventApp.views.api_event import eventRouter
from eventApp.views.api_user import userRouter
from eventApp.views.api_ticket import ticketRouter
from eventApp.views.api_venue import venueRouter

from ninja import NinjaAPI
# from ninja.security import HttpBearer
# from django.middleware.csrf import get_token

api = NinjaAPI(title="Event API",openapi_extra={"servers": [{"url": "/api"}],"externalDocs": {
            "description": "Find out more about Swagger",
            "url": "http://swagger.io"
        }, "license":[
           { "name": "Apache 2.0",
            "url": "http://www.apache.org/licenses/LICENSE-2.0.html"}
        ],"tags": [ {"name": "Event","description": "Event operations"},{"name": "User","description": "User operations"},{"name": "Ticket","description": "Ticket operations"},{"name": "Venue","description": "Venue operations"}]}, version="1.0.0")




# @api.get('/set-csrf-token')
# def get_csrf_token(request):
#     return {'csrf_token':get_token(request)}

api.add_router("/event/",eventRouter)
api.add_router("/user/",userRouter)
api.add_router('/ticket/',ticketRouter)
api.add_router('/venue/',venueRouter)
