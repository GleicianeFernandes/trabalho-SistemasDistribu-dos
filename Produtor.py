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

# Fechando a conexão
connection.close()
