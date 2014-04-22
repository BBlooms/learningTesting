
KRAKEN_URL = "https://api.kraken.com/0"
KR_API_KEY = "h4rxw48aAL8Ace8yNM0NdaCmS3vM1KF6O2G929fr1yslAIpGS9sdmjP+"
KR_API_SECRET = "m6N+pw3doarbrMxxkYx1t4QtZ/cNB9rvRGR2a94sp7A/suMc/4Y5OnZPQk++gXzxwTt2Qg2mVKyhFApSpe1M9w=="

urlpath = KRAKEN_URL + "/private/Balance"

req = {}
nonce = int(time.time())
req['nonce'] = nonce
postdata = urllib.urlencode(req)
message = urlpath + hashlib.sha256(str(req['nonce']) +
                                   postdata).digest()
signature = hmac.new(base64.b64decode(KR_API_SECRET),
                     message, hashlib.sha512)
headers = {
    'API-Key': KR_API_KEY,
    'API-Sign': base64.b64encode(signature.digest())
}
payload = {'nonce': nonce}

r = requests.post(urlpath, headers = headers, data = payload)
print r.text