from django.db import models
# from django.contrib.auth.models import AbstractUser

# Create your models here.
# class CustomUser(AbstractUser):
#     User_id = models.AutoField
#     User_name = models.CharField(max_length=50, default="")
#     User_contact_number = models.CharField(max_length=50, default="")
#     User_join_date = models.DateField()
#     profile_picture = models.ImageField(upload_to='Ex_Routines/userprofile', null=True, blank=True)

#     def __str__(self):
#         return self.User_name
    
class ex_routines(models.Model):
    routine_id = models.AutoField
    routine_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    # price = models.IntegerField(default=0)
    desc = models.CharField(max_length=1000)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='Ex_Routines/images', default="")
    step1_image = models.ImageField(upload_to='Ex_Routines/step1', default="")
    step2_image = models.ImageField(upload_to='Ex_Routines/step2', default="")
    step3_image = models.ImageField(upload_to='Ex_Routines/step3', default="")
    step4_image = models.ImageField(upload_to='Ex_Routines/step4', default="")
    step5_image = models.ImageField(upload_to='Ex_Routines/step5', default="")
    step6_image = models.ImageField(upload_to='Ex_Routines/step6', default="")

    def __str__(self):
        return self.routine_name
    
class CalorieEntry(models.Model):
    calories_consumed = models.FloatField()
    time = models.TimeField()
    date = models.DateField()

    def __str__(self):
        return f'{self.calories_consumed} calories on {self.date} at {self.time}'
    
class CaloriesBurned(models.Model):
    time = models.TimeField()
    date = models.DateField()
    weight = models.FloatField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    exercise_type = models.CharField(max_length=255)
    duration_minutes = models.IntegerField()
    
    def __str__(self):
        return self.weight
    
class LoginPageSettings(models.Model):
    background_image = models.ImageField(upload_to='loginPage/')
    login_video = models.FileField(upload_to='loginPage/')
    
    # def calculate_calories_burned(self):
        # Constants for Harris-Benedict equation
        # BMR_MALE = 88.362
        # BMR_FEMALE = 447.593
        # ACTIVITY_FACTOR = {
        #     'sedentary': 1.2,
        #     'light': 1.375,
        #     'moderate': 1.55,
        #     'active': 1.725,
        #     'very_active': 1.9,
        # }

        # # Determine BMR based on gender
        # if self.gender == 'M':
        #     bmr = BMR_MALE + (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.age)
        # else:
        #     bmr = BMR_FEMALE + (9.247 * self.weight) + (3.098 * self.height) - (4.330 * self.age)

        # # Calculate calories burned by multiplying BMR with activity factor and duration
        # calories_burned = bmr * ACTIVITY_FACTOR.get(self.exercise_type, 1.0) * (self.duration_minutes / 60.0)

        # return calories_burned
# class Product(models.Model):
#     routine_id = models.AutoField
#     routine_name = models.CharField(max_length=50)
#     category = models.CharField(max_length=50, default="")
#     subcategory = models.CharField(max_length=50, default="")
#     price = models.IntegerField(default=0)
#     desc = models.CharField(max_length=300)
#     pub_date = models.DateField()
#     image = models.ImageField(upload_to='Ex_Routines/images', default="")

#     def __str__(self):
#         return self.product_name

# class Orders(models.Model):
#     order_id = models.AutoField(primary_key=True)
#     items_json = models.CharField(max_length=5000)
#     amount = models.IntegerField( default=0)
#     name = models.CharField(max_length=90)
#     email = models.CharField(max_length=111)
#     address = models.CharField(max_length=111)
#     city = models.CharField(max_length=111)
#     state = models.CharField(max_length=111)
#     zip_code = models.CharField(max_length=111)
#     phone = models.CharField(max_length=111, default="")

# class OrderUpdate(models.Model):
#     update_id  = models.AutoField(primary_key=True)
#     order_id = models.IntegerField(default="")
#     update_desc = models.CharField(max_length=5000)
#     timestamp = models.DateField(auto_now_add=True)

    # def __str__(self):
    #     return self.update_desc[0:7] + "..."