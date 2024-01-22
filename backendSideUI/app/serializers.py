from rest_framework import serializers
from app.models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking 
        fields=(
            'name',
            'email',
            'phone',
            'email',
            'gender'
        )
