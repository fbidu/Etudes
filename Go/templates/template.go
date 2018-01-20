package main

import (
	"os"
	"text/template"
)

type Todo struct {
	Name        string
	Description string
}

type TodoPointer struct {
	Name        *string
	Description *string
}

func main() {
	td := Todo{"Hello, templates", "What can you do?"}

	t, err := template.New("todos").Parse("There is a task called \"{{.Name}}\", with description \"{{.Description}}\"\n")

	if err != nil {
		panic(err)
	}

	err = t.Execute(os.Stdout, td)

	if err != nil {
		panic(err)
	}

	var incompleteTd Todo
	incompleteTd.Name = "Hi, this works, even missing a field"

	err = t.Execute(os.Stdout, incompleteTd)

	if err != nil {
		panic(err)
	}
}
