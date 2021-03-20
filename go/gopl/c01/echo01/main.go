package main

import (
	"fmt"
	"os"
)

func main() {
	for i := 0; i < len(os.Args); i++ {
		fmt.Printf("%v ", os.Args[i])
	}
	fmt.Println()
	for idx, arg := range os.Args[1:] {
		fmt.Printf("%d %v\n", idx, arg)
	}
}
