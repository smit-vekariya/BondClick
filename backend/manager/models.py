from django.db import models
import logging
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from account.models import BondUser

# Create your models here.
LOG_LEVELS = (
    (logging.INFO, _("info")),
    (logging.WARNING, _("warning")),
    (logging.DEBUG, _("debug")),
    (logging.ERROR, _("error")),
    (logging.FATAL, _("fatal")),
)

# Create your models here.
class ErrorBase(models.Model):
    class_name = models.CharField(_("type"), max_length=128, blank=True, null=True, db_index=True)
    level = models.PositiveIntegerField(choices=LOG_LEVELS, default=logging.ERROR, blank=True, db_index=True)
    message = models.TextField()
    traceback = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)


action_types =(
    ("insert", "Insert"),
    ("update", "Update"),
    ("delete", "Delete"),
    ("error", "Error")
)
class History(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id =  models.IntegerField(null=True, blank=True)
    action = models.TextField()
    action_type = models.CharField(max_length=100, choices=action_types, null=True, blank=True)
    ip_addr = models.CharField(default="", max_length=45)
    action_on = models.DateTimeField(auto_now=True)
    action_by = models.ForeignKey(BondUser, on_delete=models.PROTECT)
