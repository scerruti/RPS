import re
import requests
import HTML_TAGS as HTML
import random
import webserver
import argparse
import logging


def play_rps(human_move, computer_move):
    """
    play_rps accepts two moves and returns the outcome of a game of
    rock, paper, scissors.

    moves should be a string containing either 'rock', 'paper' or 'scissors'
    the outcome should be as follows:
        if the human wins, return 'win'
        if the computer wins, return 'lose'
        if there is a tie, return 'tie'

    Complete the activity guide before writing your solution.
    """
    return 'win'


def rps_web_process(moves, server):
    server.send_html_header()
    human_move = moves['yourMove']
    computer_move = moves['myMove']
    outcome = play_rps(human_move, computer_move)
    result(outcome)


def result(win_or_lose):
    print(HTML.DOCSTRING)
    print(HTML.HTML_START)
    print(HTML.HTML_HEAD.format(win_or_lose))
    print(HTML.BODY_START)
    print(HTML.HEADING1.format("You "+win_or_lose+"!"))
    print(HTML.IMAGE.format(get_image(win_or_lose), win_or_lose))
    print(HTML.BODY_END)


def get_image(term):
    api_url = "https://api.giphy.com/v1/gifs/search?api_key=shPVazqpdLB5saDFA5jIWNS26UZcdpXr&limit=25&offset=0&rating=g&lang=en&q="+term
    response = requests.get(api_url)
    return response.json()['data'][random.randint(0, 24)]['images']['original']['url']


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-c", "--console", help="Run console version", action='store_true')

    arguments = arg_parser.parse_args()

    if arguments.console:
        # Console version of Rock Paper Scissors is a future assignment
        pass
    else:
        webserver.add_feature('rps', rps_web_process)
        webserver.start()
