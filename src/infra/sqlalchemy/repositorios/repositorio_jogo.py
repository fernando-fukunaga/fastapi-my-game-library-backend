# Módulo para interações com a tabela de jogos do banco
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import update
from src.infra.sqlalchemy.models import models
from src.schemas import schemas
from src.errors import errors
from typing import List


class RepositorioJogo:
    """Classe de interações com o banco de dados.

    Exemplo de instânciação:

    repositorio = RepositorioJogo(session)

    Attributes:
        session (Session): sessão do SQLAlchemy para escrita e leitura
        no nosso banco.
    """

    def __init__(self, session: Session) -> None:
        self.session = session

    def insert_jogo(self, jogo: models.Jogo) -> models.Jogo:
        try:
            self.session.add(jogo)
            self.session.commit()
            return jogo
        except Exception:
            raise errors.erro_500("Ocorreu um erro interno! Tente novamente!")
        
    def select_jogos(self) -> List[models.Jogo]:
        try:
            self.session.query(models.Jogo).filter_by(id_usuario=usuario_logado.id)
        except Exception:
            raise errors.erro_500("Ocorreu um erro interno! Tente novamente!")        





'''    def usuario_possui_plataforma(self, jogo: models.Jogo,
                                  usuario_logado: models.Usuario) -> bool:
        consulta = (self.session.query(models.Plataforma).
                    filter_by(id=jogo.id_plataforma,
                              id_usuario=usuario_logado.id).
                    first())

        if not consulta:
            return False

        return True

    def criar(self, schema_jogo: schemas.JogoCadastro,
              usuario_logado: models.Usuario):
        model_jogo = models.Jogo(nome=schema_jogo.nome,
                                 id_plataforma=schema_jogo.id_plataforma,
                                 ano=schema_jogo.ano,
                                 categoria=schema_jogo.categoria,
                                 desenvolvedora=schema_jogo.desenvolvedora,
                                 observacoes=schema_jogo.observacoes,
                                 progresso=schema_jogo.progresso)

        if not self.usuario_possui_plataforma(model_jogo, usuario_logado):
            raise errors.erro_400("Usuário não possui essa plataforma!")

        self.session.add(model_jogo)
        self.session.commit()
        self.session.refresh(model_jogo)
        return model_jogo

    def listar(self, usuario_logado: models.Usuario):
        lista_inicial = self.session.query(models.Jogo).all()
        lista_final = []

        for jogo in lista_inicial:
            if self.usuario_possui_plataforma(jogo, usuario_logado):
                lista_final.append(jogo)

        return lista_final

    def obter(self, id_jogo: int, usuario_logado: models.Usuario):
        model_jogo = (self.session.query(models.Jogo).filter_by(id=id_jogo).
                      first())

        if not model_jogo:
            raise errors.erro_404("Jogo não encontrado!")

        if not self.usuario_possui_plataforma(model_jogo, usuario_logado):
            raise errors.erro_404("Jogo não encontrado!")

        return model_jogo

    def atualizar(self, id_jogo: int, schema_jogo: schemas.JogoPut,
                  usuario_logado: models.Usuario):
        try:
            self.obter(id_jogo, usuario_logado)

        except HTTPException:
            raise errors.erro_404("Jogo não encontrado!")

        update_statement = (update(models.Jogo).
                            where(models.Jogo.id == id_jogo).
                            values(nome=schema_jogo.nome,
                                   ano=schema_jogo.ano,
                                   categoria=schema_jogo.categoria,
                                   desenvolvedora=schema_jogo.desenvolvedora,
                                   observacoes=schema_jogo.observacoes,
                                   progresso=schema_jogo.progresso))

        self.session.execute(update_statement)
        self.session.commit()
        return self.obter(id_jogo, usuario_logado)

    def remover(self, id_jogo: int, usuario_logado: models.Usuario):
        try:
            self.obter(id_jogo, usuario_logado)

        except HTTPException:
            raise errors.erro_404("Jogo não encontrado!")

        self.session.delete(self.obter(id_jogo, usuario_logado))
        self.session.commit()
        return {"mensagem": "Jogo removido com sucesso!"}'''
