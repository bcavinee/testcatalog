from django.db import models



class Test_Information(models.Model):

	test_name= models.CharField(max_length=100)
	synonym= models.CharField(max_length=200,default="")
	eap= models.CharField(max_length=250,default="")
	labs= models.CharField(max_length=250,default="")
	methodology= models.CharField(max_length=300,default="")
	instrument= models.CharField(max_length=250,default="")
	units= models.CharField(max_length=250,default="")
	reference_range= models.CharField(max_length=1000,default="")
	critical_values= models.CharField(max_length=1000,default="")
	source_of_reference_range= models.CharField(max_length=2000,default="")
	amr= models.CharField(max_length=25,default="")
	reportable_range= models.CharField(max_length=2000,default="")
	appropriate_tubetype= models.CharField(max_length=2000, default="")
	room_temp_stability= models.CharField(max_length=2000, default="")
	refrigerated_stability=models.CharField(max_length=2000,default="")
	outreach_notes= models.CharField(max_length=2000,default="")
	special_instructions= models.CharField(max_length=2000,default="")
	avaliability= models.CharField(max_length=2000,default="")
	subdiscipline= models.CharField(max_length=2000,default="")		
	profciency_testing= models.CharField(max_length=2000,default="")		
	primary_instrument= models.CharField(max_length=2000,default="")		
	complexity= models.CharField(max_length=2000,default="")		
	regulated_analyte= models.CharField(max_length=2000,default="")		
	cpt_codes= models.CharField(max_length=2000,default="")		




	def __str__(self):
		return self.test_name	

