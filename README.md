# Email Sender with Multiple Attachments

This project provides a Python script and a GUI application to send emails with multiple attachments using the `smtplib` library. The GUI is built using `tkinter`.

## Features

- Send emails with multiple attachments
- Simple and intuitive GUI for easy use
- Ability to choose files for attachment

## Requirements

- Python 3.x
- `smtplib` (comes with Python)
- `email` (comes with Python)
- `tkinter` (comes with Python)
- `filedialog` (part of `tkinter`)

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Install necessary packages (if not already installed):
    ```bash
    pip install tk
    ```

3. Update the `email_user` and `email_password` variables in the script with your email and password:
    ```python
    email_user = 'your_mail_id'
    email_password = 'mail_passwd'
    ```

4. Update the path to your icon (if using) in the GUI script:
    ```python
    m.iconbitmap(r'your_icon_path')
    ```

## Usage

### Running the Script

1. Run the GUI application:
    ```bash
    python your_script_name.py
    ```

2. Fill in the recipient email, subject, and body of the email.

3. Click the "Attach" button to choose files to attach to the email.

4. Click the "Send" button to send the email.

### Sending Email via Function

You can also use the `mail` function directly to send emails with attachments:

```python
from your_script_name import mail

email_send = 'recipient@example.com'
subject = 'Your Subject'
body = 'Your Email Body'
file_path = ['path/to/file1', 'path/to/file2']

mail(email_send, subject, body, file_path)
