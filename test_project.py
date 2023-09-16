import pytest
from project import get_auth_youtube, get_playlists, get_specific_playlist, rate_videos


def test_get_playlists():
    youtube = get_auth_youtube()
    assert type(get_playlists(youtube)) == list
    with pytest.raises(NameError):
        get_playlists(youtub)
    with pytest.raises(AttributeError):
        youtube = "a"
        get_playlists(youtube)

def test_get_specific_playlist():
    playlists = [{'snippet': {'title': 'Test1'}},
                  {'snippet': {'title': 'Test2'}}]

    assert get_specific_playlist(playlists, "Test1") == playlists[0]
    assert get_specific_playlist(playlists, "Test2") == playlists[1]
    with pytest.raises(NameError):
        get_specific_playlist(playlists, "Test123")

    assert type(get_specific_playlist(playlists, "Test1")) == dict


def test_rate_videos():
    stats = [{'id': '1', 'statistics': {'viewCount': '41364', 'likeCount': '1590', 'commentCount': '62'}},
              {'id': '2', 'statistics': {'viewCount': '834762', 'likeCount': '12350', 'commentCount': '1234'}},
              {'id': '3', 'statistics': {'viewCount': '298712', 'likeCount': '15635', 'commentCount': '938'}}]

    assert rate_videos(stats)[0]["rating"] != 0
    assert rate_videos(stats)[0]["rating"] == 3.994
    assert len(rate_videos(stats)) == 3
    assert type(rate_videos(stats)) == list

