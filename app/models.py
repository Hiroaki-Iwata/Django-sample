from django.db import models
from django.core import validators


class Item(models.Model):

    name = models.CharField(
        verbose_name='商品名',
        max_length=200,
    )
    quantity = models.IntegerField(
        verbose_name='数量',
        validators=[validators.MinValueValidator(1)],
        blank=True,
        null=True,
    )
    memo = models.TextField(
        verbose_name='備考',
        max_length=300,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True
    )

    # 以下は管理サイト上の表示設定
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'アイテム'
        verbose_name_plural = 'アイテム'
