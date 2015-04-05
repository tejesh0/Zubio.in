from django.db import models
from django.forms import ModelForm
from django.core.validators import RegexValidator

# Create your models here.

CHOICE_BOOL = (
	('Yes','Yes'),
	('No','No')
)
CHOICE_CATEGORY = (
	('Gym','Gym'),
	('Spa', 'Spa'),
	('Yoga Center', 'Yoga Center'),
	('Salon', 'Salon')
)

class FitnessListing(models.Model):
	Name_Of_The_Fitness_Center = models.CharField(max_length=10, default="")
	Choose_Fitness_Center_category = models.CharField(max_length=20,choices=CHOICE_CATEGORY, default='Gym')
	Address = models.CharField(max_length=500)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'")
	phone_number = models.CharField(default="",max_length=20,validators=[phone_regex])
	Email = models.EmailField(default="")
	Owners_Name = models.CharField(max_length=50, default="")

	#Timings


	#Pricing
	Monthly = models.CharField(max_length=10, default="")
	Quaterly = models.CharField(max_length=10, default="")
	Half_yearly = models.CharField(max_length=10, default="")
	Yearly = models.CharField(max_length=10, default="")

	Membership = models.CharField(max_length=4, choices=CHOICE_BOOL, default='No')
	AC = models.CharField(max_length=4, choices=CHOICE_BOOL, default='No')
	WiFi = models.CharField(max_length=4, choices=CHOICE_BOOL, default='No')
	Locker = models.CharField(max_length=4, choices=CHOICE_BOOL, default='No')
	Parking = models.CharField(max_length=4, choices=CHOICE_BOOL, default='No')
	Personal_Trainer = models.CharField(max_length=4, choices=CHOICE_BOOL, default='No')
	Certified_Trainer = models.CharField(max_length=4, choices=CHOICE_BOOL, default='No')
	Description = models.TextField()
	Gallery = models.FileField(upload_to='documents/%Y/%m/%d')


	def __unicode__(self):
		return self.fit_name

class FitnessListingForm(ModelForm):
	class Meta:
		model = FitnessListing
		fields = '__all__'

