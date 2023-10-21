from functions import *

window = pygame.display.set_mode((setting_win["WIDTH"], setting_win["HEIGHT"]))

def run():
    game = True

    hero = Hero(10,10,50,50)
    clock = pygame.time.Clock()

    while game:
        window.fill((12,90,120))

        hero.move(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    hero.MOVE["UP"] = True
                if event.key == pygame.K_s:
                        hero.MOVE["DOWN"] = True
                if event.key == pygame.K_a:
                        hero.MOVE["LEFT"] = True
                if event.key == pygame.K_d:
                        hero.MOVE["RIGHT"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                      hero.MOVE["UP"] = False
                if event.key == pygame.K_s:
                      hero.MOVE["DOWN"] = False
                if event.key == pygame.K_a:
                      hero.MOVE["LEFT"] = False
                if event.key == pygame.K_d:
                      hero.MOVE["RIGHT"] = False

                        
                
        clock.tick(60)
        pygame.display.flip()

run()