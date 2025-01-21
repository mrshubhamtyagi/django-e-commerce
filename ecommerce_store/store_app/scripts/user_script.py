from django.contrib.auth.models import User


def create_user():
    user, created = User.objects.get_or_create(
        username= 'Gagan',
        defaults={"password": "password123"}
    )
    
    if created:
        print(f'User Created - {user}')
    else:
        print(f'User Already Exists - {user}')
        
def delete_user():
    username='Gagan'
    try:
        user = User.objects.get(username=username) 
        user.delete()
        print(f'User Deleted - {user}')
    except User.DoesNotExist:
        print(f'User does not exist {username}')
    except Exception as e:
        print(f"Error deleting user: {e}")
        
        
def print_users():
    for user in User.objects.all():
        print(user)