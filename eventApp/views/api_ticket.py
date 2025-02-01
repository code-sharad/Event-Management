from ninja import Router

from ..models.ticket import TicketType,TicketTypeOut,TicketTypeIn,TicketIn,Ticket,TicketOut
from ..models.event import Event
from ..models.user import User
from typing import List
from ninja.security import django_auth
import random

ticketRouter = Router()



@ticketRouter.post('/book-ticket',response=TicketOut)
def bookTicket(request,payload:TicketIn):
    user = User.objects.get(id=payload.user_id)
    event = Event.objects.get(id=payload.event_id)
    ticktType = TicketType.objects.get(id=payload.ticket_type_id)
    if user and event and ticktType:
        random_number = ''.join(random.choices('0123456789', k=8))
        print(random_number)
        ticket = Ticket.objects.create(**payload.dict())
        ticket.event = event
        ticket.user = user
        ticket.code = random_number
        ticket.save()
        return ticket
    else:
        return {'success':'false'}
    

@ticketRouter.get('/list',response=List[TicketOut],auth=django_auth)
def getTicketList(request):
    return Ticket.objects.select_related('user','event').all()


@ticketRouter.post('/type',response=TicketTypeOut)
def createTicketType(request,payload:TicketTypeIn):
    event = Event.objects.get(id=payload.event_id)
    ticket = TicketType.objects.create(**payload.dict())
    ticket.event = event
    return ticket

@ticketRouter.get('/type/list',response=List[TicketTypeOut])
def getTicketTypes(request):
    return TicketType.objects.all()

# @ticketRouter.get('/type/{event_id}',response=list[TicketTypeOut])
# def getTicketTypes(request,event_id:int):
#     event = Event.objects.get(id=event_id)
#     return event.tickettype_set.all()

@ticketRouter.delete('/{ticket_id}')
def deleteTicket(request,ticket_id):
   ticket =  Ticket.objects.get(id=ticket_id)
   ticket.delete()
   return {'success':'true'}
    

@ticketRouter.delete('/type/{ticket_id}')
def deleteTicketType(request,ticket_id:int):
    ticket = TicketType.objects.get(id=ticket_id)
    ticket.delete()
    return {'success':True}

