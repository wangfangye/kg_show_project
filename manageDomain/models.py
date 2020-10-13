# _*_ coding: utf-8 _*_
from django.db import models
from django.contrib.auth.models import User

##领域表
# Create your models here.现在就一个
class DomainModel(models.Model):
    domain_id = models.AutoField(primary_key=True)
    domain_name = models.CharField(max_length=50, verbose_name="领域名称")
    users = models.ManyToManyField(User)

    class Meta:
        verbose_name = '领域管理'
        verbose_name_plural = '领域管理'
    def __str__(self):
        return self.domain_name


##属性的名称集合表，一共有哪些属性：生日、年份都属于属性
class entityModel(models.Model):
    entity_id = models.AutoField(primary_key=True)
    # 领域模型
    domain_name = models.ForeignKey(DomainModel, on_delete=models.CASCADE,verbose_name="所属领域")
    entity_label = models.CharField(max_length=50, verbose_name="属性名称")

    class Meta:
        verbose_name = '属性类型管理'
        verbose_name_plural = '属性类型管理'





# 实体的label表格： 实体是任务，地点，品牌等
##实体标签集合表
class entityLabelModel(models.Model):
    entity_id = models.AutoField(primary_key=True)
    # 领域模型
    domain_name = models.ForeignKey(DomainModel, on_delete=models.CASCADE,verbose_name="所属领域")
    entity_node_label = models.CharField(max_length=50, verbose_name="实体标签名称")

    class Meta:
        verbose_name = '实体标签管理'
        verbose_name_plural = '实体标签管理'


## 关系属性表: 保存有哪些关系的名字
class relationModel(models.Model):
    relation_id = models.AutoField(primary_key=True)
    # 领域模型
    domain_name = models.ForeignKey(DomainModel, on_delete=models.CASCADE,verbose_name="所属领域")
    relation_label = models.CharField(max_length=50, verbose_name="关系属性名称")

    class Meta:
        verbose_name = '关系管理'
        verbose_name_plural = '关系管理'

# # 抽象基类
# class BaseFileModel(models.Model):
#     """
#         BaseModel class
#     """
#     id = models.AutoField(primary_key=True)
#     desc = models.CharField(default=u"", max_length=1024, verbose_name=u"描述")
#
#     date = models.DateTimeField(verbose_name=u"最后修改日期", auto_now=True)
#
#     def __str__(self):
#         return self.desc  # base name
#
#     # 抽象基础类
#     class Meta:
#         abstract = True
#
# # 文件上传，然后保存吗，需要的话需要留三个文件
# class RawText(BaseModel):
#     """
#         raw txt file
#         保存train，test文件
#     """
#     file = models.FileField(verbose_name=u"用于批量导入的txt文件", upload_to=u'data_sets', max_length=1024)  # text file path
#     # 外键 我是上传csv文件，类别在文件里面，所以不需要这个外键
#     # text_class = models.ForeignKey(TextClass, on_delete=models.CASCADE, verbose_name=u"对应类别")     # text class
#     add_to_train_set = models.BooleanField(choices=((True, u"立即导入"), (False, u"只上传txt")), default=True, blank=False,
#                                            verbose_name=u"是否立即导入到数据库")
#     file_type = models.IntegerField(verbose_name=u"数据类型", choices=((0, u"训练集合"), (1, u"验证集")), default=0, blank=False)
#
#     def __str__(self):
#         return self.file.name + u" 修改时间:" + str(self.file_type) + str(self.date)
#
#     class Meta:
#         verbose_name = u"标记好的文本"
#
#     def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
#         """
#             重写save方法，如果add_to_train_set为True,读取文本，并把文本按行添加到数据集的表中
#         :param force_insert:
#         :param force_update:
#         :param using:
#         :param update_fields:
#         :return:
#         """
#         pass
#         # super().save(force_insert, force_update, using, update_fields)
#         # if self.add_to_train_set:
#         # # 添加到dataset（train-test）中
#         #     upload_raw_csv_text(self.file.name, self.file_type)
#         #
#         #     self.add_to_train_set = False
#         #     self.save()
#
#
#     def delete(self, using=None, keep_parents=False):
#         pass
#         # try:
#         #     file_path = predictserver.settings.BASE_DIR + "/" + self.file.name
#         #     print(file_path)
#         #     if os.path.exists(file_path):
#         #         os.remove(file_path)
#         # except Exception as e:
#         #     print(e)
#
#         return super().delete(using, keep_parents)
