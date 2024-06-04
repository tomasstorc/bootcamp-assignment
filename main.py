import os
from azure.keyvault.secrets import SecretClient
from azure.identity import ManagedIdentityCredential

def main():
    try:
        if "KV_URI" not in os.environ:
            print("Key vault URI not set, exiting set environment variable KV_URI")
            exit()
        if "SECRET_VALUE" not in os.environ:
            print("Secret value not set, exiting, set environment variable SECRET_VALUE")
            exit()
        credential = ManagedIdentityCredential()
        client = SecretClient(vault_url=os.environ['KV_URI'], credential=credential)
        client.set_secret("bootcampsecret", os.environ["SECRET_VALUE"])
    except Exception as e:
        print(f"error occurred: {e}")

if __name__ == "__main__":
    main()