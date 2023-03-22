import logging

class ActionsService:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def __init__(self, client):
        self.client = client

    def generate_standings(self, competition_id):
        # Obtener información de la competencia.
        competitions = self.client.collection('competions').get_one(competition_id)
        logging.info(competitions.id)
        logging.info('La función my_function ha sido llamada.')
        
        # Iterar sobre las categorías de la competencia.
        for category in competitions.categories:
            teams_list = self.get_teams_for_category(category)
            if len(teams_list.items) != 0:
                self.create_standings_records(competitions, category, teams_list)

        print(f'Las posiciones de la competencia {competitions.name} se han generado exitosamente.')

    def get_teams_for_category(self, category):
        # Obtener los equipos de la categoría.
        # return self.client.collection('teams').get_list(
        #     1, 50, query_params={filter: f'category = {category}'})
        return self.client.collection("teams").get_list(
    1, 20, {"filter": f'categoryId = "{category}"'})

    def create_standings_records(self, competitions, category, teams_list):
        # Iterar sobre los equipos de la categoría.

        for team in teams_list.items:
            data = {
                "teamId": team.id,
                "playedGames": 0,
                "won": 0,
                "draw": 0,
                "lost": 0,
                "points": 0,
                "name": team.name,
                "urlLogo": team.url_logo,
                "categoryId": category,
                "competionId": competitions.id
            }
            # Crear los registros de la tabla de posiciones.
            self.client.collection('standings').create(data)

