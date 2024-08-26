import pika

# Conectando ao servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Garantindo que a fila "hello" exista
channel.queue_declare(queue='hello')

# Função chamada quando uma mensagem é recebida
def callback(ch, method, properties, body):
    # Decodificando a mensagem
    mensagem_recebida = body.decode('utf-8')
    
    print(f" [x] Recebemos a mensagem: {mensagem_recebida}")
    # Aqui você pode processar a mensagem da forma que desejar

# Escutando a fila "hello"
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Esperando mensagens... Pressione CTRL+C para sair.')
channel.start_consuming()
