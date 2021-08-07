from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        """
        Override ready method and import signals and calls
        custom update total method to update totals automatically
        """
        import checkout.signals
