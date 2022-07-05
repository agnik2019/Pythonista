class Match:
  def __init__(self, team):
    self.team=team
    lst1= self.team.split("-")
    self.batting_Team=lst1[0]
    self.bowling_Team=lst1[1]
    self.run=0
    self.over=0
    self.wicket=0
    print("5..4..3..2..1.. Play !!!")
  
  def add_run(self,run):
    self.run+=run
  def add_over(self,over):
    if self.over+over>5:
          print("Warning! Cannot add 5 over/s (5 over match)")
    else:
      self.over+=over
      
  def add_wicket(self, wicket):
    self.wicket+=wicket
  def print_scoreboard(self):  
      print("Batting Team: ", self.batting_Team)
      print("Bowling Team: ", self.bowling_Team)
      print("Total Runs", self.run , "Wickets",self.wicket, "Over",self.over)

match1 = Match("Rangpur Riders-Cumilla Victorians")
print("=========================")
match1.add_run(4)
match1.add_run(6)
match1.add_over(1)
match1.print_scoreboard()
print("=========================")
match1.add_over(5)
print("=========================")
match1.add_wicket(1)
match1.print_scoreboard()