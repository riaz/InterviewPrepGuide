package main

import (
	"fmt"
	"log"

	"greetings.com/greetings"
)

func main() {
	log.SetPrefix("greetings: ")
	log.SetFlags(0)

	names := []string{"Riaz", "Yari", "Kuku"}

	messages, err := greetings.Hellos(names)

	if err != nil {
		log.Fatal(err)
	}

	// this will print the returned map of messages
	fmt.Println(messages)
}
