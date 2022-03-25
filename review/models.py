from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

class TravelReview(models.Model):

    RATINGS_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review_posts", null=True)
    content = models.TextField()
    travel_image = CloudinaryField('image', blank=True, default='https://res.cloudinary.com/legenduzair/image/upload/v1647465863/epic-expeditions/travel-placeholder_nx4cw2.jpg')
    excerpt = models.TextField(blank=True)
    published = models.DateField(auto_now_add=True)
    ratings = models.IntegerField(choices=RATINGS_CHOICES, default=0)
    likes = models.ManyToManyField(User, related_name='expedition_like', blank=True)

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return str(self.title)
    
    def no_of_likes(self):
        return self.likes.count()

class TravelComments(models.Model):

    post = models.ForeignKey(TravelReview, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
