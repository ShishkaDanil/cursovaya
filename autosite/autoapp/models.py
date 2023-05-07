from django.db import models

class CarClass(models.Model):
    name = models.CharField(max_length=100)
    deposit_amount = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        db_table = 'car_classes'
        
class Car(models.Model):
    class_type = models.ForeignKey(CarClass, on_delete=models.CASCADE)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    seats = models.IntegerField()
    doors = models.IntegerField()
    license_plate = models.CharField(max_length=20)
    has_ac = models.BooleanField()
    transmission = models.TextField(choices=[('ручная', 'ручная'), ('автоматическая', 'автоматическая')])
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.IntegerField()
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        db_table = 'cars'

class RentalAgreement(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, blank=True, null=True)
    passport_details = models.TextField()
    driver_license_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    actual_return_date = models.DateField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    rental_rate = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.IntegerField()
    class Meta:
        db_table = 'rental_agreements'
