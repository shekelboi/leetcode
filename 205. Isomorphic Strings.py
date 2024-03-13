def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_dict = dict()
    t_dict = dict()
    s_counter = 0
    t_counter = 0
    s_pattern = []
    t_pattern = []
    for i in range(len(s)):
        if s[i] not in s_dict:
            s_dict[s[i]] = s_counter
            s_counter += 1
        s_pattern.append(s_dict[s[i]])

        if t[i] not in t_dict:
            t_dict[t[i]] = t_counter
            t_counter += 1
        t_pattern.append(t_dict[t[i]])

    return s_pattern == t_pattern


s = "foo"
t = "bar"

print(isIsomorphic(s, t))