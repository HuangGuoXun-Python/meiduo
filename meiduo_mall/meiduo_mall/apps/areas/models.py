from django.db import models


class Area(models.Model):
    name = models.CharField(max_length=20)
    # 自关联，允许为空
    parent = models.ForeignKey('self', null=True, blank=True, related_name='subs')

    class Meta:
        db_table = 'tb_areas'

    def __str__(self):
        return self.name