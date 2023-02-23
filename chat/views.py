from django.shortcuts import render
from .forms import GroupForm
from .models import CustomUserGroup

def index(request):
    groups = CustomUserGroup.objects.all()
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            new_group = form.save(commit=True)
            new_group.save()
            return render(request, 'chat/new_group_created.html', {'group_name': new_group.custom_group_name})
        else:
            return render(request, 'chat/room_already_exists.html')
    else:
        form = GroupForm()
    return render(request, 'chat/index.html', {'form': form, 'groups': groups})



def room(request, room_name):
    current_user = request.user
    context = {'room_name': room_name}
    if CustomUserGroup.objects.filter(custom_group_name = room_name).exists():
        group = CustomUserGroup.objects.get(custom_group_name=room_name)
        if current_user in group.users.all():
            context['users'] = group.users.all()
            return render(request, 'chat/room.html', context)
        else:
            return render(request, 'chat/not_in_the_group.html')
    else:
        return render(request, 'chat/no_such_room.html', context)



