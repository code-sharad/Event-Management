from django.db import models
from ninja import Schema
from datetime import date
from enum import Enum
from typing import Optional,List
from ninja import ModelSchema
from ..models.user import UserOut
from ..models.venue import VenueOut
from datetime import datetime

class EventStatus(str, Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    CANCELLED = "cancelled"


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[(status.value,status.name) for status in EventStatus],
        default=EventStatus.DRAFT
    )
  
    # organizer = models.ForeignKey(
    #     Venue
    # )

class EventInSchema(Schema):
    title: str
    description: str
    start_date: date
    end_date: date
    status: str
    # created_at: date


class EventOut(ModelSchema):
    """Detailed event response schema"""
    # organizer: UserOut
    # venue: Optional[VenueOut] = None
    created_at: datetime
    
    class Meta:
        model = Event
        fields = [
            "id", 
            "title", 
            "description", 
            "start_date", 
            "end_date", 
            "status",
        ]

