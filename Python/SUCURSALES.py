
import sys
import requests
import json

url_accessToken = "https://connect.bbva.com/token?grant_type=client_credentials"

urlbranches = "https://apis.bbvabancomer.com/locations_sbx/v1/branches"

access_token = "eyJ6aXAiOiJERUYiLCJlbmMiOiJBMTI4R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.tSrnmVa9bc4921-H05gs-GnRWjVMxAe12FnvXDU_8bYISVHLJdz5sUpkwwbaAU3KBURYLtuemLpM9fcCcKkeyEFtR4OzRIyzTI-vFD3xupDzC6v8_-tL8mQUJKyxSPYUIA-Qdv1gseqNHcaVXH-mJe4JesgZBuV9RncuNbUW9xG6_VRRbUq2HYPttHSktp3kiRdILb33t7guNnVlph43rhju1p79TijRFBU0TGW-8fS24XYrP225Z6lGHSv4wn0wl0GSUio-oFP8fFq7a0oLWywIiSDOZ4urj0bxcm2LH9dppP7esT1_Y7Yjf9lsOWiKsNHsyJwvmEBLppTStnue9g.oBYcg_UTdnv6A6pO.WwQFgQrpLK_phs6TCfmL6m7LGLxi4GQ8D5fI6GB13ZzU3cIhrdLsfD_fVswK_zwNGDOE2LCkX969CJP9Ad411zESja90Bqo9ypsL6hlpNgvogWOLrWR0-VoooBGwa6OKCtdA8XhJAO1Ar5dE_VxbOsQS84Z0kLNGR-PhLA7JxnCq-6tVXIiZqzqEmeiMEqIv8EFczsfghuEtmWr-yj51LZm-mDTLETdI.uwLe_p8bWzTzvR5jPZZxYw"


def get_json():

	headers = {
			   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
			   'Authorization' : 'jwt ' + access_token,
			   "Content-Type" : "application/json"}
	r = requests.get(urlbranches, headers=headers)
	return r.json()


v = get_json()

print(v)
