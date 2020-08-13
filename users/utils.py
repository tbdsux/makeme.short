import os
import secrets
from flask import current_app, url_for
from flask_mail import Message
from PIL import Image
from makemeshort import mail


# save profile image in the server (static folder)
def save_profile_pic(formpic):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(formpic.filename)
    pic_fn = random_hex + f_ext
    pic_path = os.path.join(current_app.root_path,
                            'static/profile', pic_fn)

    output_size = (200, 200)
    i = Image.open(formpic)
    i.thumbnail(output_size)
    # save picture
    i.save(pic_path)
    return pic_fn


# send a reset email
def send_reset_email(user):
    __token = user.get_resetpass_token()
    msg = Message(subject="Request Password Reset (makeme.shrot)", recipients=[user.email])
    msg.body = f'''makeme.short - Reset Password Request
    
    To reset your password, visit the folowing link:
    {url_for('users.request_new_pass', token=__token, _external=True)}

If you did not make this request, then simply ignore this email.

Best Regards,
    administrator
    '''

    mail.send(msg)
