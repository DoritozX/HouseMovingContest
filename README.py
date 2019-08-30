
def getToken(user, password，server = 'ip-10-249-7-115.aws.sas.com'， protocol='http'):
    import requests
    protocol='http'
    server = 'ip-10-249-7-115.aws.sas.com'
    authUri='/SASLogon/oauth/token'
    headers = {
     'Accept': 'application/json',
     'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload= 'grant_type=password&username=' + user + '&password=' + password
    authReturn = requests.post(protocol + '://' + server + authUri ,
                               auth=('sas.ec', ''),
                               data=payload,
                               headers=headers)
    myToken = authReturn.json()['access_token']
    message = f"Authentication status is: {authReturn.ok}"
    print(message)
    return(myToken)
