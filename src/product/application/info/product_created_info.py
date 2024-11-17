
from common.domain.result.result import result_info_factory
from product.application.info.codes.product_codes import ProductCodes


product_created_info = result_info_factory(
    code=ProductCodes.CREATE,
    message="Product created successfully"
)