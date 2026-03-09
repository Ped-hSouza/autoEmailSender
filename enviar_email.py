import smtplib
from email.message import EmailMessage



def enviar_email(agendamento, email_remetente, password_remetente):

    msg = EmailMessage()
    msg['Subject'] = 'Consulta agendada - neuropediatra'
    msg['To'] = agendamento.email
    msg['From'] = email_remetente

    corpo_texto = """
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
        <html>
            <body>
                <p>Olá! Espero que esteja bem.<br><br>
                Conforme solicitado, <br></p>
                <p><i><u><b>Consulta agendada para {agendamento.nome}:</b></u></i></p>
                <ul>
                    <li><b></b>Neuropediatra: Dr(a). </b> {agendamento.neuropediatra}</li>
                    <li><b></b>Data: </b> {agendamento.data}</li>
                    <li><b></b>Horário:</b> {agendamento.hora}</li>
                    <li><b></b>Endereço:</b> Rua Emília Marengo, 186 Regente Feijó</li>
                </ul>

                Ficamos à disposição.<br><br>

                Atenciosamente,<br><br>

                Pedro Henrique De Souza<br>
                PROGRAMA JOVEM APRENDIZ<br>
                www.unimedcnu.coop.br</p> 
            </body>
        </html>
    """

    msg.set_content(corpo_texto)
    msg.add_alternative(corpo_html, subtype='html')


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_remetente, password_remetente)
            smtp.send_message(msg)