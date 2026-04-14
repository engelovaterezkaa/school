seznam = ["Emil", "Vojtíšek", "Jackob", "Lui", "Josefína"]

seznam.append("Nigeria")

seznam.pop(0)

for i, jmeno in enumerate(seznam, start=1):
    print(f"{i}. {jmeno}")

print(seznam[2])
print(seznam[-1])

print(len(seznam))
print(seznam)