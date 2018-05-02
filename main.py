import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plott


def show_info(data):
    create_type_pie_chart(data)
    create_genre_pie_chart(data)
    create_rating_to_price(data)
    create_recommendation_to_price(data)
    create_player_count_to_price(data)
    create_player_count_to_recommendation(data)
    create_player_count_to_rating(data)
    print('\n\n\n')
    print('############################################################')
    print('   The plots have been created in the current directory.')
    print('############################################################\n\n\n')
    main(data)



def create_type_pie_chart(data):
    free_count = data[data['IsFree'] == True].count()
    paid_count = data[data['IsFree'] == False].count()
    temp = {'': pd.Series([free_count[1], paid_count[1]],
                          index=['Free games', 'Paid games'])}
    free_paid_df = pd.DataFrame(temp)
    free_paid_df.plot(kind='pie', title='Type of games', figsize=(6, 6), subplots=True)
    plott.savefig("./type_of_games.png", bbox_inches='tight')
    print('\nCreating type_of_games.png, a pie chart of games based on their cost\n')
    plott.close()


def create_genre_pie_chart(data):
    non_game_count = data[data['GenreIsNonGame'] == True].count()
    indie_game_count = data[data['GenreIsIndie'] == True].count()
    action_game_count = data[data['GenreIsAction'] == True].count()
    adventure_game_count = data[data['GenreIsAdventure'] == True].count()
    casual_game_count = data[data['GenreIsCasual'] == True].count()
    strategy_game_count = data[data['GenreIsStrategy'] == True].count()
    rpg_game_count = data[data['GenreIsRPG'] == True].count()
    simulation_game_count = data[data['GenreIsSimulation'] == True].count()
    early_access_game_count = data[data['GenreIsEarlyAccess'] == True].count()
    free_to_play_game_count = data[data['GenreIsFreeToPlay'] == True].count()
    sports_game_count = data[data['GenreIsSports'] == True].count()
    racing_game_count = data[data['GenreIsRacing'] == True].count()
    massive_mp_game_count = data[data['GenreIsMassivelyMultiplayer'] == True].count()
    temp = {'': pd.Series([non_game_count[1], indie_game_count[1], action_game_count[1],
                           adventure_game_count[1], casual_game_count[1], strategy_game_count[1],
                           rpg_game_count[1], simulation_game_count[1], early_access_game_count[1],
                           free_to_play_game_count[1], sports_game_count[1], racing_game_count[1],
                           massive_mp_game_count[1]],
                          index=['Non game', 'Indie', 'Action', 'Adventure', 'Casual',
                                 'Strategy', 'RPG', 'Simulation', 'Early Access', 'Free To Play',
                                 'Sports', 'Racing', 'Massive Multiplayer'])}
    game_type_df = pd.DataFrame(temp)
    game_type_df.plot(kind='pie', title='Genre of games', figsize=(12, 12), subplots=True)
    plott.savefig("./genre_of_games.png", bbox_inches='tight')
    print('\nCreating genre_of_games.png, a pie chart of games based on their genre\n')
    plott.close()


def create_rating_to_price(data):
    rating_to_price = plott.scatter(data['PriceInitial'], data['Metacritic'])
    plott.xlabel('Price in USD')
    plott.ylabel('Mean Rating')
    plott.xlim((0, 80))
    plott.ylim(20, 100)
    plott.savefig('./rating_to_price.png', bbox_inches='tight')
    print('\nCreating rating_to_price.png, a scattered graph of game ratings to their cost\n')
    plott.close()


def create_recommendation_to_price(data):
    recommendation_to_price = plott.scatter(data['PriceInitial'], data['RecommendationCount'])
    plott.xlabel('Price in USD')
    plott.ylabel('Recommendation count')
    plott.xlim((0, 100))
    plott.ylim((100,200000))
    plott.savefig('./recommendation_to_price.png', bbox_inches='tight')
    print('\nCreating recommendation_to_prices.png, a scattered graph of game ratings to their cost\n')
    plott.close()


def create_player_count_to_price(data):
    player_count_to_price = plott.scatter(data['PriceInitial'], data['SteamSpyPlayersEstimate'])
    plott.xlabel('Price in USD')
    plott.ylabel('Player count')
    plott.xlim((0, 100))
    plott.ylim((0, 5000000))
    plott.savefig('./player_count_to_price.png', bbox_inches='tight')
    plott.close()


def create_player_count_to_recommendation(data):
    create_player_count_to_recommendation = plott.scatter(data['RecommendationCount'], data['SteamSpyPlayersEstimate'])
    plott.xlabel('Recommendation count')
    plott.ylabel('Player count')
    plott.xlim((0, 200000))
    plott.ylim((0, 5000000))
    plott.savefig('./player_count_to_recommendation.png', bbox_inches='tight')
    plott.close()


def create_player_count_to_rating(data):
    create_player_count_to_rating = plott.scatter(data['Metacritic'], data['SteamSpyPlayersEstimate'])
    plott.xlabel('Ratings')
    plott.ylabel('Player count')
    plott.xlim((1, 100))
    plott.ylim((0, 5000000))
    plott.savefig('./player_count_to_rating.png', bbox_inches='tight')
    plott.close()


def search(data):
    print('If you want to return to previous menu, please enter "null"')
    val = input('please enter the gamename you want to search: ')

    if val == 'null':
        main(data)

    res = data[data['Name'] == val][['ID', 'Name', 'ReleaseDate', 'Metacritic']]
    print(res)
    main(data)

def recommend(data):
    print('1. Give recommendation by specific game type')
    print('0. Return to previous menu')
    val = input('please select: ')

    if val == '0':
        main(data)
    elif val == '1':
        print('1. Type "NonGame" for non game genre')
        print('2. Type "Indie" for indie genre')
        print('3. Type "Action" for action genre')
        print('4. Type "Adventure" for adventure genre')
        print('5. Type "Casual" for casual genre')
        print('6. Type "Strategy" for strategy genre')
        print('7. Type "RPG" for role playing genre')
        print('8. Type "Simulation" for simulation genre')
        print('9. Type "EarlyAccess" for early access genre')
        print('10. Type "FreeToPlay" for free to play genre')
        print('11. Type "Sports" for sports genre')
        print('12. Type "Racing" for racing genre')
        print('13. Type "MassivelyMultiplayer" for massively multiplayer genre')
        print('0. Return to previous menu')
        choice = input('Please select one: ')
        rows = input('Please select the number of games you want to limit your results to: ')
        rows = int(rows)
        if choice == '0':
            recommend(data)
        genre_string = 'GenreIs' + choice
        temp = data[data[genre_string] == True]
        t = temp.sort_values(by=['Metacritic'], ascending=False)
        res = t.head(rows)[['Name', 'Metacritic', 'ReleaseDate']]
        print('\n\n\nThe top {} games ranked by ratings are: '.format(rows))
        print(res)
        print('\n\n\nThe top {} new matching games are: '.format(rows))
        temp = temp[temp['ReleaseDate'] != '']
        temp['ReleaseDate'] = pd.to_datetime(temp.ReleaseDate, errors='coerce')
        temp = temp[temp['ReleaseDate'] < datetime.today()]
        t = temp.sort_values(by=['ReleaseDate'], ascending=False)
        res = t.head(rows)[['Name', 'Metacritic', 'ReleaseDate']]
        print(res)
    else:
        print('Invalid input, please select again: ')
        recommend(data)
    main(data)

def rank(data):
    print('For "Overall Rank of sells", press "1"')
    print('For "Overall Rank of players", press "2"')
    print('For "New Release Rank", press "3"')
    print('For returning to previous menu， press "0"')
    val = input('please select: ')
    if val == '0':
        main(data)
    elif val == '1':
        data = data.drop_duplicates(['Name'], keep='last')
        data = data.sort_values(by='SteamSpyOwners', ascending=False)
        rank_sell = data.head(50)[['Name', 'SteamSpyOwners']]
        rank_sell['Rank'] = rank_sell['SteamSpyOwners'].rank(ascending=False).astype('int')
        print(rank_sell)
    elif val == '2':
        data = data.sort_values(by='RecommendationCount', ascending=False)
        rank_pop = data.head(50)[['Name', 'RecommendationCount']]
        rank_pop['Rank'] = rank_pop['RecommendationCount'].rank(ascending=False).astype('int')
        print(rank_pop)
    elif val == '3':
        temp = data[data['ReleaseDate'] != '']
        temp['ReleaseDate'] = pd.to_datetime(temp.ReleaseDate, errors='coerce')
        temp = temp[(temp['ReleaseDate'] < datetime.today()) & (temp['ReleaseDate'] > datetime(2016, 1 , 1))]
        temp = temp.sort_values(by='RecommendationCount', ascending=False)
        rank_new = temp.head(50)[['Name', 'RecommendationCount', 'ReleaseDate']]
        rank_new['Rank'] = rank_new['RecommendationCount'].rank(ascending=False).astype('int')
        print(rank_new)
    else:
        print('Invalid input, please select again: ')
        rank(data)
    main(data)



def main(data):
    print('############################################################')
    print('Welcome to use game box!!!')
    print('1. Basic info(Overview)')
    print('2. Search information by name')
    print('3. Recommendation')
    print('4. Rank Board')
    print('0. Exit')
    print('############################################################')
    val = input("Please enter the function you like (eg: 1): ")

    if val == '1':
        show_info(data)
    elif val == '2':
        search(data)
    elif val == '3':
        recommend(data)
    elif val == '4':
        rank(data)
    elif val == '0':
        print('Thank you for using our product!')
        exit()
    else:
        print('Invalid input, please select again: ')
        main(data)

if __name__ == "__main__":
    data = pd.read_excel("./data.xlsx", 'processed')
    main(data)
