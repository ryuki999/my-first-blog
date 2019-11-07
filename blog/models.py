from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):

    #models.ForeignKey – これは他のモデルへのリンク
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    #models.CharField – 文字数が制限されたテキストを定義するフィールド
    title = models.CharField(max_length=200)
    
    #models.TextField – これは制限無しの長いテキスト用です。ブログポストのコンテンツに理想的なフィールドでしょ？
    text = models.TextField()

    #models.DateTimeField – 日付と時間のフィールド
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title