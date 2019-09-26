from django.db import models

class todo_models(models.Model):
	task = models.CharField(max_length=40)
	complete = models.BooleanField(default=False)

	def __str__(self):
		return self.task
