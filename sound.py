class Track:
    def __init__(self, name, duration=0):
        self.name = name
        self.duration = duration

    def show(self):
        return f'<{self.name}-{self.duration}>'


class Album:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.tracks = []

    def get_tracks(self):
        print(f'{self.group}: ')
        for track in self.tracks:
            print(track.show())

    def get_duration(self):
        result = 0
        for track in self.tracks:
            result += track.duration
        return result

    def add_track(self, name, duration):
        self.tracks.append(Track(name, duration))


album1 = Album('Scorpion', 'Drake')

album1.add_track('Surival', 5)
album1.add_track('Nonstop', 3)
album1.add_track('Elevate', 4)

album1.get_tracks()

album2 = Album('Views', 'Drake')

album2.add_track('9', 5)
album2.add_track('Hype', 3)
album2.add_track('With you', 2)

album2.get_tracks()

print(
    f'Длительность альбома \'{album1.name}\' группы \'{album1.group}\' '
    f'составляет {album1.get_duration()} минут.')

print(
    f'Длительность альбома \'{album2.name}\' группы \'{album2.group}\' '
    f'составляет {album2.get_duration()} минут.')
