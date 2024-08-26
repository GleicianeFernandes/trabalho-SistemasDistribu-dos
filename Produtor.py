import pika

# Conectando ao servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Garantindo que a fila "hello" exista
channel.queue_declare(queue='hello')

# Solicitar ao usuário que insira uma mensagem
mensagem = input("Digite a mensagem que deseja enviar: ")

# Enviar a mensagem para a fila
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=mensagem)

print(f" [x] Mensagem enviada: '{mensagem}'")

# Função chamada para tratar as respostas do consumidor
def callback(ch, method, properties, body):
    print(f" [x] Resposta do consumidor: {body.decode('utf-8')}")

# Escutando as respostas na mesma fila
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Aguardando respostas...')
channel.start_consuming()
