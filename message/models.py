from django.db import models
from django.utils import timezone


class Message(models.Model):

    # author = models.CharField(max_length=200)
    # dogowner_id = models.ForeignKey('daycare', on_delete = models.CASCADE)
    # daycare_id = models.ForeignKey('daycare', on_delete = models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    Message_Reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='parent')

    def get_children(self):
        return Message.objects.filter(Message_Reply=self)
