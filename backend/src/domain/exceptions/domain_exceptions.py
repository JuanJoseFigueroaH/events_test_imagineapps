class DomainException(Exception):
    """Excepción base para el dominio."""
    pass

class EventNotFound(DomainException):
    def __init__(self, message="Evento no encontrado"):
        super().__init__(message)

class CategoryNotFound(DomainException):
    def __init__(self, message="Categoría no encontrada"):
        super().__init__(message)
