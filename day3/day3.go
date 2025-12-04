package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func findMaxNum(line string, banks int) int64 {

	// fmt.Println("trimmed: ", trimmed)
	remaining := len(line) - banks
	stack := make([]byte, 0, banks)

	for i := 0; i < len(line); i++ {
		ch := line[i]
		for remaining > 0 && len(stack) > 0 && stack[len(stack)-1] < ch {
			stack = stack[:len(stack)-1]
			remaining--
			// fmt.Println("remaining: ", remaining)
		}
		stack = append(stack, ch)
		// fmt.Println("stack: ", string(stack))
	}

	num, err := strconv.ParseInt(string(stack[:banks]), 10, 64)
	if err != nil {
		return 0
	}

	return num
}

func main() {

	lines, err := os.ReadFile("input.txt")
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}
	var total_part1 int64
	var total_part2 int64

	for _, line := range strings.Split(string(lines), "\n") {
		line := strings.TrimSpace(line)

		total_part1 += findMaxNum(line, 2)
		total_part2 += findMaxNum(line, 12)
	}

	fmt.Println("total_part1: ", total_part1)
	fmt.Println("total_part2: ", total_part2)
}
