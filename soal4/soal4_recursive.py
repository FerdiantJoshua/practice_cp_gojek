import sys


def flood_region(kingdom_map, i, j):
    owner_set = set()
    if kingdom_map[i][j]['value'] == '#':
        return owner_set
    elif kingdom_map[i][j]['value'] == '.':
        kingdom_map[i][j]['visited'] = True
        if i-1 > 0 and not kingdom_map[i-1][j]['visited']:
            owner_set = owner_set.union(flood_region(kingdom_map, i-1, j))
        if i+1 < len(kingdom_map) and not kingdom_map[i+1][j]['visited']:
            owner_set = owner_set.union(flood_region(kingdom_map, i+1, j))
        if j-1 > 0 and not kingdom_map[i][j-1]['visited']:
            owner_set = owner_set.union(flood_region(kingdom_map, i, j-1))
        if j+1 < len(kingdom_map[0]) and not kingdom_map[i][j+1]['visited']:
            owner_set = owner_set.union(flood_region(kingdom_map, i, j+1))
        # print(f'.: {owner_set}')
        return owner_set
    else:
        kingdom_map[i][j]['visited'] = True
        owner_set.add(kingdom_map[i][j]['value'])
        if i-1 > 0 and not kingdom_map[i-1][j]['visited']:
            owner_set = owner_set.union(flood_region(kingdom_map, i-1, j))
        if i+1 < len(kingdom_map) and not kingdom_map[i+1][j]['visited']:
            owner_set = owner_set.union(flood_region(kingdom_map, i+1, j))
        if j-1 > 0 and not kingdom_map[i][j-1]['visited']:
            owner_set = owner_set.union(flood_region(kingdom_map, i, j-1))
        if j+1 < len(kingdom_map[0]) and not kingdom_map[i][j+1]['visited']:
            owner_set = owner_set.union(flood_region(kingdom_map, i, j+1))
        # print(f'owner: {owner_set}')
        return owner_set


def find_owner(kingdom_map, i, j):
    owners = list(flood_region(kingdom_map, i, j))
    if len(owners) > 1:
        return 'contested'
    elif len(owners) == 0:
        return None
    else:
        return owners[0]


def count_regions(kingdom_map):
    region_owner_summary = {}
    for i in range(len(kingdom_map)):
        for j in range(len(kingdom_map[0])):
            if kingdom_map[i][j]['value'] != '#':
                if not kingdom_map[i][j]['visited']:
                    owner = find_owner(kingdom_map, i, j)
                    if owner is not None:
                        owner_total_region = region_owner_summary.get(owner) or 0
                        region_owner_summary.update({owner:owner_total_region + 1})
    contested_total = region_owner_summary.get('contested') or 0
    region_owner_summary.update({'contested':contested_total})
    return region_owner_summary


def enrich_kingdom_map(kingdom_map, n, m):
    new_kingdom_map = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(len(kingdom_map)):
        for j in range(len(kingdom_map[0])):
            new_kingdom_map[i][j] = {'value': kingdom_map[i][j], 'visited': False}
    return new_kingdom_map


if __name__ == '__main__':
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    with open(input_filename, 'r') as f_in:
        t = int(f_in.readline())
        answers = [{} for _ in range(t)]
        for i in range(t):
            print(i)
            n = int(f_in.readline())
            m = int(f_in.readline())
            kingdom_map = []
            for j in range(n):
                kingdom_map.append(f_in.readline().strip())
            kingdom_map = enrich_kingdom_map(kingdom_map, n, m)
            answers[i] = count_regions(kingdom_map)

    with open(output_filename, 'w') as f_out:
        for i in range(len(answers)):
            f_out.write(f'Case {i+1}:\n')
            for key, value in sorted(answers[i].items()):
                if key == 'contested':
                    contested = value
                else:
                    f_out.write(f'{key} {value}\n')
            f_out.write(f'contested {contested}\n')