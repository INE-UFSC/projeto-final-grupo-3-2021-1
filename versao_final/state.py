from abc import ABC, abstractmethod


class State(ABC):

    def __init__(self, sistema, fundo, musica):
        self._sistema = sistema
        self.__setup(fundo, musica)

    def __setup(self, fundo, musica):
        self._sistema.fundo_atual = fundo
        self._sistema.musica_atual = musica

    @property
    def sistema(self):
        return self._sistema

    @sistema.setter
    def sistema(self, sistema):
        self._sistema = sistema

    @abstractmethod
    def executar(self):
        pass


class Menu(State):

    def __init__(self, sistema, fundo, musica):
        super().__init__(sistema, fundo, musica)

    def executar(self):
        # do stuff

        self.sistema.proximo_estado(self.sistema)


class Jogando(State):

    def __init__(self, sistema, fundo, musica):
        super().__init__(sistema, fundo, musica)

    def executar(self):
        # do stuff

        if self.sistema.jogo.jogador.vida <= 0:
            self.sistema.proximo_estado(Final(self.sistema))


class Ranking(State):

    def __init__(self, sistema, fundo, musica):
        super().__init__(sistema, fundo, musica)

    def executar(self):
        # do stuff

        if self.sistema.resposta_usuario:
            self.sistema.proximo_estado(Menu(self.sistema))


class Final(State):

    def __init__(self, sistema, fundo, musica):
        super().__init__(sistema, fundo, musica)

    def executar(self):
        # do stuff

        if self.sistema.resposta_usuario:
            self.sistema.proximo_estado(Menu(self.sistema))