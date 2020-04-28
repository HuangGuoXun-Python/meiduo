from django.db import models


class Area(models.Model):
    name = models.CharField(max_length=20)
    # 自关联，允许为空,'self'表示自关联
    parent = models.ForeignKey('self', null=True, blank=True, related_name='subs')
    #mysql数据库里面的parent_id是根据上面这个parent创建出来的主键,并且两个名字关联在一起
    class Meta:
        db_table = 'tb_areas'

    def __str__(self):
        return self.name