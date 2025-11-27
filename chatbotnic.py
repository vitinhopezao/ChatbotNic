import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}, Absolutamente sim. Python é uma linguagem versátil, fácil de aprender e amplamente usada em áreas como desenvolvimento web, análise de dados, inteligência artificial e automação. Com a crescente demanda por profissionais qualificados, investir tempo em Python pode abrir portas para carreiras promissoras e bem remuneradas. É um esforço que compensa no longo prazo, especialmente se você gosta de resolver problemas de forma criativa.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}, Isso varia bastante dependendo do seu esforço, dedicação e experiência prévia. Para alguém que estuda consistentemente (digamos, algumas horas por dia), pode levar de 2 a 6 meses para adquirir habilidades básicas e começar a se candidatar a vagas iniciais. Fatores como portfólio de projetos pessoais, participação em comunidades e networking também ajudam a acelerar o processo. O importante é focar na prática constante.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, Você saberá quando conseguir aplicar seus conhecimentos em projetos reais, resolver problemas complexos de forma independente e sentir confiança ao explicar seu código para outros. Não há um "momento mágico" – é sobre construir um portfólio sólido, talvez com contribuições para open-source ou apps funcionais. Muitos conseguem empregos razoáveis após demonstrar habilidades em entrevistas práticas, como resolver desafios de código. Continue aprendendo e se desafiando!{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome}, Recomendo plataformas como Coursera (cursos de universidades renomadas, muitos gratuitos), edX (oferece certificados valiosos) e Codecademy (focado em prática interativa). No Brasil, Alura e Danki Code têm cursos completos e acessíveis. Para iniciantes, Asimov Academy é uma boa opção. Combine com recursos gratuitos como documentação oficial do Python e YouTube para exercícios práticos. O segredo é escolher algo que se adapte ao seu ritmo e focar em projetos aplicados.{os.linesep}')
    elif resposta == '5':
        print(f'{os.linesep}Até logo, {nome}!{os.linesep}')
        return True  # Indica que deve sair
    else:
        print('Digite apenas 1, 2, 3, 4 ou 5')
    return False  # Continua o loop

def start():
    # Apresentar o chatbot
    print('Olá! Bem-vindo ao Nic Chat bot')
    # Pedir o nome
    nome = input('Digite seu nome: ')
    # Pedir o email
    email = input('Digite seu email: ')
    while True:
        # Oferecer o menu de opções
        resposta = input(f'O que gostaria de saber hoje?{os.linesep}[1] - Vale a pena aprender Python?{os.linesep}[2] - Quanto tempo leva para eu conseguir um emprego com Python?{os.linesep}[3] - Quando vou saber que estou BOM o suficiente para conseguir um emprego razoável?{os.linesep}[4] - Onde me recomenda estudar Python para conseguir um emprego hoje?{os.linesep}[5] - Sair{os.linesep}')
        # Processar a resposta enviada
        if processar_resposta(resposta, nome):
            break  # Sai do loop se a função retornar True

if __name__ == '__main__':
    start()