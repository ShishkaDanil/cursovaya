import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autosite.settings')
import django
django.setup()

from django.contrib.auth.models import User, Group

# Получаем группы ролей
manager_group, created = Group.objects.get_or_create(name='manager')
buhgalter_group, created = Group.objects.get_or_create(name='buhgalter')

# Получаем пользователей
manager_user = User.objects.get(username='manager')
manager_user.groups.add(manager_group)

buhgalter_user = User.objects.get(username='buhgalter')
buhgalter_user.groups.add(buhgalter_group)
