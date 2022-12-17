// O(n) time | O(n) space - where n is tokens.length
func evalRPN(tokens []string) int {
    stack := []int{}
    
    ops := map[string]func(int, int) int{
        "+": func(a, b int) int { return a + b },
        "-": func(a, b int) int { return a - b },
        "*": func(a, b int) int { return a * b },
        "/": func(a, b int) int { return int(a / b) },
    }

    for _, token := range tokens {
        if op, ok := ops[token]; ok {
            a, b := stack[len(stack) - 2], stack[len(stack) - 1]
            stack = stack[:len(stack) - 2]
            stack = append(stack, op(a, b))
        } else {
            num, _ := strconv.Atoi(token)
            stack = append(stack, num)
        }
    }

    return stack[0]
}
