from domain.entities.action import Action
from infra.pg.models.user import ActionORM


class GetActionFromORM:
    @staticmethod
    def execute(action: ActionORM) -> Action:
        action_entity = Action(
            oid=action.oid, content=action.content, author_name=action.author_name
        )
        return action_entity
