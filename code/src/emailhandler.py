import email
from email import policy
import global_variables as gv

def extract_email_content(file_path):
    with open(gv.PROJECT_ROOT/file_path, 'rb') as email_file:
        msg = email.message_from_bytes(email_file.read(), policy=policy.default)
    if msg.is_multipart():
        for msg_part in msg.walk():
            if msg_part.get_content_type() == "text/plain":
                msg_content_text = msg_part.get_payload(decode=True).decode()
            elif msg_part.get_content_type() == "text/html":
                #msg_content_html = msg_part.get_payload(decode=True).decode()
                continue
    else:
        if msg.get_content_type() == "text/plain":
            msg_content_text = msg.get_payload(decode=True).decode()
        elif msg.get_content_type() == "text/html":
            msg_content_html = msg.get_payload(decode=True).decode()
            pass
    
    return msg_content_text

if __name__=="__main__":
    print(extract_email_content("./data/test_emails/adjustment_1.eml"))