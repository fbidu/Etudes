package main

import "fmt"

func main() {
	// Explicit array declaration
	var array [5]int
	array[0] = 10
	array[3] = 1
	// array[4] := 0 -> Not allowed!
	fmt.Printf("%v\n", array)

	primes := [5]int{2, 3, 5, 7, 11}

	fmt.Printf("%v\n", primes)

	var pointers [5]*int
	x := 10
	pointers[0] = &x
	// pointers[1] := &1 -- Not allowed either
	// pointers[1] = &1 -- Same here

	fmt.Printf("'Pointers' is: %v\n", pointers) // That's interesting

	fmt.Printf("Changing the value of x\n\n")
	x = 20

	fmt.Printf("Address stil the same\n")
	fmt.Printf("'Pointers' is: %v\n", pointers)

	fmt.Printf("Value changed\n")
	fmt.Printf("%d \n", *pointers[0])

	// Simple assignment test
	a := 10
	b := a
	a = 20
	fmt.Printf("%d \n", b)

}
