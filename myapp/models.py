from django.db import models
from django.utils import timezone


class Tag(models.Model) :
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Score(models.Model) :
    score = models.PositiveSmallIntegerField(choices=((1,"1"),(2,"2"),(3,"3"),(4,"4"),(5,"5")))
    rater = models.ForeignKey('auth.User')
    rated_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s (%s)" %(self.score, self.rater)

class Post(models.Model) :
    author = models.ForeignKey('auth.User', verbose_name='author', related_name='posts')
    title = models.CharField(max_length=200)
    #picture = models.ImageField()
    text = models.TextField()
    public_post = models.BooleanField('public', default=True)
    published_date=models.DateTimeField(default=timezone.now)
    tags=models.ManyToManyField(Tag, blank=True)
    scores = models.ManyToManyField(Score, blank=True)

    def __str__(self):
        return self.title
