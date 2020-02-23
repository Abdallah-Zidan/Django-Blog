from django.db import models
from django.db.models.signals import pre_save , post_delete
from django.dispatch import receiver
from django.template.defaultfilters import slugify

class Post(models.Model):
    title = models.CharField(max_length=50 , null= False , blank = False)
    body = models.TextField()
    #tags = models.ManyToManyField('Tag')
    #category = models.ForeignKey(Category, on_delete = models.DO_NOTHING)
    # user = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='../media' ,default="default.png",null=True , blank = True)
    date_published=models.DateTimeField(auto_now_add=True,verbose_name="date published")
    date_updated=models.DateTimeField(auto_now =True,verbose_name="date updated")
    img = models.SlugField(blank=True,unique=True)
    #comment = models.ManyToManyField
    class Meta:
        ordering = ('-date_published',)
    def __str__(self):
        return self.title
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url  

#delete img from file media within the post 
@receiver(post_delete,sender = Post) 
def submission_delete(sender, instance,**kwargs):
    instance.image.delete(False) 
#uncomment this block import user
def pre_save_post_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.Profile.username+"_"+instance.title) 

pre_save.connect(pre_save_post_receiver, sender=Post)        



