# Generated by Django 5.1.5 on 2025-01-31 18:41

import django.core.validators
import django.db.models.deletion
import eventApp.models.event
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('draft', 'DRAFT'), ('published', 'PUBLISHED'), ('cancelled', 'CANCELLED')], default=eventApp.models.event.EventStatus['DRAFT'], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('attendee', 'ATTENDEE'), ('organizer', 'ORGANIZER'), ('admin', 'ADMIN')], default=['attendee'], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='TicketType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the ticket type (e.g., VIP)', max_length=100)),
                ('price', models.CharField(help_text='Price per ticket', max_length=10)),
                ('quantity_available', models.PositiveIntegerField(help_text='Total tickets available for sale')),
                ('sale_start', models.DateTimeField(help_text='Start time of ticket sales')),
                ('sale_end', models.DateTimeField(help_text='End time of ticket sales')),
                ('event', models.ForeignKey(help_text='Event this ticket type belongs to', on_delete=django.db.models.deletion.CASCADE, related_name='ticket_types', to='eventApp.event')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Official name of the venue', max_length=255)),
                ('address', models.TextField(help_text='Full physical address of the venue')),
                ('capacity', models.PositiveIntegerField(help_text='Maximum number of attendees allowed', validators=[django.core.validators.MinValueValidator(1)])),
                ('amenities', models.TextField(blank=True, help_text='Comma-separated list of amenities (e.g., WiFi, Parking, Projector)', null=True)),
                ('contact_phone', models.CharField(blank=True, help_text='Primary contact phone number', max_length=20)),
                ('contact_email', models.EmailField(blank=True, help_text='Primary contact email address', max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Timestamp of venue creation')),
            ],
            options={
                'verbose_name': 'Venue',
                'verbose_name_plural': 'Venues',
                'ordering': ['name'],
                'indexes': [models.Index(fields=['name'], name='eventApp_ve_name_762e18_idx'), models.Index(fields=['capacity'], name='eventApp_ve_capacit_574c81_idx')],
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('active', 'ACTIVE'), ('used', 'USED'), ('cancelled', 'CANCELLED')], default='active', help_text='Current status of the ticket (e.g., active, used)', max_length=10)),
                ('code', models.CharField(blank=True, help_text='Unique ticket code (e.g., QR code identifier)', max_length=20, unique=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventApp.event')),
                ('ticket_type', models.ForeignKey(help_text='Type of ticket (e.g., VIP, General Admission)', on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='eventApp.tickettype')),
                ('user', models.ForeignKey(help_text='User who purchased the ticket', on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='eventApp.user')),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Tickets',
                'indexes': [models.Index(fields=['code'], name='eventApp_ti_code_7a1ad9_idx'), models.Index(fields=['status'], name='eventApp_ti_status_5ce4ec_idx')],
            },
        ),
    ]
