"""Módulo para gestão de erros/exceptions

Funções utilizadas para levantar exceptions, temos uma função para
cada status code. A função receberá uma string como parâmetro que será a
mensagem de erro a ser exibida ao usuário.
"""
from fastapi import HTTPException


def erro_400(mensagem: str) -> HTTPException:
    return HTTPException(status_code=400, detail=mensagem)


def erro_401(mensagem: str) -> HTTPException:
    return HTTPException(status_code=401, detail=mensagem)


def erro_404(mensagem: str) -> HTTPException:
    return HTTPException(status_code=404, detail=mensagem)


def erro_500(mensagem: str) -> HTTPException:
    return HTTPException(status_code=500, detail=mensagem)
