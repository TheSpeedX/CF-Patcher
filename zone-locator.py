#!/usr/bin/env python3

import requests

DOMAIN = "example.com"
EMAIL = "email@mail.com"
API_KEY = "api_key"

headers = {
    "X-Auth-Email": EMAIL,
    "X-Auth-Key": API_KEY,
}


def get_zones():
    response = requests.get(
        "https://api.cloudflare.com/client/v4/zones", headers=headers
    )
    return response.json()["result"]


def get_dns_records(zone_id):
    response = requests.get(
        f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records",
        headers=headers,
    )
    return response.json()["result"]


zones = get_zones()
for zone in zones:
    if zone["name"] == DOMAIN:
        print("ZONE ID: ", zone["id"])
        records = get_dns_records(zone["id"])
        for record in records:
            print(record["type"], record["name"], record["id"])
        break
