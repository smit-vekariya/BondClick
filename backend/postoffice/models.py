from django.db import models

# Create your models here.

STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('draft', 'Draft'),
    ('sent', 'Sent'),
    ('failed', 'Failed'),
)

class EmailLog(models.Model):
    mail_from = models.EmailField()
    mail_to = models.TextField()
    mail_cc = models.CharField(max_length=1000) #cc mail limit 3
    mail_bcc = models.CharField(max_length=1000) #bcc mail limit 3
    subject = models.CharField(max_length=500)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    error_message = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # if self.status == 'pending':
        #     send_email_task.delay(self.id)

    def __str__(self):
        return self.mail_subject
