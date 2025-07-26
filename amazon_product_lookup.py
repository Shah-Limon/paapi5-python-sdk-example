# # # import os
# # # from dotenv import load_dotenv
# # # from paapi5_python_sdk.api.default_api import DefaultApi
# # # from paapi5_python_sdk.models.get_items_request import GetItemsRequest
# # # from paapi5_python_sdk.models.get_items_resource import GetItemsResource
# # # from paapi5_python_sdk.models.partner_type import PartnerType
# # # from paapi5_python_sdk.rest import ApiException

# # # # Load credentials from .env
# # # load_dotenv()
# # # access_key = os.getenv("AMAZON_ACCESS_KEY")
# # # secret_key = os.getenv("AMAZON_SECRET_KEY")
# # # partner_tag = os.getenv("AMAZON_PARTNER_TAG")

# # # # PAAPI host and region
# # # host = "webservices.amazon.com"
# # # region = "us-east-1"

# # # def get_product_details(asin):
# # #     try:
# # #         default_api = DefaultApi(
# # #             access_key=access_key,
# # #             secret_key=secret_key,
# # #             host=host,
# # #             region=region
# # #         )

# # #         resources = [
# # #             GetItemsResource.ITEMINFO_TITLE,
# # #             GetItemsResource.ITEMINFO_BYLINEINFO,
# # #             GetItemsResource.ITEMINFO_CLASSIFICATIONS,
# # #             GetItemsResource.ITEMINFO_CONTENTINFO,
# # #             GetItemsResource.ITEMINFO_CONTENTRATING,
# # #             GetItemsResource.ITEMINFO_EXTERNALIDS,
# # #             GetItemsResource.ITEMINFO_FEATURES,
# # #             GetItemsResource.ITEMINFO_MANUFACTUREINFO,
# # #             GetItemsResource.ITEMINFO_PRODUCTINFO,
# # #             GetItemsResource.ITEMINFO_TECHNICALINFO,
# # #             GetItemsResource.ITEMINFO_TRADEININFO
# # #         ]

# # #         request = GetItemsRequest(
# # #             item_ids=[asin],
# # #             partner_tag=partner_tag,
# # #             partner_type=PartnerType.ASSOCIATES,
# # #             resources=resources
# # #         )

# # #         response = default_api.get_items(request)

# # #         if response.items_result is not None:
# # #             item = response.items_result.items[0]
# # #             print("\n🔍 Product Details for ASIN:", asin)
# # #             print("➡️ Title:", item.item_info.title.display_value if item.item_info.title else "N/A")
# # #             print("➡️ Brand:", item.item_info.by_line_info.brand.display_value if item.item_info.by_line_info and item.item_info.by_line_info.brand else "N/A")
# # #             print("➡️ Manufacturer:", item.item_info.by_line_info.manufacturer.display_value if item.item_info.by_line_info and item.item_info.by_line_info.manufacturer else "N/A")
# # #             print("➡️ Features:")
# # #             if item.item_info.features and item.item_info.features.display_values:
# # #                 for feat in item.item_info.features.display_values:
# # #                     print("   •", feat)
# # #             else:
# # #                 print("   No features listed.")

# # #             # Display extra dynamic attributes
# # #             print("\n➡️ Additional Info:")
# # #             containers = item.item_info.to_dict()
# # #             for key, value in containers.items():
# # #                 if isinstance(value, dict):
# # #                     print(f"\n📦 {key}:")
# # #                     for attr, val in value.items():
# # #                         if isinstance(val, dict) and "display_value" in val:
# # #                             print(f"  {attr}: {val['display_value']}")
# # #                         elif isinstance(val, list):
# # #                             for entry in val:
# # #                                 if isinstance(entry, dict) and "display_value" in entry:
# # #                                     print(f"  {attr}: {entry['display_value']}")
# # #             print("\n🔗 Product URL:", item.detail_page_url)

# # #         if response.errors:
# # #             print("\n❌ Errors:")
# # #             for error in response.errors:
# # #                 print(f"{error.code}: {error.message}")

# # #     except ApiException as e:
# # #         print("API Exception:", e)

# # # if __name__ == "__main__":
# # #     asin_input = input("🔍 Enter the ASIN of the product: ").strip()
# # #     get_product_details(asin_input)

# # import os
# # from dotenv import load_dotenv
# # from paapi5_python_sdk.api.default_api import DefaultApi
# # from paapi5_python_sdk.models.search_items_request import SearchItemsRequest
# # from paapi5_python_sdk.models.search_items_resource import SearchItemsResource
# # from paapi5_python_sdk.models.get_items_resource import GetItemsResource
# # from paapi5_python_sdk.models.partner_type import PartnerType
# # from paapi5_python_sdk.rest import ApiException

# # # Load credentials from .env
# # load_dotenv()
# # access_key = os.getenv("AMAZON_ACCESS_KEY")
# # secret_key = os.getenv("AMAZON_SECRET_KEY")
# # partner_tag = os.getenv("AMAZON_PARTNER_TAG")

# # # PAAPI host and region
# # host = "webservices.amazon.com"
# # region = "us-east-1"

# # def get_product_details(default_api, asin):
# #     """Get detailed info about a single product by ASIN."""
# #     resources = [
# #         GetItemsResource.ITEMINFO_TITLE,
# #         GetItemsResource.ITEMINFO_BYLINEINFO,
# #         GetItemsResource.ITEMINFO_CLASSIFICATIONS,
# #         GetItemsResource.ITEMINFO_CONTENTINFO,
# #         GetItemsResource.ITEMINFO_CONTENTRATING,
# #         GetItemsResource.ITEMINFO_EXTERNALIDS,
# #         GetItemsResource.ITEMINFO_FEATURES,
# #         GetItemsResource.ITEMINFO_MANUFACTUREINFO,
# #         GetItemsResource.ITEMINFO_PRODUCTINFO,
# #         GetItemsResource.ITEMINFO_TECHNICALINFO,
# #         GetItemsResource.ITEMINFO_TRADEININFO,
# #         GetItemsResource.OFFERS_LISTINGS_PRICE,
# #         GetItemsResource.OFFERS_LISTINGS_AVAILABILITY_MAXORDERQUANTITY,
# #         GetItemsResource.OFFERS_SUMMARY_HIGHEST_PRICE,
# #         GetItemsResource.OFFERS_SUMMARY_LOWEST_PRICE
# #     ]

# #     try:
# #         from paapi5_python_sdk.models.get_items_request import GetItemsRequest
# #         request = GetItemsRequest(
# #             item_ids=[asin],
# #             partner_tag=partner_tag,
# #             partner_type=PartnerType.ASSOCIATES,
# #             resources=resources
# #         )
# #         response = default_api.get_items(request)

# #         if response.items_result is not None and response.items_result.items:
# #             item = response.items_result.items[0]
# #             print("\n🔍 Product Details for ASIN:", asin)
# #             print("➡️ Title:", item.item_info.title.display_value if item.item_info and item.item_info.title else "N/A")
# #             print("➡️ Brand:", item.item_info.by_line_info.brand.display_value if item.item_info and item.item_info.by_line_info and item.item_info.by_line_info.brand else "N/A")
# #             print("➡️ Manufacturer:", item.item_info.by_line_info.manufacturer.display_value if item.item_info and item.item_info.by_line_info and item.item_info.by_line_info.manufacturer else "N/A")
# #             print("➡️ Features:")
# #             if item.item_info.features and item.item_info.features.display_values:
# #                 for feat in item.item_info.features.display_values:
# #                     print("   •", feat)
# #             else:
# #                 print("   No features listed.")
# #             print("\n➡️ Additional Info:")
# #             containers = item.item_info.to_dict() if item.item_info else {}
# #             for key, value in containers.items():
# #                 if isinstance(value, dict):
# #                     print(f"\n📦 {key}:")
# #                     for attr, val in value.items():
# #                         if isinstance(val, dict) and "display_value" in val:
# #                             print(f"  {attr}: {val['display_value']}")
# #                         elif isinstance(val, list):
# #                             for entry in val:
# #                                 if isinstance(entry, dict) and "display_value" in entry:
# #                                     print(f"  {attr}: {entry['display_value']}")
# #             print("\n🔗 Product URL:", item.detail_page_url)
# #         else:
# #             print(f"No detailed info found for ASIN {asin}")

# #         if response.errors:
# #             print("\n❌ Errors:")
# #             for error in response.errors:
# #                 print(f"{error.code}: {error.message}")

# #     except ApiException as e:
# #         print("API Exception:", e)


# # def search_products_by_keyword(keyword, max_results=7):
# #     """Search Amazon products by keyword and show details for first max_results items."""
# #     try:
# #         default_api = DefaultApi(
# #             access_key=access_key,
# #             secret_key=secret_key,
# #             host=host,
# #             region=region
# #         )

# #         resources = [
# #                SearchItemsResource.ITEMINFO_TITLE,
# #     SearchItemsResource.ITEMINFO_BYLINEINFO,
# #     SearchItemsResource.ITEMINFO_CLASSIFICATIONS,
# #     SearchItemsResource.ITEMINFO_CONTENTINFO,
# #     SearchItemsResource.ITEMINFO_CONTENTRATING,
# #     SearchItemsResource.ITEMINFO_EXTERNALIDS,
# #     SearchItemsResource.ITEMINFO_FEATURES,
# #     SearchItemsResource.ITEMINFO_MANUFACTUREINFO,
# #     SearchItemsResource.ITEMINFO_PRODUCTINFO,
# #     SearchItemsResource.ITEMINFO_TECHNICALINFO,
# #     SearchItemsResource.ITEMINFO_TRADEININFO,
# #     SearchItemsResource.OFFERS_LISTINGS_PRICE,
# #     SearchItemsResource.OFFERS_LISTINGS_AVAILABILITY_MAXORDERQUANTITY,
# #     SearchItemsResource.OFFERS_SUMMARIES_HIGHESTPRICE,
# #     SearchItemsResource.OFFERS_SUMMARIES_LOWESTPRICE
# #         ]

# #         request = SearchItemsRequest(
# #             partner_tag=partner_tag,
# #             partner_type=PartnerType.ASSOCIATES,
# #             keywords=keyword,
# #             resources=resources,
# #             marketplace="www.amazon.com",
# #             search_index="All"
# #         )

# #         response = default_api.search_items(request)

# #         if response.search_result is not None and response.search_result.items:
# #             items = response.search_result.items[:max_results]
# #             print(f"\n🔍 Search results for: '{keyword}'\n")
# #             for idx, item in enumerate(items, start=1):
# #                 print(f"Product #{idx}")
# #                 print("ASIN:", item.asin)
# #                 print("Title:", item.item_info.title.display_value if item.item_info and item.item_info.title else "N/A")
# #                 print("Brand:", item.item_info.by_line_info.brand.display_value if item.item_info and item.item_info.by_line_info and item.item_info.by_line_info.brand else "N/A")
# #                 print("Price:", end=" ")
# #                 try:
# #                     offers = item.offers
# #                     if offers and offers.listings and offers.listings[0].price:
# #                         print(f"{offers.listings[0].price.display_amount}")
# #                     else:
# #                         print("N/A")
# #                 except Exception:
# #                     print("N/A")
# #                 print("Detail Page URL:", item.detail_page_url)
# #                 print("-" * 40)

# #             # Optionally get detailed info per ASIN:
# #             for item in items:
# #                 get_product_details(default_api, item.asin)

# #         else:
# #             print("No items found for the keyword:", keyword)

# #         if response.errors:
# #             print("\n❌ Errors:")
# #             for error in response.errors:
# #                 print(f"{error.code}: {error.message}")

# #     except ApiException as e:
# #         print("API Exception:", e)


# # if __name__ == "__main__":
# #     keyword_input = input("🔍 Enter the product search keyword: ").strip()
# #     search_products_by_keyword(keyword_input)

# import os
# from dotenv import load_dotenv
# from paapi5_python_sdk.api.default_api import DefaultApi
# from paapi5_python_sdk.models.search_items_request import SearchItemsRequest
# from paapi5_python_sdk.models.search_items_resource import SearchItemsResource
# from paapi5_python_sdk.models.get_items_resource import GetItemsResource
# from paapi5_python_sdk.models.get_items_request import GetItemsRequest
# from paapi5_python_sdk.models.partner_type import PartnerType
# from paapi5_python_sdk.rest import ApiException
# import random

# # Load credentials from .env
# load_dotenv()
# access_key = os.getenv("AMAZON_ACCESS_KEY")
# secret_key = os.getenv("AMAZON_SECRET_KEY")
# partner_tag = os.getenv("AMAZON_PARTNER_TAG")

# # PAAPI host and region
# host = "webservices.amazon.com"
# region = "us-east-1"

# def print_separator(title="", length=80):
#     """Print a formatted separator line."""
#     if title:
#         padding = (length - len(title) - 2) // 2
#         print("=" * padding + f" {title} " + "=" * padding)
#     else:
#         print("=" * length)

# def safe_get_value(obj, *keys):
#     """Safely get nested values from objects."""
#     try:
#         current = obj
#         for key in keys:
#             if hasattr(current, key):
#                 current = getattr(current, key)
#             elif isinstance(current, dict) and key in current:
#                 current = current[key]
#             else:
#                 return "N/A"
        
#         if hasattr(current, 'display_value'):
#             return current.display_value
#         elif hasattr(current, 'display_values') and current.display_values:
#             return current.display_values
#         elif current is not None:
#             return str(current)
#         else:
#             return "N/A"
#     except:
#         return "N/A"

# def print_comprehensive_product_info(item, product_num):
#     """Print comprehensive A-Z product information."""
#     print_separator(f"PRODUCT #{product_num}")
    
#     # Basic Information
#     print("🔍 BASIC INFORMATION")
#     print(f"   ASIN: {item.asin}")
#     print(f"   Title: {safe_get_value(item, 'item_info', 'title')}")
#     print(f"   Brand: {safe_get_value(item, 'item_info', 'by_line_info', 'brand')}")
#     print(f"   Manufacturer: {safe_get_value(item, 'item_info', 'by_line_info', 'manufacturer')}")
#     print(f"   Model: {safe_get_value(item, 'item_info', 'product_info', 'item_dimensions', 'weight')}")
#     print(f"   Detail Page URL: {item.detail_page_url}")
    
#     # Pricing Information
#     print("\n💰 PRICING INFORMATION")
#     if hasattr(item, 'offers') and item.offers:
#         if hasattr(item.offers, 'listings') and item.offers.listings:
#             listing = item.offers.listings[0]
#             print(f"   Current Price: {safe_get_value(listing, 'price', 'display_amount')}")
#             print(f"   Availability: {safe_get_value(listing, 'availability', 'message')}")
#             print(f"   Max Order Quantity: {safe_get_value(listing, 'availability', 'max_order_quantity')}")
#             print(f"   Merchant: {safe_get_value(listing, 'merchant_info', 'name')}")
        
#         if hasattr(item.offers, 'summaries') and item.offers.summaries:
#             summary = item.offers.summaries[0]
#             print(f"   Lowest Price: {safe_get_value(summary, 'lowest_price', 'display_amount')}")
#             print(f"   Highest Price: {safe_get_value(summary, 'highest_price', 'display_amount')}")
#     else:
#         print("   Price: Not available")
    
#     # Classifications & Categories
#     print("\n📂 CLASSIFICATIONS")
#     if hasattr(item, 'item_info') and hasattr(item.item_info, 'classifications'):
#         classifications = item.item_info.classifications
#         print(f"   Product Group: {safe_get_value(classifications, 'product_group')}")
#         print(f"   Binding: {safe_get_value(classifications, 'binding')}")
    
#     # Features
#     print("\n⭐ FEATURES")
#     features = safe_get_value(item, 'item_info', 'features')
#     if features != "N/A" and isinstance(features, list):
#         for i, feature in enumerate(features[:10], 1):  # Limit to first 10 features
#             print(f"   {i}. {feature}")
#     else:
#         print("   No features listed")
    
#     # Technical Information
#     print("\n🔧 TECHNICAL INFORMATION")
#     if hasattr(item, 'item_info') and hasattr(item.item_info, 'technical_info'):
#         tech_info = item.item_info.technical_info
#         if hasattr(tech_info, 'formats') and tech_info.formats:
#             for format_info in tech_info.formats.display_values:
#                 print(f"   Format: {format_info}")
#         if hasattr(tech_info, 'energy_efficiency_class'):
#             print(f"   Energy Efficiency: {safe_get_value(tech_info, 'energy_efficiency_class')}")
    
#     # Dimensions & Weight
#     print("\n📏 DIMENSIONS & WEIGHT")
#     if hasattr(item, 'item_info') and hasattr(item.item_info, 'product_info'):
#         product_info = item.item_info.product_info
#         if hasattr(product_info, 'item_dimensions'):
#             dimensions = product_info.item_dimensions
#             print(f"   Height: {safe_get_value(dimensions, 'height', 'display_value')}")
#             print(f"   Length: {safe_get_value(dimensions, 'length', 'display_value')}")
#             print(f"   Width: {safe_get_value(dimensions, 'width', 'display_value')}")
#             print(f"   Weight: {safe_get_value(dimensions, 'weight', 'display_value')}")
#         if hasattr(product_info, 'package_dimensions'):
#             pkg_dimensions = product_info.package_dimensions
#             print(f"   Package Height: {safe_get_value(pkg_dimensions, 'height', 'display_value')}")
#             print(f"   Package Length: {safe_get_value(pkg_dimensions, 'length', 'display_value')}")
#             print(f"   Package Width: {safe_get_value(pkg_dimensions, 'width', 'display_value')}")
#             print(f"   Package Weight: {safe_get_value(pkg_dimensions, 'weight', 'display_value')}")
    
#     # Content Information
#     print("\n📖 CONTENT INFORMATION")
#     if hasattr(item, 'item_info') and hasattr(item.item_info, 'content_info'):
#         content = item.item_info.content_info
#         print(f"   Edition: {safe_get_value(content, 'edition')}")
#         print(f"   Language: {safe_get_value(content, 'languages', 'display_values')}")
#         print(f"   Pages Count: {safe_get_value(content, 'pages_count')}")
#         print(f"   Publication Date: {safe_get_value(content, 'publication_date', 'display_value')}")
    
#     # Manufacturing Information
#     print("\n🏭 MANUFACTURING INFORMATION")
#     if hasattr(item, 'item_info') and hasattr(item.item_info, 'manufacture_info'):
#         mfg_info = item.item_info.manufacture_info
#         print(f"   Item Part Number: {safe_get_value(mfg_info, 'item_part_number')}")
#         print(f"   Model: {safe_get_value(mfg_info, 'model')}")
#         print(f"   Warranty: {safe_get_value(mfg_info, 'warranty')}")
    
#     # External IDs
#     print("\n🆔 EXTERNAL IDENTIFIERS")
#     if hasattr(item, 'item_info') and hasattr(item.item_info, 'external_ids'):
#         ext_ids = item.item_info.external_ids
#         print(f"   EAN: {safe_get_value(ext_ids, 'eans', 'display_values')}")
#         print(f"   ISBN: {safe_get_value(ext_ids, 'isbns', 'display_values')}")
#         print(f"   UPC: {safe_get_value(ext_ids, 'upcs', 'display_values')}")
    
#     # Content Rating
#     print("\n⚠️ CONTENT RATING")
#     if hasattr(item, 'item_info') and hasattr(item.item_info, 'content_rating'):
#         rating = item.item_info.content_rating
#         print(f"   Audience Rating: {safe_get_value(rating, 'audience_rating')}")
    
#     # Additional dynamic attributes
#     print("\n📦 ADDITIONAL ATTRIBUTES")
#     if hasattr(item, 'item_info'):
#         try:
#             item_dict = item.item_info.to_dict()
#             for key, value in item_dict.items():
#                 if key not in ['title', 'by_line_info', 'features', 'classifications', 
#                               'technical_info', 'product_info', 'content_info', 
#                               'manufacture_info', 'external_ids', 'content_rating']:
#                     if isinstance(value, dict) and 'display_value' in value:
#                         print(f"   {key.replace('_', ' ').title()}: {value['display_value']}")
#         except Exception as e:
#             print(f"   Additional info extraction failed: {e}")
    
#     print_separator()

# def search_products_comprehensive(keyword, min_results=7, max_results=12):
#     """Search Amazon products and display comprehensive information."""
#     try:
#         default_api = DefaultApi(
#             access_key=access_key,
#             secret_key=secret_key,
#             host=host,
#             region=region
#         )

#         # All available search resources for maximum information
#         search_resources = [
#             SearchItemsResource.ITEMINFO_TITLE,
#             SearchItemsResource.ITEMINFO_BYLINEINFO,
#             SearchItemsResource.ITEMINFO_CLASSIFICATIONS,
#             SearchItemsResource.ITEMINFO_CONTENTINFO,
#             SearchItemsResource.ITEMINFO_CONTENTRATING,
#             SearchItemsResource.ITEMINFO_EXTERNALIDS,
#             SearchItemsResource.ITEMINFO_FEATURES,
#             SearchItemsResource.ITEMINFO_MANUFACTUREINFO,
#             SearchItemsResource.ITEMINFO_PRODUCTINFO,
#             SearchItemsResource.ITEMINFO_TECHNICALINFO,
#             SearchItemsResource.ITEMINFO_TRADEININFO,
#             SearchItemsResource.OFFERS_LISTINGS_PRICE,
#             SearchItemsResource.OFFERS_LISTINGS_AVAILABILITY_MAXORDERQUANTITY,
#             SearchItemsResource.OFFERS_SUMMARIES_HIGHESTPRICE,
#             SearchItemsResource.OFFERS_SUMMARIES_LOWESTPRICE,
#             SearchItemsResource.IMAGES_PRIMARY_SMALL,
#             SearchItemsResource.IMAGES_PRIMARY_MEDIUM,
#             SearchItemsResource.IMAGES_PRIMARY_LARGE
#         ]

#         # Randomize the number of results between min and max
#         target_results = random.randint(min_results, max_results)
        
#         request = SearchItemsRequest(
#             partner_tag=partner_tag,
#             partner_type=PartnerType.ASSOCIATES,
#             keywords=keyword,
#             resources=search_resources,
#             marketplace="www.amazon.com",
#             search_index="All",
#             item_count=target_results
#         )

#         print_separator(f"AMAZON PRODUCT SEARCH: '{keyword.upper()}'")
#         print(f"🎯 Fetching {target_results} products with comprehensive details...\n")

#         response = default_api.search_items(request)

#         if response.search_result is not None and response.search_result.items:
#             items = response.search_result.items
#             print(f"✅ Found {len(items)} products")
            
#             # Get detailed information for each product using GetItems API
#             for idx, item in enumerate(items, start=1):
#                 # First display basic search result info
#                 print_comprehensive_product_info(item, idx)
                
#                 # Then get additional detailed info using GetItems API
#                 try:
#                     get_items_resources = [
#                         GetItemsResource.ITEMINFO_TITLE,
#                         GetItemsResource.ITEMINFO_BYLINEINFO,
#                         GetItemsResource.ITEMINFO_CLASSIFICATIONS,
#                         GetItemsResource.ITEMINFO_CONTENTINFO,
#                         GetItemsResource.ITEMINFO_CONTENTRATING,
#                         GetItemsResource.ITEMINFO_EXTERNALIDS,
#                         GetItemsResource.ITEMINFO_FEATURES,
#                         GetItemsResource.ITEMINFO_MANUFACTUREINFO,
#                         GetItemsResource.ITEMINFO_PRODUCTINFO,
#                         GetItemsResource.ITEMINFO_TECHNICALINFO,
#                         GetItemsResource.ITEMINFO_TRADEININFO,
#                         GetItemsResource.OFFERS_LISTINGS_PRICE,
#                         GetItemsResource.OFFERS_LISTINGS_AVAILABILITY_MAXORDERQUANTITY,
#                         GetItemsResource.OFFERS_SUMMARY_HIGHEST_PRICE,
#                         GetItemsResource.OFFERS_SUMMARY_LOWEST_PRICE,
#                         GetItemsResource.PARENTASIN,
#                         GetItemsResource.IMAGES_PRIMARY_SMALL,
#                         GetItemsResource.IMAGES_PRIMARY_MEDIUM,
#                         GetItemsResource.IMAGES_PRIMARY_LARGE,
#                         GetItemsResource.IMAGES_VARIANTS_SMALL,
#                         GetItemsResource.IMAGES_VARIANTS_MEDIUM,
#                         GetItemsResource.IMAGES_VARIANTS_LARGE
#                     ]
                    
#                     detailed_request = GetItemsRequest(
#                         item_ids=[item.asin],
#                         partner_tag=partner_tag,
#                         partner_type=PartnerType.ASSOCIATES,
#                         resources=get_items_resources
#                     )
                    
#                     detailed_response = default_api.get_items(detailed_request)
                    
#                     if (detailed_response.items_result and 
#                         detailed_response.items_result.items):
#                         detailed_item = detailed_response.items_result.items[0]
                        
#                         # Print additional details from GetItems API
#                         print("🔍 ADDITIONAL DETAILED INFORMATION")
#                         if hasattr(detailed_item, 'images') and detailed_item.images:
#                             if hasattr(detailed_item.images, 'primary'):
#                                 print(f"   Primary Image (Large): {safe_get_value(detailed_item.images.primary, 'large', 'url')}")
#                                 print(f"   Primary Image (Medium): {safe_get_value(detailed_item.images.primary, 'medium', 'url')}")
                        
#                         if hasattr(detailed_item, 'parent_asin'):
#                             print(f"   Parent ASIN: {detailed_item.parent_asin}")
                        
#                         print_separator()
                        
#                 except Exception as e:
#                     print(f"   ⚠️ Could not fetch additional details: {e}")
#                     print_separator()
                
#                 print()  # Extra spacing between products

#         else:
#             print("❌ No items found for the keyword:", keyword)

#         if hasattr(response, 'errors') and response.errors:
#             print("\n❌ API ERRORS:")
#             for error in response.errors:
#                 print(f"   {error.code}: {error.message}")

#     except ApiException as e:
#         print(f"❌ API Exception: {e}")
#     except Exception as e:
#         print(f"❌ Unexpected error: {e}")

# def main():
#     """Main function to run the product search."""
#     print("🛒 COMPREHENSIVE AMAZON PRODUCT SEARCH")
#     print("=" * 50)
    
#     if not all([access_key, secret_key, partner_tag]):
#         print("❌ Error: Missing required environment variables.")
#         print("Please ensure AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, and AMAZON_PARTNER_TAG are set in your .env file.")
#         return
    
#     keyword_input = input("🔍 Enter the product search keyword: ").strip()
    
#     if not keyword_input:
#         print("❌ Error: Please enter a valid search keyword.")
#         return
    
#     print(f"\n🚀 Starting comprehensive search for '{keyword_input}'...")
#     search_products_comprehensive(keyword_input)

# if __name__ == "__main__":
#     main()

import os
from dotenv import load_dotenv
from paapi5_python_sdk.api.default_api import DefaultApi
from paapi5_python_sdk.models.search_items_request import SearchItemsRequest
from paapi5_python_sdk.models.search_items_resource import SearchItemsResource
from paapi5_python_sdk.models.get_items_resource import GetItemsResource
from paapi5_python_sdk.models.get_items_request import GetItemsRequest
from paapi5_python_sdk.models.partner_type import PartnerType
from paapi5_python_sdk.rest import ApiException
import random

# Load credentials from .env
load_dotenv()
access_key = os.getenv("AMAZON_ACCESS_KEY")
secret_key = os.getenv("AMAZON_SECRET_KEY")
partner_tag = os.getenv("AMAZON_PARTNER_TAG")

# PAAPI host and region
host = "webservices.amazon.com"
region = "us-east-1"

def print_separator(title="", length=80):
    """Print a formatted separator line."""
    if title:
        padding = (length - len(title) - 2) // 2
        print("=" * padding + f" {title} " + "=" * padding)
    else:
        print("=" * length)

def safe_get_value(obj, *keys):
    """Safely get nested values from objects."""
    try:
        current = obj
        for key in keys:
            if hasattr(current, key):
                current = getattr(current, key)
            elif isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return "N/A"
        
        if hasattr(current, 'display_value'):
            return current.display_value
        elif hasattr(current, 'display_values') and current.display_values:
            return current.display_values
        elif current is not None:
            return str(current)
        else:
            return "N/A"
    except:
        return "N/A"

def has_data(obj, *keys):
    """Check if nested data exists and is not empty."""
    try:
        current = obj
        for key in keys:
            if hasattr(current, key):
                current = getattr(current, key)
            elif isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return False
        
        if hasattr(current, 'display_value'):
            return current.display_value and current.display_value != "N/A"
        elif hasattr(current, 'display_values'):
            return current.display_values and len(current.display_values) > 0
        elif current is not None:
            return str(current) != "N/A" and str(current).strip() != ""
        else:
            return False
    except:
        return False

def print_section_if_has_data(title, emoji, data_checks):
    """Print a section only if it has actual data."""
    has_any_data = False
    section_content = []
    
    for label, obj, *keys in data_checks:
        if has_data(obj, *keys):
            value = safe_get_value(obj, *keys)
            if isinstance(value, list):
                if len(value) > 0:
                    section_content.append((label, value))
                    has_any_data = True
            else:
                section_content.append((label, value))
                has_any_data = True
    
    if has_any_data:
        print(f"\n{emoji} {title}")
        for label, value in section_content:
            if isinstance(value, list):
                if label == "Features":
                    for i, feature in enumerate(value[:10], 1):
                        print(f"   {i}. {feature}")
                else:
                    formatted_value = ", ".join(str(v) for v in value)
                    print(f"   {label}: {formatted_value}")
            else:
                print(f"   {label}: {value}")

def print_comprehensive_product_info(item, product_num):
    """Print comprehensive A-Z product information."""
    print_separator(f"PRODUCT #{product_num}")
    
    # Basic Information - Always show
    print("🔍 BASIC INFORMATION")
    print(f"   ASIN: {item.asin}")
    print(f"   Title: {safe_get_value(item, 'item_info', 'title')}")
    print(f"   Detail Page URL: {item.detail_page_url}")
    
    # Brand & Manufacturer Info
    brand_data = [
        ("Brand", item, 'item_info', 'by_line_info', 'brand'),
        ("Manufacturer", item, 'item_info', 'by_line_info', 'manufacturer'),
        ("Author", item, 'item_info', 'by_line_info', 'author'),
        ("Contributors", item, 'item_info', 'by_line_info', 'contributors')
    ]
    print_section_if_has_data("BRAND & CREATOR INFORMATION", "🏢", brand_data)
    
    # Classifications & Categories
    classification_data = [
        ("Product Group", item, 'item_info', 'classifications', 'product_group'),
        
    ]
    print_section_if_has_data("CLASSIFICATIONS", "📂", classification_data)
    
    # Features
    if has_data(item, 'item_info', 'features'):
        features = safe_get_value(item, 'item_info', 'features')
        if isinstance(features, list) and len(features) > 0:
            print("\n⭐ FEATURES")
            for i, feature in enumerate(features[:10], 1):
                print(f"   {i}. {feature}")
    
    # Technical Information
    tech_data = [
        ("Format", item, 'item_info', 'technical_info', 'formats'),
        ("Energy Efficiency", item, 'item_info', 'technical_info', 'energy_efficiency_class')
    ]
    print_section_if_has_data("TECHNICAL INFORMATION", "🔧", tech_data)
    
    # Dimensions & Weight
    dimension_data = [
        ("Height", item, 'item_info', 'product_info', 'item_dimensions', 'height'),
        ("Length", item, 'item_info', 'product_info', 'item_dimensions', 'length'),
        ("Width", item, 'item_info', 'product_info', 'item_dimensions', 'width'),
        ("Weight", item, 'item_info', 'product_info', 'item_dimensions', 'weight'),
        ("Package Height", item, 'item_info', 'product_info', 'package_dimensions', 'height'),
        ("Package Length", item, 'item_info', 'product_info', 'package_dimensions', 'length'),
        ("Package Width", item, 'item_info', 'product_info', 'package_dimensions', 'width'),
        ("Package Weight", item, 'item_info', 'product_info', 'package_dimensions', 'weight')
    ]
    print_section_if_has_data("DIMENSIONS & WEIGHT", "📏", dimension_data)
    
    # Content Information
    content_data = [
        ("Edition", item, 'item_info', 'content_info', 'edition'),
        ("Languages", item, 'item_info', 'content_info', 'languages'),
        ("Pages Count", item, 'item_info', 'content_info', 'pages_count'),
        ("Publication Date", item, 'item_info', 'content_info', 'publication_date')
    ]
    print_section_if_has_data("CONTENT INFORMATION", "📖", content_data)
    
    # Manufacturing Information
    manufacturing_data = [
        ("Item Part Number", item, 'item_info', 'manufacture_info', 'item_part_number'),
        ("Model", item, 'item_info', 'manufacture_info', 'model'),
        ("Warranty", item, 'item_info', 'manufacture_info', 'warranty')
    ]
    print_section_if_has_data("MANUFACTURING INFORMATION", "🏭", manufacturing_data)
    
    # External IDs
    external_id_data = [
        ("EAN", item, 'item_info', 'external_ids', 'eans'),
        ("ISBN", item, 'item_info', 'external_ids', 'isbns'),
        ("UPC", item, 'item_info', 'external_ids', 'upcs')
    ]
    print_section_if_has_data("EXTERNAL IDENTIFIERS", "🆔", external_id_data)
    
    # Content Rating
    rating_data = [
        ("Audience Rating", item, 'item_info', 'content_rating', 'audience_rating')
    ]
    print_section_if_has_data("CONTENT RATING", "⚠️", rating_data)
    
    # Images
    image_data = [
        ("Primary Image (Large)", item, 'images', 'primary', 'large', 'url'),
        ("Primary Image (Medium)", item, 'images', 'primary', 'medium', 'url'),
        ("Primary Image (Small)", item, 'images', 'primary', 'small', 'url')
    ]
    print_section_if_has_data("IMAGES", "🖼️", image_data)
    
    # Trade-in Information
    trade_data = [
        ("Trade-in Eligible", item, 'item_info', 'trade_in_info', 'is_eligible_for_trade_in'),
        ("Trade-in Price", item, 'item_info', 'trade_in_info', 'price')
    ]
    print_section_if_has_data("TRADE-IN INFORMATION", "💱", trade_data)
    
    print_separator()

def search_products_comprehensive(keyword, min_results=10, max_results=12):
    """Search Amazon products and display comprehensive information."""
    try:
        default_api = DefaultApi(
            access_key=access_key,
            secret_key=secret_key,
            host=host,
            region=region
        )

        # All available search resources for maximum information (excluding pricing)
        search_resources = [
            SearchItemsResource.ITEMINFO_TITLE,
            SearchItemsResource.ITEMINFO_BYLINEINFO,
            SearchItemsResource.ITEMINFO_CLASSIFICATIONS,
            SearchItemsResource.ITEMINFO_CONTENTINFO,
            SearchItemsResource.ITEMINFO_CONTENTRATING,
            SearchItemsResource.ITEMINFO_EXTERNALIDS,
            SearchItemsResource.ITEMINFO_FEATURES,
            SearchItemsResource.ITEMINFO_MANUFACTUREINFO,
            SearchItemsResource.ITEMINFO_PRODUCTINFO,
            SearchItemsResource.ITEMINFO_TECHNICALINFO,
            SearchItemsResource.ITEMINFO_TRADEININFO,
            SearchItemsResource.IMAGES_PRIMARY_SMALL,
            SearchItemsResource.IMAGES_PRIMARY_MEDIUM,
            SearchItemsResource.IMAGES_PRIMARY_LARGE
        ]

        # Randomize the number of results between min and max
        target_results = random.randint(min_results, max_results)
        
        request = SearchItemsRequest(
            partner_tag=partner_tag,
            partner_type=PartnerType.ASSOCIATES,
            keywords=keyword,
            resources=search_resources,
            marketplace="www.amazon.com",
            search_index="All",
            item_count=target_results
        )

        print_separator(f"AMAZON PRODUCT SEARCH: '{keyword.upper()}'")
        print(f"🎯 Fetching {target_results} products with comprehensive details...\n")

        response = default_api.search_items(request)

        if response.search_result is not None and response.search_result.items:
            items = response.search_result.items
            print(f"✅ Found {len(items)} products")
            
            # Get detailed information for each product using GetItems API
            for idx, item in enumerate(items, start=1):
                # First display basic search result info
                print_comprehensive_product_info(item, idx)
                
                # Then get additional detailed info using GetItems API
                try:
                    get_items_resources = [
                        GetItemsResource.ITEMINFO_TITLE,
                        GetItemsResource.ITEMINFO_BYLINEINFO,
                        GetItemsResource.ITEMINFO_CLASSIFICATIONS,
                        GetItemsResource.ITEMINFO_CONTENTINFO,
                        GetItemsResource.ITEMINFO_CONTENTRATING,
                        GetItemsResource.ITEMINFO_EXTERNALIDS,
                        GetItemsResource.ITEMINFO_FEATURES,
                        GetItemsResource.ITEMINFO_MANUFACTUREINFO,
                        GetItemsResource.ITEMINFO_PRODUCTINFO,
                        GetItemsResource.ITEMINFO_TECHNICALINFO,
                        GetItemsResource.ITEMINFO_TRADEININFO,
                        GetItemsResource.PARENTASIN,
                        GetItemsResource.IMAGES_PRIMARY_SMALL,
                        GetItemsResource.IMAGES_PRIMARY_MEDIUM,
                        GetItemsResource.IMAGES_PRIMARY_LARGE,
                        GetItemsResource.IMAGES_VARIANTS_SMALL,
                        GetItemsResource.IMAGES_VARIANTS_MEDIUM,
                        GetItemsResource.IMAGES_VARIANTS_LARGE
                    ]
                    
                    detailed_request = GetItemsRequest(
                        item_ids=[item.asin],
                        partner_tag=partner_tag,
                        partner_type=PartnerType.ASSOCIATES,
                        resources=get_items_resources
                    )
                    
                    detailed_response = default_api.get_items(detailed_request)
                    
                    if (detailed_response.items_result and 
                        detailed_response.items_result.items):
                        detailed_item = detailed_response.items_result.items[0]
                        
                        # Print additional details from GetItems API if available
                        additional_data = []
                        
                        if hasattr(detailed_item, 'parent_asin') and detailed_item.parent_asin:
                            additional_data.append(("Parent ASIN", detailed_item.parent_asin))
                        
                        if hasattr(detailed_item, 'images') and detailed_item.images:
                            if hasattr(detailed_item.images, 'primary'):
                                if hasattr(detailed_item.images.primary, 'large') and detailed_item.images.primary.large:
                                    additional_data.append(("Primary Image (Large)", detailed_item.images.primary.large.url))
                        
                        if additional_data:
                            print("🔍 ADDITIONAL DETAILED INFORMATION")
                            for label, value in additional_data:
                                print(f"   {label}: {value}")
                        
                except Exception as e:
                    print(f"   ⚠️ Could not fetch additional details: {e}")
                
                print()  # Extra spacing between products

        else:
            print("❌ No items found for the keyword:", keyword)

        if hasattr(response, 'errors') and response.errors:
            print("\n❌ API ERRORS:")
            for error in response.errors:
                print(f"   {error.code}: {error.message}")

    except ApiException as e:
        print(f"❌ API Exception: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

def main():
    """Main function to run the product search."""
    print("🛒 COMPREHENSIVE AMAZON PRODUCT SEARCH")
    print("=" * 50)
    
    if not all([access_key, secret_key, partner_tag]):
        print("❌ Error: Missing required environment variables.")
        print("Please ensure AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, and AMAZON_PARTNER_TAG are set in your .env file.")
        return
    
    keyword_input = input("🔍 Enter the product search keyword: ").strip()
    
    if not keyword_input:
        print("❌ Error: Please enter a valid search keyword.")
        return
    
    print(f"\n🚀 Starting comprehensive search for '{keyword_input}'...")
    search_products_comprehensive(keyword_input)

if __name__ == "__main__":
    main()