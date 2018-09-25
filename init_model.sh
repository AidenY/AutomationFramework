python manage.py migrate  # 创建表结构
python manage.py makemigrations PlatformModel   # 让 Django 知道我们在我们的模型有一些变更
python manage.py migrate PlatformModel