import os
from dotenv import load_dotenv
from paapi5_python_sdk.api.default_api import DefaultApi
from paapi5_python_sdk.models.get_items_request import GetItemsRequest
from paapi5_python_sdk.models.partner_type import PartnerType
from paapi5_python_sdk.models.get_items_resource import GetItemsResource
from paapi5_python_sdk.rest import ApiException

# Load credentials from .env
load_dotenv()

access_key = os.getenv("AMAZON_ACCESS_KEY")
secret_key = os.getenv("AMAZON_SECRET_KEY")
partner_tag = os.getenv("AMAZON_PARTNER_TAG")
host = "webservices.amazon.com"
region = "us-east-1"

def get_product_details(asin):
    default_api = DefaultApi(
        access_key=access_key,
        secret_key=secret_key,
        host=host,
        region=region,
    )

    # Resources you want to fetch
    resources = [
        GetItemsResource.ITEMINFO_TITLE,
        GetItemsResource.ITEMINFO_FEATURES,
        GetItemsResource.ITEMINFO_MANUFACTURER,
        GetItemsResource.IMAGES_PRIMARY_LARGE,
        GetItemsResource.ITEMINFO_BYLINEINFO,
        GetItemsResource.OFFERS_LISTINGS_PRICE,
    ]

    request = GetItemsRequest(
        partner_tag=partner_tag,
        partner_type=PartnerType.ASSOCIATES,
        item_ids=[asin],
        resources=resources,
    )

    try:
        response = default_api.get_items(request)
        if response.items_result and response.items_result.items:
            item = response.items_result.items[0]
            print(f"\n🆔 ASIN: {item.asin}")
            print(f"🔗 URL: {item.detail_page_url}")
            print(f"📦 Title: {item.item_info.title.display_value}")
            
            # Features
            if item.item_info.features and item.item_info.features.display_values:
                print("✨ Features:")
                for feature in item.item_info.features.display_values:
                    print(f"   • {feature}")

            # Manufacturer
            if item.item_info.manufacturer and item.item_info.manufacturer.display_value:
                print(f"🏭 Manufacturer: {item.item_info.manufacturer.display_value}")
                
            # ByLine Info (Brand or Creator)
            if item.item_info.by_line_info and item.item_info.by_line_info.brand:
                print(f"🏷 Brand: {item.item_info.by_line_info.brand.display_value}")

            # Price
            if (item.offers and item.offers.listings 
                and item.offers.listings[0].price 
                and item.offers.listings[0].price.display_amount):
                print(f"💰 Price: {item.offers.listings[0].price.display_amount}")

            # Image
            if item.images and item.images.primary and item.images.primary.large:
                print(f"🖼 Image: {item.images.primary.large.url}")
        else:
            print("❌ No item details found.")

        if response.errors:
            print("Errors:")
            for error in response.errors:
                print(f" - {error.code}: {error.message}")

    except ApiException as e:
        print("API Exception:", e)

if __name__ == "__main__":
    asin_input = input("🔍 Enter the ASIN of the product: ").strip()
    get_product_details(asin_input)
