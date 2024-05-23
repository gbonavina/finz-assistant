from django.contrib.auth.models import User
from .models import UserProfile
from django.utils import timezone

def get_or_create_guest_user(request):
    if 'guest_user_id' in request.session:
        guest_user = UserProfile.objects.get(id=request.session['guest_user_id'])
    else:
        username = "convidado_finz_n" + str(User.objects.count())
        password = "dNH0w7OT#£2SiRsr9K7"  
        
        user = User.objects.create_user(username=username, password=password)
        
        guest_user = UserProfile.objects.create(user=user)
        
        request.session['guest_user_id'] = guest_user.id
        guest_user.last_active = timezone.now()
        guest_user.save(update_fields=['last_active'])

    return guest_user