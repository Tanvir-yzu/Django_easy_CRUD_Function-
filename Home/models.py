from django.db import models

# Create your models here.
class baseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class companyInformation(baseModel):
    name = models.CharField(max_length=255, verbose_name="Company Name")
    email = models.EmailField(max_length=255, verbose_name="Company Email")
    phone = models.CharField(max_length=255, verbose_name="Company Phone")
    address = models.CharField(max_length=255, verbose_name="Company Address")
    city = models.CharField(max_length=255, verbose_name="Company City")
    country = models.CharField(max_length=255, verbose_name="Company Country")
    website = models.CharField(max_length=255, verbose_name="Company Website")
    industry = models.CharField(max_length=255, verbose_name="Company Industry")
    employee_count = models.CharField(max_length=255, verbose_name="Company Employee Count")
    description = models.TextField(verbose_name="Company Description")
    logo = models.ImageField(upload_to='media/', verbose_name="Company Logo")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Company Information"
        verbose_name_plural = "Company Information"
