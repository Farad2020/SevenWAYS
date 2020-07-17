from django.db import models
from multiselectfield import MultiSelectField
from django import forms

week_days = (
    ("Monday", "Понедельник"), ("Tuesday", "Вторник"), ("Wednesday", "Среда"), ("Thursday", "Четверг"),
    ("Friday", "Пятница"), ("Saturday", "Суббота"), ("Sunday", "Воскресенье"),
)

building_type = (
    ("Residential Buildings", "Residential Buildings"), ("Educational Buildings", "Educational Buildings"),
    ("Institutional Buildings", "Institutional Buildings"), ("Assembly Buildings", "Assembly Buildings"),
    ("Business Buildings", "Business Buildings"), ("Mercantile Buildings", "Mercantile Buildings"),
    ("Industrial Buildings", "Industrial Buildings"), ("Storage Buildings", "Storage Buildings"),
    ("Wholesale Establishments", "Wholesale Establishments"), ("Hazardous Buildings", "Hazardous Buildings"),
    ("Multi-Level Car Parking", "Multi-Level Car Parking"),
)

review_attitude = (
    ("Good", "Хорошо"), ("Tolerable", "Терпимо"), ("Impossible", "Невозможно"),
)

disability_type = (
    ("Wheelchair", "Коляска"), ("Powered Wheelchair", "Коляска С Электроприводом"), ("Cane Walker", "Трость"),
)


# Create your models here.
class Place(models.Model):
    place_name = models.CharField(max_length=1000)
    place_phone = models.CharField(default="", max_length=100, blank=True)
    place_address = models.TextField(default="", max_length=100, blank=True)
    place_building_type = MultiSelectField(choices=building_type, max_choices=1, default=None)
    place_email = models.CharField(default="", max_length=100, null=True, blank=True)


class WorkTime(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    working_days = MultiSelectField(choices=week_days, max_choices=7, default=None)
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)


class PlaceImages(models.Model):
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)
    place_img = models.ImageField(upload_to='places_imgs/', default='NULL')


class Review(models.Model):
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)
    reviewers_disability_type = MultiSelectField(choices=disability_type, max_choices=1, default=None)
    reviewers_attitude = MultiSelectField(choices=review_attitude, max_choices=1, default=None)
    reviewers_comment = models.TextField(default="", max_length=700)
    review_date = models.DateTimeField(auto_now_add=True)

