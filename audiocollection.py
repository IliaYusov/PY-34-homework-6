class Album:
    def __init__(self, name, group='Various artists'):
        self.name = name
        self.group = group
        self.track_list = []

    def add_track(self, track):
        self.track_list.append(track)

    def get_tracks(self):
        print(f'<{self.name.upper()}> tracks:')
        for track in self.track_list:
            track.show()

    def get_duration(self):
        album_duration = 0
        for track in self.track_list:
            album_duration += track.duration
        print(f'<{self.name.upper()}> duration: {album_duration} min.')


class Track:
    def __init__(self, name, duration=0):
        self.name = name
        self.duration = duration

    def show(self):
        print(f'<{self.name:_<45}{self.duration}_min.>')


let_there_be_more_light = Track('Let There Be More Light', 5)
remember_a_day = Track('Remember a Day', 4)
set_the_controls_for_the_heart_of_the_sun = Track('Set the Controls for the Heart of the Sun', 5)
corporal_clegg = Track('Corporal Clegg', 4)
a_saucerful_of_secrets = Album('A Saucerful of Secrets', 'Pink Floyd')
a_saucerful_of_secrets.add_track(let_there_be_more_light)
a_saucerful_of_secrets.add_track(remember_a_day)
a_saucerful_of_secrets.add_track(set_the_controls_for_the_heart_of_the_sun)
a_saucerful_of_secrets.add_track(corporal_clegg)

whole_lotta_love = Track('Whole Lotta Love', 5)
what_is_and_what_should_never_be = Track('What Is and What Should Never Be', 4)
the_lemon_song = Track('The Lemon Song', 6)
thank_you = Track('Thank You', 4)
led_zeppelin_ii = Album('Led Zeppelin II', 'Led Zeppelin')
led_zeppelin_ii.add_track(whole_lotta_love)
led_zeppelin_ii.add_track(what_is_and_what_should_never_be)
led_zeppelin_ii.add_track(the_lemon_song)
led_zeppelin_ii.add_track(thank_you)

a_saucerful_of_secrets.get_tracks()
a_saucerful_of_secrets.get_duration()
print()
led_zeppelin_ii.get_tracks()
led_zeppelin_ii.get_duration()

