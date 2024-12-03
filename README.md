# Py-Email

A Python script for sending emails with attachments using Microsoft Graph API.

## Prerequisites

1. Azure AD App Registration with following permissions:
   - Mail.Send
   - Mail.ReadWrite

2. Required Python packages:
   ```bash
   pip install azure-identity msgraph-core
   ```

## Environment Setup

Create a `.env` file with your Azure credentials:
```
AZURE_CLIENT_ID=your_client_id
AZURE_TENANT_ID=your_tenant_id
AZURE_CLIENT_SECRET=your_client_secret
```

## Usage

1. Import the EmailSender class:
```python
from send_email import EmailSender
```

2. Create an instance and send email:
```python
sender = EmailSender()
sender.send_email_with_attachment(
    to_email='recipient@example.com',
    subject='Test Email',
    body='Email content',
    file_path='path/to/file.txt'
)
```

## Features
- Send emails with attachments
- Secure authentication using Azure AD
- Simple and reusable code

## Error Handling
The script includes basic error handling and will print error messages if something goes wrong during the email sending process.