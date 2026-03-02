num_applicants = int(input())

applicant_rankings = []
for i in range(num_applicants):
    applicant_rankings.append(input())

for i in range(len(applicant_rankings)):
    print("Name: " + applicant_rankings[i] + ", Position: " + str(i + 1))

