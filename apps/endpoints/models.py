from django.db import models

# Create your models here.
class Endpoints(models.Model):
    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

class MLAlgorithm(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=500000)
    description = models.CharField(max_length=128)
    version = models.CharField(max_length=128)
    parent_endpoint = models.ForeignKey(Endpoints, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

class MLRequest(models.Model):
    input_data = models.CharField(max_length=1000000)
    response = models.CharField(max_length = 1000000, default='SOME STRING')
    full_response = models.CharField(max_length=1000000)
    created_date = models.DateField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE)

class MLAlgorithm_Status(models.Model):
    status = models.CharField(max_length=128, default='')
    active = models.BooleanField()
    created_date = models.DateField(auto_now_add=True, blank=True)
    user = models.CharField(max_length=128)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE, related_name="status")

    
