from django.db import models


class Product(models.Model):
    """A item to be sold.

    The `price` is recorded in Philippine Centavo. So PHP 100.00 is recorded
    as 10_000. This is to ensure that floating point arithmetic is not used.
    """

    name = models.CharField(max_length=200)
    quantity = models.PositiveSmallIntegerField()
    price = models.IntegerField()
    discount = models.DecimalField(max_digits=2, decimal_places=2)

    @property
    def in_stock(self):
        """Check if a product is in stock."""

        return self.quantity > 0
