import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

def send_email(to_email, subject, body, resume_path):
    # Configurações do seu e-mail
    from_email = "t.i.viniciushuan@gmail.com"  # Altere para o seu e-mail
    password = "qmuk wwfc nheb oscb"  # Altere para sua senha ou use um app password
    
    try:
        # Criando a mensagem
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Adicionando o corpo do e-mail
        msg.attach(MIMEText(body, 'plain'))
        
        # Adicionando o anexo (currículo)
        with open(resume_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(resume_path)}")
            msg.attach(part)
        
        # Conectando ao servidor SMTP e enviando o e-mail
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        
        print(f"E-mail enviado com sucesso para {to_email}")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

# Exemplo de uso
to_email = "rh@grupoagil.com.br"  # Altere para o e-mail do destinatário
subject = "Currículo - Vinicius Huan Cardoso"
body = "Olá, segue meu currículo para análise. Fico no aguardo de um retorno."
resume_path = "c:\Curriculo Vinicius-T.I.pdf "# Altere para o caminho do seu currículo

send_email(to_email, subject, body, resume_path)
