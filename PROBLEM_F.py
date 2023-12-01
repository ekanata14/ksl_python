statement = str(input("Masukkan Kata/Kalimat: "))
word_statement = statement.split()
statement_result = str()

for word in word_statement:
    for i in range(1, len(word_statement), 2):
        word = word[:i] + "$" + word[i + 1:]
    print(word, end=' ')

print(statement_result)
# statement_result = "".join(word_statement)

# for i in range(len(statement_result)):
#     print("-", end="")
# print("\r")
# print(statement_result)
# for i in range(len(statement_result)):
#     print("-", end="")

