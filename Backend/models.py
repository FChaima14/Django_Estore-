from django.db import models
from django.contrib.auth.models import User
# Create your models here.
CATEGORY_CHOICES=(
    ('S', 'Shoeses'),
    ('SW', 'Sport'),
    ('Ow', 'Outwear'),
    ('W', 'Watches'),
    ('C', 'Causal'),
    ('H', 'Huts'),

)
LABEL_CHOICES=(
    ('p', 'primary'),
    ('S', 'secondary'),
    ('d', 'danger')
)
class Customer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True);
    name=models.CharField(max_length=100, null=True);
    email=models.EmailField(null=True, blank=True);

    def __str__(self):
        return self.name;



class Product(models.Model):
    title=models.CharField(max_length=100);
    price=models.FloatField();
    rate=models.IntegerField(null=True, blank=True)
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, null=True, blank=True)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    digital=models.BooleanField(null=True, default=False);

    def __str__(self):
        return self.title;

    @property
    def imageURL(self):
        try:
            url= self.image.url;
        except:
            url= '';
        return url;



class Order(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True);
    order_Date=models.DateTimeField(auto_now_add=True);
    complete=models.BooleanField(default=False);
    transaction_id=models.CharField(max_length=100, null=True);

    def __str__(self):
        return str(self.id);

    @property
    def shipping(self):
        shipping=False;
        orderitems= self.orderitem_set.all();
        for i in orderitems:
            if i.product.digital == False:
                shipping=True;
        return shipping

    @property
    def getTotatlCart(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems]);
        return total

    @property
    def getItemCart(self):
        orderitems=self.orderitem_set.all();
        total=sum([item.quantity for item in orderitems]);
        return total
 

class OrderItem(models.Model):
    product=models.ForeignKey(Product, on_delete=models.SET_NULL, null=True);
    order=models.ForeignKey(Order, on_delete=models.SET_NULL, null=True);
    quantity=models.IntegerField(default=0, null=True, blank=True);
    date_added=models.DateTimeField(auto_now_add=True);

    @property
    def get_total(self):
        total=self.product.price *self.quantity
        return total;


class ShippingAddress(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True);
    order=models.ForeignKey(Order, on_delete=models.SET_NULL, null=True);
    adress=models.CharField(max_length=200, null=False);
    city=models.CharField(max_length=200, null=False);
    state=models.CharField(max_length=200, null=False);
    ZipCode=models.CharField(max_length=200, null=False);
    date_added=models.DateTimeField(auto_now_add=True);

    def __str__(self):
        return self.adress;


