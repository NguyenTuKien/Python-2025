from sys import stdin

class GV:
    def __init__(self, id, name, code, score1, score2):
        self.id = f"GV{id:02d}"
        self.name = name
        self.code = code
        self.score1 = score1
        self.score2 = score2
    
    def getSubject(self):
        if self.code[0] == 'A':
            return 'TOAN'
        elif self.code[0] == 'B':
            return 'LY'
        else :
            return 'HOA'
    
    def getTotalScore(self):
        totalScore = self.score1 * 2 + self.score2
        if self.code[1] == '1':
            return totalScore + 2.0
        elif self.code[1] == '2':
            return totalScore + 1.5
        elif self.code[1] == '3':
            return totalScore + 1.0
        else :
            return totalScore
        
    def getStatus(self):
        if self.getTotalScore() >= 18 : 
            return 'TRUNG TUYEN'
        else :
            return 'LOAI'
        
    def __lt__ (self, other):
        return self.getTotalScore() > other.getTotalScore()

    def __str__ (self):
        return self.id + ' ' + self.name + ' ' + self.getSubject() + ' ' + f"{self.getTotalScore():.1f}" + ' ' + self.getStatus() 
    
def main():
    listGV = []
    for i in range(int(stdin.readline())):
        name = stdin.readline().strip()
        code = stdin.readline().strip()
        score1 = float(stdin.readline())
        score2 = float(stdin.readline())
        listGV.append(GV(i + 1, name, code, score1, score2))
    listGV.sort()
    for gv in listGV:
        print(gv)

if __name__ == "__main__":
    main()
