from ninja import Router,Query
from ..models.venue import Venue,VenueCreate,VenueOut,VenueFilter
from typing import List
venueRouter = Router()

@venueRouter.post("/create", response=VenueOut)
def create_venue(request, payload: VenueCreate):
    venue = Venue.objects.create(**payload.dict())
    return venue

@venueRouter.get('/list',response=List[VenueOut])
def get_venue_list(request):
    venue = Venue.objects.all();
    return venue;


# Get a single venue
@venueRouter.get("/id={venue_id}", response=VenueOut)
def get_venue(request, venue_id: int):
    venue = Venue.objects.get(id=venue_id)
    return venue


# List venues with filtering

# http://localhost:8000/api/venue/venues/?min_capacity=1000&amenities=WiFi 
@venueRouter.get("/venues/", response=list[VenueOut])
def list_venues(request, filters: VenueFilter = Query(...)):
    queryset = Venue.objects.all()
    if filters.name:
        queryset = queryset.filter(name__icontains=filters.name)
    if filters.min_capacity:
        queryset = queryset.filter(capacity__gte=filters.min_capacity)
    if filters.max_capacity:
        queryset = queryset.filter(capacity__lte=filters.max_capacity)
    if filters.amenities:
        queryset = queryset.filter(amenities__icontains=filters.amenities)
    return queryset