# first store some comment in the comment file

results = False
bad_words = ['fuck','shit','cock','titties','boner','muff','pussy','asshole', 'cunt', 'ass', 'cockfoam', 'nigger','bloody','bitch']
with open('bad_words_comment.txt') as f:
    comment = f.read()
for i in range(len(bad_words)):
    if bad_words[i] in comment:
        results = True
        break

if results:
    print("The comment was toxic we removed it...")
    with open('bad_words_comment.txt','w') as f:
        f.write("")
else:
    print("It was all okay...")







