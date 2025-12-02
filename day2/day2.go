package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func isInvalidPart1(productId string) bool {
	if len(productId)%2 != 0 {
		return false
	}

	first, second := productId[0:len(productId)/2], productId[len(productId)/2:]
	if first == second {
		return true
	}

	return false
}

func isInvalidPart2(productId string) bool {
	for i := 0; i < len(productId); i++ {
		subString := productId[0 : i+1]
		if len(subString) > len(productId)/2 {
			continue
		}
		newStr := strings.Repeat(subString, len(productId)/len(subString))
		if newStr == productId {
			return true
		}
	}
	return false
}

func findInvalidProductIds(productIdRange string) ([]int, []int) {
	productIds := []int{}
	invalidProductIdsPart1 := []int{}
	invalidProductIdsPart2 := []int{}
	for _, productId := range strings.Split(productIdRange, "-") {
		productIdInt, err := strconv.Atoi(productId)
		if err != nil {
			fmt.Println("Error converting productId to int:", err)
			return []int{}, []int{}
		}
		productIds = append(productIds, productIdInt)

	}
	numRange := makeRange(productIds[0], productIds[1])
	for _, num := range numRange {
		if isInvalidPart1(strconv.Itoa(num)) {
			invalidProductIdsPart1 = append(invalidProductIdsPart1, num)
		}
		if isInvalidPart2(strconv.Itoa(num)) {
			invalidProductIdsPart2 = append(invalidProductIdsPart2, num)
		}
	}
	return invalidProductIdsPart1, invalidProductIdsPart2
}

func makeRange(start, end int) []int {
	r := []int{}
	for i := start; i <= end; i++ {
		r = append(r, i)
	}
	return r
}

func sum(productIds []int) int {
	sum := 0
	for _, productId := range productIds {
		sum += productId
	}
	return sum
}

func main() {
	content, err := os.ReadFile("input.txt")
	sumOfInvalidProductIdsPart1 := 0
	sumOfInvalidProductIdsPart2 := 0

	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	productIdsRanges := []string{}
	for _, line := range strings.Split(string(content), ",") {
		productIdsRanges = append(productIdsRanges, line)
	}

	for _, productIdRange := range productIdsRanges {
		// fmt.Println("productIdRange: ", productIdRange)
		invalidProductIdsPart1, invalidProductIdsPart2 := findInvalidProductIds(productIdRange)
		// fmt.Println(invalidProductIds)

		sumOfInvalidProductIdsPart1 += sum(invalidProductIdsPart1)
		sumOfInvalidProductIdsPart2 += sum(invalidProductIdsPart2)
	}
	fmt.Println("sumOfInvalidProductIdsPart1: ", sumOfInvalidProductIdsPart1)
	fmt.Println("sumOfInvalidProductIdsPart2: ", sumOfInvalidProductIdsPart2)

}
