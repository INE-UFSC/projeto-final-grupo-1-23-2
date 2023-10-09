from MenuAbstrato import MenuAbstrato

class MenuVitoria(MenuAbstrato):
    def __init__(self, screen, background: str, musica: str, botoes: list):
        super().__init__(screen, background, musica, botoes)
    
    def draw(self):
        pass