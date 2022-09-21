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

    pt.typewrite("\n", interval=.01)

#Processo de mensagens
def process_response(message):

    match message:

        case "1": 

            return "Anakin Skywalker"
        
        case "2":

            return "Obi-Wan Kenobi"

        case "3":

            return "Mestre Windu"

        case "4":

            return "Darth Tyrannus"

        case "5":

            return "Darth Sidius"

        case "obrigado":

            return "Não precisa agradecer :D"

        case _: 

            return """Ola, eu sou seu assistente virtual, seja bem-vindo ao suporte do DTI. 
            Por favor, selecione e me informe um numero que corresponde ao seu problema:
            \n1 - Lorem ipsum sit amet\n2 - Lorem ipsum sit amet\n3 - Lorem ipsum sit amet\n4 - Lorem ipsum sit amet\n5 - Lorem ipsum sit amet
            """

#Checar se tem novas mensagens
def check_for_new_messages():
    pt.moveTo(x + 100, y - 26, duration=.5)

    while True:

        try:
            position = pt.locateOnScreen("green_circle.png", confidence=.7)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()
                sleep(.5)

        except(Exception):

            print("Sem novas mensagens de novos usuários")

        if pt.pixelMatchesColor(int(x + 100), int(y - 26), (255, 255, 255), tolerance=10):

            processed_message = process_response(get_message())
            post_response(processed_message)
        
        else:

            print("Sem novas mensagens")

        sleep(5)

check_for_new_messages()