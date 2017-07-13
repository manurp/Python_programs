(_, A) = (
    input(),
    set(map(int, input().split()))
)

for _ in range(int(input())):
    (command, newSet) = (
        input().split()[0],
        set(map(int, input().split()))
    )

    # Cool trick. Since our commands are method names, just
    # execute the method on A with our new set as its argument.
    getattr(A, command)(newSet)

print (sum(A))
