import requests, urllib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.patches import Circle, Rectangle, Arc
from matplotlib.offsetbox import  OffsetImage

'''
tutorial: http://savvastjortjoglou.com/nba-shot-sharts.html
'''

def process_data(shot_chart_url):

    # Get the webpage containing the data
    response = requests.get(shot_chart_url)

    # Grab the headers to be used as column headers for our DataFrame
    player_headers = response.json()['resultSets'][0]['headers']
    # headers = [u'GRID_TYPE', u'GAME_ID', u'GAME_EVENT_ID', u'PLAYER_ID', u'PLAYER_NAME', u'TEAM_ID', u'TEAM_NAME', u'PERIOD', u'MINUTES_REMAINING', u'SECONDS_REMAINING', u'EVENT_TYPE', u'ACTION_TYPE', u'SHOT_TYPE', u'SHOT_ZONE_BASIC', u'SHOT_ZONE_AREA', u'SHOT_ZONE_RANGE', u'SHOT_DISTANCE', u'LOC_X', u'LOC_Y', u'SHOT_ATTEMPTED_FLAG', u'SHOT_MADE_FLAG']

    # Grab the shot chart data
    player_shots = response.json()['resultSets'][0]['rowSet']

    # Obtain the league data
    league_average = response.json()['resultSets'][1]['rowSet']
    league_headers = response.json()['resultSets'][1]['headers']

    shot_df = pd.DataFrame(player_shots, columns=player_headers)

    return shot_df

def plot_fancy_figure(shot_df):

    # # we pass in the link to the image as the 1st argument the 2nd argument tells urlretrieve what we want to scrape
    # pic = urllib.urlretrieve("http://stats.nba.com/media/players/230x185/201935.png", "201935.png")

    # # urlretrieve returns a tuple with our image as the first element and imread reads in the image as a mutlidimensional numpy array so matplotlib can plot it
    # player_pic = plt.imread(pic[0])

    # create our jointplot

    # get our colormap for the main kde plot
    # Note we can extract a color from cmap to use for the plots that lie on the side and top axes
    cmap = plt.cm.YlOrRd_r 

    # n_levels sets the number of contour lines for the main kde plot
    joint_shot_chart = sns.jointplot(shot_df.LOC_X, shot_df.LOC_Y, stat_func=None, kind='kde', space=0, color=cmap(0.1), cmap=cmap, n_levels=50)

    joint_shot_chart.fig.set_size_inches(12,11)

    # A joint plot has 3 Axes, the first one called ax_joint is the one we want to draw our court onto and adjust some other settings
    ax = joint_shot_chart.ax_joint
    draw_court(ax)

    # Adjust the axis limits and orientation of the plot in order to plot half court, with the hoop by the top of the plot
    ax.set_xlim(-250,250)
    ax.set_ylim(422.5, -47.5)

    # Get rid of axis labels and tick marks
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.tick_params(labelbottom='off', labelleft='off')

    # Add a title
    ax.set_title('James Harden FGA 2014-15 Reg. Season', y=1.2, fontsize=18)

    # Add Data Scource and Author
    ax.text(-250, 445, 'Data Source: stats.nba.com' '\nTutorial: http://savvastjortjoglou.com/nba-shot-sharts.html', fontsize=12)

    # # Add player's image to the top right
    # # First create our OffSetImage by passing in our image and set the zoom level to make the image small enough to fit on our plot
    # img = OffsetImage(player_pic, zoom=0.6)
    # # Pass in a tuple of x,y coordinates to set_offset to place the plot where you want, I just played around with the values until I found a spot where I wanted the image to be
    # img.set_offset((625,621))
    # # add the image
    # ax.add_artist(img)

    plt.savefig('JamesHarden_fancy.png', bbox_inches='tight')
    # plt.show()

def plot_plain_figure(shot_df):

    plt.figure(figsize=(12,11))
    plt.scatter(shot_df.LOC_X, shot_df.LOC_Y)
    draw_court()
    # Adjust plot limits to just fit in half court
    plt.xlim(-250,250)
    # Descending values along th y axis from bottom to top in order to place the hoop by the top of plot
    plt.ylim(422.5, -47.5)
    # get rid of axis tick labels
    plt.tick_params(labelbottom=False, labelleft=False)
    plt.savefig('JamesHarden_plain.png', bbox_inches='tight')

def draw_court(ax=None, color='black', lw=2, outer_lines=False):

    # If an axes object isn't provided to plot onto, just get current one
    if ax is None:
        ax = plt.gca()

    # Create the various parts of an NBA basketball court

    # Create the basketball hoop
    # Diameter of a hoop is 18" so it has a radius of 9",
    # which is a value 7.5 in our coordinate system
    hoop = Circle((0, 0), radius=7.5, linewidth=lw, color=color, fill=False)

    # Create backboard
    backboard = Rectangle((-30, -7.5), 60, -1, linewidth=lw, color=color)

    # The paint
    # Create the outer box of the paint, width=16ft, height=19ft
    outer_box = Rectangle((-80, -47.5), 160, 190, linewidth=lw, color=color, fill=False)

    # Create the inner box of the paint, widt=12ft, height=19ft
    inner_box = Rectangle((-60, -47.5), 120, 190, linewidth=lw, color=color, fill=False)

    # Create free throw top arc
    top_free_throw = Arc((0, 142.5), 120, 120, theta1=0, theta2=180, linewidth=lw, color=color, fill=False)

    # Create free throw bottom arc
    bottom_free_throw = Arc((0, 142.5), 120, 120, theta1=180, theta2=0, linewidth=lw, color=color, linestyle='dashed')

    # Restricted Zone, it is an arc with 4ft radius from center of the hoop
    restricted = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=lw, color=color)

    # Three point line
    # Create the side 3pt lines, they are 14ft long before they begin to arc
    corner_three_a = Rectangle((-220, -47.5), 0, 140, linewidth=lw, color=color)
    corner_three_b = Rectangle((220, -47.5), 0, 140, linewidth=lw, color=color)

    # 3pt arc - center of arc will be the hoop, arc is 23'9" away from hoop
    # I just played around with the theta values until they lined up with the threes
    three_arc = Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=lw, color=color)

    # Center Court
    center_outer_arc = Arc((0, 422.5), 120, 120, theta1=180, theta2=0, linewidth=lw, color=color)
    center_inner_arc = Arc((0, 422.5), 40, 40, theta1=180, theta2=0, linewidth=lw, color=color)

    # List of the court elements to be plotted onto the axes
    court_elements = [hoop, backboard, outer_box, inner_box, top_free_throw, bottom_free_throw, restricted, corner_three_a, corner_three_b, three_arc, center_outer_arc, center_inner_arc]

    if outer_lines:
        # Draw the half court line, baseline and side out bound lines
        outer_lines = Rectangle((-250, -47.5), 500, 470, linewidth=lw, color=color, fill=False)
        court_elements.append(outer_lines)

    # Add the court elements onto the axes
    for element in court_elements:
        ax.add_patch(element)

    return ax

def main():

    # parse James Harden's data
    shot_chart_url = 'http://stats.nba.com/stats/shotchartdetail?CFID=33&CFPAR'\
                    'AMS=2014-15&ContextFilter=&ContextMeasure=FGA&DateFrom=&D'\
                    'ateTo=&GameID=&GameSegment=&LastNGames=0&LeagueID=00&Loca'\
                    'tion=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&'\
                    'PaceAdjust=N&PerMode=PerGame&Period=0&PlayerID=201935&Plu'\
                    'sMinus=N&Position=&Rank=N&RookieYear=&Season=2014-15&Seas'\
                    'onSegment=&SeasonType=Regular+Season&TeamID=0&VsConferenc'\
                    'e=&VsDivision=&mode=Advanced&showDetails=0&showShots=1&sh'\
                    'owZones=0'

    shot_df = process_data(shot_chart_url)

    plot_plain_figure(shot_df)
    plot_fancy_figure(shot_df)


if __name__ == '__main__':
    main()