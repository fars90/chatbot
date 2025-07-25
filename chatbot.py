import os
from datetime import datetime

def obter_resposta(texto: str) -> str:
    comando: str = texto.lower()

    #if comando in ('olá', 'boa tarde', 'bom dia'):
    #    return 'Olá tudo bem!'
    #if comando == 'como estás':
    #    return 'Estou bem, obrigado!'
    #if comando == 'como te chamas?':
    #    return 'O meu nome é: Bot :)'
    #if comando == 'tempo':
    #    return 'Está um dia de sol!'
    #if comando in ('bye', 'adeus', 'tchau'):
    #    return 'Gostei de falar contigo! Até breve...'
    #if 'horas' in comando:
    #    return f'São: {datetime.now():%H:%M} horas'
    #if 'data' in comando:
    #    return f'Hoje é dia: {datetime.now():%d-%m-%Y}'

    #return f'Desculpa, não entendi a questão! {texto}'

    respostas = {
        ('olá', 'boa tarde', 'bom dia'): 'Olá tudo bem!',
        'como estás': 'Estou bem, obrigado!',
        'como te chamas?': 'O meu nome é: Bot :)',
        'tempo': 'Está um dia de sol!',
        'que dia é hoje?': f'Hoje é dia: {datetime.now():%d-%m-%Y}',
        'que horas são?': f'São: {datetime.now():%H:%M} horas',
        'tudo bem?': 'Está tudo ótimo, e contigo?',
        'o que sabes fazer?': 'Sei responder a perguntas simples e conversar contigo!',
        'estás aí?': 'Estou sempre aqui :)',
        'qual é a capital de portugal?': 'Lisboa!',
        'o que achas do caso anjos?': 'Ridiculo!',
        'tens algum filme favorito?': 'Claro, o Matrix ;)',
        'gostas de musica?': 'Sim, musica classica!',
        'és adepto de algum clube de futebol?': 'O grande Sporting!!!!',
        'qual é a tua cor favorita?': 'Azul',
        'sagres ou super-bock?': 'super-bock, obvio!',
        'o que és': 'Sou um simples chatbot, mas com muito para dar!',
        'estás a aprender': 'Estou sempre a aprender com as tuas perguntas!',
        'quantos anos tens': 'Fui criado recentemente, mas envelheço muito devagar :)',
        'fala sobre ti': 'Sou um bot simpático que adora conversar contigo!',
        ('bye', 'adeus', 'tchau'): 'Gostei de falar contigo! Até breve...',
    }

    for chave, resposta in respostas.items():
        if isinstance(chave, tuple):
            if comando in chave:
                return resposta
        elif chave in comando:
            return resposta

    return f'Desculpa, não entendi a questão! {texto}'

def chat() -> None:
    print('Bem-vindo ao ChatBot!')
    print('Escreva "bye" para sair do chat')
    name: str = input('Bot: Como te chamas? ')
    print(f'Bot: Olá, {name}! \n Como te posso ajudar?')

    while True:
        user_input: str = input('Tu: ')
        resposta: str = obter_resposta(user_input)
        print(f'Bot: {resposta}')
        if resposta == 'Gostei de falar contigo! Até breve...':
            break

    print('Chat acabou')
    print()


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()


if __name__ == '__main__':
    main()