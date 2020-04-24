from django.db.models.signals import post_save
#from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Team, User, Pass

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, Permission


@receiver(post_save, sender=Team)
def set_team_permissions(sender, instance, created, **kwargs):
    if getattr(instance, 'from_admin_site', False):
        print("in Signals")
        print(instance)
        new_group, created = Team.objects.get(team_name=instance.team_name)
        ct = ContentType.objects.get_for_model(Pass)

        # Now what - Say I want to add 'Can add project' permission to new_group?
        permission = Permission.objects.create(codename='can_add_pass',
                                               name='Can add pass',
                                               content_type=ct)
        new_group.permissions.set(permission)
        print(new_group.permissions.all())
        print("SUCCESS post_save")




    #if created:



@receiver(post_save, sender=User)
def set_user_to_team(sender, instance, created, **kwargs):
    #if created:
    if instance.user_teamid is not None:
        tempuser = User.objects.get(user_id = instance.user_id)
        tempteam = Team.objects.get(team_id = instance.user_teamid)
        tempuser.groups.add(tempteam)
    print("User added to team")

