def dfs(cur, cur_value, cur_weight, bag_weight, cave, visited):
    if cur not in cave:
        return cur_value
    if cur in visited:
        return cur_value

    value, weight, next1, next2 = cave[cur]
    new_weight = cur_weight + weight
    if new_weight > bag_weight:
        return cur_value

    new_value = cur_value + value
    best = new_value

    visited.add(cur)

    if next1 != 0:
        best = max(best, dfs(next1, new_value, new_weight, bag_weight, cave, visited))
    if next2 != 0:
        best = max(best, dfs(next2, new_value, new_weight, bag_weight, cave, visited))

    visited.remove(cur)
    return best


def main():
    bag_weight = int(input())
    number_of_caves = int(input())
    cave = {}

    for _ in range(number_of_caves):
        cave_id, value, weight, next1, next2 = map(int, input().split())
        cave[cave_id] = (value, weight, next1, next2)

    ans = -1
    best_start = None

    for start in cave:  # 每個洞都當起點試一次
        visited = set()
        gold = dfs(start, 0, 0, bag_weight, cave, visited)

        if gold > ans:
            ans = gold
            best_start = start
        

    print(best_start, ans)


main()


main()

