package models

type Account struct {
	ID             int
	Name           string
	Balance        float64
	TransactionLog []string
}