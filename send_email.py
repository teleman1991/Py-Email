import os
from msgraph.core import GraphClient
from kiota_authentication_azure.azure_identity_authentication_provider import AzureIdentityAuthenticationProvider
from azure.identity import DefaultAzureCredential

class EmailSender:
    def __init__(self):
        self.graph_config = {
            'client_id': os.getenv('AZURE_CLIENT_ID'),
            'tenant_id': os.getenv('AZURE_TENANT_ID'),
            'client_secret': os.getenv('AZURE_CLIENT_SECRET'),
            'scopes': ['https://graph.microsoft.com/.default']
        }
        
        # Initialize the Graph client
        credential = DefaultAzureCredential()
        auth_provider = AzureIdentityAuthenticationProvider(credential, self.graph_config['scopes'])
        self.client = GraphClient(auth_provider)
    
    def send_email_with_attachment(self, to_email, subject, body, file_path):
        try:
            # Read file content
            with open(file_path, 'rb') as upload:
                file_content = upload.read()
                file_name = os.path.basename(file_path)
            
            # Prepare email message
            message = {
                'message': {
                    'subject': subject,
                    'body': {
                        'contentType': 'Text',
                        'content': body
                    },
                    'toRecipients': [
                        {
                            'emailAddress': {
                                'address': to_email
                            }
                        }
                    ],
                    'attachments': [
                        {
                            '@odata.type': '#microsoft.graph.fileAttachment',
                            'name': file_name,
                            'contentBytes': file_content
                        }
                    ]
                }
            }
            
            # Send email
            self.client.post('/me/sendMail', json=message)
            print(f'Email sent successfully to {to_email}')
            
        except Exception as e:
            print(f'Error sending email: {str(e)}')

# Example usage
if __name__ == '__main__':
    sender = EmailSender()
    sender.send_email_with_attachment(
        to_email='recipient@example.com',
        subject='Test Email',
        body='This is a test email with attachment',
        file_path='path/to/your/file.txt'
    )