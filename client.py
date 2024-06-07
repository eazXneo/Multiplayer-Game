import pygame

# TODO: WIT
clientNumber = 0


class Player:
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        # ... these seem to be passed by value
        # ... also seems to simplify passing character params to other pygame methods?
        self.rect = (x, y, width, height)
        # ... distance moved in one move
        self.vel = 3

    def draw(self, win):
        """
        TODO: WIT
        """

        pygame.draw.rect(win, self.colour, self.rect)

    def move(self):
        """
        s.ab. this allows for diagonal movement, whereas checking in main() doesn't allow for that
        (because one key checked at one time?)
        """

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.rect = (self.x, self.y, self.width, self.height)

    # TODO: so, similar to move(), maybe drag() using pygame to allow for dragging?


"""
Pygame project basics start
"""
def redraw_window(win, player):
    """
    TODO: WIT
    """

    win.fill((255,255,255))
    player.draw(win)
    pygame.display.update()

def main():
    # initialize the pygame module
    pygame.init()

    # ... create UI window
    width = 500
    height = 500
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Client")

    run = True
    p = Player(50, 50, 100, 100, (0, 255, 0))

    # debug
    clock = pygame.time.Clock()

    while run:
        # debug
        clock.tick(60)

        # ... either move to the top, or break to not hit this when pygame has quit.
        # now moved, let's see.
        p.move()
        redraw_window(win, p)

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed) (TODO: WIT)
if __name__=="__main__":
    # call the main function
    main()

"""
Pygame project basics end
"""