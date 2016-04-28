from django.db import models

class Ehr1(models.Model):
	name = models.CharField("Full name",max_length = 50)
	why = models.TextField("Why did you come in today?")
	when = models.TextField("When did this problem begin?")
	medication = models.CharField("what are the medications that you are taking now?", max_length = 100)
	allergic = models.CharField("Are you allergic to anything?",max_length = 50)
	highBloodPressure = models.BooleanField("I or anyone in my family have high blood pressure",default=False)
	heartDisease = models.BooleanField("I or anyone in my family have heart disease",default=False)
	diabetes = models.BooleanField("I or anyone in my family have diabetes",default=False)
	thyroid = models.BooleanField("I or anyone in my family have thyroid",default=False)
	cancer = models.BooleanField("I or anyone in my family have cancer",default=False)
	highCholesterol = models.BooleanField("I or anyone in my family have heart high cholesterol",default=False)
	appointmentDate = models.DateTimeField("when do you want to get the appointment?",default=False)	
	def __str__(self):
	    return self.name
