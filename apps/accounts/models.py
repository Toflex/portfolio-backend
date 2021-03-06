from random import random

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager

SEX_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Unknown', 'Unknown')
)

# STATUS_CHOICE = (
#     ('UNAVAILABLE', 'Unavailable'),
#     ('AVAILABLE', 'Available'),
#     ('DEACTIVATED', 'Deactivated')
# )


class UserManager(BaseUserManager):

    def get_all_users(self):
        """Returns all users"""
        return super(UserManager, self).get_queryset().all()

    def get_active_users(self):
        """Returns all users"""
        return super(UserManager, self).get_queryset().filter(status=0)

    # Add Oauth Authentication later
    def create_user(self, last_name, first_name, email, password=None):
        user = self.model(
            last_name=last_name,
            first_name=first_name,
            email=self.normalize_email(email.lower())
        )
        does_username_exist = super(UserManager, self).get_queryset().filter(username=first_name+last_name)
        if does_username_exist:
            user.username = first_name+last_name+random.randint(100, 9000)
        else:
            user.username = first_name+last_name
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, last_name, first_name, middle_name, email, password):
        user = self.create_user(
            last_name, first_name, middle_name, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    REQUIRED_FIELDS = ['first_name', 'last_name', ]

    first_name = models.CharField(verbose_name=_('First name'), max_length=50, null=False, blank=False)
    last_name = models.CharField(verbose_name=_('Last name'), max_length=50, null=False, blank=False)
    middle_name = models.CharField(verbose_name=_('Middle name'), max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=254, verbose_name=_('Email Address'), blank=False, null=False, unique=True)
    gender = models.CharField(max_length=10, choices=SEX_CHOICES, default='', null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    bio = models.CharField(max_length=200, help_text="Professional Summary", null=True, blank=False)
    languages = models.CharField(max_length=100, null=True, blank=True)
    resume = models.URLField('resume', null=True, blank=True)
    nationality = models.CharField(max_length=20, null=True, blank=True)
    state_of_residence = models.CharField(max_length=20, null=True, blank=True)
    # status = models.CharField(max_length=15, choices=STATUS_CHOICE, null=False, blank=False, default='Available')
    date_of_birth = models.DateField(null=True, blank=True)  # applicant should be greater than 17
    profession = models.CharField(max_length=50, verbose_name=_("Job Title"), null=False, blank=False,
                                  default='')  # Todo: convert to choice field
    profile_pix = models.URLField('avatar', null=True, blank=True)

    # USERNAME_FIELD = 'email'

    def __str__(self):
        return "(%d) - %s %s" %(self.id, self.last_name, self.first_name)

    class Meta:
        app_label = 'accounts'
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ('first_name',)

    def get_full_name(self):
        return "%s %s" % (self.last_name, self.first_name)


class Contact(models.Model):
    email = models.EmailField(_("Email Address"), null=False, blank=False)
    full_name = models.CharField(max_length=80, null=False, blank=False)
    message = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return "(%s: %s)" % (self.full_name[:15], self.email[:15])


