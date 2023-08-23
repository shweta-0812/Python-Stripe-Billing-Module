from common.choice import Choice


class StripeConstant:
    PRICE_INF = "inf"
    PRICE_ZERO_INTEGER_VALUE = 0
    PRICE_ZERO_DECIMAL_VALUE = 0.00
    PRICE_TYPE = "recurring"
    PRICE_CURRENCY = "usd"
    PRICE_TIERS_MODE = "graduated"
    PRICE_RECURRING_USAGE_TYPE = "metered"
    PRICE_RECURRING_AGGREGATE_USAGE = "sum"
    PRICE_RECURRING_INTERVAL_COUNT = 1
    SUBSCRIPTION_COLLECTION_METHOD = "charge_automatically"
    STRIPE_ID_LENGTH = 255


class StripeProductPriceUsageTypeEnum(Choice):
    METERED = "metered"
    LICENSED = "licensed"


class StripeProductPriceBillingSchemeEnum(Choice):
    PER_UNIT = "per_unit"
    TIERED = "tiered"


class StripeProductPriceIntervalEnum(Choice):
    MONTH = "month"
    YEAR = "year"


class StripeProductPriceTypeEnum(Choice):
    MONTHLY = "monthly"
    ANNUAL = "annual"


class StripeSubscriptionStatusEnum(Choice):
    ACTIVE = "active"
    PAST_DUE = "past_due"
    UNPAID = "unpaid"
    CANCELED = "canceled"
    INCOMPLETE = "incomplete"
    INCOMPLETE_EXPIRED = "incomplete_expire"
    TRIALING = "trialing"


class StripePeriodTypeEnum(Choice):
    monthly = "monthly"
    month = "month"
    annual = "annual"
    annually = "annually"
    yearly = "yearly"
    year = "year"


class StripeEventTypeEnum(Choice):
    CUSTOMER_SUBSCRIPTION_CREATED = "customer.subscription.created"
    CUSTOMER_SUBSCRIPTION_UPDATED = "customer.subscription.updated"
    CUSTOMER_SUBSCRIPTION_DELETED = "customer.subscription.deleted"
    CUSTOMER_SUBSCRIPTION_TRIAL_WILL_END = "customer.subscription.trial_will_end"

    PAYMENT_METHOD_AUTOMATICALLY_UPDATED = "payment_method.automatically_updated"
    PAYMENT_METHOD_UPDATED = "payment_method.updated"
    PAYMENT_METHOD_ATTACHED = "payment_method.attached"
    PAYMENT_METHOD_DETACHED = "payment_method.detached"


class StripeEventObjectTypeEnum(Choice):
    SUBSCRIPTION = "subscription"
    CUSTOMER = "customer"
