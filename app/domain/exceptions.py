class DomainError(Exception):
    """Base de todos os erros de regra de negócio."""


class NotFoundError(DomainError):
    """Base dos erros de 'não encontrado'."""


class ItemNotFound(NotFoundError):
    """O item procurado não existe."""


class CharacterNotFound(NotFoundError):
    """O personagem procurado não existe."""


class ItemNotForging(DomainError):
    """Tentativa de terminar a forja de um item que não está em forja."""


class ItemNotReady(DomainError):
    """Tentativa de equipar um item que ainda não está pronto."""


class CharacterInactive(DomainError):
    """Tentativa de equipar um item em um personagem inativo."""
