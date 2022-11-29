def decrypt(code, k):
    solution = []
    original_k = k
    if k == 0:
        return [0 for c in code]

    for i in range(len(code)):
        k = original_k
        solution.append(0)
        if k > 0:
            while k > 0:
                index = k + i if k + i < len(code) else k + i - len(code)
                solution[i] += code[index]
                # print(f"index={index}, k={k}, i={i}")
                k -= 1
        else:
            while k < 0:
                index = k + i if k + i >= 0 else k + i + len(code)
                solution[i] += code[index]
                k += 1

    return solution


code = [5, 7, 1, 4]
k = -2
print(decrypt(code, k))
