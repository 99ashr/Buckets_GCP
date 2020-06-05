
from google.cloud import storage


def new_bucket(bucket_name):

    storage_client = storage.Client.from_service_account_json(
        "./yash-rnd-031df0bc7bfa.json"
    )

    # Creating bucket
    storage_client.create_bucket(bucket_name)
    print("Bucket", bucket_name, "created!")


new_bucket("bucket-ashish-gaur")
