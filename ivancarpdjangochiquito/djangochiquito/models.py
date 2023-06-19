import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

class Question(models.Model):
    """
    ``Attributes:``
        -question_text(CharField):Text that is stored in the database in the question area
            - Max 200 chars,
        -pub_date(DateTimeField):almacenar la fecha y hora de publicación de algún contenido en el modelo correspondiente 
    """
    
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        """
         Returns:
            (str):returns the value of the object's "question_text" attribute.
        """
        return self.question_text

    def was_published_recently(self):
        """
        Returns:
                (boolean):El decorador @admin.display en Django ofrece opciones de visualización adicionales en la interfaz de administración. Con boolean=True, el campo se mostrará como un valor booleano. El parámetro ordering="pub_date" indica que el modelo se ordenará según el campo pub_date.
        """
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        """
        Returns:
                (boolean):The `was_published_recently(self)` method compares the `pub_date` attribute of the object with a time range of the last 24 hours. If it is within the range, it returns `True`; otherwise, it returns `False`. Use `timezone.now()` to get the current time and `datetime.timedelta(days=1)` to subtract 1 day.
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    


class Choice(models.Model):
    """
    ``Attributes:``
        -question(ForeignKey):The line of code defines a foreign key field called question in a model. It is specified that if the related question is deleted, the current object will also be cascaded.
        -choice_text(CharField):The line of code defines a text field named choice_text in a model. This field has a maximum length of 200 characters.
            -max_length:200
        -votes(IntegerField):The line of code defines a field called votes in a model. This field is an integer representing the number of votes and has a default value of 0.
            -default=0 
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        """
        return:
            (srt):defines the string representation of the object. Returns the value of the choice_text attribute, which is the text of a choice.
        
        """
        return self.choice_text
    def was_published_recently(self):
            """
            return
                (boolean):The was_published_recently(self) method checks if the object's pub_date attribute is within the range of the last 24 hours. Returns True if it is, and False otherwise.
            """
            now = timezone.now()
            return self.pub_date <= now and self.pub_date >= now - datetime.timedelta(days=1)
#Ejemplo mio de modelo creado ivan c,s
class BuenasPracticas(models.Model):
    """
    ``Attributes:``
        -nombre(CharField):that represents the name of the best practice.
            -max_length=100
        -descripcion(TextField):that represents the description of the good practice.
        -fecha_creacion(DateTimeField):the current datetime when a new instance of the model is created.
            -auto_now_add=True
        -categoria(ForeignKey):a ForeignKey field that establishes a relationship with the 'Category' model. If the related category is deleted, it will be set to null instead of deleting the current object
            -null=True
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """
        return:
            (srt):returns the value of the name attribute as the string representation of the object.  
        """
        return self.nombre


class Categoria(models.Model):
    """
     ``Attributes:``
        -nombre(CharField):that represents the name of the category.
            -max_length=50
    """
    nombre = models.CharField(max_length=50)

    def __str__(self):
        """
        return:
            (srt):returns the value of the name attribute as the string representation of the object.  
        """
        return self.nombre
