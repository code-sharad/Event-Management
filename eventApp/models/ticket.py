from django.db import models
from ninja import Schema
from enum import Enum
from .user import User,UserOut,UserIn
from .event import Event,EventOut
from ninja import ModelSchema
from datetime import datetime

class TicketStatus(str, Enum):
    ACTIVE = "active"    # Ticket is valid
    USED = "used"        # Ticket has been checked in
    CANCELLED = "cancelled"  # Ticket was refunded/voided

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='tickets',help_text="User who purchased the ticket")
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=[(status.value, status.name) for status in TicketStatus],
        default=TicketStatus.ACTIVE.value,
        help_text="Current status of the ticket (e.g., active, used)"
    )

    ticket_type = models.ForeignKey(
        "TicketType", 
        on_delete=models.CASCADE, 
        related_name="tickets", 
        help_text="Type of ticket (e.g., VIP, General Admission)"
    )
    code = models.CharField(
        max_length=20, 
        blank=True, 
        help_text="Unique ticket code (e.g., QR code identifier)"
    )
    def __str__(self):
        return f"Ticket #{self.id} - {self.user.email} ({self.ticket_type.name})"

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
        indexes = [
            models.Index(fields=["code"]),  # Faster lookups by ticket code
            models.Index(fields=["status"]),
        ]


class TicketType(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the ticket type (e.g., VIP)")
    price = models.CharField(max_length=10, help_text="Price per ticket")
    quantity_available = models.PositiveIntegerField(help_text="Total tickets available for sale")
    sale_start = models.DateTimeField(help_text="Start time of ticket sales")
    sale_end = models.DateTimeField(help_text="End time of ticket sales")
    event = models.ForeignKey(
        "Event", 
        on_delete=models.CASCADE, 
        related_name="ticket_types", 
        help_text="Event this ticket type belongs to"
    )

    def __str__(self):
        return f"{self.name} - {self.event.title}"




class TicketTypeIn(Schema):
    name: str
    price: str
    quantity_available: int
    sale_start: datetime
    sale_end: datetime
    event_id: int

class TicketTypeOut(Schema):
    """Essential ticket type info for responses"""
    id: int
    name: str
    quantity_available: int
    price: str
    sale_start: datetime
    sale_end: datetime
    event: EventOut

class TicketIn(Schema):
    user_id: int
    event_id: int
    status: str
    ticket_type_id: int

# class TicketOut(Schema):
#     id:int
#     user_id: UserIn
#     event_id: EventOut
#     status: str
#     ticket_type_id: TicketTypeOut

class TicketCreate(Schema):
    """Schema for ticket purchase requests"""
    ticket_type_id: int

class TicketOut(ModelSchema):
    """Full ticket details with relationships"""
    user: UserOut
    event: EventOut
    ticket_type: TicketTypeOut
    code: str
    # purchase_date: datetime
    
    class Meta:
        model = Ticket
        fields = [
            "id",
            "status",
            "code"
        ]