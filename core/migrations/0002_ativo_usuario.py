import django.db.models.deletion
import django.utils.timezone
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import migrations, models


def get_default_user_id():
    User = get_user_model()
    return User.objects.first().id  # Aqui você pode usar a lógica que preferir para definir o usuário padrão

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='ativo',
            name='usuario',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='ativos',
                to=settings.AUTH_USER_MODEL,
                default=get_default_user_id
            ),
            preserve_default=False,
        ),
    ]