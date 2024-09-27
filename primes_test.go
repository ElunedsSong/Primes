package main

import (
	"context"
	"math/big"
	"reflect"
	"strconv"
	"testing"
)

var prime bool

func BenchmarkIsPrime(b *testing.B) {
	for n := 0; n < b.N; n++ {
		for i := 600; i < 800; i++ {
			prime = isPrime(big.NewInt(int64(i)))
		}
	}
}

func TestIsPrime(t *testing.T) {
	testCases := []struct {
		num   int64
		prime bool
	}{
		{2, true},
		{3, true},
		{4, false},
		{5, true},
		{6, false},
		{7, true},
		{8, false},
		{9, false},
		{10, false},
	}
	for _, tC := range testCases {
		t.Run(strconv.FormatInt(tC.num, 10), func(t *testing.T) {
			isPrime(big.NewInt(tC.num))
		})
	}
}

func TestIsTwinPrime(t *testing.T) {
	testCases := []struct {
		num       int64
		twinPrime bool
	}{
		{2, false},
		{3, true},
		{4, false},
		{5, true},
		{6, false},
		{7, false},
		{8, false},
		{9, false},
		{10, false},
	}
	for _, tC := range testCases {
		t.Run(strconv.FormatInt(tC.num, 10), func(t *testing.T) {
			isTwinPrime(big.NewInt(tC.num))
		})
	}
}

func TestPrimesInRange(t *testing.T) {
	testCases := []struct {
		a     int64
		b     int64
		count int
	}{
		{2, 3, 2},
		{2, 6, 3},
		{12, 20, 3},
	}
	for _, tC := range testCases {
		t.Run(strconv.FormatInt(tC.a, 10)+"-"+strconv.FormatInt(tC.b, 10), func(t *testing.T) {
			count, _ := predInRange(context.TODO(), big.NewInt(tC.a), big.NewInt(tC.b), isPrime)
			if count != tC.count {
				t.Fatalf("expected %v but got %v", tC.count, count)
			}
		})
	}
}

func TestCreateRange(t *testing.T) {
	testCases := []struct {
		desc string
		i    int
		a    int64
		b    int64
	}{
		{
			desc: "zero through five",
			i:    0,
			a:    0,
			b:    5,
		},
		{
			desc: "six through twenty-five",
			i:    1,
			a:    6,
			b:    25,
		},
		{
			desc: "twenty-six through one-hundred twenty-five",
			i:    2,
			a:    26,
			b:    125,
		},
	}
	for _, tC := range testCases {
		t.Run(tC.desc, func(t *testing.T) {
			a, b := createRange(tC.i)
			if a.Cmp(big.NewInt(tC.a)) != 0 {
				t.Fatalf("expected %v but got %v", tC.a, a)
			}
			if b.Cmp(big.NewInt(tC.b)) != 0 {
				t.Fatalf("expected %v but got %v", tC.b, b)
			}
		})
	}
}

func TestCalculateRatios(t *testing.T) {
	testCases := []struct {
		desc   string
		counts []int
		ratios []float64
	}{
		{
			desc:   "0-5, 6-25",
			counts: []int{3, 6},
			ratios: []float64{2.0},
		},
	}
	for _, tC := range testCases {
		t.Run(tC.desc, func(t *testing.T) {
			ratios := calculateRatios(tC.counts)
			if !reflect.DeepEqual(tC.ratios, ratios) {
				t.Fatalf("expected %v but got %v", tC.ratios, ratios)
			}
		})
	}
}
