from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class UserDetail(models.Model):
	SEX_CHOICES = (("Male",'Male'),("Female",'Female'),("Other",'Other'))
	STATE_CHOICES = (
		("Githurai",'Githurai'),
		("Kahawa",'Kahawa'),
		("Ruiru",'Ruiru'),
		("Juja",'Juja'),
		("Kasarani",'Kasarani'),
		("Thika",'Thika'),
		("Kayole",'Kayole'),
		("Eastleigh",'Eastleigh'),
		("CBD",'CBD'),
		("Westlands",'Westlands'),
		("Kibera",'Kibera'),
		("Kayole",'Kayole'),

	
		)
	user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
	dob = models.DateField(null = True)
	photo = models.ImageField(default='default.png',upload_to='user_photos')
	mobile = models.CharField(max_length=10,null=True)
	alternate_mobile = models.CharField(max_length=10,null=True,blank=True)
	address = models.TextField()
	# pincode = models.CharField(max_length=6, null=True)
	landmark = models.CharField(max_length=500, null=True, blank=True)
	locality = models.CharField(max_length=100, null=True, blank=True)
	city = models.CharField(max_length=100, null=True, blank=True)
	area = models.CharField(max_length=50,choices=STATE_CHOICES, null=True)
	sex = models.CharField(max_length=6,choices=SEX_CHOICES, null=True)
        
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.photo.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.photo.path)

class Slider(models.Model):
	name = models.CharField(max_length=50, default = "", null=True)
	image = models.ImageField(upload_to='slider_img')
	url = models.CharField(max_length=200, default = "#", null=True)

	def __str__(self):
		return f'{self.name}'

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)
		if img.height > 1024 or img.width > 1024:
			output_size = (1024, 1024)
			img.thumbnail(output_size)
			img.save(self.image.path)


class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product_id = models.CharField(max_length=100)
	product_size = models.CharField(max_length=20,default='',null=True)
	number = models.PositiveIntegerField(default=0)

class Contact(models.Model):
	date = models.DateField(auto_now=True)
	name = models.CharField(max_length=100)
	email = models.EmailField()
	subject = models.CharField(max_length=100)
	message = models.TextField()
	
	def __str__(self):
		return self.email