from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from ecommerce.users.managers import UserManager
import uuid


class User(AbstractUser):
    """
    Default custom user model for Ecommerce.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    # name = None # type: ignore
    first_name = CharField(
        _("First Name of User"), 
        blank=True, 
        max_length=200,
        help_text= _("Holds the First name of the user."),
        )
    
    last_name = CharField(
        _("Last Name of User"), 
        blank=True, 
        max_length=200,
        help_text= _("Holds the Last name of the user")
        )
    
    email = EmailField(
        _("email address"), 
        unique=True,
        help_text=_("The email address of the customer.")
        )

    id = models.UUIDField(
        default = uuid.uuid4,
        editable=False,
        primary_key=True,
        help_text=_("The unique identifier of the customer.")
    )
    
    username = None  # type: ignore

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.id})
    
    class Meta:
        verbose_name = _("users  Account")
        verbose_name_plural = _("users  Account")

    # def __str__(self):
    #     return str(self.email)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
