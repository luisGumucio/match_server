from pocketbase import PocketBase  # Client also works the same
import os

def init():
    client = PocketBase(os.environ.get('POCKETBASE_URL', 'http://192.168.1.15:8090'))
    # client.collection('sd').get_list()
    # teams = client.collection('teams').get_list(1, 50, {filter: 'category = 5walm6hfnwmqs2q'})
    # print(teams)
    # client.collection('teams')._get_first_list_item
    #  result = client.collection("example").get_list(
    # 1, 20, {"filter": 'status = true && created > "2022-08-01 10:00:00"'})
    # client.records.get_list(1, 50, {filter: 'categoryId = 5walm6hfnwmqs2q'})
    # client.collection('teams')._get_full_list(query_params={filter: 'categoryId = 5walm6hfnwmqs2q'})
    # client.collection("teams").get_list(
    # 1, 20, {"filter": 'categoryId = "5walm6hfnwmqs2q"'})
    return client
    