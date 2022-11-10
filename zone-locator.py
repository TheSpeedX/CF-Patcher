import requests


headers = {
    "X-Auth-Email": "email",
    "X-Auth-Key": "key",
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


domain = "example.com"
zones = get_zones()
for zone in zones:
    if zone["name"] == domain:
        print("ZONE ID: ", zone["id"])
        records = get_dns_records(zone["id"])
        for record in records:
            print(record["name"], record["id"])
        break
