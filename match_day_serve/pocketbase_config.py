from pocketbase import PocketBase  # Client also works the same

def init():
    client = PocketBase('http://192.168.1.15:8090')
    # client.collection('sd').get_list()
    # teams = client.collection('teams').get_list(1, 50, {filter: 'category = 5walm6hfnwmqs2q'})
    # print(teams)
    return client
    