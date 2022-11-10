#!/usr/bin/env python3

import CloudFlare
import json
import requests
import time

config = json.load(open("config.json"))


def get_public_ip():  # sourcery skip: raise-specific-error
    endpoint = "https://ipinfo.io/json"
    response = requests.get(endpoint, verify=True)

    if response.status_code != 200:
        raise Exception(f"Status: {response.status_code}")

    data = response.json()
    return data["ip"]


class CloudflarePatcher:
    def __init__(self, account) -> None:
        self.cf = CloudFlare.CloudFlare(account["email"], account["api_key"])
        self.account = account
        self.zone_id = account["zone_id"]

    def load_variables(self):
        self.variables = {}
        for variable in self.account["variables"]:
            self.variables[variable] = globals()[f"get_{variable}"]()
        print("New Variables:", self.variables)

    def parse_record(self, record):
        record_str = json.dumps(record)
        for variable in self.variables:
            record_str = record_str.replace(
                "{{" + variable + "}}", self.variables[variable]
            )
        return json.loads(record_str)

    def patch_dns_records(self):
        for dns_record in self.account["dns_records"]:
            record = self.parse_record(dns_record["value"])
            try:
                self.cf.zones.dns_records.patch(
                    self.zone_id, dns_record["id"], data=record
                )
                dns_record["value"] = record
                print(f"Updated {dns_record}")
            except Exception as e:
                exit(f"/zones.dns_records.patch {dns_record} - {e}")


def main():
    last_ip = None
    while True:
        curr_ip = get_public_ip()
        if curr_ip != last_ip:
            for account in config:
                patcher = CloudflarePatcher(account)
                patcher.load_variables()
                patcher.patch_dns_records()
            last_ip = curr_ip
        time.sleep(60 * 15)


if __name__ == "__main__":
    main()
