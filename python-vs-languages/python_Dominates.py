import pygame
import random
import math

pygame.init()

# NEW SIZE
WIDTH, HEIGHT = 400, 680
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Dominates")

clock = pygame.time.Clock()

BLACK = (10, 10, 10)
WHITE = (255, 255, 255)

# x, y, vx, vy, radius, color, label, alive
balls = [
    [WIDTH//2, HEIGHT//2, 0, 0, 16, (255, 200, 0), "Python", True],

    [50, 120, 1, 1, 10, (80, 255, 120), "C", True],
    [400, 120, -1, 1, 10, (80, 150, 255), "Java", True],
    [100, 650, 1, -1, 10, (255, 80, 80), "C++", True],
    [350, 650, -1, -1, 10, (200, 80, 255), "JS", True],
    [50, 400, 1, -1, 10, (255, 150, 50), "Go", True],
    [400, 400, -1, 1, 10, (150, 150, 150), "Rust", True],
]

particles = []

font = pygame.font.SysFont("Arial", 16)
big_font = pygame.font.SysFont("Arial", 32)

def distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def limit_speed(vx, vy, max_speed):
    speed = math.hypot(vx, vy)
    if speed > max_speed:
        vx = (vx / speed) * max_speed
        vy = (vy / speed) * max_speed
    return vx, vy

def spawn_particles(x, y, color):
    for _ in range(15):
        angle = random.uniform(0, 2*math.pi)
        speed = random.uniform(1, 2.5)
        particles.append([x, y, math.cos(angle)*speed, math.sin(angle)*speed, 15, color])

def move_targets():
    px, py = balls[0][0], balls[0][1]

    for b in balls[1:]:
        if not b[7]:
            continue

        dx = b[0] - px
        dy = b[1] - py
        dist = math.hypot(dx, dy)

        if dist < 180:
            b[2] += (dx/dist) * 0.25
            b[3] += (dy/dist) * 0.25

        b[2] *= 0.98
        b[3] *= 0.98

        b[2], b[3] = limit_speed(b[2], b[3], 1.8)

        b[0] += b[2]
        b[1] += b[3]

                # X-axis
        if b[0] - b[4] < 0:
            b[0] = b[4]
            b[2] *= -1

        elif b[0] + b[4] > WIDTH:
            b[0] = WIDTH - b[4]
            b[2] *= -1

        # Y-axis
        if b[1] - b[4] < 0:
            b[1] = b[4]
            b[3] *= -1

        elif b[1] + b[4] > HEIGHT:
            b[1] = HEIGHT - b[4]
            b[3] *= -1

def move_python():
    py = balls[0]
    targets = [b for b in balls[1:] if b[7]]
    if not targets:
        return

    target = min(targets, key=lambda b: distance(py, b))

    dx = target[0] - py[0]
    dy = target[1] - py[1]
    dist = math.hypot(dx, dy)

    if dist != 0:
        py[2] += (dx/dist) * 0.18
        py[3] += (dy/dist) * 0.18

    py[2] *= 0.97
    py[3] *= 0.97

    py[2], py[3] = limit_speed(py[2], py[3], 2.3)

    py[0] += py[2]
    py[1] += py[3]

def check_collisions():
    py = balls[0]
    for b in balls[1:]:
        if not b[7]:
            continue

        if distance(py, b) < py[4] + b[4]:
            b[7] = False
            spawn_particles(b[0], b[1], b[5])
            py[4] += 4

def update_particles():
    for p in particles[:]:
        p[0] += p[2]
        p[1] += p[3]
        p[4] -= 1
        if p[4] <= 0:
            particles.remove(p)

def draw_particles():
    for p in particles:
        pygame.draw.circle(screen, p[5], (int(p[0]), int(p[1])), 2)

running = True

while running:
    clock.tick(60)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    move_targets()
    move_python()
    check_collisions()
    update_particles()

    draw_particles()

    for b in balls:
        if not b[7]:
            continue

        pygame.draw.circle(screen, b[5], (int(b[0]), int(b[1])), int(b[4]))
        label = font.render(b[6], True, WHITE)
        screen.blit(label, (b[0]-15, b[1]-25))

    # Ending
    alive_targets = [b for b in balls[1:] if b[7]]
    if not alive_targets:
        balls[0][4] += 0.6
        text = big_font.render("Python Wins", True, WHITE)
        screen.blit(text, (WIDTH//2 - 130, HEIGHT//2 - 20))

    pygame.display.flip()

pygame.quit()
