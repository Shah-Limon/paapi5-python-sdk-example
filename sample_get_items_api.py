# -*- coding: utf-8 -*-
"""
 Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

 Licensed under the Apache License, Version 2.0 (the "License").
 You may not use this file except in compliance with the License.
 A copy of the License is located at

      http://www.apache.org/licenses/LICENSE-2.0

 or in the "license" file accompanying this file. This file is distributed
 on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 express or implied. See the License for the specific language governing
 permissions and limitations under the License.
"""

import os
from paapi5_python_sdk.api.default_api import DefaultApi
from paapi5_python_sdk.models.condition import Condition
from paapi5_python_sdk.models.get_items_request import GetItemsRequest
from paapi5_python_sdk.models.get_items_resource import GetItemsResource
from paapi5_python_sdk.models.partner_type import PartnerType
from paapi5_python_sdk.rest import ApiException

def parse_response(item_response_list):
    """
    The function parses GetItemsResponse and creates a dict of ASIN to Item object
    :param item_response_list: List of Items in GetItemsResponse
    :return: Dict of ASIN to Item object
    """
    mapped_response = {}
    for item in item_response_list:
        mapped_response[item.asin] = item
    return mapped_response


def get_product_info():
    """
    This function prompts the user for an ASIN and fetches its product information
    using the Amazon Product Advertising API.
    """
    # --- Step 1: Securely Get Credentials & Partner Tag from Environment Variables ---
    try:
        access_key = os.environ['PAAPI_ACCESS_KEY']
        secret_key = os.environ['PAAPI_SECRET_KEY']
        partner_tag = os.environ['PAAPI_PARTNER_TAG']
    except KeyError:
        print("Error: Make sure you have set PAAPI_ACCESS_KEY, PAAPI_SECRET_KEY, and PAAPI_PARTNER_TAG environment variables.")
        return

    # --- Step 2: Set API Host and Region ---
    host = "webservices.amazon.com"
    region = "us-east-1"

    # --- Step 3: Initialize the API ---
    default_api = DefaultApi(
        access_key=access_key, secret_key=secret_key, host=host, region=region
    )

    # --- Step 4: Get ASIN from User Input ---
    # The API expects a list of item IDs.
    asin = input("Please enter the product ASIN and press Enter: ")
    if not asin:
        print("ASIN cannot be empty.")
        return
    item_ids = [asin]


    # --- Step 5: Define the Product Information to Retrieve ---
    # We are requesting comprehensive details about the product.
    get_items_resource = [
        GetItemsResource.ITEMINFO_TITLE,
        GetItemsResource.ITEMINFO_FEATURES,
        GetItemsResource.ITEMINFO_MANUFACTURE,
        GetItemsResource.OFFERS_LISTINGS_PRICE,
        GetItemsResource.IMAGES_PRIMARY_LARGE,
        GetItemsResource.ITEMINFO_CONTENT_INFO,
        GetItemsResource.ITEMINFO_PRODUCT_INFO,
        GetItemsResource.ITEMINFO_TECHNICAL_INFO,
        GetItemsResource.BROWSENODEINFO_WEBSITESSALESRANK,
    ]

    # --- Step 6: Form and Send the Request ---
    try:
        get_items_request = GetItemsRequest(
            partner_tag=partner_tag,
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com",
            condition=Condition.NEW,
            item_ids=item_ids,
            resources=get_items_resource,
        )
    except ValueError as exception:
        print("Error in forming GetItemsRequest: ", exception)
        return

    try:
        # Send the request to the API
        response = default_api.get_items(get_items_request)
        print("\nAPI called Successfully!")

        # --- Step 7: Parse and Display the Response ---
        if response.items_result is not None and response.items_result.items:
            print("\n--- Product Information ---")
            item = response.items_result.items[0]

            # Display basic info
            if item.asin: print(f"ASIN: {item.asin}")
            if item.detail_page_url: print(f"URL: {item.detail_page_url}")

            # Display Title
            if item.item_info and item.item_info.title and item.item_info.title.display_value:
                print(f"Title: {item.item_info.title.display_value}")

            # Display Price
            if item.offers and item.offers.listings and item.offers.listings[0].price:
                print(f"Price: {item.offers.listings[0].price.display_amount}")

            # Display Features (bullet points)
            if item.item_info and item.item_info.features and item.item_info.features.display_values:
                print("\nFeatures:")
                for feature in item.item_info.features.display_values:
                    print(f"- {feature}")

            # Display Manufacturer
            if item.item_info and item.item_info.manufacture and item.item_info.manufacture.display_value:
                print(f"\nManufacturer: {item.item_info.manufacture.display_value}")
            
            # Display Primary Image URL
            if item.images and item.images.primary and item.images.primary.large:
                print(f"Image URL: {item.images.primary.large.url}")


        # Handle any errors returned by the API
        if response.errors is not None:
            print("\nAPI Errors:")
            for error in response.errors:
                print(f"- Code: {error.code}, Message: {error.message}")

    except ApiException as exception:
        print("\n--- ERROR ---")
        print("Error calling PA-API 5.0!")
        print("Status code:", exception.status)
        print("Errors :", exception.body)
        print("Request ID:", exception.headers["x-amzn-RequestId"])
    except Exception as exception:
        print("An unexpected error occurred:", exception)


# --- Run the main function ---
if __name__ == "__main__":
    get_product_info()