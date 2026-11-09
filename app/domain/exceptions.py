class DomainError(Exception):
    """Base de todos os erros de regra de negócio."""


class ItemNotFound(DomainError):
    """O item procurado não existe."""


class ItemNotForging(DomainError):
    """Tentativa de terminar a forja de um item que não está em forja."""
