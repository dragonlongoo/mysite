from __future__ import unicode_literals

from django.db import models
# Create your models here.

class Project(models.Model):
    name = models.Model(max_length=32)
    category = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name

class TestState(models.Model):
    name = models.CharField(max_length=16)

    def __unicode__(self):
        return self.name

class TestCase(models.Model):
    project_id = models.IntegerField()
    case_type = models.CharField(max_length=32)
    order_number = models.CharField(max_length=32)
    case_desc = models.CharField(max_length=128)
    case_order = models.CharField(max_length=32)
    case_state = models.IntegerField()
    slqr_state = models.IntegerField()
    slqr_text = models.TextField(null=True)
    zypz_state = models.IntegerField()
    zypz_text = models.TextField(null=True)
    fkqr_state = models.IntegerField()
    fkqr_text = models.TextField(null=True)
    jhqr_state = models.IntegerField()
    jhqr_text = models.TextField(null=True)
    kdqr_state = models.IntegerField()
    kdqr_text = models.TextField(null=True)

    # def __unicode__(self):
    #     return 

    def get_case_state(self):
        return TestState.objects.get(self.case_state)
    def get_slqr_state(self):
        return TestState.objects.get(self.slqr_state)
    def get_zypz_state(self):
        return TestState.objects.get(self.zypz_state)
    def get_fkqr_state(self):
        return TestState.objects.get(self.fkqr_state)
    def get_jhqr_state(self):
        return TestState.objects.get(self.jhqr_state)
    def get_kdqr_state(self):
        return TestState.objects.get(self.kdqr_state)

