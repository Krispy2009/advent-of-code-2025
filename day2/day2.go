package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func isInvalid(productId string) bool {
	if len(productId)%2 != 0 {
		return false
	}

	first, second := productId[0:len(productId)/2], productId[len(productId)/2:]
	if first == second {
		return true
	}

	return false
}

func findInvalidProductIds(productIdRange string) []int {
	productIds := []int{}
	invalidProductIds := []int{}
	for _, productId := range strings.Split(productIdRange, "-") {
		productIdInt, err := strconv.Atoi(productId)
		if err != nil {
			fmt.Println("Error converting productId to int:", err)
			return []int{}
		}
		productIds = append(productIds, productIdInt)

	}
	numRange := makeRange(productIds[0], productIds[1])
	for _, num := range numRange {
		if isInvalid(strconv.Itoa(num)) {
			invalidProductIds = append(invalidProductIds, num)
		}
	}
	return invalidProductIds
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
	sumOfInvalidProductIds := 0

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
		invalidProductIds := findInvalidProductIds(productIdRange)
		// fmt.Println(invalidProductIds)

		sumOfInvalidProductIds += sum(invalidProductIds)
	}
	fmt.Println("sumOfInvalidProductIds: ", sumOfInvalidProductIds)

}
