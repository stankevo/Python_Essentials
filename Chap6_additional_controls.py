
secret = 'swordfish'
pw = ''
count = 0
auth = False

max_attempts = 5

while pw != secret:
    count += 1
    if count > max_attempts: break
    pw = input(f'{count}: What is the secret word? ')
else:
    auth = True

print('Authorized.' if auth else 'Calling FBI...')

