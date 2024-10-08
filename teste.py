from datetime import datetime, timedelta
import os


caminho = r'C:\Users\c866790\Downloads'

caminho_bot_1= r''

meses = {
    '01': 'Janeiro',
    '02': 'Fevereiro',
    '03': 'Março',
    '04': 'Abril',
    '05': 'Maio',
    '06': 'Junho',
    '07': 'Julho',
    '08': 'Agosto',
    '09': 'Setembro',
    '10': 'Outubro',
    '11': 'Novembro',
    '12': 'Dezembro'
}


hoje = datetime.now().date() - timedelta(days=8)
print(hoje)

hoje_str = str(hoje).split('-')
print(hoje_str)

dia = hoje_str[2]
mes = hoje_str[1]
ano = hoje_str[0]

print(meses['07'])
caminho_novo = os.path.join(caminho, ano, meses[mes])
print(caminho_novo)

print(hoje.weekday())


