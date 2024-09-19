from django.db import models
from User.models import User
class Blog(models.Model):
    owner =models.ForeignKey(User,on_delete=models.CASCADE,related_name="blogModel")
    title=models.CharField(max_length=200,blank=False,null=False, unique=True)
    summary=models.TextField(blank=False,null=False)
    context=models.TextField(blank=False,null=False)
    category = models.TextField(blank=False,null=False)  #jsonfield veya yeni model kullanılabilir
    is_active =models.BooleanField(default=True)
    isGenByAi=models.BooleanField(default=False)
    keywords=models.TextField(blank=False,null=False)   
    IsDeleted=models.BooleanField(default=False)    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural='Blogs'

    def __str__(self):
        return str(self.title)