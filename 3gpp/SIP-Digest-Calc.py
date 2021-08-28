
#Author : AFY
#Only usable on Python3.

import hashlib

#============Test variables====================
#Username / Password : 02140050888
#Realm : fixims.mnc009.mcc510.3gppnetwork.org
#nonce : "5a53f46e3634aab7"
#clientNonce : "0621809303"
#method : INVITE
#URI : sip:085781132000@scscf.sprout.jkt.fixims.mnc009.mcc510.3gppnetwork.org:5054
#response = bf8db68fe826009972e1f28342030b33

username = str(input("Enter the username : "))
realm = str(input("Enter the authentication realm : "))
password = str(input("Enter the password : "))
nonce = str(input("Enter the nonce : "))
clientNonce = str(input("Enter the client nonce : "))
method = str(input("Enter the method (INVITE or REGISTER) : "))
uri = str(input("Enter the URI (including the sip:) : "))
nonceCount = "00000001"
qop = "auth"

print("\nCalculating HA1, HA2 and response. Will use nonceCount = \"00000001\" and qop = \"auth\".")
hash1 = hashlib.md5((username+":"+realm+":"+password).encode()).hexdigest()
hash2 = hashlib.md5((method+":"+uri).encode()).hexdigest()

print("\n\nHA1 is : {}".format(hash1))
print("\nHA2 is : {}".format(hash2))

response = hash1 + ":" + nonce + ":" + nonceCount + ":" + clientNonce + ":" + qop + ":" + hash2
responsefinal = hashlib.md5(response.encode()).hexdigest()
print("\nResponse is : {}".format(responsefinal))