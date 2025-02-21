# r for read, w for write, a for append,
# W and read: w+  
# A and read: a+

with open('./example.txt', 'a+') as file:
    file.write("steve")
    file.seek(0)  # Move pointer to the start to read the full file
    content = file.read()
    print(f"Content: {content}")

try:
    with open('./example2.txt', 'r') as file:
        content = file.read()
        print(f"Content: {content}")
except Exception as e:
    print("Exception: ", e)