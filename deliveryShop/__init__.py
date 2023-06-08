default_app_config = 'deliveryShop.apps.DeliveryshopConfig'

from django.apps import AppConfig

class DeliveryShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'deliveryShop'

    def ready(self):
        import deliveryShop.signals  # Import your signals module
