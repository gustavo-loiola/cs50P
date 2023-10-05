import os.path
import sys

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

CLIENT_SECRETS_FILE = "client_secret.json"
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def main():
    """
    Main function call other functions and structures the project main function (sort videos)
    """
    youtube = get_auth_youtube()
    my_playlists = get_playlists(youtube)
    watch_later = get_specific_playlist(my_playlists, playlist_name="Watch Later.py")
    videosId = get_videosID(youtube, watch_later)
    videos_stats = get_stats(youtube, videosId)
    rate_videos(videos_stats).sort(key=lambda x: x["rating"], reverse=True)
    sort_playlist(youtube, watch_later, videos_stats)


def get_auth_youtube():
    """
    Get credentials and create an API client.

    :return: youtube API client
    :rtype: resource
    """
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json")
    if (not creds) or (creds.expired):
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRETS_FILE, SCOPES
            )
            creds = flow.run_console()
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    try:
        return build("youtube", "v3", credentials=creds)
    except HttpError as error:
        print("An error occured:", error)


def get_playlists(youtube):
    """
    Get user's playlists

    :param youtube: youtube API client
    :return: playlists owned by the authenticated user
    :rtype: list
    """

    playlists = []
    res = (
        youtube.playlists().list(part="snippet,id", mine=True, maxResults=10).execute()
    )

    playlists.extend(res["items"])
    return playlists


def get_specific_playlist(playlists, playlist_name):
    """
    Get a specific playlist from playlists

    :param playlists: playlists owned by the authenticated user
    :type playlists: list
    :param playlist_name: playlist name of interest
    :type playlist_name: str
    :return: playlist of interest and it's data
    :rtype: dict
    """
    found = True
    while found:
        for i in range(len(playlists)):
            if playlists[i]["snippet"]["title"] == playlist_name:
                return playlists[i]
        found = False
    if not(found):
        raise NameError


def get_videosID(youtube, playlist):
    """
    Get videos ID

    :param youtube: youtube API client
    :type youtube: resource
    :param playlist: playlist of interest and its data
    :type playlist: dict
    :return: 2 IDs related to each video at the playlist of interest
    :rtype: dict
    """
    nextPage_token = None
    playlist_videos = []
    playlistId = playlist["id"]
    while True:
        res = (
            youtube.playlistItems()
            .list(
                part="snippet",
                playlistId=playlistId,
                maxResults=50,
                pageToken=nextPage_token,
            )
            .execute()
        )
        playlist_videos += res["items"]
        nextPage_token = res.get("NextPageToken")
        if nextPage_token is None:
            break

    dic_id = {}
    for video in playlist_videos:
        dic_id[video["snippet"]["resourceId"]["videoId"]] = video["id"]

    return dic_id


def get_stats(youtube, videosId):
    """
    Get videos statistics

    :param youtube: youtube API client
    :type youtube: resource
    :param videosId: IDs related to videos
    :type videosId: dict
    :return: list of videos and it's statistical details where each list item is a video-dictionary
    :rtype: list

    """
    stats = []
    for video_id in list(videosId):
        res = youtube.videos().list(part="statistics", id=video_id).execute()
        res["items"][0]["id2"] = videosId[video_id]
        stats += res["items"]
    return stats


def rate_videos(stats):
    """
    Rate videos using a personal method

    :param stats: list of videos and it's statistical details
    :type stats: list
    :return: a playlist with an additional section 'rating' which contains the videos grade
    :rtype: list
    """
    likes = list(map(lambda x: int(x["statistics"]["likeCount"]), stats))
    views = list(map(lambda x: int(x["statistics"]["viewCount"]), stats))
    comments = list(map(lambda x: int(x["statistics"]["commentCount"]), stats))
    for i in range(len(stats)):
        rate = round(100 * (likes[i] + comments[i]) / views[i], 3)
        stats[i]["rating"] = rate
    return stats


def sort_playlist(youtube, playlist, new_position):
    """
    Sort the playlist based on the personal classification method

    :param youtube: youtube API client
    :type youtube: resource
    :param playlist: original playlist to be sorted
    :type playlist: dict
    :param new_position: list containing the correct video position
    :type new_position: list
    """
    for i in range(len(new_position)):
        id = new_position[i]["id2"]
        videoId = new_position[i]["id"]
        res = (
            youtube.playlistItems()
            .update(
                part="snippet",
                body={
                    "id": id,
                    "snippet": {
                        "playlistId": playlist["id"],
                        "position": i,
                        "resourceId": {"kind": "youtube#video", "videoId": videoId},
                    },
                },
            )
        ).execute()


if __name__ == "__main__":
    """
    Disable OAuthlib's HTTPS verification when running locally and call main.
    """
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    main()
