from django.db import models
from ninja import Schema,ModelSchema
from django.core.validators import MinValueValidator
from typing import List,Optional
from datetime import datetime

class Venue(models.Model):
    name = models.CharField(
        max_length=255,
        help_text="Official name of the venue",
    )
    address = models.TextField(
        help_text="Full physical address of the venue"
    )
    capacity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Maximum number of attendees allowed"
    )
    amenities = models.TextField(
        blank=True,
        null=True,
        help_text="Comma-separated list of amenities (e.g., WiFi, Parking, Projector)"
    )
    contact_phone = models.CharField(
        max_length=20,
        blank=True,
        help_text="Primary contact phone number"
    )
    contact_email = models.EmailField(
        blank=True,
        help_text="Primary contact email address"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp of venue creation"
    )

    def __str__(self):
        return f"{self.name} ({self.address})"

    class Meta:
        verbose_name = "Venue"
        verbose_name_plural = "Venues"
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),  # Faster search by name
            models.Index(fields=["capacity"]),
        ]

    def get_amenities_list(self):
        """Convert comma-separated amenities to list"""
        return [a.strip() for a in self.amenities.split(",")] if self.amenities else []
    

class VenueOut(Schema):
    id: int
    name: str
    address: str
    capacity: int
    amenities: List[str]  # Converted from comma-separated string to list
    contact_phone: Optional[str]
    contact_email: Optional[str]
    created_at: datetime

    @staticmethod
    def resolve_amenities(obj):
        """Convert comma-separated amenities to a list."""
        return [a.strip() for a in obj.amenities.split(",")] if obj.amenities else []

class VenueFilter(Schema):
    name: Optional[str] = None
    min_capacity: Optional[int] = None
    max_capacity: Optional[int] = None
    amenities: Optional[str] = None  # Filter by specific amenities

class VenueCreate(Schema):
    name: str
    address: str
    capacity: int
    amenities: Optional[str] = None
    contact_phone:str
    contact_email: str

class VenueOut(ModelSchema):
    class Meta:
        model = Venue
        fields = ["id", "name", "address", "capacity"]