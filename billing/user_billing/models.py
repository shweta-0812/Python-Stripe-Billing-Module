from django.db import models
from django.db.models import JSONField

from user_billing.constants import (
    StripeConstant,
    StripeEventObjectTypeEnum,
    StripeEventTypeEnum,
    StripeProductPriceBillingSchemeEnum,
    StripeProductPriceTypeEnum,
    StripeProductPriceUsageTypeEnum,
)

from user_manager.models import Client


STRIPE_PERIOD_TYPE = ["monthly", "month"]
STRIPE_PRODUCT_PRICE_ANNUAL_TYPE = ["year", "yearly", "annual", "annually"]
STRIPE_PRODUCT_PRICE_MONTHLY_TYPE = ["monthly"]


class StripePaymentMethod(models.Model):
    id = models.CharField(primary_key=True, max_length=StripeConstant.STRIPE_ID_LENGTH, db_index=True)
    stripe_object = JSONField()


class StripeCustomer(models.Model):
    id = models.CharField(primary_key=True, max_length=StripeConstant.STRIPE_ID_LENGTH, db_index=True)
    default_payment_method = models.OneToOneField(
        to=StripePaymentMethod, on_delete=models.CASCADE, null=True, blank=True
    )
    client = models.OneToOneField(to=Client, on_delete=models.CASCADE, related_name="stripe_customer", db_index=True)
    stripe_object = JSONField()
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)


class StripeProduct(models.Model):
    id = models.CharField(primary_key=True, max_length=StripeConstant.STRIPE_ID_LENGTH, db_index=True)
    name = models.CharField(max_length=StripeConstant.STRIPE_ID_LENGTH, db_index=True,)
    row_limit = models.BigIntegerField()
    is_active = models.BooleanField(default=True)
    stripe_object = JSONField()
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)


class StripeProductPrice(models.Model):
    id = models.CharField(primary_key=True, max_length=StripeConstant.STRIPE_ID_LENGTH, db_index=True)
    is_active = models.BooleanField(default=True)
    base_price = models.IntegerField(default=0)
    overage_price = models.IntegerField(default=0)
    type = models.CharField(max_length=10, choices=StripeProductPriceTypeEnum.choices(),)
    billing_scheme = models.CharField(max_length=10, choices=StripeProductPriceBillingSchemeEnum.choices(),)
    usage_type = models.CharField(max_length=10, choices=StripeProductPriceUsageTypeEnum.choices(),)
    stripe_product = models.ForeignKey(
        to=StripeProduct, related_name="stripe_product_price", on_delete=models.CASCADE, db_index=True
    )
    stripe_object = JSONField()
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)


class StripeSubscription(models.Model):
    id = models.CharField(primary_key=True, max_length=StripeConstant.STRIPE_ID_LENGTH, db_index=True)
    start_at = models.DateTimeField()
    canceled_at = models.DateTimeField(null=True, blank=True)
    trial_end_at = models.DateTimeField(null=True, blank=True)
    cancel_at_period_end = models.BooleanField(default=False)
    subscription_status = models.CharField(max_length=10, db_index=True)
    stripe_product_price = models.ForeignKey(
        to=StripeProductPrice, related_name="stripe_subscription", on_delete=models.CASCADE, db_index=True
    )
    stripe_customer = models.ForeignKey(
        to=StripeCustomer, related_name="stripe_subscription", on_delete=models.CASCADE, db_index=True
    )
    stripe_object = JSONField()
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)


class StripeSubscriptionItem(models.Model):
    id = models.CharField(primary_key=True, max_length=StripeConstant.STRIPE_ID_LENGTH, db_index=True)
    stripe_subscription = models.ForeignKey(
        to=StripeSubscription, related_name="stripe_subscription_item", on_delete=models.CASCADE, db_index=True
    )
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)


class StripeInvoice(models.Model):
    id = models.CharField(primary_key=True, max_length=StripeConstant.STRIPE_ID_LENGTH, db_index=True)
    invoice_status = models.CharField(max_length=10, db_index=True)
    invoice_pdf_url = models.CharField(
        max_length=StripeConstant.STRIPE_ID_LENGTH, db_index=True, null=True, blank=True
    )
    stripe_customer = models.ForeignKey(
        to=StripeCustomer, related_name="stripe_invoice", on_delete=models.CASCADE, db_index=True
    )
    stripe_object = JSONField()


class StripeEvent(models.Model):
    date = models.DateTimeField(auto_now_add=True, db_index=True)
    event_type = models.CharField(max_length=StripeConstant.STRIPE_ID_LENGTH, choices=StripeEventTypeEnum.choices())
    object_type = models.CharField(max_length=50, choices=StripeEventObjectTypeEnum.choices())
    object_id = models.CharField(max_length=StripeConstant.STRIPE_ID_LENGTH)
    stripe_customer = models.ForeignKey(
        to=StripeCustomer, related_name="stripe_event", on_delete=models.CASCADE, db_index=True
    )
    stripe_object = JSONField()
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
