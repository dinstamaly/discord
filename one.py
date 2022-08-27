import requests

from password import generate_password

user_email = input("email: ")
user_name = input("name: ")
user_password = generate_password()

api_key = "bf41b8358a863d234cfcd2a49e922593"
capcha_key = "P0_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiT2tXNWJwdTFVd1UrSHMrSFFidDRNaW91bmVpZjE4M0ZyZlVrVGw4M21mY3pkRjZ1TkgrY3pYTjU2QWFqWnFPVVhNb0JqbnZoVGMwL2E0b3EyVjFnaG9aQ3RCbDJUQ0xqSWNjOWFIcitKY3RVYms5OSs1VTEzbGV5U1A5SVhMQ2FQbGlYTDhXZU5HTGFsbFFYeWlhQ2s2OVRBWFFCTGNCQkQ0Zk8zZlZxQVFZdCtLTDhQTWk1QnlUaW54czBQdTVVZ1ZVdGN6QzNvVXVKVS9Vd1M1QWhrYTFxZ3orYWtXQWZuWGp0WDdKeE5Qa04yMzVXaW1NV05mcmYwU09hczJwQWpwS3JoVGNvWGpXRXR5Q2pTTUlJaGlteUhOWlpmWCtRaFMwY0RkWGZOcE1rQyt2RS94bzFLaTQ0bDRIYTF5Zyt0SDVHVFNYUU0zVWZYaUoyelNoUlJTanZtc2VYK1g1VVhrVkdrTTI4aDBLQnBqcVhoekoyUEpFbUhqa1JTVy9GQkZRcnRKUUNJT1ZpdHY5Y1JmVXUvMjYxaW5qMGt0UnhrMVVJRWdDKzJQOEJhN3hCVVo4NnA5WXp5WGJpZUtUZjRnUUMwQjE5R3k4eEVORDdsVG9EREYvaFBaWFowYjZGdnR2WDY5VXhFNGVEdjhpWGR2OGRKN1c3aWxYYUpBS3VCZ1hxQUsvTSszcUQ5MC9NZnZla0ZyL3E5T0UwQlZZaDRmcGpsZ2wxMUE4b0t1Yi9sUUlmVXdUYXdLS1EwN3hzTktUR1hSNUc4RDZHN0ZOSGVyMnBabEVpSzJUWWhxblRhZmg0a2d0OW83ZFdMdFBaNFRFQ1hnVWgxK213a1F4bWJYeDVjUW1VNXNEM3QrQmJGRWhLL0M3VGhEbWR1d01ZUGMwSE94WHB5QWFQck8vRXI2RFdETDdMMVVNd2pSdWdUendMMnZMWXI5aW5UcGF6Z0FQSGlhT2ZJM2FjYUY3aGV1MWhzQ2RlVHIzRDN6blJFVDFDMDlnTEdNQmg5Z0tERlNNaHNCNmFjYzh6SDFRVU9BU0dhdUNuREUyc0pQRCsvUlI1UzRUMTM0TnRaUkpkUmtMTkpEMXYyd3U2Uit6T3FqRG5CRHBDVFZJdzBWZHpVM24zbWl0RHRraEZoTTBCMWFRa3BramVPb0xad082bXZiNUppWng1VDJmcVJrNkRSRE1OempzbUUzVktyNm40cEJTTVpTZUdjcGUzU1p0NUYrd3QyMTFMR05FTVFSb3l3d3NNUklRVG85SjFCWlpWZmRESlNjVVRrL0F4NHBRVG9xd1Y5dU15a0ZVQzVxdUZ5anJ0aEljUXhDN2tFK3lBU3lNS2x1UU9DQk9TMW9wR0FaVm5uOUlRcmNsRm90V3VTY0h4Q1kwbjl6cWo0UU1DUE11Ni9ZcGhxa2xmKzg2RktkZzhzSjgyMnVFVE9aKzhBVkRJUTBZNk5FRUJkbktUNTZWMTZzUWtKMHFFYXlCZ0t0eEFLQ0JrWlFuVDhwRzNpNUVva2V0UU1JWWo2MG8rclpWVVRRSFpzRGZDSDRSN0tEcjd6bWFKZENuYkowNnFrdm9aMTRheWpVOHVPNUFyL1Q0T0x3a0xHbmg5OE5UVDY3cXRnN1RSbjRIUWZpNmhhbWhmajFDNEZHdnJqbHVEdkxxbjJ6UzJUeGlwc0ttTWxsR1VsYTlBcVRyR2VGbFh6bE0yNEF3TEY1NkJ5ODZPMXZMbkoxM3YyUWxmMDhGWFl3LzdHOWRtUjVtZzJBVVZ4VXdIMXpvd3NqR2IxNk0yMWJPQmtqbTd4cFViOEJrbnlnWlJkelZBK2NMdXd5cENnU3pzMERFVWQ4SWFrbTQ2MisvNUxZaHBhZndNNmdFM1hHNGdiZDloQ1p2N0J1amhNaTZhdnpETWVFTlViOGRDcHhMRVdsZnU1UE1tbldzb0ZjVVZkOHRXWVo0c2pDMThyMW4xcFA4OG8wVnRDdkN4dEtzT053Y2ovdFVPMVU5bDZIZVZaRHJVd0FUZkZyUU5kVW5GTGlReVZFMURIT21FTHhpR0gzNjJHeUc2bjlvc1FWYWN3bnVTenczQVhoZDdVQjRhbDNXc1lrMzI3SGI4bEdrTFdxVXEweVJsTXBWamZRTk15a1JpdXdKbDRFWFgxSk1CRVJmd2VFNTROMm1ZY3BFdEpHNElLc1oyclJTUEpndGE3UDVTYXF6OVJVQVJyRUpzd1FkR0tFL1UzNmRiMkRmR1N3QWROZ1dLK0k4MVgrWUkxRWE2dTNFeDdvUk0wTjF5RlNiSEZxcGw1TUdqUlVTUVZEaXhCRXlKSURSNmppSUo5YldMN1dzRHk0dHJyUXJ0VVNVWEdpQlkyUUxyckl4K1dxNEorckM2eDJzRloyblVrUFZYSEQrME5UeDlSVGZQNVJJclhYTllJNTRsRHYrOXhoWSt4ZjI1dTNUVTZKOGtMMy9OVzZ4Q2dSem1aRkQyUkNNTXF6NHY4a2hhTml5RkFSRk8yc1oyWjRtYkd1ZXRraU5peVVTV050cDRwak0vVG0xeEN2Sm1xTTNoZmh6YjkwNVMrVlhNOVdPVWJQaGZhbm9DalUrWm5HMm1paG5lOWgvak82VzgwczN3cU9COHFkd1pWZDN2VXJtbnkxU3JOeHNtUVBpZElUUEJBNDkzbzUrVjZvRTU3dXRIUEptd1Z5bndUaTllT09wak40VVdDeWJyeXJkZEFqbzdGdzdlNjdBd1VKZzN1ZWdOeVljT0hDRXgvSGl3ekhkbXRjWjJWcmRVZE9PT2FXVXFqbkQreGY1OFdyTFNlRWVEMEUrQkpRT2M2LytRSEl3clA1TmFGSTFXNzkxNDg4b1Z4aFFVNzRpb0hlZEcxVGNKd2lSdEpodURDS1JSSGhCZDBYOFRrZVpCa0RKbFN3bmdRNURsb0FubmY0WE45Y2cxVVZzWGp0YWVxOXRkdTdJWldZdWJWUkd0bW05NXlJVkVzdnlwcGo0WEN4YzNFc3R3TG5mTkljeGtyTUlNaUJqRyt0NkpPd0YvNy9Xem5LQ0NnYnppd0kxZmEwSDhJUUUrSXhMWDlyZU1GVTNreEtzcnJseStMeUZWUEhhSHBWR3VQS002bG9KelZjcnBSMjJEemM0dmpleGlXUUVPU0JkTUtnM0JGdE52T0x3Wkl5dTJxWVlLTmZOV2xaRDdCS0dHdmlaMGloZDRVTnp2MVRxaFlOZ0pzZ3dOdnZ2K3U4T2hNSGtESWVmdGFOZ1hmQ3VFQXJzank2eC9CTldWemp5eG80VC93TERvSzZPWkNtMlh5VWdpU1RHalBKTHBjTThaWWFsZGZ3R0RzNmlCbzZrYTZtdlpZSDhKS3RIMHEwM1Z3ZUdLLzh2SFNLN3luMkNyWGdKZTk0RXRSVTUrWjZPNlRyclM0VUdhVndIb0ZUU3diSldlaHVhQTlrMUpKbnV1L0pkK1dMbWxNdHJJelNRRmllQm5va0tOTDYvNm5rcXJJSnhwTjZoQ2hnY21oZktnMFJLMVNMUlIrNEhzWm5ETUhmMDNQem1xWFlpRTBTaG5hVWtDdHJRS1BraVVpb3JuOEl5WVVlMXhVbzdwY1Y3eXRlZS9ibUd3ZzRKTUhtbERiVGdQZ1UwSUZJTHVRSFZiWXBmTWozOTdzSWd4SW94N0FaT3ZIT1NIZU1CMVlydTEvaHA4cW9XK095UHdFU2d1NWZSNUQ5UXNiK0pXejU5RHdiazBWK3ZnN1FBRHM2Rk9uekZJYUVZVnVyeXJHNDl5UCthbldoUG9sbjc1ZTJxYWp2NHd3aVc2K0cwRGlnVENFQmhJaGpSM1REVVhOWGdNMmplQUNwS2M1OFQ4WDVYdWs0a0RkMi9YZGE4UVpaeVZtcFl6akFqdzNDd0R2UVRPSnp2ZVBJa0ZUUHlIc3lqWithWWxlSXEzVXZSazdVSU5LRGFUS2MyV1pDdUxYVGhUTTVXU0pSSTJpdWtnN1QrN3p1aFRKZWFrMGR2WXlKOWlBb2dqRXdXQ2NHNUg3bzc4VFNIK3U4V2pzVVpaZ3IzeEZWcE02cmhndW9PdDV6UlF0ODE5eVN6aEwwd2tMQXRabXRhVnE3VmZkMXlrTldHZ3dxZE41TE90N29TUDFpaC9BVEtQQlliM2dneGxPeFdPMjA2bHRBSVlnSjJUVEt4UDljaXM4Y2dyMFFISDBiZUFkeTZWU1U2ZFdpTUNlWXR4Z29ETGlIbzdTVzVXWTZLMUxlK09lL3JLQkgwQ01nb3NTcitadFNrcEFZSlVhbk5mYXhMUmJvdDBJMHZHWXRUUitUTmxLN2sxcHlHSkd4aW4yQW9OWExUZVAzSllSQ1lZcjlzSnF0V3pSdWltZWh2SUdaU0YvU0lzZVJISG1ncWpBS1JSVjNtV1Y4aEF0V3JzQzdjd0VwLzBXQjA3K3dkY3E0NDRVTmhjT01uWXozbGNjMGkxdTRpdnZOc3NJN3NONERyeGZOdkxHcUNaQ2x2OXBCdmlUc2VNZ0RtSFBSajBmeWdibE1OU08vSlpDRkc1UnFrYXlLNHBwTWl5WHR0VTRrL01MNS9Kc2ZvUVpuOXROa0l6TU9iNTJaMldhditXS0FLTDdGNTB4MDFsTmNSVTJ3bUoyY3dVenZ0SlloQ05EeVlLajl3dHlIZG0vOWl2dllFN3Q2YndiZGVxWXRyMWpsNm5vSWFTMHZTK1RLOUh2bkxaVzNQaXpncDNVZUJ3U0ludFlqT01xcVVXbm5IdjVKQzcvOUlBUElteXZZeU9JNTlOMlhkTnkyZW5USW9GTFp0WG45a1pwNGhpWGJCVDlJRUxSb01kcVBmY29jeThsVEJheUlFdUthdG4wRTQ5T2xlVm9GWTVxcE0xaVQ1Q3I5Tmd6czZnem5NZE1KZksyeDEvdElJPW1IZUpjVUtGc2ZIeE9HaFEiLCJleHAiOjE2NjE1NzYwOTksInNoYXJkX2lkIjo1MzU3NjU1OSwicGQiOjB9.jitV8bFSBusIXglqdSfnRURcGlSt-lD4EvG4Ttc0DqU"
site_key = "4c672d35-0701-42b2-88c3-78380b0db560"

url = f"http://2captcha.com/in.php?key={api_key}&method=hcaptcha&sitekey={site_key}&pageurl=http://discord.com/register"
r = requests.get(url)
result = r.text
result = result.replace("OK|", "")

register_url = "https://discord.com/api/v9/auth/register"

while True:
    url2 = f"http://2captcha.com/res.php?key={api_key}&action=get&id={result}"
    r2 = requests.get(url2)
    result2 = r2.text
    print("captcha", result)
    if "OK" in result2:
        result2 = result2.replace("OK|", "")
        print(result2)
        data = {"fingerprint": "", "email": user_email, "username": user_name, "password": user_password, "invite": "null", "consent": "true",  "date_of_birth": "2000-04-22", "gift_code_sku_id": "null", "captcha_key": str(result2)}
        r = requests.post(register_url, json=data)
        print("Token", r.text)
        exit()
