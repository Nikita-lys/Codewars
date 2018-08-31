# https://www.codewars.com/kata/dubstep/

def song_decoder(song):
    # return " ".join(song.replace('WUB', ' ').split())
    """
    For example, a song with words "I AM X" can transform into a dubstep remix as "WUBWUBIWUBAMWUBWUBX"
    and cannot transform into "WUBWUBIAMWUBX".

    :param song: song with WUB
    :return: song without WUB
    """
    res = ''
    l = song.split("WUB")
    for x in l:
        if x != '':
            res += x + ' '
    return(res.strip())


assert song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB") == "WE ARE THE CHAMPIONS MY FRIEND"
assert song_decoder("AWUBBWUBC") == "A B C"
assert song_decoder("AWUBWUBWUBBWUBWUBWUBC") == "A B C"
assert song_decoder("WUBAWUBBWUBCWUB") == "A B C"



