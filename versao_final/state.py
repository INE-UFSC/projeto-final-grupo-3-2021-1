from abc import ABC, abstractmethod
from sistema import Sistema


class State(ABC):

    @property
    def sistema(self) -> Sistema:
        return self._sistema

    @sistema.setter
    def sistema(self, sistema: Sistema):
        self._sistema = sistema

    @abstractmethod
    def executar(self):
        pass


class Menu(State):

    def executar(self):
        # do stuff

        self.sistema.proximo_estado()


class Jogando(State):

    def executar(self):
        # do stuff

        if self.sistema.jogo.jogador.vida <= 0:
            self.sistema.proximo_estado(Final())


class Ranking(State):

    def executar(self):
        # do stuff

        if self.sistema.resposta_usuario:
            self.sistema.proximo_estado(Menu())


class Final(State):

    def executar(self):
        # do stuff

        if self.sistema.resposta_usuario:
            self.sistema.proximo_estado(Menu())