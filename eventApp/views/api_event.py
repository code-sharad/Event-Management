from ninja import Router
from django.http import HttpResponse
from ..models.event import EventInSchema,Event,EventOut
from ..models.user import Error
from django.shortcuts import get_object_or_404

# from ninja.security import django_auth
eventRouter = Router()


@eventRouter.post("/create", response={201: EventOut, 403: Error},tags=["event"],description="Create a new event")
def create_event(request, payload: EventInSchema):
    # if request.auth.role not in ["organizer", "admin"]:
        # return 403, {"error": "Permission denied"}
    event = Event.objects.create(**payload.dict())
    return 201, event


@eventRouter.get("/events", response=list[EventOut],tags=["event"],description="List all events")
def list_events(request, status: str = None):
    print(request)
    queryset = Event.objects.all()  
    print(queryset)
    if status:      
        queryset = queryset.filter(status=status)
    return queryset

@eventRouter.get("/events/{event_id}", response=EventOut,tags=["event"],description="Get a single event")
def get_event(request, event_id: int):
    return Event.objects.get(id=event_id)


@eventRouter.delete("/events/{event_id}", response={200: dict},tags=["event"],description="Delete an event")
def delete_event(request,event_id:int):
    e =  get_object_or_404(Event,id=event_id)
    e.delete()
    return {'success':True}
