package main

import "fmt"

func main() {

	// Simple map initialization
	ages := make(map[string]int)
	ages["felipe"] = 25
	ages["flávia"] = 27
	ages["matheus"] = 25

	fmt.Printf("%v\n", ages)

	// Initializing a map with values
	areas := map[string][]string{"Exatas": {"Felipe", "Matheus"}, "Artes": {"Flávia"}}
	fmt.Printf("%v\n", areas)

	// Appending to a value
	areas["Exatas"] = append(areas["Exatas"], "Osvaldo")
	fmt.Printf("%v\n", areas)

	var stranger map[string]string // This is a 'nil map'
	fmt.Printf("%v\n", stranger)
	// stranger["test"] = "hi" You can't assign to a nil map!

	stranger = make(map[string]string) // Initialize it...
	stranger["test"] = "hi"            // And there you go
	fmt.Printf("%v\n", stranger)

	// Accessing an item using a tuple
	item, exists := areas["Artes"]

	if exists {
		fmt.Printf("I found the item! %v\n", item)
	}

	// Single access
	item1 := areas["Exatas"]

	if item != nil {
		fmt.Printf("I found the item! %v\n", item1)
	}

	for name, age := range ages {
		fmt.Printf("%s is %d years old\n", name, age)
	}

	// Maps are passed by reference!
	addHumanities(areas)
	fmt.Printf("%v\n", areas)
}

func addHumanities(areas map[string][]string) {
	areas["Humanities"] = []string{"Rita", "Luciano"}
}
