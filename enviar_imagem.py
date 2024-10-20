import pywhatkit as kit
import time
import logging

# Configuração básica do logging para registrar erros e eventos importantes
logging.basicConfig(filename='whatsapp_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def enviar_mensagem(numero, mensagem, delay=2):
    """Envia uma mensagem de texto pelo WhatsApp agendada para alguns minutos à frente."""
    try:
        hora_atual = time.localtime().tm_hour
        minuto_atual = time.localtime().tm_min + delay

        kit.sendwhatmsg(numero, mensagem, hora_atual, minuto_atual)
        logging.info(f"Mensagem enviada para {numero}")
    except Exception as e:
        logging.error(f"Erro ao enviar mensagem para {numero}: {str(e)}")

def enviar_imagem(numero, imagem, legenda="Aqui está a imagem!", delay=10):
    """Envia uma imagem pelo WhatsApp com uma legenda opcional."""
    try:
        time.sleep(delay)  # Aguarda para garantir que o WhatsApp carregou
        kit.sendwhats_image(numero, imagem, legenda, wait_time=10)
        logging.info(f"Imagem enviada para {numero}")
    except Exception as e:
        logging.error(f"Erro ao enviar imagem para {numero}: {str(e)}")

def enviar_para_contatos(numeros, imagem, mensagem):
    """Envia uma mensagem e uma imagem para uma lista de contatos."""
    for numero in numeros:
        enviar_mensagem(numero, mensagem)
        enviar_imagem(numero, imagem)

if __name__ == "__main__":
    # Lista de números de telefone (com código do país +55 para Brasil)
    numeros = ["+5518XXXXXXXX", "+5518XXXXXXXX"]

    # Caminho da imagem que você deseja enviar
    imagem = r"C:\Users\Andre Junior\Downloads\Nova pasta\amor.jpg"
    
    # Mensagem de boas-vindas
    mensagem = "Olá! Seja bem-vindo à Loja Online"

    # Enviar mensagem e imagem para todos os números da lista
    enviar_para_contatos(numeros, imagem, mensagem)
