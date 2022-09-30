import pyautogui as pt
from time import sleep
import pyperclip

sleep(2)

position1 = pt.locateOnScreen("smile_paperclip.png", confidence=.6)
x = position1[0]
y = position1[1]

#Busca a mensagem
def get_message():
    global x, y

    position = pt.locateOnScreen("smile_paperclip.png", confidence=.6)
    x = position[0]
    y = position[1]

    pt.moveTo(x, y, duration=.5)
    pt.moveTo(x + 103, y - 36, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(+ 50, - 125, duration=.5)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print(f"Mensagem recebida: {whatsapp_message}")

    return whatsapp_message

#Posta uma mensagem
def post_response(message):
    global x, y

    position = pt.locateOnScreen("smile_paperclip.png", confidence=.6)
    x = position[0]
    y = position[1]

    pt.moveTo(x + 190, y + 30, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)

    #pt.typewrite("\n", interval=.01)

#O cardapio
def make_a_wish(message):

    message = str("""Ola, eu sou seu assistente virtual, seja bem-vindo ao suporte do DTI. Por favor, selecione e me informe um numero que corresponde ao seu problema:""")

    return message

#Processo de mensagens
def process_response(message):

    match message:

        case "1": 

            return "O suporte tecnico visa lhe auxiliar com problemas como: impossibilidade de conectar-se a internet, computador travando, nao abrindo programas, nao iniciando, mensagens de erro de procedencia duvidosa, nao conectando com impressora ou afins e auxilio em instalacao de programas e afins. Caso seu problema esteja dentre estes, por favor descreva-o."
        
        case "2":

            return "Problemas de usuario ou acesso visa lhe auxiliar caso perca a senha de seu acesso, nao esteja conseguindo entrar em seu perfil ou tenha acessado o seu usuario em outra maquina e nao consiga mais acessar em sua propria. Caso seu problema se encaixe em uma das opcoes, por favor descreva-o."

        case "3":

            return "Virus ou perca de arquivos visa lhe auxiliar caso seu computador esteja apresentando sintomas incomuns, como apagar arquivos recentes ou especificos de sua maquina, criar arquivos de texto, pastas ou .exe suspeitos, esteja apresentando propagandas, janelas ou sites suspeitos sem que voce os acesse por conta propria ou caso tenha perdido um arquivo importante de forma desconhecida. Caso seu problema se encaixe em alguma das opcoes, por favor descreva-o."

        case "4":

            return "Aparentemente seu problema nao se encaixa em nenhuma das alternativas, por favor, descreva detalhadamente seu problema e aguarde que sera repassado para um de nossos tecnicos."

        case _: 

            return "Desculpe, nao consegui entender seu problema. Caso sua opcao nao esteja presente, por favor aguarde que seu problema sera repassado para a administracao e alguem ira atende-lo :)"

#Checar se tem novas mensagens
def check_for_new_messages():
    pt.moveTo(x + 100, y - 26, duration=.5)
    first_msg = 0

    while True:

        try:
            position = pt.locateOnScreen("green_circle.png", confidence=.7)

            if position is not None:
                first_msg = 0
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()
                sleep(.5)

        except(Exception):

            print("Sem novas mensagens de novos usuários")

        if pt.pixelMatchesColor(int(x + 100), int(y - 26), (255, 255, 255), tolerance=10):

            if first_msg == 0:

                processed_message = make_a_wish(get_message())

                first_msg = 1

            else:

                processed_message = process_response(get_message())

            post_response(processed_message)
        
        else:

            print("Sem novas mensagens")

        sleep(5)

check_for_new_messages()