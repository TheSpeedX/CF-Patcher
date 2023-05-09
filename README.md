# 🚀 CF-Patcher

CF-Patcher is a tool that allows you to update DNS entries, even if you have a dynamic IP address. This is commonly known as DynDNS. This tool requires a Cloudflare account to manage your domain's DNS records.

## 📋 Requirements

In order to use CF-Patcher, you will need:

A Cloudflare account where you manage your domain with DNS records
A Global API Key
## 🛠️ Installation

Follow these steps to install CF-Patcher:

Clone this project to your computer:

``git clone https://github.com.0n1cOn3/CF-Patcher
cd CF-Patcher``

## Build the Docker image:

``sudo docker build -t CF-Patcher``

## Start the Docker container:
``sudo docker compose up -d``
## ⚙️ Configuration

To configure CF-Patcher, you will need 

- Run zone-locator.py:
- Get the Global API Key from Cloudflare.

Fill in your email and API key in zone-locator.py, along with your domain name.

> Run zone-locator.py, and you will get all DNS records for that domain.
Take a note of ZONE ID and the DNS RECORD ID if you want to update them.

> Edit config.json:
Enter your email, zone ID, API key, DNS record ID, and whatever domain/subdomain you want to regularly update.
Save the file and start the Docker image.

## ⏰ Changing the IP Check Time

The IP check is set to 15 minutes by default. You can adjust this in main.py under the variable:

``print("Sleeping for 15 minutes") time.sleep(60 * 15)``
