import "strings"

func wordPattern(pattern string, s string) bool {
    words := strings.Split(s, " ")
    if len(pattern) != len(words) {
        return false
    }

    charToWord, wordToChar := make(map[string]string), make(map[string]string)
    for i := 0; i < len(pattern); i++ {
        char, word := string(pattern[i]), words[i]
        if mapWord, ok := charToWord[char]; ok && word != mapWord {
            return false
        }
        if mapChar, ok := wordToChar[word]; ok && char != mapChar {
            return false
        }
        charToWord[char] = word
        wordToChar[word] = char
    }
    return true
}
