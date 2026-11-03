
words = ["They", "can", "fish"]

# Initial tags
tags = ["PRP", "NN", "NN"]

print("Before Transformation:")
print(list(zip(words, tags)))

# Transformation rule:
# Change NN to VB if the previous tag is MD

for i in range(1, len(words)):
    if tags[i-1] == "MD" and tags[i] == "NN":
        tags[i] = "VB"

# Assign can as MD
for i in range(len(words)):
    if words[i] == "can":
        tags[i] = "MD"

# Apply transformation again
for i in range(1, len(words)):
    if tags[i-1] == "MD" and tags[i] == "NN":
        tags[i] = "VB"

print("After Transformation:")
print(list(zip(words, tags)))
