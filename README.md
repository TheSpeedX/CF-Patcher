# CF-Patcher

CF patchers were written by my colleague SpeedX.

CF-Patcher allows updating the DNS entries even if a Dynamic IP is given. Also better known as DynDNS.

## Requirements

- a Cloudflare account where you manage your domain with DNS records.

- Global API Key from your Cloudflare account

- Email address you use at Cloudflare

- Docker & Docker-Compose

This repo contains a build file for Docker & Docker Compose.

## Build

Clone this project to your computer:

> git clone https://github.com.0n1cOn3/CF-Patcher

> cd CF-Patcher

> sudo docker build -t CF-Patcher

> sudo docker compose up -d

## Configure

zone-locator.py:
1. Get the Global API Key from Cloudflare 
2. fill your email and api key in zone-locator.py and your domain name 
3. Run zone-locator.py and you will get all DNS records for that domain

Take a note of ZONE ID and the DNS RECORD ID if you wanna update.

config.json:
1. Enter your email, zone_id, api_key, dns_record id and whatever domain/subdomain you wanna regulary update.
2. Save it and start building the container

## Change IP Check time

The IP check is set to 15min. 
This can be adjusted in main.py under the variable:

> print("Sleeping for 15 minutes")
> time.sleep(60 * 15)
