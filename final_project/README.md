# Youtube Videos Prioritizer
#### Video Demo: https://youtu.be/ZFFH-xSrOno
#### Description:
Since I am a college student, most part of my day is spent studing. Because of that, I lack of free time to watch youtube videos and I have a lot of them waiting to be watched in my playlist. The thing is that some of them are better than the others and I don't have enough time to watch them all.

Now my problem is solved. This program sort my playlist'videos based on a personal rating method and makes my life easier. By using this program, when I have free time and watch some youtube videos, I can use the sorted playlist to select the top ranked videos as they are more likely to be better in my personal opinion.

#### 1. __requirements.txt file__

- Contains the list of pip-installable libraries that the project requires, one per line.

#### 2. __project.py file__

Contains the main project's code.

```python
def get_auth_youtube():
```
 - Get credentials and create an API client.
 - Returns
    - youtube API client
 - Returns type
    - resource

```python
def get_playlists(youtube):
```
- Get user's playlists
- Parameteres
    - youtube: youtube API client
- Returns
    - playlists owned by the authenticated user
- Returns type
    - list


```python
def get_specific_playlist(playlists, playlist_name):
```
- Get a specific playlist from playlists
- Parameteres
    - playlists: playlists owned by the authenticated user
    - playlist_name: playlist name of interest
- Parameteres Type
    - playlists: list
    - playlist_name: str
- Returns
    - playlist of interest and it's data
- Returns type
    - dict

```python
def get_videosID(youtube, playlist):
```
- Get videos ID
- Parameteres
    - youtube: youtube API client
    - playlist: playlist of interest and its data
- Parameteres Type
    - youtube: resource
    - playlist: dict
- Returns
    - 2 IDs related to each video at the playlist of interest
- Returns type
    - dict

```python
def get_stats(youtube, videosId):
```
- Get videos statistics
- Parameteres
    - youtube: youtube API client
    - videosId: IDs related to videos
- Parameteres Type
    - youtube: resource
    - videosId: dict
- Returns
    - list of videos and it's statistical details where each list item is a video-dictionary
- Returns type
    - list

```python
def rate_videos(stats):
```
- Rate videos using a personal method
- Parameteres
    - stats: list of videos and it's statistical details
- Parameteres Type
    - stats: list
- Returns
    - a playlist with an additional section 'rating' which contains the videos grade
- Returns type
    - list

```python
def sort_playlist(youtube, playlist, new_position):
```
- Sort the playlist based on the personal classification method
- Parameteres
    - youtube: youtube API client
    - playlist: original playlist to be sorted
    - new_position: list containing the correct video position
- Parameteres Type
    - youtube: resource
    - playlist: dict
    - new_position: list

### 3. test_project.py file
File that contains all test functions for project.py

```python
def test_get_playlists():
```
- Test 'get_playlists' function

```python
def test_get_specific_playlist():
```
- Test 'get_specific_playlist' function

```python
def test_rate_videos():
```
- Test 'rate_videos' function