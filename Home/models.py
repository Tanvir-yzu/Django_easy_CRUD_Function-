from django.db import models

# Create your models here.
class baseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class CompanyInformation(baseModel):
    name = models.CharField(max_length=255, verbose_name="Company Name")
    email = models.EmailField(max_length=255, verbose_name="Company Email")
    phone = models.CharField(max_length=255, verbose_name="Company Phone", blank=True, null=True)
    address = models.CharField(max_length=255, verbose_name="Company Address", blank=True, null=True)
    city = models.CharField(max_length=255, verbose_name="Company City", blank=True, null=True)
    country = models.CharField(max_length=255, verbose_name="Company Country", blank=True, null=True)
    website = models.URLField(max_length=255, verbose_name="Company Website", blank=True, null=True)
    industry = models.CharField(max_length=255, verbose_name="Company Industry", blank=True, null=True)
    employee_count = models.CharField(max_length=255, verbose_name="Company Employee Count", blank=True, null=True)
    description = models.TextField(verbose_name="Company Description", blank=True, null=True)
    logo = models.ImageField(upload_to='media/', verbose_name="Company Logo", blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Company Information"
        verbose_name_plural = "Company Information"

class Employee(baseModel):
    DEPARTMENT_CHOICES = [
        ('HR', 'Human Resources'),
        ('IT', 'Information Technology'),
        ('FINANCE', 'Finance'),
        ('MARKETING', 'Marketing'),
        ('SALES', 'Sales'),
        ('OPERATIONS', 'Operations'),
        ('ENGINEERING', 'Engineering'),
        ('SUPPORT', 'Customer Support'),
        ('ADMIN', 'Administration'),
        ('OTHER', 'Other'),
    ]
    
    EMPLOYMENT_STATUS = [
        ('FULL_TIME', 'Full Time'),
        ('PART_TIME', 'Part Time'),
        ('CONTRACT', 'Contract'),
        ('INTERN', 'Intern'),
        ('FREELANCE', 'Freelance'),
    ]
    
    company = models.ForeignKey(CompanyInformation, on_delete=models.CASCADE, related_name='employees', verbose_name="Company")
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    email = models.EmailField(max_length=255, verbose_name="Employee Email", unique=True)
    phone = models.CharField(max_length=20, verbose_name="Phone Number", blank=True, null=True)
    employee_id = models.CharField(max_length=50, verbose_name="Employee ID", unique=True)
    position = models.CharField(max_length=100, verbose_name="Job Position")
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES, verbose_name="Department")
    employment_status = models.CharField(max_length=20, choices=EMPLOYMENT_STATUS, default='FULL_TIME', verbose_name="Employment Status")
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Salary", blank=True, null=True)
    hire_date = models.DateField(verbose_name="Hire Date")
    birth_date = models.DateField(verbose_name="Birth Date", blank=True, null=True)
    address = models.TextField(verbose_name="Address", blank=True, null=True)
    emergency_contact = models.CharField(max_length=100, verbose_name="Emergency Contact", blank=True, null=True)
    emergency_phone = models.CharField(max_length=20, verbose_name="Emergency Phone", blank=True, null=True)
    profile_picture = models.ImageField(upload_to='employees/', verbose_name="Profile Picture", blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    notes = models.TextField(verbose_name="Notes", blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        ordering = ['last_name', 'first_name']
