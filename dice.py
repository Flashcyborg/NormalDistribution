import random
import plotly.express as px
import plotly.figure_factory as ff

sum_of_dice = []
count = []
for a in range(1,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceresult = dice1 + dice2 
    sum_of_dice.append(diceresult)
    count.append(a)

print (sum_of_dice)
print (count)
bar_graph = px.bar(x = sum_of_dice, y = count)
bar_graph.show()




