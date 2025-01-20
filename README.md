# Quote of the Day

This project is designed to provide you with a daily dose of inspiration through a selection of quotes from famous personalities throughout history like Karen Lamb and Bruce Lee.

The application sends one random quote directly to your email using Python and the `smtplib` library for handling email transmission.
The implementation involves setting up an SMTP server connection using your Gmail account credentials. The script formats the email content with the quote of the day and sends it to the specified recipients. 

## Installation

To get started with the Quote of the Day project, follow these steps:

1. Clone the repository:
2. Navigate to the project directory:
    ```bash
    cd QuoteOfTheDay
    ```
3. Install the necessary dependencies:
    ```bash
    npm install
    ```

## Usage

To start the application, run:
```bash
python3 main.py
```

You can use your own Gmail account to send the quotes via email. To do this, you need to create an application password in Gmail. Follow these steps:

1. Go to your Google Account.
2. Select Security.
3. Under "Signing in to Google," select App Passwords.
4. Create a password for an app. Use this password in your application to send emails (`main.py`: my_password)
5. Add a list of recipients to send that mail to (`main.py`: recipient_list)

## Scheduling the Script

To program the execution of this script through `crontab`, follow these steps:

1. Open the crontab file for editing:
    ```bash
    crontab -e
    ```
2. Add the following line to schedule the script to run daily at a specific time (e.g., 8 AM):
    ```bash
    0 8 * * * /usr/bin/python3 /path/to/your/project/QuoteOfTheDay/main.py
    ```
3. Save and close the crontab file.
4. Restart the `cron` service to ensure the changes take effect:
    ```bash
    sudo systemctl restart cron
    ```
Alternatively, you can use other scheduling tools like `systemd` timers or task schedulers available on your operating system to achieve similar results.

## Contributing

This project is open-source so feel free to fork this project and submit pull requests for improvements or new features. Suggestions or enhancements are always welcome!
