import pygame
import random
import math

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("GUI")

clock = pygame.time.Clock()

run = True

rot_tick = 0


def draw_car_info(throttle, brake, speed, steering_angle, score, sensor_data, location_x=0, location_y=0, size_x=0,
                  size_y=0):
    write_on_canvas(0, 0, "Throttle: " + str(throttle))
    write_on_canvas(0, 20, "Brake: " + str(brake))
    write_on_canvas(0, 40, "Speed: " + str(speed))
    write_on_canvas(0, 60, "Steering angle: " + str(steering_angle) + "°")
    write_on_canvas(0, 80, "Score :" + str(score))
    for i in range(len(sensor_data)):
        write_on_canvas(150, i * 20, "Sensor " + str(i) + " value: " + str(sensor_data[i]))

    return


def write_on_canvas(x, y, text):
    font = pygame.font.SysFont("arial", 12)
    img = font.render(text, True, (0, 0, 0))  # Text, Antialiasing, Color
    win.blit(img, (x, y))
    return


def draw_image(img_name, x, y, img_draw_scale=1, rot_angle=0, root_pos=[0, 0]):
    # root_pos = [x,y]:[0,0] Drehpunkt in Mitte, [-1,-1] oben links [1,-1] oben rechts etc.
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


def draw_UI():
    throttle_value = round(random.random(), 2)
    brake_value = round(random.random(), 2)
    speed_value = round(random.random() * 3, 2)
    steering_angle_value = random.randrange(-45, 45, 1)
    score_value = random.randrange(5000)
    sensor_data_list = [round(random.random(), 2) for i in range(8)]

    draw_car_info(throttle_value, brake_value, speed_value, steering_angle_value, score_value, sensor_data_list)

    draw_image("car.png", 100, 300, 0.3)
    draw_image("Scale.png", 300, 350, 0.3, 0, [0, 0.9])
    draw_image("Neadle.png", 300, 350, 0.3, steering_angle_value * (-1), [0, 0.75])

    pygame.draw.rect(win, (0, 200, 0), (215, 400, 50, 20))
    pygame.draw.rect(win, (200, 0, 0), (215-50, 420, 50, 20))
    draw_image("SpeedImage.png", 50, 400, 0.3, 0, [-1, -1])


while run:
    clock.tick(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((200, 200, 200))  # Fills the screen with white
    draw_UI()
    pygame.display.update()

pygame.quit()
