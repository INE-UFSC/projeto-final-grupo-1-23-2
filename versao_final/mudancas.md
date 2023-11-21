# Mudanças feitas para organizar tilemap

- Classe TileMap -> Tile:
  - Não possui mais cor como parametro, pois são imagens
  - Ela serve como base para a criação de todos os tiles

- Classe TileEstatico
  - serve para criar tiles que não são animados

- Classe TileAnimado
  - cria tiles com animações