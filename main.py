from functions import *

window = pygame.display.set_mode((setting_win["WIDTH"], setting_win["HEIGHT"]))

def run():
    game = True

    hero = Hero(10,10,setting_hero["WIDTH"],setting_hero["HEIGHT"],50,50, image= hero_image_list)
    clock = pygame.time.Clock()
    bot1 = Bot(150, 100,setting_bot["WIDTH"],setting_bot["HEIGHT"], image= bot_walk_image_list, vertical= True)
    bot1 = Bot(150, 100,setting_bot["WIDTH"],setting_bot["HEIGHT"], image= bot_walk_image_list, vertical= True)
    

    while game:
        window.fill((12,90,190))

        for wall in wall_list:
            pygame.draw.rect(window, (255, 255, 255), wall)


        
        x, y = 0, 0
        for i in range(100):
            pygame.draw.line(window, (255, 255, 255), (0, y), (setting_win["WIDTH"], y))
            pygame.draw.line(window, (255, 255, 255), (x, 0), (x, setting_win["HEIGHT"]))
            x += 20
            y += 20

        hero.move(window)
        
        bot1.move(window)

        bot2.shoot(window, hero)

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