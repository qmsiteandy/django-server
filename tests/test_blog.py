from django.urls import reverse
from modules.blog.models import Articles  # 导入您的模型
import pytest

@pytest.mark.django_db
def test_my_model_creation():
    # 创建一个模型实例
    Articles.objects.create(title="Test", content='Test')

    # 查询数据库并验证模型是否创建成功
    model = Articles.objects.get(title="Test")
    assert model is not None

@pytest.mark.django_db
def test_my_view(client):
    # 使用Django test client模拟GET请求
    response = client.get(reverse('blog:index'))
    # 检查视图返回状态码是否为200
    assert response.status_code == 200