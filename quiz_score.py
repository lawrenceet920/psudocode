# Ethan Lawrence
# September 25 2024
# Quiz score

# Input
fname = input('Please input your first name:    ')
score1 = float(input('Please enter the First quiz score:    '))
score2 = float(input('Please enter the Second quiz score:    '))
score3 = float(input('Please enter the Third quiz score:    '))

# Process
average_score = (score1 + score2 + score3) / 3

# Output
print(f'{score1}, {score2}, {score3}.')
print (f'(Hello {fname} Your average score is {average_score}')