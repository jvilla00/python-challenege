import os
import csv
total_votescast= 0
Candidates= []
Candidates_votes= {}
Stockham_votes= 0
DeGette_votes= 0
Doane_votes= 0
csvelection = os.path.join('..', 'Resources', 'election_data.csv')
with open(csvelection, 'r') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')  
  header= next(csvreader)
  for row in csvreader:
   total_votescast +=1 
   Candidates.append(row[2])

reducecandidates=list(set(Candidates))
#print(reducecandidates)

candidateonetotal= Candidates.count(reducecandidates[0])

#print(candidateonetotal)
candidatetwototal= Candidates.count(reducecandidates[1])
#print(candidatetwototal)
candidatethreetotal= Candidates.count(reducecandidates[2])
#print(candidatethreetotal)

canonepercent="{:.03%}".format((candidateonetotal/total_votescast)*100)
cantwopercent="{:.03%}".format((candidatetwototal/total_votescast)*100)
canthreepercent="{:.03%}".format((candidatethreetotal/total_votescast)*100)

#print(canonepercent)
#print(cantwopercent)
#print(canthreepercent)

canvoteslist=[candidateonetotal,candidatetwototal,candidatethreetotal]
#print(canvoteslist)

winnervote=0
for i in range(len(canvoteslist)):
    if canvoteslist[i] > winnervote:
        winnervote=canvoteslist[i]
#print(winnervote)

winner=reducecandidates[canvoteslist.index(max(canvoteslist))]
#print(winner)
print("Election Result")
print(".........................")
print("totl votes", total_votescast)
print(".........................")
print(reducecandidates[0],canonepercent, canvoteslist[0])
print(reducecandidates[1],cantwopercent, canvoteslist[1])
print(reducecandidates[2],canthreepercent,canvoteslist[2])
print(winner)

output_file="pypollelection.txt"
with open(output_file, "w") as file:
    file.write("Election Results\n")
    file.write(".........................\n")
    file.write("totl votes" + (str(total_votescast))+ "\n")
    file.write(".........................\n")
    file.write(f"reducecandidates[0],canonepercent, canvoteslist[0] \n")
    file.write(f"reducecandidates[1]+cantwopercent+canvoteslist[1] \n")
    file.write(f"reducecandidates[2]+canthreepercent+canvoteslist[2] \n")
    file.write(winner+"\n")
