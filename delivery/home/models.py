from django.db import models

# Create your models here.



class item(models.Model):
    ID        = models.IntegerField('id', primary_key=True, auto_created=True)
    name      = models.TextField('nombre', max_length=20)

    valor     = models.IntegerField('precio')
    fabricado = models.DateField('fab')
    valido    = models.DateField('val')
    imagen    = models.FileField('imagen', upload_to='static')

class car(models.Model):
    car_id = models.IntegerField('id', primary_key=True,auto_created=True)
    items  = models.ManyToManyField('item')
    date   = models.DateField('car date', auto_now_add=True)
    
    def __str__(self):
        return "$ " + str(self.car_id)

class onder(models.Model):
    order_id  = models.IntegerField('Order id', primary_key=True, auto_created=True)
    user_id   = models.IntegerField('user id')
    car       = models.ForeignKey('car', on_delete=models.CASCADE) 
    status    = models.BooleanField('estado')
    create_at = models.DateTimeField('creado',auto_now=True)    
   
    def __str__(self):
        return "# " + str(self.order_id)
    
    class Meta:
        verbose_name_plural = 'orders'