from code import playerShot
from code.const import *
from code.enemy import Enemy
from code.entity import Entity
from code.player import Player
from code.playerShot import PlayerShot
from code.enemyShot import EnemyShot


# DESIGN PATTERN MEDIATOR
class EntityMediator(Entity):

    @staticmethod
    def __verify_collision_window(ent: Entity): # __ torna o metodo privado
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0

        # Tiro do player da esquerda para a direita tem vida zerada quando passa do canto direito da tela
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0

        # Tiro do inimigo da direita para o ponto 0 tem vida zerada
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0
        pass

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False

        # tiro do player atinge nave inimiga
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True

        # tiro nave inimiga atinge player
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction: # if valid_interaction == True:
            # A borda DIREITA de E1 está à direita da borda ESQUERDA de E2?
            if (ent1.rect.right >= ent2.rect.left and
                    # A borda ESQUERDA de E1 está à esquerda da borda DIREITA de E2?
                    ent1.rect.left <= ent2.rect.right and
                    # A borda INFERIOR de E1 ABAIXO da borda SUPERIOR de E2
                    ent1.rect.bottom >= ent2.rect.top and
                    # A borda SUPERIOR de E1 ACIMA da borda INFERIOR de E2
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage

                # rastreando qual entidade matou outra entidade
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Player1Shot':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score

        if enemy.last_dmg == 'Player2Shot':
            for ent in entity_list:
                if ent.name == 'Player2':
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        # pega uma entidade (player1, player2, enemhy)
        for i in range(len(entity_list)):
            ent1 = entity_list[i]
            EntityMediator.__verify_collision_window(ent1)
            # verifica se a entidade escolhida colidiu com alguma outra entidade
            for j in range(i+1, len(entity_list)):
                ent2 = entity_list[j]
                EntityMediator.__verify_collision_entity(ent1, ent2)

    # Verificando entidade por entidade e destruindo se vida <= a 0
    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)

