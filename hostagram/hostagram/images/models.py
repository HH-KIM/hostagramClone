from django.db import models
from hostagram.users import models as user_models
# Create your models here.


class TimeStampedModel(models.Model):
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        class Meta:
            abstract = True


class Image(TimeStampedModel):

        file = models.ImageField()
        location = models.CharField(max_length=140)
        caption = models.TextField()
        creator = models.ForeignKey(user_models.User, on_delete=models.PROTECT)


class Comment(TimeStampedModel):

    message = models.TextField()
    creator = models.ForeignKey(user_models.User, on_delete=models.PROTECT, null = True)
    image = models.ForeignKey(Image , on_delete=models.PROTECT, null = True)

class Like(TimeStampedModel):

    creator = models.ForeignKey(user_models.User , on_delete=models.PROTECT, null = True)
    image = models.ForeignKey(Image , on_delete=models.PROTECT, null = True)