from DAO.DAO import DAO


class RankingDAO(DAO):

    def __init__(self):
        super().__init__('versao_final/src/ranking.json')
