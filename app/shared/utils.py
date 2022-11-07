from google.cloud import secretmanager
import os

class Utils:

    def access_secret_version(project_id, secret_id, version_id="latest"):
        # Create the Secret Manager client.
        client = secretmanager.SecretManagerServiceClient()

        # Build the resource name of the secret version.
        name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

        # Access the secret version.
        response = client.access_secret_version(name=name)
        print("valor del secreto " + secret_id)
        print(response.payload.data.decode('UTF-8'))
        # Return the decoded payload.
        return response.payload.data.decode('UTF-8')
    
    def getVariables(_self, project_id, secret_id):
        try:
            return _self.access_secret_version(project_id, secret_id)
        except Exception as error:
            print(error)
            return os.getenv(secret_id)