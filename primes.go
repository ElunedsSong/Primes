package main

import (
	"context"
	"math/big"
)

func isPrime(num *big.Int) bool {
	return num.ProbablyPrime(0)
}

func isTwinPrime(num *big.Int) bool {
	twin := big.NewInt(2)
	twin.Add(twin, num)
	return num.ProbablyPrime(0) && twin.ProbablyPrime(0)
}

func isTripletPrime(num *big.Int) bool {
	two := big.NewInt(2)
	two.Add(two, num)
	six := big.NewInt(6)
	six.Add(six, num)
	return num.ProbablyPrime(0) && two.ProbablyPrime(0) && six.ProbablyPrime(0)
}

func isQuadpletPrime(num *big.Int) bool {
	two := big.NewInt(2)
	two.Add(two, num)
	six := big.NewInt(6)
	six.Add(six, num)
	eight := big.NewInt(8)
	eight.Add(eight, num)
	return num.ProbablyPrime(0) && two.ProbablyPrime(0) && six.ProbablyPrime(0) && eight.ProbablyPrime(0)
}

func isQuintpletPrime(num *big.Int) bool {
	two := big.NewInt(2)
	two.Add(two, num)
	six := big.NewInt(6)
	six.Add(six, num)
	eight := big.NewInt(8)
	eight.Add(eight, num)
	twelve := big.NewInt(12)
	twelve.Add(twelve, num)
	return num.ProbablyPrime(0) &&
		two.ProbablyPrime(0) &&
		six.ProbablyPrime(0) &&
		eight.ProbablyPrime(0) &&
		twelve.ProbablyPrime(0)
}

func isSexpletPrime(num *big.Int) bool {
	two := big.NewInt(2)
	two.Add(two, num)
	six := big.NewInt(6)
	six.Add(six, num)
	eight := big.NewInt(8)
	eight.Add(eight, num)
	twelve := big.NewInt(12)
	twelve.Add(twelve, num)
	fourteen := big.NewInt(14)
	fourteen.Add(fourteen, num)
	return num.ProbablyPrime(0) &&
		two.ProbablyPrime(0) &&
		six.ProbablyPrime(0) &&
		eight.ProbablyPrime(0) &&
		twelve.ProbablyPrime(0) &&
		fourteen.ProbablyPrime(0)
}

func predInRange(ctx context.Context, a *big.Int, b *big.Int, pred func(*big.Int) bool) (int, bool) {
	count := 0
	n := big.NewInt(0)
	n.Add(n, a)
	for ; n.Cmp(b) < 1; n.Add(n, big.NewInt(1)) {
		select {
		case <-ctx.Done():
			return 0, false
		default:
		}
		if pred(n) {
			count++
		}
	}
	return count, true
}

func createRange(i int) (a *big.Int, b *big.Int) {
	if i > 0 {
		_, a = createRange(i - 1)
		a.Add(a, big.NewInt(1))
	} else {
		a = big.NewInt(0)
	}

	c := big.NewInt(5)
	power := big.NewInt(int64(i + 1))
	b = c.Exp(c, power, nil)

	return a, b
}

func calculateRatios(counts []int) []float64 {
	ratios := []float64{}
	prev := counts[0]
	for i := 1; i < len(counts); i++ {
		curr := counts[i]
		ratios = append(ratios, float64(curr)/float64(prev))
		prev = curr
	}
	return ratios
}
