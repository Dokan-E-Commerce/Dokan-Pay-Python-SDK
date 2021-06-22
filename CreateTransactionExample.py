#Importing Dokan Pay Class - تبويب كلاس دكان باي
from lib.DokanPaySDKPython import DokanPaySDKPython

#Creating Data Object to pass to dokan pay - عمل متغير بيانات لنقله لدُكان باي
#The ones without Nullable are necessary - الي مو بجنبهم غير إلزامي مهمين
data = {
    'name':'Ahmed Ali', #Nullable - غير إلزامي
    'number' : '+966555555555', # Nullable - غير إلزامي
    'amount' : 50,
    'custom-param' : 'user id = 4', # Nullable - غير إلزامي
    'email' : 'dev@dokan.sa', #Nullable - غير إلزامي
    'success_url' : 'http://localhost/checkpayment.php',# Nullable But important to return the user with transaction data in GET PARAM - غير إلزامي ولكن ضروري إذا كنت تود إرجاع العميل لصفحة ما مع تمرير بيانات المعاملة في الرابط كمتغيرات قيت
}

# Creating Transaction Via Dokan Pay SDK - عمل معاملة من خلال كلاس دُكان باي
DokanPaySDKPython.CreateTransaction(data)