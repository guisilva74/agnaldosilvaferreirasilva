import datetime
import pygame

def configurar_lembrete(data, hora):
    # Obter a data e hora atual
    data_atual = datetime.datetime.now().date()
    hora_atual = datetime.datetime.now().time()

    # Converter a data e hora fornecidas para objetos datetime
    data_lembrete = datetime.datetime.strptime(data, '%d/%m/%Y').date()
    hora_lembrete = datetime.datetime.strptime(hora, '%H:%M').time()

    # Calcular a diferença entre a data/hora atual e a do lembrete
    diferenca_data = data_lembrete - data_atual
    diferenca_hora = datetime.datetime.combine(datetime.date.min, hora_lembrete) - datetime.datetime.combine(datetime.date.min, hora_atual)

    # Calcular o tempo restante em segundos
    tempo_restante = diferenca_data.total_seconds() + diferenca_hora.total_seconds()

    # Agendar o alarme
    pygame.init()
    pygame.mixer.music.load('c:/users/o/agnal/de/Downloads/Metralhadora.mp3')  # Insira o caminho para o arquivo de áudio do alarme
    pygame.mixer.music.play()
    pygame.time.wait(int(tempo_restante * 1000))  # Converter segundos para milissegundos

    # Quando o tempo restante acabar, o alarme será ativado
    print("Alarme ativado!")

# Exemplo de uso
(configurar_lembrete)
