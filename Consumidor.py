import pika
from googletrans import Translator

# Conectando ao servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Garantindo que a fila "hello" exista
channel.queue_declare(queue='hello')

# Criando o tradutor
translator = Translator()

# Função chamada quando uma mensagem é recebida
def callback(ch, method, properties, body):
    # Decodificando a mensagem
    mensagem_recebida = body.decode('utf-8')
    
    print(f" [x] Recebemos a mensagem: {mensagem_recebida}")
    
    # Traduzindo a mensagem para o inglês
    traducao = translator.translate(mensagem_recebida, dest='en')
    print(f" [x] Tradução: {traducao.text}")
    
    # Respondendo ao produtor
    resposta = f"Resposta à mensagem: {mensagem_recebida}"
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=resposta)
    print(f" [x] Resposta enviada: {resposta}")

# Escutando a fila "hello"
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Esperando mensagens... Pressione CTRL+C para sair.')
channel.start_consuming()
