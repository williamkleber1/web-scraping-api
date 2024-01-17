import requests
import json
import datetime
import http.client

class JobSubmitter:
  
    

    def send_form(self, title, locale, efetivo):
        conn = http.client.HTTPSConnection("forms.office.com")
        #payload = "{\"startDate\":\"2024-01-15T14:57:54.583Z\",\"submitDate\":\"2024-01-15T14:58:15.264Z\",\"answers\":\"[{\\\"questionId\\\":\\\"r28823796bb8b461195112faa4376895e\\\",\\\"answer1\\\":\\\"cargo teste\\\"},{\\\"questionId\\\":\\\"r62327b3de37b4158b46eb9bf1ff8b45d\\\",\\\"answer1\\\":\\\"cidade teste\\\"},{\\\"questionId\\\":\\\"rb496f0bcd3a44b0baf03ea81caa84243\\\",\\\"answer1\\\":\\\"Sim\\\"}]\"}"
        payload1 = "{\"startDate\":\"2024-01-15T14:57:54.583Z\",\"submitDate\":\"2024-01-15T14:58:15.264Z\",\"answers\":\"[{\\\"questionId\\\":\\\"r28823796bb8b461195112faa4376895e\\\",\\\"answer1\\\":\\\"" + title
        payload2 = payload1 + "\\\"},{\\\"questionId\\\":\\\"r62327b3de37b4158b46eb9bf1ff8b45d\\\",\\\"answer1\\\":\\\"" + locale
        payload3 = payload2 +"\\\"},{\\\"questionId\\\":\\\"rb496f0bcd3a44b0baf03ea81caa84243\\\",\\\"answer1\\\":\\\"" + efetivo + "\\\"}]\"}"

        
 
        print(payload3)
        headers = {
            'authority': "forms.office.com",
            '__requestverificationtoken': "x7Gwmp0q6cYbBgL2anyVLQjziYX_OakcBbAyUZlAuB9d1ufQmULRrAyUZsWR2jmDXOBRmzaDSwokx0YiSkTKmnJ1rpWTwgl8AcyTA0v5DuY1",
            'accept': "application/json",
            'accept-language': "pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7",
            'authorization': "",
            'content-type': "application/json",
            'cookie': "FormsWebSessionId=b13c080a-3096-4bad-a871-d2b4c8a08618; RpsAuthNonce=fd46fe2c-33c5-48f9-af93-1b57d7f2c2fc; RpsAuthNonce=fd46fe2c-33c5-48f9-af93-1b57d7f2c2fc; __RequestVerificationToken=6Lx2hHUKXrw6_1h9N39jvxpDsSMSBTO1rEGuHt5BtL4x1uJKkZre6h8-okupSqFRJ0irWY3aEsiReOGMLpgQMCwAApGtCUvUpPNLGmsmbp01; MUID=3BE5F52291466D5F16FCE64B90466CC1",
            'odata-maxverion': "4.0",
            'odata-version': "4.0",
            'origin': "https://forms.office.com",
            'referer': "https://forms.office.com/pages/responsepage.aspx?id=QhQEvrbz4UuFCeypyBdSj7tyC7WzU59DoUmUzzgLXidUNllOQ0JYNjVMSDZSN1Q4MUFZWlVXQkw0UC4u",
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'sec-ch-ua-mobile': "?0",
            'sec-ch-ua-platform': "macOS",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            'x-correlationid': "69a82929-bfd9-4410-a4f9-57dbc2fa9b00",
            'x-ms-form-muid': "3BE5F52291466D5F16FCE64B90466CC1",
            'x-ms-form-request-ring': "business",
            'x-ms-form-request-source': "ms-formweb",
            'x-usersessionid': "b16e3eb4-a51b-42b6-bc3d-53263c0287bf"
            }

        conn.request("POST", "/formapi/api/be041442-f3b6-4be1-8509-eca9c817528f/users/b50b72bb-53b3-439f-a149-94cf380b5e27/forms(%27QhQEvrbz4UuFCeypyBdSj7tyC7WzU59DoUmUzzgLXidUNllOQ0JYNjVMSDZSN1Q4MUFZWlVXQkw0UC4u%27)/responses", payload3, headers)

        res = conn.getresponse()
        data = res.read()

        return data.decode("utf-8")
    
    def execute(self, jobs):
       
        for job in jobs:
            efetivo = 'Sim' if job.get('type','') == 'Efetivo' else 'Não'
            res = self.send_form(job.get('title',''), job.get('locale',''), efetivo)

        print("Dados enviados ao formulário com sucesso.")

