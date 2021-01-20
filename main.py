import pygame
import random
import math

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("GUI")

clock = pygame.time.Clock()

run = True


def draw_car_info(throttle, brake, speed, steering_angle, score, sensor_data, location_x=0, location_y=0, size_x=0,
                  size_y=0):
    column_1_x = 10
    write_on_canvas(column_1_x, 0, "Throttle: " + str(throttle))
    write_on_canvas(column_1_x, 20, "Brake: " + str(brake))
    write_on_canvas(column_1_x, 40, "Speed: " + str(speed))
    write_on_canvas(column_1_x, 60, "Steering angle: " + str(steering_angle) + "°")
    write_on_canvas(column_1_x, 80, "Score :" + str(score))
    for i in range(len(sensor_data)):
        write_on_canvas(400, i * 20, "Sensor " + str(i) + " value: " + str(sensor_data[i]))
    return


def write_on_canvas(x, y, text):
    font = pygame.font.SysFont("arial", 12)
    img = font.render(text, True, (0, 0, 0))  # Text, Antialiasing, Color
    win.blit(img, (x, y))
    return


def draw_image(img_name, x, y, img_draw_scale=1, rot_angle=0, root_pos=[0, 0]):
    # root_pos = [x,y]:[0,0] Drehpunkt/Positionierungspunkt in Mitte, [-1,-1] oben links [1,-1] oben rechts etc.
    img = pygame.image.load(img_name)
    new_size = (round(img.get_width() * img_draw_scale), round(img.get_height() * img_draw_scale))
    img = pygame.transform.smoothscale(img, new_size)
    original_width = img.get_width()
    original_height = img.get_height()
    rot_in_rad = math.radians(rot_angle)
    img = pygame.transform.rotate(img, rot_angle)
    draw_x = x - img.get_width() / 2 - math.sin(rot_in_rad) * original_height * 0.5 * root_pos[1] - math.cos(
        rot_in_rad) * original_width * 0.5 * root_pos[0]
    draw_y = y - img.get_height() / 2 - math.cos(rot_in_rad) * original_height * 0.5 * root_pos[1] + math.sin(
        rot_in_rad) * original_width * 0.5 * root_pos[0]
    win.blit(img, (draw_x, draw_y))
    return


def draw_circle_piece(x, y, radius, start_angle, end_angle, width=1, color=[0, 0, 0]):
    pygame.draw.arc(win, color, (x - radius, y - radius, radius * 2, radius * 2), math.radians(start_angle),
                    math.radians(end_angle), width=width)
    return


def draw_ui(throttle_value, brake_value, speed_value, steering_angle_value, score_value, sensor_data_list):
   # draw_car_info(throttle_value, brake_value, speed_value, steering_angle_value, score_value, sensor_data_list)

    #Score Darstellen
    score_text = "Score: " + str(score_value)
    font = pygame.font.SysFont("arial", 24)
    img = font.render(score_text, True, (0, 0, 0))  # Text, Antialiasing, Color
    win.blit(img, (350, 200))

    # Auto Sensordaten Visualisierung
    car_img_x = 150
    car_img_y = 300
    num_of_sensors = len(sensor_data_list)
    draw_image("car.png", car_img_x, car_img_y, 0.3)
    # Min Durchmesser = 50+Stiftbreite bei Auto 0.3 Scale
    for i in range(num_of_sensors):
        if sensor_data_list[i] < 1 / 3:
            sensor_color = (230, 0, 0)
        elif 1 / 3 <= sensor_data_list[i] < 2 / 3:
            sensor_color = (230, 120, 30)
        else:
            sensor_color = (100, 220, 0)
        draw_circle_piece(car_img_x, car_img_y, sensor_data_list[i] * 70 + 50 + 10, (360 / num_of_sensors) * i,
                          (360 / num_of_sensors) * (i + 1), 10, sensor_color)

    # Lenkwinkel Anzeige
    angle_img_x = 400
    angle_img_y = 400
    draw_image("Scale.png", angle_img_x, angle_img_y, 0.3, 0, [0, 0.9])
    draw_image("Neadle.png", angle_img_x, angle_img_y, 0.3, steering_angle_value * (-1), [0, 0.75])

    # Lineartacho
    # Maximale Breite der Balken ist ca. 160px bei 0.3-facher Skalierung vom UI Bild "SpeedImage.png"
    # Positionsursprung ist oben links
    vel_img_x = 100
    vel_img_y = 450
    # Geschwindigkeit
    if speed_value >= 0:
        pygame.draw.rect(win, (152, 245, 255), (vel_img_x + 165, vel_img_y, speed_value * 160, 20))
    else:
        pygame.draw.rect(win, (152, 245, 255), (vel_img_x + 165 + speed_value * 160, vel_img_y, -speed_value * 160, 20))
    # Gas
    pygame.draw.rect(win, (0, 200, 0), (vel_img_x + 165, vel_img_y + 20, throttle_value * 160, 21))
    # Bremse
    pygame.draw.rect(win, (200, 0, 0), (vel_img_x + 165 - brake_value * 164, vel_img_y + 20, brake_value * 164, 21))
    # Bild über die Balken malen
    draw_image("speedImage.png", vel_img_x, vel_img_y, 0.3, 0, [-1, -1])

    return


while run:
    clock.tick(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((200, 200, 200))  # Fills the screen with white

    # Zufallswerte als simulierte Daten
    throttle_value = round(random.random(), 2)
    brake_value = round(random.random(), 2)
    speed_value = round(random.random() * 2 - 1, 2)
    steering_angle_value = random.randrange(-45, 45, 1)
    score_value = random.randrange(5000)
    sensor_data_list = [round(random.random(), 2) for i in range(16)]

    # Visualisierung aufrufren
    draw_ui(throttle_value, brake_value, speed_value, steering_angle_value, score_value, sensor_data_list)

    pygame.display.update()

pygame.quit()
