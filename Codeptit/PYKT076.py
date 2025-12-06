from sys import stdin
from datetime import datetime as dt

class Movie:
    def __init__ (self, id, gerne, day, title, chaps):
        self.id = f"P{id:03d}"
        self.gerne = gerne
        self.day = dt.strptime(day, "%d/%m/%Y")
        self.title = title
        self.chaps = chaps

    def __lt__ (self, other):
        return self.day < other.day
    
    def __str__ (self):
        return f"{self.id} {self.gerne} {self.day.strftime('%d/%m/%Y')} {self.title} {self.chaps}"

def main():
    n, m = map(int, stdin.readline().split())

    gernes = {}
    for i in range(n):
        id = f"TL{i + 1:03d}"
        gernes[id] = stdin.readline().strip()
    
    movies = []
    for i in range(m):
        gerne_id = stdin.readline().strip()
        day = stdin.readline().strip()
        title = stdin.readline().strip()
        chaps = stdin.readline().strip()
        movies.append(Movie(i + 1, gernes[gerne_id], day, title, chaps))
    movies.sort()
    for movie in movies:
        print(movie)

if __name__ == "__main__":
    main()