"""Pruebas de calculos.py (actividad 2.3-A4).

Cada función que empieza por test_ es una PRUEBA: comprueba con  assert
que una función devuelve lo que esperamos. pytest las encuentra solas.
"""

from calculos import es_par, es_primo, media, nota_textual, sumar


# --- PARTE A · pruebas que ya pasan -----------------------------------------

def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0


def test_es_par():
    assert es_par(4)
    assert not es_par(7)


# --- PARTE B · E4.1 media ----------------------------------------------------

def test_media():
    assert media([4, 6, 8]) == 6
    assert media([5]) == 5


def test_media_lista_vacia():
    assert media([]) == 0


# --- PARTE B · E4.2 nota_textual ---------------------------------------------

def test_nota_textual():
    assert nota_textual(3) == "Insuficiente"
    assert nota_textual(5) == "Suficiente"
    assert nota_textual(6.5) == "Bien"
    assert nota_textual(8) == "Notable"
    assert nota_textual(10) == "Sobresaliente"


def test_nota_textual_limites():
    assert nota_textual(4.99) == "Insuficiente"
    assert nota_textual(9) == "Sobresaliente"


# --- PARTE B · E4.3 es_primo -------------------------------------------------

def test_es_primo():
    assert es_primo(2)
    assert es_primo(13)
    assert not es_primo(9)


def test_es_primo_casos_especiales():
    assert not es_primo(1)
    assert not es_primo(0)
    assert not es_primo(-7)


# --- PARTE B · E4.4 contar_vocales: escribe aquí TUS pruebas ------------------
