#Importing Dokan Pay Class - تبويب كلاس دكان باي
from lib.DokanPaySDKPython import DokanPaySDKPython

#Creating Data Object to pass to dokan pay - عمل متغير بيانات لنقله لدُكان باي
txid = 'TXID HERE'

# Cancel Transaction Via Dokan Pay SDK - إلغاء معاملة من خلال كلاس دُكان باي
DokanPaySDKPython.CancelTransaction(txid)