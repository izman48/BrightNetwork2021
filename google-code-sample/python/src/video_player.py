"""A video player class."""

from .video_library import VideoLibrary
import operator
import random
# This is where all my code goes

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._currently_playing = None
        self._isPaused = False
        self._playlists = {}
        self._flagged = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        print("Here's a list of all available videos:")
        videos = self._video_library.get_all_videos()
        videos.sort(key=operator.attrgetter('_title'))
        for video in videos:
            # print(video.title)
            title = video.title
            id = video.video_id
            tags = " ".join(video.tags)
            name = "  " + title + " (" + id + ")" +  " [" + tags + "]"
            if id in self._flagged:
                name += " - FLAGGED (reason: " + self._flagged[id] + ")"
            print(name)
                
 
    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        next_video = self._video_library.get_video(video_id)
        
        if next_video == None:
            print("Cannot play video: Video does not exist")
        else:
            if video_id in self._flagged:
                print(f"Cannot play video: Video is currently flagged (reason: {self._flagged[video_id]})")
            else:
                if not self._currently_playing == None:
                    name = self._currently_playing.title
                    print(f"Stopping video: {name}")
                
                name = next_video.title
                print(f"Playing video: {name}")
                self._currently_playing = next_video
                self._isPaused = False

        # print("show_all_videos needs implementation")
       

    def stop_video(self):
        """Stops the current video."""
        if self._currently_playing == None:
            print("Cannot stop video: No video is currently playing")
        else:
            name = self._currently_playing.title
            print(f"Stopping video: {name}")
            self._currently_playing = None

        # print("stop_video needs implementation")

    def play_random_video(self):
        """Plays a random video from the video library."""
        videos = self._video_library.get_all_videos()
        i = 0
        while i < len(videos):
            video = videos[i]
            if video.video_id in self._flagged:
                videos.remove(video)
                i -= 1
            i += 1
        number_of_videos = len(videos)
        # print(number_of_videos)
        if number_of_videos == 0:
            print("No videos available")
        else:
            # random_number = random.randint(0,number_of_videos)
            # videos = self._video_library.get_all_videos()
            video = random.choice(videos)
            self.play_video(video.video_id)

        # print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""
        if self._currently_playing == None:
            print("Cannot pause video: No video is currently playing")
        else:
            # print(self._isPaused)
            name = self._currently_playing.title
            if self._isPaused:
                print(f"Video already paused: {name}")
            else:
                print(f"Pausing video: {name}")
                self._isPaused = True
        # print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""
        if self._currently_playing == None:
            print("Cannot continue video: No video is currently playing")
        else:
            # print(self._isPaused)
            name = self._currently_playing.title
            if self._isPaused:
                print(f"Continuing video: {name}")
                self._isPaused = False
            else:
                print("Cannot continue video: Video is not paused")
                
        # print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""
        if self._currently_playing == None:
            print("No video is currently playing")
        else:
            title = self._currently_playing.title
            id = self._currently_playing.video_id
            tags = " ".join(self._currently_playing.tags)
            
            name = "Currently playing: " + title + " (" + id + ")" +  " [" + tags + "]"
            if self._isPaused:
                name += " - PAUSED"


            print(name)

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        if not playlist_name.lower() in self._playlists:
            print(f"Successfully created new playlist: {playlist_name}")
            self._playlists[playlist_name.lower()] = [playlist_name]
        else:
            print("Cannot create playlist: A playlist with the same name already exists")

        # print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        # self.create_playlist(playlist_name)
        if video_id in self._flagged:
            print(f"Cannot add video to {playlist_name}: Video is currently flagged (reason: {self._flagged[video_id]})")
        else:
            if playlist_name.lower() in self._playlists: 
                selected_playlist = self._playlists[playlist_name.lower()]
                video = self._video_library.get_video(video_id)
                if video:
                    if video_id not in selected_playlist:
                        selected_playlist.append(video_id)
                        print(f"Added video to {playlist_name}: {video.title}")
                    else:
                        print(f"Cannot add video to {playlist_name}: Video already added")
                else:
                    print(f"Cannot add video to {playlist_name}: Video does not exist")
            # next_video = self._video_library.get_video(video_id)
            else:
                print(f"Cannot add video to {playlist_name}: Playlist does not exist")


        # print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""
        if len(self._playlists) == 0:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            names = []
            playlists = self._playlists.keys()
            
            for playlist in playlists:
                selected_playlist = self._playlists[playlist]
                names.append(selected_playlist[0])
            names.sort()
            for name in names:
                print("  " + name)
            
        # print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in self._playlists:
            # thing
            print(f"Showing playlist: {playlist_name}")
            playlist = self._playlists[playlist_name.lower()]
            playlist = playlist[1:]
            if len(playlist) == 0:
                print("  No videos here yet.")
            else:
                for name in playlist:
                    video = self._video_library.get_video(name)
                    title = video.title
                    id = video.video_id
                    tags = " ".join(video.tags)
                    name = "  " + title + " (" + id + ")" +  " [" + tags + "]"
                    if id in self._flagged:
                        name += " - FLAGGED (reason: " + self._flagged[id] + ")"
                    print(name)
        else:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")


        # print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """

        if playlist_name.lower() in self._playlists:
            selected_playlist = self._playlists[playlist_name.lower()]
            video = self._video_library.get_video(video_id)
            if video:
                if video_id in selected_playlist:
                    selected_playlist.remove(video_id)
                    print(f"Removed video from {playlist_name}: {video.title}")
                else:
                    print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
            else:
                print(f"Cannot remove video from {playlist_name}: Video does not exist")
            # next_video = self._video_library.get_video(video_id)


        else:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
        # print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in self._playlists:
            selected_playlist = self._playlists[playlist_name.lower()]
            selected_playlist = selected_playlist[0:1]
            self._playlists[playlist_name.lower()] = selected_playlist
            print(f"Successfully removed all videos from {playlist_name}")

        else:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
        # print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in self._playlists:
            self._playlists.pop(playlist_name.lower())
            print(f"Deleted playlist: {playlist_name}")

        else:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")
        # print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        videos = self._video_library.get_all_videos()
        videos.sort(key=operator.attrgetter('_title'))
        results = []
        valid_ids = []
        index = 1 
        for video in videos:
            # print(video.title)
            title = video.title
            id = video.video_id
            tags = " ".join(video.tags)
            if id not in self._flagged and search_term.lower() in title.lower():
                name = "  " + str(index) + ") " + title + " (" + id + ")" +  " [" + tags + "]"
                results.append(name)
                valid_ids.append(id)
                index += 1
        if len(results) == 0:
            print(f"No search results for {search_term}")
        else:
            print(f"Here are the results for {search_term}:")
            for result in results:
                print(result) 
            print("Would you like to play any of the above? If yes, specify the number of the video.") 
            print("If your answer is not a valid number, we will assume it's a no.")       
            number = input("")
            try:
                val = int(number)
                if val - 1 in range(0,len(results)):
                    # print(val)
                    self.play_video(valid_ids[val-1])

            except ValueError:
                return
            

        # print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        videos = self._video_library.get_all_videos()
        videos.sort(key=operator.attrgetter('_title'))
        results = []
        valid_ids = []
        index = 1 
        for video in videos:
            # print(video.title)
            title = video.title
            id = video.video_id
            tags = " ".join(video.tags)
            if id not in self._flagged and video_tag[0] == '#' and video_tag.lower() in tags.lower():
                name = "  " + str(index) + ") " + title + " (" + id + ")" +  " [" + tags + "]"
                results.append(name)
                valid_ids.append(id)
                index += 1
        if len(results) == 0:
            print(f"No search results for {video_tag}")
        else:
            print(f"Here are the results for {video_tag}:")
            for result in results:
                print(result) 
            print("Would you like to play any of the above? If yes, specify the number of the video.") 
            print("If your answer is not a valid number, we will assume it's a no.")       
            number = input("")
            try:
                val = int(number)
                if val - 1 in range(0,len(results)):
                    # print(val)
                    self.play_video(valid_ids[val-1])

            except ValueError:
                return
        # print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        next_video = self._video_library.get_video(video_id)
        
        if next_video == None:
            print("Cannot flag video: Video does not exist")
        else:
            if video_id in self._flagged:
                print("Cannot flag video: Video is already flagged")
            else:
                if not self._currently_playing == None and video_id == self._currently_playing.video_id:
                    self.stop_video()
                if flag_reason == "":
                    flag_reason = "Not supplied" 
                self._flagged[video_id] = flag_reason
                print(f"Successfully flagged video: {next_video.title} (reason: {flag_reason})")
        # print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        next_video = self._video_library.get_video(video_id)
        
        if next_video == None:
            print("Cannot remove flag from video: Video does not exist")
        else:
            if video_id in self._flagged:
                self._flagged.pop(video_id)
                title = next_video.title
                print(f"Successfully removed flag from video: {title}")
            else:
                print("Cannot remove flag from video: Video is not flagged")
        # print("allow_video needs implementation")
