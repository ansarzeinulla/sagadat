import firebase_admin
from firebase_admin import credentials, firestore
import sys

# Firebase service account configuration
service_account = {
    "type": "service_account",
    "project_id": "sagadat-toi",
    "private_key_id": "247821ee634df46723a68cd8400aaeebf12ad558",
    "private_key": """-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC7iZrQ25eb8agY
atCs5aQcM5q9OsI0GyV2x3v5X53QtmZRbtbJwVKldUQjgE9kwrQKF6WQgcaqFw9u
79waqZVSwIqG7bASO5U9tt84T/bVkdl8rr2QoB0BvE2BZZN62j1bpKvbaLRv7FXH
nKI2QA3cdiI11PpRs/FaEN7yV+qnYLUHXU2ZBMB9XNA6Dd5vcsAlK2shPu49+Ka8
HTX/Frjhip1U8/z6p8TFgXXjHrp1Ht7L7ZuEwEkZu+dQ1m9pf8HQJ4/EiD3vny+i
nN+NUM+FNVk7jmwiIOkG/Tuf9fYEdER0l015rqhYgKMJPqP60OwAfye1j9KdqKkV
T9wBIS9jAgMBAAECggEABL7yOofcGdevO9L0LfPvx8DskQ5cHMp1E8Dvm7t2OHJt
O3FVISzxxPsnOsjD+ZZNzRWVHIeUOfi0bMfIJ6qT+1ChENISCxwT5khq9LddVUFI
IjYf2PmcUk9sHLKv3UOJmvibWsWXD2AJObB2kG3li+c3bWpS3V9y46capUJhT1QB
l8jtmya+3WwsEo9l9OdSqkZwiRvzHUOsqHK1fOsjLk05KVKOf4DIG3uhVf/3+zxx
jVw/moe+Tsyg+7wxSG/ZqZN3/tiylvsWK/KsJwXDmHm1CnkXJ62/31a5OpmcbR+x
rjCaste7hNSv7y/rlEhCJLSzfZinw7zR8GosNB2W6QKBgQDjcmjQD9LFQOuCg6un
UBseNB6vhTma5MM1yaWrpKbPCpZ32rDpf8x80641XJurToWxS/r/P30euyd6I0ne
myCqMkuNFCodSpL7EhCBf5Z1cOorKxmTs1dEwLBqIuqNHHTEJIJj70/I3f1VS4BC
Gbw8DqwHgzfQ6Cfe4RU44esVKQKBgQDTFJq/vhXPEHH/ugP6ae4yU6rSrZ6k5IxH
VEWxdoK6xTeu2QDOyDkc1p8vS2xy6RlTgHEIqbHdL0eDbR3jrO7IXbRAsQhQsv1d
E+37d41WuUD9ago+HK9Q6JdI6QqiSmGzuzz8JgyzF2JihYDUiOQnWEOfCBrTayrc
/87ND/ZFqwKBgAFODrvi21q2XKOLDdkP5JfvxJ1NLl9tIJGWbpTlhO97KBHX91vf
l9S/gihcN6hr8uhpfy8nthgPCtLwkOPuD+nqD/TnQLaaTu2R1PZpPPu/ghhtTuBC
DyYd1OVG/gGBQEo/y1+3Z8XHQETVAg9fBm1xyBri7dcM/e2RbQW+hhLBAoGAQEOo
rbIAz88Q9iu7JFV2COqCOqxTfZ57uwfERDhxqs16m4hD/7Dj+oy5YFvVQ9MGO+8B
+wI3PcE0Q6ZIEFZJSMWGqJ99iZxFGT6FGSeX54x1ZfIP9kMjeT2nObKB41FEF8Vs
1tP6z9fRw28j/xFCbVwpElUUXcPmA+z6GGLAtwsCgYEApEkP3bPpWAf/SdXBTG2C
+H/jDCz+9jSyocS57myFfucj3v0BSFSb0u0WSqSkSk4NDxdpMEhJaIFuUluNwTZ/
1bYadY1FdF42R81jv4B7BRkf5zncDwb43Cxlbl/n74i111IWbHnDKFOs0GtiB/Hm
Qn/gj4cRdR2yaIPOrXyLh0c=
-----END PRIVATE KEY-----""",
    "client_email": "firebase-adminsdk-fbsvc@sagadat-toi.iam.gserviceaccount.com",
    "client_id": "101388204784798146785",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fbsvc%40sagadat-toi.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

# Initialize Firebase Admin SDK with service account config
cred = credentials.Certificate(service_account)
firebase_admin.initialize_app(cred)
db = firestore.client()

def main():
    # Get ID from user
    doc_id = input("Enter ID: ").strip()
    
    # Collect names until newline
    names = []
    print("Enter names (press Enter twice to finish):")
    
    while True:
        try:
            name = input()
            if name == "":  # Check for empty line (Enter pressed twice)
                break
            if name.strip():  # Only add non-empty names
                names.append(name.strip())
        except KeyboardInterrupt:
            print("\nInput interrupted")
            sys.exit(1)

    if not names:
        print("No names entered")
        return

    # Prepare data for Firestore
    data = {
        "numberOfPeople": len(names)
    }
    
    # Add each person's name with person1, person2, etc.
    for i, name in enumerate(names, 1):
        data[f"person{i}"] = name

    try:
        # Update Firestore document
        doc_ref = db.collection("sagadat").document(doc_id)
        doc_ref.set(data, merge=True)
        if len(names) == 1:
            print(f"https://ansarzeinulla.github.io/sagadat/main.html?id={doc_id} {names[0]}")
        else:
            print(f"https://ansarzeinulla.github.io/sagadat/main.html?id={doc_id} {names[0]}-{names[-1]}")
        
    except Exception as e:
        print(f"Error updating Firestore: {str(e)}")

if __name__ == "__main__":
    main()