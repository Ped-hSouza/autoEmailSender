corpo_email_neuropsico_info = """
            <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <style>
                body { font-family: Arial, sans-serif; color: #444; line-height: 1.6; }
                .container { max-width: 600px; margin: 20px auto; border: 1px solid #e0e0e0; padding: 20px; }
                
                .header-title { color: #007d4f; font-size: 20px; font-weight: bold; border-bottom: 2px solid #007d4f; padding-bottom: 10px; margin-bottom: 20px; }
                
                .section-box { background-color: #f8f9fa; border-left: 5px solid #007d4f; padding: 15px; margin-bottom: 20px; }
                .section-title { color: #007d4f; font-weight: bold; text-decoration: underline; margin-bottom: 15px; display: block; }
                
                .alert-box { background-color: #fff9e6; border: 1px solid #ffeeba; border-radius: 8px; padding: 15px; margin-bottom: 15px; color: #856404; font-size: 14px; }
                .info-box { background-color: #e6f7ef; border: 1px solid #c3e6d9; border-radius: 8px; padding: 15px; margin-bottom: 20px; color: #004d30; font-size: 14px; }
                
                .signature { margin-top: 30px; border-top: 1px solid #eee; padding-top: 20px; }
                .name { color: #00a859; font-size: 18px; font-weight: bold; margin-bottom: 2px; }
                .role { color: #007d4f; font-size: 14px; font-weight: bold; text-transform: uppercase; margin-bottom: 5px; }
                .link { color: #007d4f; font-size: 12px; text-decoration: none; }
                
                ul { padding-left: 20px; }
                li { margin-bottom: 8px; }
                b { color: #333; }
            </style>
        </head>
        <body>

        <div class="container">
            <div class="header-title">Orientação para Agendamento</div>

            <p>Prezado(a) Beneficiário(a),</p>
            <p>Este informe detalha o processo para o agendamento da <b>Avaliação Neuropsicológica</b>.</p>

            <div class="section-box">
                <span class="section-title">1. Documentação Necessária para Autorização</span>
                <p>Para dar início ao processo, é imprescindível a apresentação dos seguintes documentos (validade de <b>30 dias</b>):</p>
                <ul>
                    <li><b>Pedido Médico:</b> Deve conter CID, Hipótese Diagnóstica, assinatura e carimbo legíveis.</li>
                    <li><b>Relatório Médico Detalhado:</b> Deve informar claramente o motivo da solicitação, com assinatura e carimbo.</li>
                </ul>
            </div>

            <div class="info-box">
                <strong>2. Processo de Autorização</strong><br>
                O pedido será encaminhado à Unimed de Origem. O prazo para retorno da análise é de <b>até 10 dias úteis</b>.
            </div>

            <div class="section-box">
                <span class="section-title">3. Agendamento da Avaliação</span>
                <p>Após a autorização, nossa equipe entrará em contato via e-mail ou telefone.</p>
                <ul>
                    <li>A avaliação é composta por <b>10 sessões</b>.</li>
                    <li>As sessões ocorrem <b>1 vez por semana</b> em dia e horário fixos.</li>
                </ul>
            </div>

            <div class="alert-box">
                <strong>⚠️ Atenção:</strong> Caso o beneficiário seja menor de idade, a primeira sessão é destinada à <b>anamnese</b> e deve ser realizada exclusivamente com o responsável (Pai ou Mãe), sem a necessidade da presença da criança.
            </div>

            <p>Seguimos à disposição para quaisquer esclarecimentos.</p>

            <div class="signature">
                <div class="name">Pedro Henrique De Souza</div>
                <div class="role">PROGRAMA JOVEM APRENDIZ</div>
                <a href="http://www.unimedcnu.coop.br" class="link">www.unimedcnu.coop.br</a>
            </div>
        </div>

        </body>
        </html>
""" ##confirmado

corpo_email_neuropsico_confirmacao = """
    <!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px;">

    <h2 style="color: #00995d; border-bottom: 2px solid #00995d; padding-bottom: 10px;">Confirmação de Agendamento</h2>

    <p>Bom dia! Espero que esteja bem.</p>
    
    <p>Conforme solicitado, seguem os detalhes do seu agendamento:</p>

    <div style="background-color: #f1f8f5; border-left: 4px solid #00995d; padding: 15px; margin: 20px 0;">
        <h3 style="color: #007c4b; margin-top: 0; text-decoration: underline;">Avaliação Neuropsicológica Agendada</h3>
        <ul style="list-style: none; padding: 0; margin: 0;">
            <li style="margin-bottom: 8px;"><strong>📅 Data de início:</strong> 03/03</li>
            <li style="margin-bottom: 8px;"><strong>🗓️ Dia da semana:</strong> Terça-feira</li>
            <li style="margin-bottom: 8px;"><strong>⏰ Horário:</strong> 11:00</li>
            <li style="margin-bottom: 8px;"><strong>👩‍⚕️ Profissional:</strong> Gabriela</li>
            <li><strong>📍 Endereço:</strong> Rua Emília Marengo, 186 - Regente Feijó</li>
        </ul>
    </div>

    <div style="background-color: #fff4e5; border: 1px solid #ffcc80; border-radius: 5px; padding: 15px; margin-bottom: 20px;">
        <p style="margin: 0; color: #856404;">
            <strong>⚠️ Observação importante:</strong> Caso a avaliação seja para beneficiário <strong>menor de idade</strong>, a 1ª sessão será a anamnese com o responsável (pai ou mãe), não sendo necessária a presença da criança neste primeiro encontro.
        </p>
    </div>

    <p style="background-color: #e6f4ee; padding: 10px; border-radius: 5px; border: 1px solid #c2e2d5;">
        <strong>Lembrando:</strong> Serão <strong>10 sessões</strong> (1 por semana) no mesmo dia da semana e horário definidos acima.
    </p>

    <p>Ficamos à disposição para qualquer dúvida.</p>

    <p style="margin-top: 30px;">Atenciosamente,</p>

    <hr style="border: 0; border-top: 1px solid #eee; margin: 20px 0;">

    <table style="width: 100%; border-collapse: collapse;">
        <tr>
            <td>
                <div style="color: #00995d; font-size: 20px; font-weight: bold; margin-bottom: 2px;">Pedro Henrique De Souza</div>
                <div style="color: #007c4b; font-size: 14px; font-weight: bold; text-transform: uppercase;">Programa Jovem Aprendiz</div>
                <div style="margin-top: 5px;">
                    <a href="https://www.unimedcnu.coop.br" style="color: #007c4b; text-decoration: none; font-size: 13px;">www.unimedcnu.coop.br</a>
                </div>
            </td>
        </tr>
    </table>

</body>
</html>
"""