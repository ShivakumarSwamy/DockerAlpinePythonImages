"""
Script to send message(MIME: https://en.wikipedia.org/wiki/MIME) via email using Gmail

"""

import os


def check_env_variable_values(environment_variable):
    """
    check environment variable value

    Parameters
    ---------
    environment_variable: str

    Returns
    -------
    Any

    """
    environment_variable_value = os.getenv(environment_variable)

    if environment_variable_value is None or len(environment_variable_value) == 0:
        print("\n---- Environment Variable Value Error -----",
              f"'{environment_variable}' has value '{environment_variable_value}'",
              sep="\n")
        raise SystemExit

    return environment_variable_value


def set_variables_using_docker_env():
    """
    Set variable use Dockerfile 'ENV'

    Returns
    -------
    (str, str, str, str, str)

    """

    return map(check_env_variable_values,
               ("FROM_ADDRESS", "PASSWORD", "TO_ADDRESS", "SUBJECT", "MESSAGE"))


def handler_smtp_response_exception(exception_object):
    """
    handle 'SMTPResponseException' errors

    Parameters
    ----------
    exception_object: SMTPResponseException

    """
    print("\n---- SMTPResponseException ----")

    if exception_object.smtp_code == 534:
        print("Allow less secure apps access your account using the following link "
              "'https://support.google.com/accounts/answer/6010255'",
              f"\n---- Error Code and Message ----",
              f"[{exception_object.smtp_code}] {exception_object.smtp_error}",
              sep="\n")

    elif exception_object.smtp_code == 535:
        print(f"Check Username: '{from_address}' and Password: '{password}'",
              f"\n---- Error Code and Message ----",
              f"[{exception_object.smtp_code}] {exception_object.smtp_error}",
              sep="\n")

    else:
        print(f"\n---- Error Code and Message ----",
              f"[{exception_object.smtp_code}] {exception_object.smtp_error}",
              sep="\n")

    raise SystemExit


if __name__ == '__main__':
    # setup variables
    from_address, password, to_address, subject, message = set_variables_using_docker_env()

    import smtplib
    from email.mime.text import MIMEText

    mime_message = MIMEText(message)
    mime_message["Subject"], mime_message["From"], mime_message["To"] = subject, from_address, to_address

    try:
        with smtplib.SMTP("smtp.gmail.com",
                          587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            # from address login credentials
            smtp.login(from_address,
                       password)
            # send MIME (Multipurpose Internet Mail Extensions) message
            smtp.send_message(mime_message)

    except smtplib.SMTPResponseException as e:
        handler_smtp_response_exception(e)

    print(f"Message sent from '{from_address}' to '{to_address}'")
