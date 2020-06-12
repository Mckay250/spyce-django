import smtplib
from email.message import EmailMessage

from django.conf import settings

EMAIL_ADDRESS = settings.EMAIL_ADDRESS
EMAIL_PASSWORD = settings.EMAIL_PASSWORD


def items(x, data, *args, **kwargs):
    data = data
    rows = """"""
    for i in range(x):
        rows += f"""<tr>
            <td style="border: 1px solid rgb(54, 54, 54)">{data['products'][i]}</td>
            <td style="border: 1px solid rgb(54, 54, 54)">{data['types'][i]}</td>
            <td style="border: 1px solid rgb(54, 54, 54)"><a href="{data['links'][i]}" download={data['products'][i]}>Download {data['types'][i]} file</a></td>
            </tr>"""
    return rows


def receipt(x, info, *args, **kwargs):
    data = info
    rows = """"""
    for i in range(x):
        rows += f"""<tr>
                        <td style="border: 1px solid rgb(54, 54, 54)">{data['products'][i]}</td>
                        <td style="border: 1px solid rgb(54, 54, 54)">{data['types'][i]}</td>
                        <td style="border: 1px solid rgb(54, 54, 54)">${data['prices'][i]}</td>
                    </tr>"""
    return rows

def mail_transaction(data):
    data = data
    msg = EmailMessage()
    msg['Subject'] = 'Beat Purchase'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = f"{data['email']}"
    msg.set_content('Please turn on HTML to view your transaction details')

    msg.add_alternative(f"""\
    <!Doctype html>
    <html>
        <body style="text-align: center;">
            <div style="display: inline-block;
                        border: solid 2px rgb(17, 17, 17);">
                <div style="background : rgb(17, 17, 17);
                            padding: 0.1px 2rem;
                            color : white">
                    <h1>Thanks for your Patronage</h1>
                    <h3>Your order has been processed</h3>
                </div>
                <div style="margin: 1rem 1rem; text-align: left;">
                    <h3>Items</h3>
                    <table style="border: 1px solid rgb(54, 54, 54);
                                  border-collapse: collapse;
                                  text-align: center;
                                  width: 100%;">
                        <tr style="border: 1px solid rgb(54, 54, 54)">
                            <th style="border: 1px solid rgb(54, 54, 54)">Product</th>
                            <th style="border: 1px solid rgb(54, 54, 54)">Type</th>
                            <th>Download</th>
                        </tr>""" +
                        f"{items(len(data['products']), data)}"
                        + f"""\
                    </table>
                </div>

                <div style="margin: 1rem 1rem; text-align: left;">
                    <h3>Receipt [Transaction ID: {data['trans_id']}]</h3>
                    <table style="border: 1px solid rgb(54, 54, 54);
                                  border-collapse: collapse;
                                  text-align: center;
                                  width: 100%;">
                        <tr style="border: 1px solid rgb(54, 54, 54)">
                            <th style="border: 1px solid rgb(54, 54, 54)">Product</th>
                            <th style="border: 1px solid rgb(54, 54, 54)">Type</th>
                            <th>Price</th>
                        </tr>""" +
                        f"{receipt(len(data['products']), data)}"
                        + f"""
                        <tr>
                            <td>Total</td>
                            <td style="border-right: 1px solid rgb(54, 54, 54)"></td>
                            <td style="border-top: 1px solid rgb(54, 54, 54)">${data['total']}</td>
                        </tr>
                    </table>
                </div>
                <p>Thanks for shopping with us</p>
                <a href="#">Spycebeatz</a>
            </div>
        </body>
    </html>
    """, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)