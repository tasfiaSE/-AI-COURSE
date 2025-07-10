# Alpha-Beta Pruning Function
def alphabeta(current, game_tree, level, alpha, beta, is_maximizing):
    if not game_tree[current]['children']:
        print(f"{'  '*level}Leaf Node '{current}' with value = {game_tree[current]['value']}")
        return game_tree[current]['value']

    if is_maximizing:
        max_score = float('-inf')
        print(f"{'  '*level}Maximizing at Node '{current}'")
        for next_node in game_tree[current]['children']:
            score = alphabeta(next_node, game_tree, level + 1, alpha, beta, False)
            max_score = max(max_score, score)
            alpha = max(alpha, score)
            print(f"{'  '*level}Max Node '{current}': score = {score}, alpha = {alpha}, beta = {beta}")
            if beta <= alpha:
                print(f"{'  '*level}Pruned at Node '{current}' (beta <= alpha)")
                break
        return max_score
    else:
        min_score = float('inf')
        print(f"{'  '*level}Minimizing at Node '{current}'")
        for next_node in game_tree[current]['children']:
            score = alphabeta(next_node, game_tree, level + 1, alpha, beta, True)
            min_score = min(min_score, score)
            beta = min(beta, score)
            print(f"{'  '*level}Min Node '{current}': score = {score}, alpha = {alpha}, beta = {beta}")
            if beta <= alpha:
                print(f"{'  '*level}Pruned at Node '{current}' (beta <= alpha)")
                break
        return min_score

# Wrapper Function
def get_optimal_value(source, game_tree):
    print("Starting Alpha-Beta Pruning...\n")
    optimal_score = alphabeta(source, game_tree, 0, float('-inf'), float('inf'), True)
    print("\nAlpha-Beta Pruning Finished.")
    return optimal_score

# Game Tree
game_tree = {
    'A': {'children': ['B', 'C'], 'value': None},
    'B': {'children': ['D', 'E'], 'value': None},
    'C': {'children': ['F', 'G'], 'value': None},
    'D': {'children': [], 'value': 3},
    'E': {'children': [], 'value': 5},
    'F': {'children': [], 'value': 2},
    'G': {'children': [], 'value': 9},
}

# Run the code
if __name__ == "__main__":
    optimal_value = get_optimal_value('A', game_tree)
    print(f"\n🔍 The optimal value from node 'A' is: {optimal_value}")


 