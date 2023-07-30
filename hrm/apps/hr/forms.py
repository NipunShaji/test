from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError


class HrAuthenticationForm(AuthenticationForm):

    def confirm_login_allowed(self, user: AbstractUser) -> None:
        super().confirm_login_allowed(user)

        if not user.is_staff:
            raise ValidationError(
                "Only HR is allowed to login in this portal"
            )
