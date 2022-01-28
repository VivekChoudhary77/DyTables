from pickle import TRUE
from django.db import models

# Create your models here.


class UserTables(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    table_name = models.CharField(unique=TRUE, max_length=60, null=False)
    actual_table_name = models.CharField(max_length=100)
    table_schema = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user_table"


class SavedFilter(models.Model):
    id = models.AutoField(primary_key=True)
    column = models.CharField(max_length=25)
    filter_type = models.CharField(max_length=25)
    value = models.CharField(max_length=25)
    table_id = models.ForeignKey(
        UserTables, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class AuditHistory(models.Model):
    id = models.AutoField(primary_key=True)
    update_type = models.CharField(max_length=25)
    row_data = models.CharField(max_length=500)
    table_id = models.ForeignKey(
        UserTables, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
