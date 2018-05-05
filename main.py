import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plott


# Wrapper function which helps plot graphs and images to visualize the data better
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


# Creates a pie chart showing how many games are free and how many are paid
def create_type_pie_chart(data):
    # Get the count of games based on if they are paid or not
    free_count = data[data['IsFree'] == True].count()
    paid_count = data[data['IsFree'] == False].count()

    temp = {'': pd.Series([free_count[1], paid_count[1]],
                          index=['Free games', 'Paid games'])}
    free_paid_df = pd.DataFrame(temp)

    # Plot the information stored in the dataframe
    free_paid_df.plot(kind='pie', title='Type of games', figsize=(6, 6), subplots=True)
    plott.savefig("./type_of_games.png", bbox_inches='tight')
    print('\nCreating type_of_games.png, a pie chart of games based on their cost\n')
    plott.close()

# Creates a pie chart showing the count of games based on their genre
def create_genre_pie_chart(data):
    # Get the count of games based on the genre
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

    # Plot the information stored in the dataframe
    game_type_df.plot(kind='pie', title='Genre of games', figsize=(12, 12), subplots=True)
    plott.savefig("./genre_of_games.png", bbox_inches='tight')
    print('\nCreating genre_of_games.png, a pie chart of games based on their genre\n')
    plott.close()

# Creates a scattered graph of game ratings to their cost
def create_rating_to_price(data):
    # Plot a scattered graph
    rating_to_price = plott.scatter(data['PriceInitial'], data['Metacritic'])
    plott.xlabel('Price in USD')
    plott.ylabel('Mean Rating')
    plott.xlim((0, 80))
    plott.ylim(20, 100)
    plott.savefig('./rating_to_price.png', bbox_inches='tight')
    print('\nCreating rating_to_price.png, a scattered graph of game ratings to their cost\n')
    plott.close()

# Creates a scattered graph of game recommendations to their cost
def create_recommendation_to_price(data):
    # Plot a scattered graph
    recommendation_to_price = plott.scatter(data['PriceInitial'], data['RecommendationCount'])
    plott.xlabel('Price in USD')
    plott.ylabel('Recommendation count')
    plott.xlim((0, 100))
    plott.ylim((100,200000))
    plott.savefig('./recommendation_to_price.png', bbox_inches='tight')
    print('\nCreating recommendation_to_prices.png, a scattered graph of recommendation to their cost\n')
    plott.close()

# Creates a scattered graph of player count to their cost
def create_player_count_to_price(data):
    # Plot a scattered graph
    player_count_to_price = plott.scatter(data['PriceInitial'], data['SteamSpyPlayersEstimate'])
    plott.xlabel('Price in USD')
    plott.ylabel('Player count')
    plott.xlim((0, 100))
    plott.ylim((0, 5000000))
    plott.savefig('./player_count_to_price.png', bbox_inches='tight')
    print('\nCreating player_count_to_price.png, a scattered graph of player count to their cost\n')
    plott.close()

# Creates a scattered graph of player count to game recommendations
def create_player_count_to_recommendation(data):
    # Plot a scattered graph
    create_player_count_to_recommendation = plott.scatter(data['RecommendationCount'], data['SteamSpyPlayersEstimate'])
    plott.xlabel('Recommendation count')
    plott.ylabel('Player count')
    plott.xlim((0, 200000))
    plott.ylim((0, 5000000))
    plott.savefig('./player_count_to_recommendation.png', bbox_inches='tight')
    print('\nCreating player_count_to_recommendation.png, a scattered graph of player count to the game recommendations\n')
    plott.close()

# Creates a scattered graph of player count to the game ratings
def create_player_count_to_rating(data):
    # Plot a scattered graph
    create_player_count_to_rating = plott.scatter(data['Metacritic'], data['SteamSpyPlayersEstimate'])
    plott.xlabel('Ratings')
    plott.ylabel('Player count')
    plott.xlim((1, 100))
    plott.ylim((0, 5000000))
    plott.savefig('./player_count_to_rating.png', bbox_inches='tight')
    print('\nCreating player_count_to_rating.png, a scattered graph of player count to the game ratings\n')
    plott.close()

# Looks for a game by name in the data and returns some basic information
def search(data):
    print('If you want to return to previous menu, please enter "null"')
    val = input('please enter the gamename you want to search: ')

    if val == 'null':
        main(data)

    # Extract the id, name, release date and the critics rating for the game with the name 'val'
    res = data[data['Name'] == val][['ID', 'Name', 'ReleaseDate', 'Metacritic']]
    print(res)
    main(data)

# Recommends a list of game to the user based on the genre selected.
# Created two lists, one sorted by the critics rating in descending order
# And another sorted by the release date showing the latest games.
def recommend(data):
    print('1. Give recommendation by specific game type')
    print('0. Return to previous menu')
    val = input('please select: ')

    if val == '0':
        main(data)
    elif val == '1':
        # Get the genre from the user
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

        # Sort by the critics rating
        t = temp.sort_values(by=['Metacritic'], ascending=False)

        # Select top 'rows' number of results
        res = t.head(rows)[['Name', 'Metacritic', 'ReleaseDate']]
        print('\n\n\nThe top {} games ranked by ratings are: '.format(rows))
        print(res)

        # Filter the data and select only the games with release date smaller than today's date
        temp = temp[temp['ReleaseDate'] != '']
        temp['ReleaseDate'] = pd.to_datetime(temp.ReleaseDate, errors='coerce')
        temp = temp[temp['ReleaseDate'] < datetime.today()]

        # Sort it by the release date
        t = temp.sort_values(by=['ReleaseDate'], ascending=False)
        # Select top 'rows' number of results
        res = t.head(rows)[['Name', 'Metacritic', 'ReleaseDate']]
        print('\n\n\nThe top {} new matching games are: '.format(rows))
        print(res)
    else:
        print('Invalid input, please select again: ')
        recommend(data)
    main(data)

# Ranks the games by the category chosen
def rank(data):
    # Get the category from the user
    print('For "Overall Rank of sells", press "1"')
    print('For "Overall Rank of players", press "2"')
    print('For "New Release Rank", press "3"')
    print('For returning to previous menu， press "0"')
    val = input('please select: ')
    if val == '0':
        main(data)
    elif val == '1':
        # Drop duplicates with the same name
        data = data.drop_duplicates(['Name'], keep='last')

        # Sort the data by the number of owners
        data = data.sort_values(by='SteamSpyOwners', ascending=False)

        # Select the top 50 results
        rank_sell = data.head(50)[['Name', 'SteamSpyOwners']]
        rank_sell['Rank'] = rank_sell['SteamSpyOwners'].rank(ascending=False).astype('int')
        print(rank_sell)
    elif val == '2':
        # Sort the data by the recommendation count
        data = data.sort_values(by='RecommendationCount', ascending=False)

        # Select the top 50 results
        rank_pop = data.head(50)[['Name', 'RecommendationCount']]
        rank_pop['Rank'] = rank_pop['RecommendationCount'].rank(ascending=False).astype('int')
        print(rank_pop)
    elif val == '3':
        # Filter invalid data
        temp = data[data['ReleaseDate'] != '']
        temp['ReleaseDate'] = pd.to_datetime(temp.ReleaseDate, errors='coerce')
        temp = temp[(temp['ReleaseDate'] < datetime.today()) & (temp['ReleaseDate'] > datetime(2016, 1 , 1))]

        # Sort by the recommendation count
        temp = temp.sort_values(by='RecommendationCount', ascending=False)

        # Select the top 50 results
        rank_new = temp.head(50)[['Name', 'RecommendationCount', 'ReleaseDate']]
        rank_new['Rank'] = rank_new['RecommendationCount'].rank(ascending=False).astype('int')
        print(rank_new)
    else:
        print('Invalid input, please select again: ')
        rank(data)
    main(data)



def main(data):
    # The home page or the welcome screen
    print('############################################################')
    print('Welcome to game box!!!')
    print('1. Basic info(Overview)')
    print('2. Search information by name')
    print('3. Recommendation')
    print('4. Rank Board')
    print('0. Exit')
    print('############################################################')
    val = input("Please enter the function you like (eg: 1): ")

    # Appropriate functions to be called based on user input
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
    # Read the data from the excel workbook
    data = pd.read_excel("./data.xlsx", 'processed')
    main(data)
