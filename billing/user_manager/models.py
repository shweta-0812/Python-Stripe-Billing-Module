import pprint

from django.db import models
from django.core.validators import RegexValidator, URLValidator


class Client(models.Model):
    name = models.CharField(db_index=True, max_length=50)
    is_active = models.BooleanField(default=True)
    trial_expiry_date = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ["-id"]

    def __repr__(self) -> str:
        return pprint.pformat(self.to_dict())

    def __str__(self) -> str:
        return "<{} | id:{}>".format(self._meta.model_name, self.id)


class User(models.Model):
    email = models.EmailField(db_index=True)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    time_zone = models.CharField(max_length=50, null=True, blank=True)
    avatar = models.TextField(validators=[URLValidator()], null=True, blank=True)
    PHONE_REGEX = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number should not have spaces and special characters: '999999999'. Up to 15 digits allowed.",
    )
    phone_country_code = models.CharField(max_length=6, null=True, blank=True)
    phone_national_number = models.CharField(
        validators=[PHONE_REGEX], max_length=15, db_index=True, null=True, blank=True
    )
    admin_access_token = models.CharField(max_length=100, null=True, blank=True, db_index=True)
    is_email_validated = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ["-id"]
        unique_together = ("client", "email")


