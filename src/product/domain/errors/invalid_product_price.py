
from common.domain.error.domain_error import domain_error_factory

INVALID_PRODUCT_PRICE_ERROR = 'invalid_price_name'

invalid_product_price_error = domain_error_factory(INVALID_PRODUCT_PRICE_ERROR, 'Prices starts at 0.00')