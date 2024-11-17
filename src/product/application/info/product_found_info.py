from common.domain.result.result import result_info_factory
from product.application.info.codes.product_codes import ProductCodes


product_found_info = result_info_factory(
    code=ProductCodes.FIND_ONE, message="Product found successfully"
)
