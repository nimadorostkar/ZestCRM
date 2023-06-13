from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, national_code, password=None, **other_fields):
        if not national_code:
            raise ValueError("national code is required...!")
        user = self.model(national_code=national_code, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, national_code, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser muse have is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser muse have is_superuser=True')
        return self.create_user(national_code, password, **other_fields)
