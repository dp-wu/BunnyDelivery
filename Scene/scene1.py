import pygame


class Scene1(pygame.sprite.Sprite):
    def __init__(self, bg_image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(bg_image)
        self.rect = self.image.get_rect(topleft=pos)
