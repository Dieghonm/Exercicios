import pygame
import sys

# Defina as dimensões da tela e o tamanho dos pixels
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
PIXEL_SIZE = 10

# Defina algumas cores RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pixel Art")

    pixels = [[WHITE for _ in range(SCREEN_HEIGHT // PIXEL_SIZE)] for _ in range(SCREEN_WIDTH // PIXEL_SIZE)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Obtém a posição do mouse
                mouse_pos = pygame.mouse.get_pos()
                # Calcula o índice do pixel
                pixel_x, pixel_y = mouse_pos[0] // PIXEL_SIZE, mouse_pos[1] // PIXEL_SIZE
                # Atualiza a cor do pixel com base na cor selecionada
                if event.button == 1:  # Botão esquerdo do mouse
                    pixels[pixel_x][pixel_y] = RED
                elif event.button == 3:  # Botão direito do mouse
                    pixels[pixel_x][pixel_y] = BLUE
                elif event.button == 2:  # Botão do meio do mouse
                    pixels[pixel_x][pixel_y] = YELLOW
                elif event.button == 4:  # Botão de rolagem para cima
                    pixels[pixel_x][pixel_y] = WHITE
                elif event.button == 5:  # Botão de rolagem para baixo
                    pixels[pixel_x][pixel_y] = BLACK

        # Desenha os pixels na tela
        for x in range(len(pixels)):
            for y in range(len(pixels[x])):
                pygame.draw.rect(screen, pixels[x][y], (x * PIXEL_SIZE, y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
