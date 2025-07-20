
from django.db import models
from django.conf import settings
import qrcode
from io import BytesIO
from django.core.files import File

class ParkingSlot(models.Model):
    station = models.CharField(max_length=100)
    slot_number = models.CharField(max_length=10)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.station} - {self.slot_number}"

class ParkingReservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    qr_code = models.ImageField(upload_to='qrcodes/', blank=True)
    status = models.CharField(max_length=20, default='active')

    def save(self, *args, **kwargs):
        # Generate QR code
        qr_data = f"Reservation: {self.user.username} | Slot: {self.slot.slot_number}"
        qr_img = qrcode.make(qr_data)
        canvas = BytesIO()
        qr_img.save(canvas, format='PNG')
        self.qr_code.save(f"qr_{self.id}.png", File(canvas), save=False)
        super().save(*args, **kwargs)


# Create your models here.
