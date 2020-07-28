from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
# Create your models here.


#CALLED WHEN THE USER MAKES A POST
class Post(models.Model):
    author = models.ForeignKey('auth.User') #CONNECTS WITH SUPER USER ON SITE
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    #METHODS IN POST
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return  self.comments.filter(approved_comment=True)

    # FUNCTION GETS CALLED WHEN A POST IS MADE
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return  self.title

#CALLED WHEN THE USER MAKES A COMMENT UNDER A POST
class Comment(models.Model):
    post = models.ForeignKey('blog.Post',related_name = 'comments') #LINKED TO POST BY FK
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    #METHODS IN COMMENT
    def approve(self):
        self.approved_comment = True
        self.save()
    #FUNCTION GETS CALLED WHEN A COMMENT IS MADE
    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text