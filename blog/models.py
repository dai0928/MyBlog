from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
import uuid
from django.contrib.auth import get_user_model


class CreateBlogModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # idはmodelで定義しなくても自動で生成されるが、記事（データ）を作成するごとに連番でidがつけられてしまう(1→2→3のように)為、UUIDを使って上書きしている
    # UUIDは絶対に重複しないランダムな文字列が与えられる
    blog_title = models.CharField(max_length=100, unique=False, default="ここにタイトルを入力")
    text = models.TextField(default="文章を入力")
    created_date = models.DateTimeField(verbose_name="作成日時", default=now)
    updated_date = models.DateTimeField(verbose_name="更新日時", default=now)
    user = models.CharField(max_length=50, null=True)
    # 作成したブログにuserの値を登録することによって、usernameと一致するブログのみを表示させる事が可能となる

    def __str__(self):
        return self.blog_title
# __str__で管理サイトで表示されるトップの項目を指定している　上記の場合はblog_titleが一覧に並ぶ
