from email.message import EmailMessage
from email.utils import make_msgid
from email.mime.image import MIMEImage

import mimetypes


class Message:

    def __init__(self, email_from, email_to, subject, plain_text_content="", alternative_contet="", image_path_list=[]):
        self.message = EmailMessage()
        self.message['From'] = email_from
        self.message['To'] = ", ".join(email_to) if isinstance(email_to, list) else email_to
        self.message['Subject'] = subject
        self.message.set_content(plain_text_content)
        self.alternative_content = alternative_contet
        self.image_list = image_path_list
        self.image_config = []
        self._create_attachement_config()
        self._add_alterantive()
        self._attach_image()

    def _create_attachement_config(self):
        conf_image_list = []
        for img in self.image_list:
            maintype, subtype = mimetypes.guess_type(img)
            img_conf = {
                'cid': make_msgid(domain="kurbads.lv"),
                'name': img.split('/')[-1],
                'maintype': maintype,
                'subtype': subtype,
                'path': img,
            }
            conf_image_list.append(img_conf[:])
        self.image_config
        # self.message.add_alternative()
        
    def _add_alterantive(self):
        self.message.add_alternative(self.alternative_content.format(*[img.cid for img in self.image_config]), subtype="html")
        
    def _attach_image(self):
        for img in self.image_config:
            with open(img.path, 'rb') as image:
                self.message.get_payload()[1].add_related(
                    image.read(), maintype=img.maintype, subtype=img.subtype, cid=img.cid)
        
# def create_message():
#     """Create message"""
#     message = EmailMessage()

#     message['Subject'] = 'Sveiciens ziemassvētkos'
#     message['From'] = 'uldis.calpa@gmail.com'
#     message['To'] = 'uldis.calpa@kurbads.lv'

#     test_image_path = './media/kurbads.jpg'
#     test_image_cid1 = make_msgid(domain="kurbads.lv")
#     test_image_cid2 = make_msgid(domain="kurbads.lv")

#     message.set_content('Sveiciens svētkos vienkāršais teksts \n Jānis')
#     message.add_alternative("""\
#         <h1> X-mas <\h1>
#         <img src="cid:{img_src1}" />
#         <h3> no Kurbads </h3>
#         <img src="cid:{img_src2}" />
        
#         """.format(img_src1=test_image_cid1[1:-1], img_src2=test_image_cid2[1:-1]), subtype='html')

#     # message.add_alternative()

#     with open(test_image_path, 'rb') as image:
#         message.get_payload()[1].add_related(
#             image.read(), maintype='image', subtype='jpeg', cid=test_image_cid1)
#         message.get_payload()[1].add_related(
#             image.read(), maintype='image', subtype='jpeg', cid=test_image_cid2)
#         print(message.get_payload())
#         print(message.get_payload()[0])
#         print(message.get_payload()[1])
#         print(len(message.get_payload()))

#     with open(test_image_path, 'rb') as image:
#         message.get_payload()[1].add_related(
#             image.read(), maintype='image', subtype='jpeg', cid=test_image_cid2)

#     return message


if __name__ == '__main__':
    # msg = create_message()
    # send(msg)
    pass