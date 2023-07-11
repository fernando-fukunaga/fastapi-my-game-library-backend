from sqlalchemy.orm import Session
from sqlalchemy import update
from src.infra.sqlalchemy.models import models
from src.schemas import schemas
from src.infra.sqlalchemy.repositorios.repositorio_plataforma import \
    RepositorioPlataforma


class RepositorioJogo:

    def __init__(self, session: Session):
        self.session = session

    def usuario_possui_plataforma(self, jogo: models.Jogo,
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
            return None

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

        if not self.usuario_possui_plataforma(model_jogo, usuario_logado):
            return None

        return model_jogo

    def atualizar(self, id_jogo: int, schema_jogo: schemas.JogoCadastro,
                  usuario_logado: models.Usuario):
        if not self.obter(id_jogo, usuario_logado):
            return None

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
        jogo_a_ser_excluido = self.obter(id_jogo, usuario_logado)

        if not jogo_a_ser_excluido:
            return None

        self.session.delete(jogo_a_ser_excluido)
        self.session.commit()
        return {"mensagem": "Jogo removido com sucesso!"}
