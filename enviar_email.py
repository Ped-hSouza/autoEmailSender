import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from neuropsico import *
from terapias import *

def enviar_email(agendamento, email_remetente, password_remetente):

    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Consulta agendada - neuropediatra'
    msg['To'] = agendamento.email
    msg['From'] = email_remetente

    corpo_texto = f"""
        Olá! Espero que esteja bem.

        Conforme solicitado,

        Consulta agendada para {agendamento.nome}
        Neuropediatra: Dr(a). {agendamento.neuropediatra}
        Data: {agendamento.data}
        Horário: {agendamento.hora}
        Endereço: Rua Emília Marengo, 186 Regente Feijó

        Instruções importantes:
        - Chegar com 20 minutos de antecedência para abertura da ficha e solicitação de autorização da consulta junto ao convênio.
        - Tolerância de atraso: 10 minutos.

        Ficamos à disposição.

        Atenciosamente,

        Pedro Henrique De Souza
        PROGRAMA JOVEM APRENDIZ
        www.unimedcnu.coop.br 
    """
    corpo_html = f"""
        <!DOCTYPE html>
        <html lang="pt-br">
            <head>
                <meta charset="UTF-8">
            </head>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px;">

                <h2 style="color: #00995d; border-bottom: 2px solid #00995d; padding-bottom: 10px;">Confirmação de Agendamento</h2>

                <p>Prezado(a), Espero que esteja bem!</p>
                
                <p>Conforme solicitado, seguem os detalhes da consulta:</p>

                <div style="background-color: #f1f8f5; border-left: 4px solid #00995d; padding: 15px; margin: 20px 0;">
                    <h3 style="color: #007c4b; margin-top: 0; text-decoration: underline;">Consulta Agendada para {agendamento.nome}</h3>
                    <ul style="list-style: none; padding: 0; margin: 0;">
                        <li style="margin-bottom: 8px;"><strong>⚕️ Consulta com neuropediatra:</strong> Dr. {agendamento.neuropediatra}</li>
                        <li style="margin-bottom: 8px;"><strong>📅 Data:</strong> {agendamento.data}</li>
                        <li style="margin-bottom: 8px;"><strong>⏰ Horário:</strong> {agendamento.hora}</li>
                        <li><strong>📍 Endereço:</strong> Rua Emília Marengo, 186 - Regente Feijó</li>
                    </ul>
                </div>

                <div style="background-color: #e6f4ee; border: 1px solid #c2e2d5; border-radius: 5px; padding: 15px; margin-bottom: 20px;">
                    <strong style="color: #007c4b; display: block; margin-bottom: 5px;">Instruções Importantes:</strong>
                    <ul style="margin: 0; padding-left: 20px; color: #333;">
                        <li style="margin-bottom: 5px;">Chegar com <strong>20 minutos de antecedência</strong> para abertura da ficha e solicitação de autorização junto ao convênio.</li>
                        <li><strong>Tolerância de atraso:</strong> 10 minutos.</li>
                    </ul>
                </div>

                <p>Ficamos à disposição.</p>

                <p style="margin-top: 30px;">Atenciosamente,</p>

                <hr style="border: 0; border-top: 1px solid #eee; margin: 20px 0;">

                <table style="width: 100%; border-collapse: collapse;">
                    <tr>
                        <td>
                            <div style="color: #00995d; font-size: 20px; font-weight: bold; margin-bottom: 2px;">Pedro Henrique de Souza</div>
                            <div style="color: #007c4b; font-size: 14px; font-weight: bold; text-transform: uppercase;">PROGRAMA JOVEM APRENDIZ</div>
                            <div style="margin-top: 5px;">
                                <a href="https://www.unimedcnu.coop.br" style="color: #007c4b; text-decoration: none; font-size: 13px;">www.unimedcnu.coop.br</a>
                            </div>
                        </td>
                    </tr>
                </table>
            </body>
        </html>
    """

    msg.attach(MIMEText(corpo_texto, 'plain'))
    msg.attach(MIMEText(corpo_html, 'html'))


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_remetente, password_remetente)
            smtp.send_message(msg)