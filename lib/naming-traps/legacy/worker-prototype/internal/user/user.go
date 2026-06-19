// Legacy prototype — not used in production
package user

import "fmt"

type User struct {
	ID    string
	Email string
	Name  string
}

func FindByID(id string) (*User, error) {
	return nil, fmt.Errorf("not implemented")
}