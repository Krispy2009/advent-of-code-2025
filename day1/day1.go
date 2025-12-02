package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func parseLine(line string) (string, int) {
	direction := string(line[0])
	clicks, err := strconv.Atoi(strings.TrimSpace(string(line[1:])))
	if err != nil {
		fmt.Println("Error parsing clicks:", err)
		return "", 0
	}
	return direction, clicks
}

func main() {

	start := 50
	max := 99
	min := 0
	part1 := 0
	part2 := 0

	lines, err := os.ReadFile("input.txt")

	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}
	for _, line := range strings.Split(string(lines), "\n") {
		direction, clicks := parseLine(line)

		if direction == "L" {
			for i := 0; i < clicks; i++ {
				start -= 1
				if start == 0 {
					part2 += 1
				}
				if start < min {
					start = max
				}
			}
		} else if direction == "R" {
			for i := 0; i < clicks; i++ {
				start += 1
				if start > max {
					start = min
					part2 += 1
				}
			}
		}
		if start == 0 {
			part1 += 1
		}
	}
	fmt.Println("Part 1: " + strconv.Itoa(part1))
	fmt.Println("Part 2: " + strconv.Itoa(part2))
}
