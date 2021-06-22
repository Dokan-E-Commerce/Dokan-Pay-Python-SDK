import requests

class DokanPaySDKPython:
    
    MerchantApiToken = 'PLACE-IT-HERE' # Your Dokan.sa Merchant API Token
    DokanPayApiEndPoint = 'https://merchant-api.dokan.sa/v1/DokanPay/Transaction/'# DOKAN.SA API Endpoint.
    headers = { 'Authorization': 'Bearer ' + MerchantApiToken }

    def CreateTransaction(data) :
        r = requests.post(DokanPaySDKPython.DokanPayApiEndPoint + 'Create',data=data,headers=DokanPaySDKPython.headers)
        return r.text
    
    def CancelTransaction(txid):
        data = {'id' : txid}
        r = requests.post(DokanPaySDKPython.DokanPayApiEndPoint + 'Cancel',data=data,headers=DokanPaySDKPython.headers)
        return r.text

    def CheckTransaction(txid):
        r = requests.get(DokanPaySDKPython.DokanPayApiEndPoint + 'Check/' + txid,headers=DokanPaySDKPython.headers)
        return r.text