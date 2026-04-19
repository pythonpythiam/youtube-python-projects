import pygame
import math
import random

pygame.init()

# 📱 9:16 screen
WIDTH, HEIGHT = 540, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Satisfying Bounce Game")

clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 70)
WHITE = (255, 255, 255)

# Center
center = (WIDTH // 2, HEIGHT // 2 + 50)

# Circle
radius = 200

# Ball
ball_radius = 6
ball_x = center[0] + 80
ball_y = center[1]

speed = 7
angle = random.uniform(0, 2 * math.pi)
vx = math.cos(angle) * speed
vy = math.sin(angle) * speed

# Score
score = 0

# Fonts
font_big = pygame.font.SysFont("Arial", 36, bold=True)
font_small = pygame.font.SysFont("Consolas", 18)

# Matrix background
columns = WIDTH // 20
drops = [random.randint(0, HEIGHT) for _ in range(columns)]

def draw_matrix():
    for i in range(len(drops)):
        char = chr(random.randint(33, 126))
        text = font_small.render(char, True, GREEN)
        screen.blit(text, (i * 20, drops[i]))
        drops[i] += random.randint(6, 12)
        if drops[i] > HEIGHT:
            drops[i] = 0

# Sound (simple)
pygame.mixer.init()
sound = pygame.mixer.Sound(buffer=b'\x00\x00' * 1000)

# Collision control
collision_cooldown = 0
COOLDOWN_TIME = 8

# Glow
glow_timer = 0

running = True

while running:
    screen.fill(BLACK)
    draw_matrix()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Slow motion when small
    dt = 0.5 if radius < 80 else 1

    # Move ball
    ball_x += vx * dt
    ball_y += vy * dt

    dx = ball_x - center[0]
    dy = ball_y - center[1]
    distance = math.hypot(dx, dy)

    if collision_cooldown > 0:
        collision_cooldown -= 1

    # 🎯 Collision
    if distance + ball_radius >= radius and collision_cooldown == 0:
        nx = dx / distance
        ny = dy / distance

        dot = vx * nx + vy * ny
        vx -= 2 * dot * nx
        vy -= 2 * dot * ny

        # Push inside (important fix)
        ball_x = center[0] + nx * (radius - ball_radius - 2)
        ball_y = center[1] + ny * (radius - ball_radius - 2)

        # 🔥 CLEAR shrink
        radius -= 2   # increased reduction for visibility

        # 🔥 Ball grows (satisfying effect)
        ball_radius += 0.5
        if ball_radius > 20:
            ball_radius = 20  # limit

        score += 1

        # Slight speed increase
        vx *= 1.02
        vy *= 1.02

        glow_timer = 4
        sound.play()

        collision_cooldown = COOLDOWN_TIME

        if radius < 50:
            running = False

    # 💥 Glow (lighter so shrink is visible)
    if glow_timer > 0:
        pygame.draw.circle(screen, (0, 200, 0), center, int(radius + 3), 2)
        glow_timer -= 1

    # Draw circle
    pygame.draw.circle(screen, GREEN, center, int(radius), 2)

    # Ball
    pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), int(ball_radius))

    # Title
    title = font_big.render("WATCH CLOSELY", True, WHITE)
    screen.blit(title, (WIDTH//2 - title.get_width()//2,  HEIGHT - 730))

    # Score
    score_text = font_big.render(f"{score}", True, WHITE)
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT - 130))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
