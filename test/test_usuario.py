import pytest
from app..usuario import Usuario


def test_autenticar_usuario_correcto():
    usuario = Usuario("admin", "admin123", "Coordinador")
    assert usuario.autenticar("admin123") is True


def test_autenticar_usuario_incorrecto():
    usuario = Usuario("admin", "admin123", "Coordinador")
    assert usuario.autenticar("wrongpassword") is False


def test_crear_usuario():
    usuario = Usuario("juan", "juan123", "Analista")
    assert usuario.username == "juan"
    assert usuario.rol == "Analista"
