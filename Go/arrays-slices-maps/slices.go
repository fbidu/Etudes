package main

import (
	"fmt"
)

func main() {

	// Initializing the slice
	x := []int{1, 2, 3, 4, 5, 6}
	fmt.Printf("%v\n", x)

	// Slicing it...
	l := x[2:5]
	fmt.Printf("%v\n", l)

	// Changing the value on the original slice
	// and printing the 'new' slice
	x[2] = 20
	fmt.Printf("%v\n", l) // Surpriiise

	l[0] = -1
	fmt.Printf("%v\n", x)

	// Another slice
	numbers := []int{1, 2, 3, 4, 5}

	// And another
	numbersILike := numbers[2:5]
	fmt.Printf("Numbers: %v\n", numbers)
	fmt.Printf("Slice of Numbers:%v\n", numbersILike)
	fmt.Printf("Adding a bunch of elements to SLICE!\n\n")
	numbersILike = append(numbersILike, 20)
	numbersILike = append(numbersILike, 30)
	numbersILike = append(numbersILike, 40)
	numbersILike = append(numbersILike, 50)
	fmt.Printf("Slice now is... %v\n", numbersILike)
	fmt.Printf("And numbers... %v\n", numbers)

}
